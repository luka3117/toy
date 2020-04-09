


# rf 


smbc$y<-smbc$`６か月以内来店有無`
smbc<-smbc %>% select(y, everything())
smbc<-smbc %>% select(-６か月以内来店有無) %>% select(y, everything())


set.seed(0) #乱数に再現性があるように初期値を固定
index <- sample(1:nrow(smbc), round(nrow(smbc) * 0.6)) #6割で訓練、4割で評価

# 訓練データ
smbc.train <- smbc[index, ]
smbc.test <- smbc[-index, ]

# library(randomForest)
# smbc.rf.train<-randomForest(y~., data=smbc.train, method = "class")

# save.image("rf.Rdata")


load("rf.Rdata")

smbc.rf.train$importance %>% tbl_df() %>% mutate(var=colnames(smbc.train)[-1]) %>% arrange(desc(MeanDecreaseGini)) %>% knitr::kable()


par(family= "HiraKakuProN-W3")

varImpPlot(smbc.rf.train)


Predicted.test <- predict(smbc.rf.train, smbc.test, type="prob")

Predicted.train <- predict(smbc.rf.train, smbc.train, type="prob")


Predicted.test %>% tbl_df()



m<-glm(formula = y ~ ex + 年齢 + 
         性別 +  顧客カテゴリ + 自動払いフラグ + 
         チャネル + 口座開設月数 + 年収  + 
         Q2運用期間 + Q3投資目的 + Q4許容リスク + Q5金融資産総額 + 
         Q7運用資産の割合 + Q81年以内の使用予定 + 営業担当者の職位 + 
         外貨預金残高 + 運用商品残高 + 総預り残高 + 
         支店からの距離, family = binomial(), data = smbc)


m$fitted.values


library(pROC)
roc(
  m$y ~ m$fitted.values, 
  plot = T,
  print.auc = T,
  col = "red",
  legacy.axes = T,
  xlab="False Positive",
  ylab="True Positive"
)

roc(
  d.complete$y ~ predict(res.cart)[, 2],
  plot = T,
  print.auc = T,
  col = "blue",
  add = T,
  print.auc.y = 0.3
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


