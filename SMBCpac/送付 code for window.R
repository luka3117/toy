install.packages("SMBCpac_0.1.0.tar.gz", repos = NULL)


# ---- 使用package ---
library(SMBCpac)
library(randomForest)
library(tidyverse)
library(magrittr)
library(pROC)


colnames(smbc) %<>% iconv("utf8", "cp932")
colnames(smbc.test) %<>% iconv("utf8", "cp932")
colnames(smbc.train) %<>% iconv("utf8", "cp932")
row.names(smbc.rf.train$importance) %<>% iconv("utf8", "cp932")


# data 概要
help(smbc)
help(smbc.test)
help(smbc.train)


# RF importtance 表示
# smbc.rf.train <- randomForest(y ~ ., data = smbc.train, method = "class")
smbc.rf.train$importance %>% tbl_df() %>% mutate(var=colnames(smbc.train)[-1]) %>% arrange(desc(MeanDecreaseGini)) %>% knitr::kable()


# importtance plot

par(family= "HiraKakuProN-W3")
varImpPlot(smbc.rf.train)

# Predicted.test <- predict(smbc.rf.train, smbc.test, type="prob")
# Predicted.train <- predict(smbc.rf.train, smbc.train, type="prob")


# importtance 中身

Predicted.test %>% tbl_df()
Predicted.train %>% tbl_df()


# ---- ROC curve ----
# rf 訓練データ
roc(
  smbc.test$y ~ Predicted.test[,2],
  plot = T,
  print.auc = T,
  col = "orange",
  # add = T,
  print.auc.y = 0.4,
  print.auc.x = 1
  
)

# rf 評価データ
roc(
  smbc.train$y ~ Predicted.train[,2],
  plot = T,
  print.auc = T,
  col = "grey",
  add = T,
  print.auc.y = 0.3,
  print.auc.x = 1
  
)


legend("bottomright", legend = c("RF.test", "RF.train"),
       col = c("orange", "grey"), lwd=4)



# set.seed(0) #乱数に再現性があるように初期値を固定
# index <- sample(1:nrow(smbc), round(nrow(smbc) * 0.6)) #6割で訓練、4割で評価
# 
# # 訓練データ
# smbc.train <- smbc[index, ]
# smbc.test <- smbc[-index, ]

