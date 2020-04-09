# 使用package
suppressMessages(library(readxl))
suppressMessages(library(dplyr))
suppressMessages(library(tidyverse))
suppressMessages(library(data.table))
suppressMessages(library(curl))
suppressMessages(library(randomForest))
suppressMessages(library(pROC))


load("rf.Rdata")
smbc

set.seed(0) #乱数に再現性があるように初期値を固定
index <- sample(1:nrow(smbc), round(nrow(smbc) * 0.6)) #6割で訓練、4割で評価

# 訓練データ
smbc.train <- smbc[index, ]
smbc.test <- smbc[-index, ]

library(randomForest)
# smbc.rf.train<-randomForest(y~., data=smbc.train, method = "class")
# save.image("rf.Rdata")

load("rf.Rdata")

smbc.rf.train$importance %>% tbl_df() %>% mutate(var=colnames(smbc.train)[-1]) %>% arrange(desc(MeanDecreaseGini)) %>% knitr::kable()

smbc.test %>% tbl_df()
smbc.train

par(family= "HiraKakuProN-W3")
varImpPlot(smbc.rf.train)

Predicted.test <- predict(smbc.rf.train, smbc.test, type="prob")
Predicted.train <- predict(smbc.rf.train, smbc.train, type="prob")


Predicted.test %>% tbl_df()
Predicted.train %>% tbl_df()


# library(pROC)
roc(
  m$y ~ m$fitted.values, 
  plot = T,
  print.auc = T,
  col = "red",
  legacy.axes = T,
  xlab="False Positive",
  ylab="True Positive"
)


# rf 訓練データ
roc(
  smbc.test$y ~ Predicted.test[,2],
  plot = T,
  print.auc = T,
  col = "orange",
  add = T,
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


legend("bottomright", legend = c("logistic", "CART", "RF.train", "RF.test"), 
       col = c("red", "blue", "orange", "grey"), lwd=4)


# 
# 
# 
# 
# # rf 
# 
# 
# smbc$y<-smbc$`６か月以内来店有無`
# smbc<-smbc %>% select(y, everything())
# smbc<-smbc %>% select(-６か月以内来店有無) %>% select(y, everything())
# 
# 
# 
# 
# 
