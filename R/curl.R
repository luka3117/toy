# 使用package
suppressMessages(library(readxl))
suppressMessages(library(dplyr))
suppressMessages(library(tidyverse))
suppressMessages(library(data.table))
library(curl)

aa<-"https://drive.google.com/drive/u/0/my-drive//Cardiotocographic.csv"

read.csv(curl(aa))




read.csv(curl("https://raw.githubusercontent.com/luka3117/toy/master/csv/iris.csv")) %>% 
  tbl_df()

https://drive.google.com/drive/u/0/my-drive

  