library(drake)
# 使用package
suppressMessages(library(readxl))
suppressMessages(library(dplyr))
suppressMessages(library(data.table))
suppressMessages(library(kableExtra))
suppressMessages(library(curl))
suppressMessages(library(tidyverse))


plan<-drake::drake_plan(
  
  a=iris %>% select(Sepal.Length),
  b=lm(iris$Sepal.Length~iris$Petal.Length)
  
)

drake::make(plan)