# 使用package
suppressMessages(library(readxl))
suppressMessages(library(dplyr))
suppressMessages(library(tidyverse))
suppressMessages(library(data.table))
library(curl)

file=curl("https://raw.githubusercontent.com/luka3117/toy/master/csv/iris.csv")
read.csv(file)
