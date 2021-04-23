# devtools::install_github(repo = "luka3117/JcPackage/OsakaUniv2020")

# 使用package
suppressMessages(library(readxl))
suppressMessages(library(dplyr))
suppressMessages(library(data.table))
suppressMessages(library(kableExtra))
suppressMessages(library(curl))
suppressMessages(library(tidyverse))
suppressMessages(library(plotly))


# d<-read_csv("../..//data/DataFormat.csv", skip=1, locale = readr::locale(encoding = "CP932"))

# file<-"./data/DataFormat-32021年3月11日受領/DataFormat.csv"


# ----------------- make d  -----------------

file<-"./data/DataFormat-32021年3月11日受領/DataFormat.csv"
d<-read_csv(file, skip=1, locale = readr::locale(encoding = "CP932"))

# ./data/DataFormat-32021年3月11日受領

d<-d[-95,]
d %>% dim()
## [1]  94 168
d<-d %>% rename(key=X1)
d %>% DT::datatable()



file<-"./data/DataFormat-32021年3月11日受領/var_name_Eng.csv"
var<-read.csv(file)
colnames(d)<-var$var_name_Eng

# ----------------- make d  end -----------------



# ----------------- make JpnEng 変数対応表 # -----------------


file<-"./data/DataFormat-32021年3月11日受領/JpnEng.csv"
JpnEng<-read.csv(file)

# JpnEng %>% tbl_df()


# ----------------- make JpnEng 変数対応表 # -----------------


# -----------------  d_common データ -----------------

d_common<-d[, sapply(d[48,], is.na)]

d_common<-d_common[1:47, ]

# d_common%>% DT::datatable()

d_common<-d %>% select(1:6) %>% .[1:47,] %>% bind_cols(d_common)

d_common %>% DT::datatable()

# -----------------  d_common データ end  -----------------


# -----------------　3.6 男女区別のあるデータ # -----------------
# -----------------　d_mf,d_m,d_f　# -----------------

name <- function(x) {
  !is.na(x)
}
d_mf<-d[, sapply(d[48,], name)]
d_mf %>% DT::datatable()

d_m<-d_mf %>% filter(sex=="M")
d_f<-d_mf %>% filter(sex=="F")




# -----------------　3.6 男女区別のあるデータ # -----------------
# -----------------　d_mf,d_m,d_f　end # -----------------


# -----------------5 寿命(目的変数)の都道府県の順位確認

suppressMessages(library(plotly))

t<-d_m %>% select(pref.J,HLE_2016,LE_2015) %>%
  mutate(pref.J=forcats::fct_reorder(pref.J, LE_2015))
t$pref.J

# -----------------5 寿命(目的変数)の都道府県の順位確認




#
#
# system("open .")
#
# see
#
# 「WakayamaHtml_mid_report.html」
#



#
# system("open .")
