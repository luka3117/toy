load("rf.Rdata")

library(randomForest)

Predicted.test <- predict(smbc.rf.train, smbc.test, type="prob")
Predicted.train <- predict(smbc.rf.train, smbc.train, type="prob")
