city.code <- read.csv("city code.txt")

library(tidyverse)
pref<-read.csv("data1.csv")
pref<-pref %>% select(contains("pre")) %>% select(2,3,4) %>% .[1:47, ]



