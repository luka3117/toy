# snbc --------------------------------------------------------------------
library(SMBCpac)
help(package = "SMBCpac")
d<-smbc.train
d<-d[sample(1:dim(d)[1], 1e+4), ]


# iris--------------------------------------------------------------------
d<-iris
d$y<-d$Species
d<-d[,-5]


library(randomForest)
system.time(
  res <- randomForest(y~., data=d, method = "class", ntree=500)
)

library(doParallel)

# colnames(d)<-c("y",sprintf("%s%d", "x", 1:23))

stopCluster(cl)

cores <- 4
cl <- makePSOCKcluster(cores)
registerDoParallel(cl)

system.time(
  foreach_forest <- foreach(
    ntree = rep(125, 4),
    .combine = combine,
    # .multicombine = TRUE,
    .packages = "randomForest"
  ) %dopar%
    randomForest(
      y~., data=d, 
      method = "class", ntree = ntree 
    )
)



# 予測確率
Predicted <- predict(res, type="prob")
roc3 <- roc(y, Predicted[,2],tt)

