# SMBCpac package install ----------------------------------------------------------------------
install.packages("SMBCpac_0.1.0.tar.gz", repos = NULL)

# 使用 package ----------------------------------------------------------------------
library(SMBCpac)
library(randomForest)
library(tidyverse)
library(magrittr)
library(pROC)

# windosの場合は以下を実装 -----------------------------------------------------------------

colnames(smbc) %<>% iconv("utf8", "cp932")
colnames(smbc.test) %<>% iconv("utf8", "cp932")
colnames(smbc.train) %<>% iconv("utf8", "cp932")
row.names(smbc.rf.train$importance) %<>% iconv("utf8", "cp932")



# data 概要 -------------------------------------------------------------------

help(smbc)
help(smbc.test)
help(smbc.train)


# RF推定 -------------------------------------------------------------------
# smbc.rf.train <- randomForest(y ~ ., data = smbc.train, method = "class")


# RF importtance 表示 ----------------------------------------------------------------------
smbc.rf.train$importance %>% tbl_df() %>% mutate(var = colnames(smbc.train)[-1]) %>% arrange(desc(MeanDecreaseGini)) %>% knitr::kable()



# importtance plot ------------------------------------------------------------------
par(family = "HiraKakuProN-W3")
varImpPlot(smbc.rf.train)



# 訓練、テスト予測 ------------------------------------------------------------------
# Predicted.train <- predict(smbc.rf.train, smbc.train, type="prob")
# Predicted.test <- predict(smbc.rf.train, smbc.test, type="prob")

# 訓練、テスト予測結果 ------------------------------------------------------------------
Predicted.test %>% tbl_df()
Predicted.train %>% tbl_df()


# ROC curve -----------------------------------------------------------------
roc(
  smbc.test$y ~ Predicted.test[, 2],
  plot = T,
  print.auc = T,
  col = "orange",
  # add = T,
  print.auc.y = 0.4,
  print.auc.x = 1
  
)

# rf 評価データ
roc(
  smbc.train$y ~ Predicted.train[, 2],
  plot = T,
  print.auc = T,
  col = "grey",
  add = T,
  print.auc.y = 0.3,
  print.auc.x = 1
  
)

legend(
  "bottomright",
  legend = c("RF.test", "RF.train"),
  col = c("orange", "grey"),
  lwd = 4
)

# misc --------------------------------------------------------------------
# index <- sample(1:nrow(smbc), round(nrow(smbc) * 0.6)) #6割で訓練、4割で評価
#  訓練データ
# smbc.train <- smbc[index, ]
# smbc.test <- smbc[-index, ]
