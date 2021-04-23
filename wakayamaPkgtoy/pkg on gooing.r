# ---
# title: "和歌山県報告書(under working for mid report)"
# subtitle: "健康寿命"
# author: "李鍾賛(jc lee, 滋賀大助教、数理統計学博士)"
# date: "最終更新: `r format(Sys.time(), '%Y/%m/%d')`"
# output:
# # word_document:
# html_document:
# number_section: true
# toc: true
# # code_folding: hide
# # toc_float:
#   smooth_scroll: false
#   collapsed: false

# output:
#   ioslides_presentation:
#   widescreen: true
#   number_section: true
#   toc: true
#   transition: faster
# css: 'scrollable_slides.css'

# runtime: shiny
# https://bookdown.org/yihui/rmarkdown/ioslides-presentation.html

# The following single character keyboard shortcuts enable alternate display modes:
#
# 'f': enable fullscreen mode
#
# 'w': toggle widescreen mode
#
# 'o': enable overview mode
#
# 'h': enable code highlight mode
#
# # 'p': show presenter notes
# ---
#
#
# #  データ情報および変更履歴：
# # - "DataFormat.csv" latest version 2021年2月10日
# # - "DataFormat.csv" latest version 2021年3月11日受領


# > ＜追記修正箇所等＞
#
# - V列
# - 熊本県の欠損値について、国の示す推定方法により数値を記載 -
# - 熊本県女性の**健康寿命の推定値**
#
# - FI列、FJ列、FK列、FL列 　収集元データの**年度修正**（新しいデータに置き換え）
# - 野菜摂取量_2016(20歳以上平均値(g/日)
# - 食塩摂取量_2016(20歳以上平均値(g/日)
# - BMI平均値_2016(男性20〜69歳)(女性40〜69歳)(単位Kg/u)
# - 歩数_2016(20歳以上平均値(歩/日)
#
#
# - DH列、DI列、DJ列、DK列のデータ収集**元URLを修正**
# - 悪性新生物(子宮)_年齢調整死亡率2015
# - 心疾患_年齢調整死亡率2015
# - 肺炎_年齢調整死亡率2015
# - 急性心筋梗塞_年齢調整死亡率2015
# - （✕「患者調査」から→〇「人口動態統計特殊報告」）
#
# - EF列、EG列、EH列、EI列、EJ列
#
# - バリアフリー化の**総数**であったものをバリアフリー化**率に置き換え**
# - 一定のバリアフリー化率_2018
# - 高度のバリアフリー化率_2018
# - バリアフリー_手すりがある2018
# - バリアフリー_廊下などが車いすで通行可能な幅2018
# - バリアフリー_段差のない屋内2018
# - 参考事項：バリアフリー化率の出典元を発見
#
#
# ```{r, warning=FALSE}

# devtools::install_github(repo = "luka3117/JcPackage/OsakaUniv2020")

# 使用package
suppressMessages(library(readxl))
suppressMessages(library(dplyr))
suppressMessages(library(data.table))
suppressMessages(library(kableExtra))
suppressMessages(library(curl))
suppressMessages(library(tidyverse))
suppressMessages(library(plotly))



set.seed(42)

p <- ggplot(mtcars, aes(y = wt, x = 1, label = rownames(mtcars))) +
geom_point(color = "red") +
ylim(1, 5.5) +
theme(
axis.line.x  = element_blank(),
axis.ticks.x = element_blank(),
axis.text.x  = element_blank(),
axis.title.x = element_blank()
)

p1 <- p +
xlim(1, 1.375) +
geom_text_repel(
force        = 0.5,
nudge_x      = 0.15,
direction    = "y",
hjust        = 0,
segment.size = 0.2
) +
ggtitle("hjust = 0")

p2 <- p +
xlim(1, 1.375) +
geom_text_repel(
force        = 0.5,
nudge_x      = 0.2,
direction    = "y",
hjust        = 0.5,
segment.size = 0.2
) +
ggtitle("hjust = 0.5 (default)")

p3 <- p +
xlim(0.25, 1) +
scale_y_continuous(position = "right") +
geom_text_repel(
force        = 0.5,
nudge_x      = -0.25,
direction    = "y",
hjust        = 1,
segment.size = 0.2
) +
ggtitle("hjust = 1")

gridExtra::grid.arrange(p1, p2, p3, ncol = 3)

getwd()
# d<-read_csv("../..//data/DataFormat.csv", skip=1, locale = readr::locale(encoding = "CP932"))

# file<-"../../data/DataFormat-32021年3月11日受領/DataFormat.csv"
file<-"./data/DataFormat-32021年3月11日受領/DataFormat.csv"
d<-read_csv(file, skip=1, locale = readr::locale(encoding = "CP932"))


d<-d[-95,]
d %>% dim()
d<-d %>% rename(key=X1)
d %>% DT::datatable()
```

## 変数名を英語に変換 :data名`d`
```{r}
var<-read.csv("../../var_name_Eng.csv")
colnames(d)<-var$var_name_Eng
# d %>% DT::datatable()
```


### 変数名：和英対応表

```{r}
read.csv("../../JpnEng.csv") %>% DT::datatable()

```


## 男女区別のないデータ `d_common`
- 変数は 104
```{r}
d_common<-d[, sapply(d[48,], is.na)]

d_common<-d_common[1:47, ]

# d_common%>% DT::datatable()

d_common<-d %>% select(1:6) %>% .[1:47,] %>% bind_cols(d_common)

d_common %>% DT::datatable()
d_common %>% dim()

```

### `d_common` data 変数名
{.tabset .tabset-fade .tabset-pills}

#### 全体

```{r, warning=FALSE}
d_common %>% colnames() %>%tbl_df() %>%  DT::datatable()
```

#
#
#
# #### 健康/疾患
# Trt_rate_Hospitalization_Malignant_neoplasm_2017
# Trt_rate_hospitalization_heart_dz_2017
# Trt_rate_Hospitalization_Cerebrovascular_dz_2017
# Trt_rate_Outpatient_Malignant_neoplasm_2017
# Trt_rate_outpatient_heart_dz_2017
# Trt_rate_Outpatient_Cerebrovascular_dz_2017
#
#
# #### 医療施設
# Num_of_hospitals_2019
# Num_of_clinics_2019
# Num_of_general_clinics
# HM_Num_of_general_hospitals
# HM_Num_of_general_dental_clinics_per_100k_pop
# HM_Num_of_doctors_engaged_in_medical_facilities_per_100k_pop
# HM_Num_of_public_health_nurses_per_100k_pop
#
# #### 医療従事者
# Num_of_certified_cancer_doctors_2020
# Num_of_cardiologists_2020
# Num_of_endoscopists_2020
#
# #### 文化
# Book_purchase_price_2019
# Num_of_libraries
# Sports_Participant_Rate
# Travel_Rate1
# Volunteer_Activity_Participant_Rate
#
# #### 人口
# pop_Young_pop_Ratio_2020
# pop_oldElderly_pop_Ratio_2020
# pop_Working_Age_pop_Ratio_2020
# pop_Rough_Mortality_2020
# pop_Double_income_household_ratio_2020
#
# #### 自然環境
# Natural_environment_annual_avg_temperature
# Natural_environment_annual_avg_relative_humidity
# Natural_environment_annual_rain
# Natural_environment_annual_Num_of_snow_days
#
# #### 経済
# Economic_pref_income
# Admin_base_Financial_strength_index
# Admin_base_balance_ratio
# Admin_infrastructure_living_protection_cost_ratio_(prefectural_finance)
# Admin_infrastructure_Edu_cost_ratio_(prefectural_finance)
# Gini_coeff_2014
# Income_Gini_Coeff_Working_Household_2014
#
# #### 教育
# Edu_Ptc_of_university_graduate_students_with_a_final_academic_background
# Academic_ability_middle_school_2015
# Academic_ability_elementary_school_2015
#
# #### 労働
# Labor_primary_industry_emp_ratio
# Labor_secondary_industry_emp_ratio
# Labor_tertiary_industry_emp_ratio
# Labor_Unemp_rate
# Total_working_hours_2016
# Total_salary_2016
#
# #### 住居
# Residence_owner_ratio
# Residence_house_ratio
# Residence_water_supply_pop_ratio
# Residence_sewerage_ratio
# Residential_city_park_area_(per_pop)
# Residence_road_pavement_rate
# Residence_simachi_pavement_rate
# Safety_Num_of_traffic_accidents_per_100k_pop
# Residence_Num_of_city_parks
#
# #### 家計経済
# Household_actual_income
# Household_consumption_expenditure
# Household_Edu_cost_ratio
# Household_Liberal_Arts_and_Entertainment_Expenditure_Ratio
# Household_Savings
# Household_Smartphone_ownership_quantity
# Household_PC_ownership_quantity
# Household_Car_ownership_quantity
# Household_Tablet_terminal_Ownership_quantity
# pop_Household_Ratio_of_elderly_single_person_households
#
# #### 疾患
# Hypertension_Hospitalization_2014
# Hypertension_Outpatient_2014
# Diabetes_hospitalization_2014
# Diabetes_Outpatient_2014
# Total_Num_of_caries_2014
# Total_Num_of_periodontal_2014
# Bone_density_disorder_2014
# Fracture_2014
# Tooth_supplement_2014
# Alzheimer_dz_2014
#
# #### 食
# Meat_2014
# Seafood_2014
# Milk_2014
# Dairy_2014
# Egg_2014
# Soybean_2014
#
# #### 住居施設
# Usual_barrier_free_handrails_2013
# Usual_barrier_free_no_steps_2013
# High_barrier_free_handrails_2013
# High_barrier_free_no_steps_2013
# High_barrier_free_wheelchairs_pass_Width
#
# #### 食消費
# Fish_meat_consumption_2014
# Fish_meat_consumption_2015
# Fish_meat_consumption_2016
# Fish_meat_consumption_avg_2014_2016
# Confectionery_consumption_2014
# Confectionery_consumption_2015
# Confectionery_consumption_2016
# Confectionery_consumption_avg_2014_2016
# Fruits_consumption_2014
# Fruits_consumption_2015
# Fruits_consumption_2016
# Fruit_consumption_avg_2014_2016
#
# #
#
#
# - 男女区別のないデータの***変数は`r dim(d_common)[2]-6`個***
#
#
# ## 男女区別のあるデータ `d_mf`,`d_m`,`d_f`
# {.tabset .tabset-fade .tabset-pills}
#
#
# ### `d_mf`

# ```{r}
name <- function(x) {
!is.na(x)
}
d_mf<-d[, sapply(d[48,], name)]
d_mf %>% DT::datatable()
d_mf %>% dim()
d_m<-d_mf %>% filter(sex=="M")
d_f<-d_mf %>% filter(sex=="F")
# summary(d_mf)

# ```
#
# ### 男性データ`d_m`
#
# ```{r}
# d_m %>% DT::datatable()
# ```
#
# ### 女性データ`d_f`
# ```{r}
# d_f %>% DT::datatable()
# ```

#
# ## 以下分析対象データ`d_common`, `d_m`, `d_f`
#
# # dataの変数属性を確認
# {.tabset .tabset-fade .tabset-pills}
#
# ## `d_common`
#
# ```{r}
# d_common %>% colnames() %>% enframe() %>% DT::datatable()
# ```
#
#
# ## `d_m`
#
# ```{r}
# d_m %>% colnames() %>% enframe() %>% DT::datatable()
#
# ```
#
# ## `d_f`
# ```{r}
# d_f %>% colnames() %>% enframe() %>% DT::datatable()
# ```
#
#
#
# # 寿命(目的変数)の都道府県の順位確認
# {.tabset .tabset-fade .tabset-pills}
#
# ## 男性の平均寿命と健康寿命の差
# ```{r, warning=FALSE}
suppressMessages(library(plotly))

t<-d_m %>% select(pref.J,HLE_2016,LE_2015) %>%
mutate(pref.J=forcats::fct_reorder(pref.J, LE_2015))
t$pref.J

t %>%
plot_ly() %>%
add_segments(
x=~HLE_2016,y=~pref.J ,
xend=~LE_2015,yend=~pref.J ,
# x = ~c, y = ~model,
# xend = ~h, yend = ~model,
color = I("gray"), showlegend = FALSE
) %>%
add_markers(
# x = ~c, y = ~model,
x=~HLE_2016,y=~pref.J ,
color = I("blue"),
name = "健康寿命"
) %>%
add_markers(
# x = ~h, y = ~model,
x=~LE_2015,y=~pref.J ,
color = I("red"),
name  = "平均寿命"
) %>%
layout(
xaxis = list(
range=c(60,83),
title="男性の平均寿命と健康寿命の差"
)
)

```

## 女性の平均寿命と健康寿命の差
```{r, warning=FALSE}

suppressMessages(library(plotly))

t<-d_f %>% select(pref.J,HLE_2016,LE_2015) %>%
mutate(pref.J=forcats::fct_reorder(pref.J, LE_2015))
t$pref.J

t %>%
# plot_ly(width = 600, height = 1000) %>%
plot_ly() %>%
add_segments(
x=~HLE_2016,y=~pref.J ,
xend=~LE_2015,yend=~pref.J ,
# x = ~c, y = ~model,
# xend = ~h, yend = ~model,
color = I("gray"), showlegend = FALSE
) %>%
add_markers(
# x = ~c, y = ~model,
x=~HLE_2016,y=~pref.J ,
color = I("blue"),
name = "健康寿命"
) %>%
add_markers(
# x = ~h, y = ~model,
x=~LE_2015,y=~pref.J ,
color = I("red"),
name  = "平均寿命"
) %>%
layout(
xaxis = list(
range=c(60,88),
title="女性の平均寿命と健康寿命の差"
)
)

```


## 男性の平均寿命


```{r}
d_m %>% select(LE_2015) %>% bind_cols(Wakayama::pref["pref.J"]) %>% dplyr::arrange(LE_2015) %>% mutate(rank=row_number()) %>%DT::datatable()
```


```{r}
jc.dotplot <- function(x) {
# x is HLE or LE in c()　vector
names(x)<-Wakayama::pref$pref.J
x<-x[order(x)]

}

colfunc <- colorRampPalette(c("gray90","black"))

par(family= "HiraKakuProN-W3")

dotchart(
main = "平均寿命(2015年, 男性)",
jc.dotplot(d_m$LE_2015),
cex = 0.7,
lcolor = "gray90",
pch = 19,
col = colfunc(47),
pt.cex = 1.5
)

abline(v = 79, lty = 2)

```



## 男性の健康寿命

```{r}
d_m %>% select(HLE_2016) %>% bind_cols(Wakayama::pref["pref.J"]) %>% dplyr::arrange(HLE_2016) %>% mutate(rank=row_number()) %>%DT::datatable()
```


```{r}
jc.dotplot <- function(x) {
# x is HLE or LE in c()　vector
names(x)<-Wakayama::pref$pref.J
x<-x[order(x)]

}

colfunc <- colorRampPalette(c("gray90","black"))

par(family= "HiraKakuProN-W3")

dotchart(
main = "健康寿命(2016年, 男性)",
jc.dotplot(d_m$HLE_2016),
cex = 0.7,
lcolor = "gray90",
pch = 19,
col = colfunc(47),
pt.cex = 1.5
)

abline(v = 79, lty = 2)

```



## 女性の平均寿命


```{r}
d_f %>% select(LE_2015) %>% bind_cols(Wakayama::pref["pref.J"]) %>% dplyr::arrange(LE_2015) %>% mutate(rank=row_number()) %>%DT::datatable()
```


```{r}
jc.dotplot <- function(x) {
# x is HLE or LE in c()　vector
names(x)<-Wakayama::pref$pref.J
x<-x[order(x)]

}

colfunc <- colorRampPalette(c("gray90","black"))

par(family= "HiraKakuProN-W3")

dotchart(
main = "平均寿命(2015年, 女性)",
jc.dotplot(d_f$LE_2015),
cex = 0.7,
lcolor = "gray90",
pch = 19,
col = colfunc(47),
pt.cex = 1.5
)

abline(v = 79, lty = 2)

```





## 女性の健康寿命


```{r}
d_f %>% select(HLE_2016) %>% bind_cols(Wakayama::pref["pref.J"]) %>% dplyr::arrange(HLE_2016) %>% mutate(rank=row_number()) %>%DT::datatable()
```


```{r}
jc.dotplot <- function(x) {
# x is HLE or LE in c()　vector
names(x)<-Wakayama::pref$pref.J
x<-x[order(x)]

}

colfunc <- colorRampPalette(c("gray90","black"))

par(family= "HiraKakuProN-W3")

dotchart(
main = "平均寿命(2015年, 女性)",
jc.dotplot(d_f$HLE_2016),
cex = 0.7,
lcolor = "gray90",
pch = 19,
col = colfunc(47),
pt.cex = 1.5
)

abline(v = 79, lty = 2)

```




# `d_common data`の説明変数の順位確認及び正規性検定
{.tabset .tabset-fade .tabset-pills}

## `d_common data`の和歌山県の順位確認

```{r}
d_common %>% dplyr::select_if(is.numeric) %>% sapply(rank) %>%
tbl_df() %>%dplyr::filter(key==30) %>% t() %>% as.data.frame() %>% DT::datatable()
```


## `d_common data`の連続データ分布確認1

```{r, warning=FALSE}

# purrr::map(iris[,-5], ~hist(.x))

suppressMessages(library(plotly))


d_common_standarize<-
d_common %>% dplyr::select_if(is.numeric) %>%
select(-key, -pref.id) %>% scale() %>% tbl_df()

d_common_standarize<-bind_cols(d_common["pref.id"], d_common_standarize)


d_common_standarize_long<-

d_common_standarize %>% dplyr::select_if(is.numeric) %>%
pivot_longer(
cols = -pref.id,
names_to ="var_name" ,
values_to ="value"
)


plot_ly(
x =d_common_standarize_long$value,
type = "histogram",
name = "Histogram",
frame =  ~d_common_standarize_long$var_name
)


```


## `d_common data`の連続データ分布確認2

```{r}
name1 <- function(temp) {
temp %>% select(value) %>% .[[1]] %>% density() %>%
broom::tidy()
}

d_common_standarize_long_density<-
d_common_standarize_long %>% group_by(var_name) %>% nest() %>% mutate(dens=map(data, name1)) %>% select(var_name, dens) %>% unnest()

d_common_standarize_long_density %>% DT::datatable()

d_common_standarize_long_density %>%
plot_ly(x=~x, y=~y) %>%
add_lines(frame=~var_name)

# add_lines(color=~status) %>%
# storms %>%



```


```{r}
density <- density(diamonds$carat)

# diamonds$carat



fig <-
plot_ly(x = ~density$x, y = ~density$y, type = 'scatter', mode = 'lines', fill = 'tozeroy')
fig <- fig %>% layout(xaxis = list(title = 'Carat'),
                yaxis = list(title = 'Density'))

fig


```



## `d_common data`の連続データの正規性検定
- shapiro 検定

```{r, warning=FALSE}
jc_shapiro <- function(x) {
shapiro.test(x) %>% broom::tidy() %>% select(p.value) %>% round(3)
}


d_common_normality_test<-d_common %>% dplyr::select_if(is.numeric) %>%
select(-key, -pref.id) %>%
# scale() %>%
tbl_df() %>% purrr::map_df(jc_shapiro)

rownames(d_common_normality_test)<-d_common %>% dplyr::select_if(is.numeric) %>%
select(-key, -pref.id) %>% colnames()

DT::datatable(d_common_normality_test)
```


## `d_common data`連続データの正規性を満たさない変数
- **要対数変換：47個の変数**

```{r}
d_common_normality_test %>% filter(p.value<0.05) %>% DT::datatable()
```

# `d_common data` 和歌山,青森,滋賀,長野の説明変数の様子

```{r}
library(plotly)
temp<-left_join(d_common_standarize_long, d_common,
          by = c("pref.id"="key")) %>% select(pref.J, 2,3)


temp %>% filter(pref.J=="和歌山"|
            pref.J=="青森"|
            pref.J=="滋賀"|
            pref.J=="長野") %>%
plot_ly(y =  ~ pref.J,
    x =  ~ value,
    color =  ~ pref.J) %>%
add_bars(frame=~var_name)

```






# 出典整理
{.tabset .tabset-fade .tabset-pills}

## 出典元
-
```
for i in open("txt"):
if re.serach(「」, i)
print(i)
```

## 出典リンク先の詳細
#
# - [受療率_入院_悪性新生物_2017][1]
# - [受療率_入院_心疾患_2017][1]
# - [受療率_入院_脳血管疾患_2017][1]
# - [受療率_外来_悪性新生物_2017][1]
# - [受療率_外来_心疾患_2017][1]
# - [受療率_外来_脳血管疾患_2017][1]
# - [病院数_2019][2]
# - [診療所数_2019][2]
#
# - [がん治療認定医数_2020][3]
# - [循環器専門医数_2020][4]
# - [内視鏡専門医数_2020][5]
# - [75歳未満調整死亡率_悪性新生物_2018][6]
# - [書籍購入代金_2019][7]
# - [平均寿命_2015][8]
# - [健康寿命_2016][9]
# - [75歳未満調整死亡率_悪政新生物_2019][10]
# - [年齢調整死亡率_心疾患_2015][11]
# - [年齢調整死亡率_脳血管疾患_2015][11]
#
# - [60歳以上人口_2015][12]
# - [学習率_2016][13]
# - [読書率_2016][14]
#
#
# - [人口・世帯_年少人口割合2020][15]
# - [人口・世帯_老年人口割合2020][15]
# - [人口・世帯_生産年齢人口割合2020][15]
# - [人口・世帯_粗死亡率2020][15]
# - [人口・世帯_共働き世帯割合2020][15]
#
#
# - [自然環境_年平均気温][16]
# - [自然環境_年平均相対湿度][16]
# - [自然環境_降水量（年間）][16]
# - [自然環境_雪日数（年間）][16]
#
#
#
# - [経済基盤_県民所得][17]
#
#
#
# - [行政基盤_財政力指数][18]
#
# - [行政基盤_収支比率][19]
#
# - [行政基盤_生活保護費割合（県財政）][20]
#
# - [行政基盤_教育費割合（県財政）][21]
#
# - [教育_最終学歴が大学・大学院卒の者の割合][22]
#
# - [労働_１次産業就業者比率][23]
#
# - [労働_２次産業就業者比率][24]
#
# - [労働_３次産業就業者比率][25]
#
# - [労働_完全失業率][26]
#
# - [文化・スポーツ_図書館数（人口100万人当たり）][27]
#
# - [健康・医療_一般診療所数(可住地面積100k㎡当たり)][28]
#
#
# - [文化・スポーツ_スポーツの行動者率][29]
#
#
# - [文化・スポーツ_旅行・行楽行動者率][30]
#
#
#
#
# - [居住_持ち家比率][31]
#
# - [居住_一戸建住宅比率][32]
#
# - [居住_上水道給水人口比率][33]
#
# - [居住_下水道普及比率][34]
#
# - [文化・スポーツ_ボランティア活動行動者率][35]
#
# - [居住_都市公園面積（人口１人当たり）][36]
#
# - [居住_都市公園数(可住地面積100k㎡当たり)][37]
#
# - [健康・医療_一般病院数(可住地面積100k㎡当たり)][38]
#
# - [居住_主要道路舗装率][39]
#
# - [居住_市町村舗装率][40]
#
# - [健康・医療_一般歯科診療所数（人口10万人当たり）][41]
#
# - [健康・医療_医療施設に従事する医師数（人口10万人当たり）][42]
#
# - [健康・医療_保健師数（人口10万人当たり）][43]
#
# - [安全_交通事故発生件数（人口10万人当たり）][44]
#
# - [家計_実収入（一世帯当たり１か月）][34]
#
# - [家計_消費支出（一世帯当たり１か月）][34]
#
# - [家計_教育費割合（対消費支出）][34]
#
# - [家計_教養娯楽費割合（対消費支出）][34]
#
# - [家計_貯蓄現在高][34]
#
# - [家計_スマートフォン所有数量（千世帯当たり）][34]
#
# - [家計_パソコン所有数量（千世帯当たり）][34]
#
# - [家計_自動車所有数量（千世帯当たり）][34]
#
# - [家計_タブレット端末所有数量（千世帯当たり）][34]
#
#
#
#
# - [人口・世帯_高齢単身者世帯の割合][34]
#
# - [スポーツ総行動率][801]
#
# - [スポーツ総行動率-器具を使ったトレーニング][801]
#
# - [スポーツ行動率−ウォーキング][801]
#
# - [旅行・行楽−旅行・行楽・観光総行動率][804]
#
# - [旅行・行楽−旅行率][804]
#
# - [旅行・行楽−行楽率][804]
#
# - [旅行・行楽−観光率][804]
#
# - [ボランティア総行動率−総数][808]
#
# - [ボランティア総行動率−まちづくり活動][808]
#
# - [ボランティア総行動率−国際協力活動][808]
#
# - [ボランティア総行動率−健康や医療サービスに関係した活動][808]
#
# - [ボランティア総行動率−高齢者を対象とした活動][808]
#
# - [ボランティア総行動率−障害者を対象とした活動][808]
#
# - [ボランティア総行動率−子供を対象とした活動][808]
#
# - [趣味・娯楽−趣味娯楽総行動率][815]
#
# - [趣味・娯楽−園芸・庭いじり・ガーデニング][815]
#
# - [趣味・娯楽−スポーツ観覧][815]
#
# - [趣味・娯楽−読書][815]
#
# - [自己啓発・訓練−学習・自己啓発・訓練率][819]
#
# - [自己啓発・訓練−芸術・文化][819]
#
# - [自己啓発・訓練−英語][819]
#
# - [自己啓発・訓練−英語以外の外国語][819]
#
# - [自己啓発・訓練−パソコンなどの情報処理][819]
#
# - [ボランティア活動−安全な生活のための活動][824]
#
# - [ボランティア活動−自然や環境の活動][824]
#
# - [ボランティア活動−災害活動][824]
#
# - [高血圧疾患_入院2014年][901]
#
# - [高血圧疾患_外来2014年][901]
#
# - [糖尿病_入院2014年][901]
#
# - [糖尿病_外来2014年][901]
#
# - [脳血管疾患_年齢調整死亡率2015][905]
#
# - [悪性新生物(胃)_年齢調整死亡率2015][906]
#
# - [悪性新生物(大腸)_年齢調整死亡率2015][907]
#
# - [悪性新生物(肝及び肝内胆管)_年齢調整死亡率2015][908]
#
# - [悪性新生物(気管、気管支及び肺)_年齢調整死亡率2015][909]
#
# - [悪性新生物(乳房)_年齢調整死亡率2015][910]
#
# - [悪性新生物(子宮)_年齢調整死亡率2015][911]
#
# - [心疾患_年齢調整死亡率2015][912]
#
# - [肺炎_年齢調整死亡率2015][913]
#
# - [急性心筋梗塞_年齢調整死亡率2015][914]
#
# - [血圧を下げる薬の使用_回答・はい(40〜64歳)2014][915]
#
# - [インシュリン注射、血糖を下げる薬の使用_回答・はい(40〜74歳)2014][916]
#
# - [コレステロールを下げる薬の使用_回答・はい(40〜74歳)2014][917]
#
# - [就寝前の2時間以内に夕食_回答・はい(40〜74歳)2014][918]
#
# - [日常生活において歩行等の身体活動(1日1時間以上実施)_回答・はい(40〜74歳)2014][919]
#
# - [軽く汗をかく運動週2回_回答・はい(40〜74歳)2014][920]
#
# - ["喫煙率(計100本以上,6ヵ月以上&直近1ヵ月)_回答・はい(40〜74歳)2014"][921]
#
# - [20歳に比べて10kg体重増加.回答_はい(40〜74歳)2014][922]
#
# - [歩く速度が速い(同年齢と比較).回答_はい(40〜74歳)2014][923]
#
# - [飲酒日1日当たり2合以上飲む割合(頻度)_回答・はい(40〜74歳)2014][924]
#
# - [毎日酒を飲む割合(頻度)_回答・はい(40〜74歳)2014][925]
#
# - [睡眠休養が十分とれている.回答_はい(40〜74歳)2014][926]
#
# - [朝食を抜くことが週3回ある.回答_はい(40〜74歳)2014][927]
#
# - [夕食後に間食することが週3回ある.回答_はい(40〜74歳)2014][928]
#
# - [肉類_2014][401]
#
# - [魚介類_2014][402]
#
# - [牛乳_2014][403]
#
# - [乳製品_2014][404]
#
# - [卵_2014][405]
#
# - [大豆_2014][406]
#
# - [一定のバリアフリー化率手すりの設置_2013][501]
#
# - [50一定のバリアフリー化率段差のない屋内_2013][502]
#
# - [50高度のバリアフリー化率手すりの設置_2013][503]
#
# - [50高度のバリアフリー化率段差のない屋内_2013][504]
#
# - [50高度のバリアフリー廊下等が車いすで通行可能な幅_2013][505]
#
# - [50総実労働時間_2016][506]
#
# - [50現金給与総額_2016][507]
#
# - [50生鮮肉(世帯数消費支出)_2014][508]
#
# - [50生鮮肉(世帯数消費支出)_2015][509]
#
# - [50生鮮肉(世帯数消費支出)_2016][510]
#
# - [50生鮮肉平均_世帯数消費支出(2014〜2016）][511]
#
# - [菓子類(世帯数消費支出)_2014][512]
#
# - [菓子類(世帯数消費支出)_2015][513]
#
# - [菓子類(世帯数消費支出)_2016][514]
#
# - [菓子類平均_世帯数消費支出(2014〜2016）][515]
#
# - [果物(世帯数消費支出)_2014][516]
#
# - [果物(世帯数消費支出)_2015][517]
#
# - [果物(世帯数消費支出)_2016][518]
#
# - [果物平均_世帯数消費支出(2014〜2016）][519]
#
# - [全国学力・学習状況(公立学校数)(中学校)_2015][520]
#
# - [全国学力・学習状況(公立学校数)(小学生)_2015][521]
#
# - [う蝕外来総数_2014][522]
#
# - [歯周疾患(歯肉炎)外来総数_2014][523]
#
# - [骨の密度障害_2014][524]
#
# - [骨折_2014][525]
#
# - [歯の補てつ_2014][526]
#
# - [アルツハイマー等(脳血管疾患)_2014][527]
#
# - [ジニ係数総世帯_2014][528]
#
# - [収入ジニ係数勤労世帯_2014][529]
#
# - [野菜摂取量_2012(20歳以上平均値(g/日)][530]
#
# - [食塩摂取量_2012(20歳以上平均値(g/日)][531]
#
# - [BMI平均値_2012(男性20〜69歳)(女性40〜69歳)(単位Kg/㎡)][532]
#
# - [歩数_2012(20歳以上平均値(歩/日)][533]

#
# ## リンク先の修正箇所
#
# ＜追記修正箇所等＞
# - V列
# 熊本県の欠損値について、国の示す推定方法により数値を記載
# ー熊本県女性の健康寿命の推定値
#
#
# - FI列、FJ列、FK列、FL列
# 収集元データの年度修正（新しいデータに置き換え）
#
# - 野菜摂取量_2016(20歳以上平均値(g/日)
# - 食塩摂取量_2016(20歳以上平均値(g/日)
# - BMI平均値_2016(男性20〜69歳)(女性40〜69歳)(単位Kg/u)
# - 歩数_2016(20歳以上平均値(歩/日)
#
#
# - DH列、DI列、DJ列、DK列のデータ収集元URLを修正
#
# >  悪性新生物(子宮)_年齢調整死亡率2015
# - 心疾患_年齢調整死亡率2015
# - 肺炎_年齢調整死亡率2015
# - 急性心筋梗塞_年齢調整死亡率2015
#
# - （✕「患者調査」から→〇「人口動態統計特殊報告」）
#
#
#
# - EF列、EG列、EH列、EI列、EJ列
# - バリアフリー化の**総数**であったものをバリアフリー化**率に置き換え**
# - 一定のバリアフリー化率_2018
# - 高度のバリアフリー化率_2018
# - バリアフリー_手すりがある2018
# - バリアフリー_廊下などが車いすで通行可能な幅2018
# - バリアフリー_段差のない屋内2018
# -（バリアフリー化率の出典元を発見
#
#
#
# <!-- # 出典 -->
# ```{r child="ref.Rmd"}
#
# ```
#
#
#
#
# **/Users/jclee/Dropbox/00000健康和歌山県/0 wakayamaPkg/変数説明byJc.txt
# 参考
# と
# /Users/jclee/Dropbox/00000健康和歌山県/0 wakayamaPkg/working/slide/ref.Rmd
# を比較して記入する！！
# 記入完了令和3年2月26日
# **
#
#
# # 説明変数の標準化と計量化(scoring)
# -  variable combining
#
#
#
# #  ヘルスケア産業の創出や健康経営の推進に係る要因分析??
#
# ヘルスケア産業とは
#
#
# ①経済産業省におけるヘルスケア産業政策について
# https://www.meti.go.jp/policy/mono_info_service/healthcare/01metihealthcarepolicy.pdf
#
#
# ②健康経営の推進について
# https://www.meti.go.jp/policy/mono_info_service/healthcare/downloadfiles/180710kenkoukeiei-gaiyou.pdf
#
#
# ③中小企業への健康経営の普及
# https://www.meti.go.jp/policy/mono_info_service/healthcare/downloadfiles/191030chushohenofukyu.pdf
#
#
#
# 〇経済産業省－ヘルスケア産業ホームページ
# https://www.meti.go.jp/policy/mono_info_service/healthcare/index.html
#
#
#
# 利用出来そうなデータ①
#
# 〇オープンデータ
#
#
# ●わかやま健康推進事業所（和歌山県健康推進課の取組）
# ・「わかやま健康づくりチャレンジ運動サポート企業」登録事業所一覧
# ・「わかやま健康づくりチャレンジ運動」登録事業所一覧
# ・「わかやま健康推進事業所」認定事業所一覧
# https://www.pref.wakayama.lg.jp/prefg/041200/h_kenkou/d00156483.html
#
#
# ●健康経営優良法人2020（大規模法人部門）認定法人一覧 　など（経済産業省の取組）
# https://www.meti.go.jp/policy/mono_info_service/healthcare/kenkoukeiei_yuryouhouzin.html
#
#
# ●健康経営度調査結果集計データ（平成26年度～令和元年度）Excelファイル（経済産業省）
# https://www.meti.go.jp/policy/mono_info_service/healthcare/kenko_keiei.html
#
#
# 分析イメージ（案）
#
#
# 〇経済産業省が実施している企業活動基本調査の統計ミクロデータと帝国データバンクや東京商工
# リサーチの企業データを接続して生産性の分析
#
# 〇「わかやま健康推進事業所」に認定されている企業へのアンケート調査の実施
#
# 〇健康経営の推進が生産性向上に繋がる一つのファクターでは。生産性を上げるには設備投資や
# ＩＴ化などがあるが、相関がみられるかも。
#
# 〇横軸に「わかやま健康推進事業所」認定にあたっての評価ポイントを、縦軸に従業員あたりの生産性
# をとり、複数の企業をプロットしてみる。
#
# 〇上記の場合、同業種においてプロットする。病院や郵便局などの判定は難しい。
#
# 〇近々、経済センサス基礎調査の２０１９が公表される。事業名を含んだ調査票情報を取得できれば
# 分析できるのでは。
