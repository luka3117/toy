
# 使用package
suppressMessages(library(readxl))
suppressMessages(library(dplyr))
suppressMessages(library(data.table))
suppressMessages(library(kableExtra))
suppressMessages(library(curl))
suppressMessages(library(tidyverse))
library(xtable)
class <- read.table("class.txt", header = T)

# 変数追加
class$grade <- sample(c("A", "B", "C"), 19, replace = T)
class$preference <-
  sample(c("pepsi", "cola", "coffee"), 19, replace = T)
class$income <-
sample(c("<15000", "15000-25000", "25000-40000", ">40000")
         # jobsat <- c("VD", "LD", "MS", "VS")
         ,19,replace = T)
# class <- class[1:10,-1]

write.table(class, "class1.txt")

xtable(class)


class[1] %>% xtable()
class[2] %>% xtable()
class[3] %>% xtable()
class[4] %>% xtable()
class[5] %>% xtable()
class[6] %>% xtable()
class[7] %>% xtable()
class[8] %>% xtable()
class[9] %>% xtable()


colnames(class) %>% cat()


class %>% colnames()

table(class$Sex) %>% xtable()
table(class$Sex, class$preference) %>% xtable()
table(class$Sex, class$preference, class$grade)

aa<-xtabs(~Sex+preference+grade, data = class)

aa[[1]]

class$

?xtabs

DF <- as.data.frame(UCBAdmissions)

xtabs( ~ Gender + Admit, DF)


%>% xtable()


# attach(class)

# xtable(table(Sex))
# xtable(table(preference))
# xtable(table(Sex, preference))
# table(class$grade, class$income) %>% xtable()


# job satisfaction
income <- c("<15000", "15000-25000", "25000-40000", ">40000")
jobsat <- c("VD", "LD", "MS", "VS")
table.2.8 <- expand.grid(income = income, jobsat = jobsat)
data <- c(1, 2, 1, 0, 3, 3, 6, 1, 10, 10, 14, 9, 6, 7, 12, 11)
table.2.8 <- cbind(table.2.8, count = data)
(temp <- xtabs(count ~ income + jobsat, table.2.8))

xtable(temp)

# 使用package


class




class %>% table(.$Sex)

class$Sex %>% table() %>% xtable()
class$preference %>% table() %>% xtable()
class$preference %>% table()

table(class$Sex, class$preference)
