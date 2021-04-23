# 使用package
suppressMessages(library(readxl))
suppressMessages(library(dplyr))
suppressMessages(library(data.table))
suppressMessages(library(kableExtra))
suppressMessages(library(curl))
suppressMessages(library(tidyverse))


#  "DataFormat.csv" data from Wakayama received from R2 11. 2
#  latest version 2021年2月10日


# ----------------- data import
getwd()
d<-read_csv("data/DataFormat.csv", skip=1, locale = readr::locale(encoding = "CP932"))
# d<-read_csv("data/DataFormat.csv", skip=1)
d<-d[-95,]
d %>% dim()
d<-d %>% rename(key=X1)
d %>% colnames() %>% head()
# d %>% colnames() %>% tbl_df() %>%
#   write_csv("var_name_Jpn.csv")
var<-read.csv("var_name_Eng.csv")


# ----------------- data varname change
d
colnames(d)<-var$var_name_Eng

d %>% select(contains("dz"))


# -----------------　data Jpn and Eng table

# 連番

JpnEng <-
  read_csv(file = "var_name_Jpn.csv") %>% bind_cols(., read_csv(file = "var_name_Eng.csv")) %>%
  mutate(id = row_number()) %>%
  select(id, everything())

# write_csv(JpnEng, "JpnEng.csv")


# ----------------- descriptve stat

# install.packages("DataExplorer")
library(DataExplorer)


# d %>% select(Treatment_rate_Hospitalization_Malignant_neoplasm_2017:pop_Double_income_household_ratio_2020) %>%
# DataExplorer::create_report()

# -----------------　男女区別のないデータ d_common
# [1] 47 98


d_common<-d[, sapply(d[48,], is.na)]

d_common<-d_common[1:47, ]

d_common%>% DT::datatable()

d_common %>% dim()



# -----------------　男女区別のあるデータ d_mf
# [1] 94 70

name <- function(x) {
  !is.na(x)
}
d_mf<-d[, sapply(d[48,], name)]

d_mf %>% DT::datatable()
d_mf %>% dim()

summary(d_mf)

ls()=


d_m<-d_mf %>% filter(sex=="M")
d_f<-d_mf %>% filter(sex=="F")







d_m

d_f




# [1] "d"
"d_common"
"d_mf"



# -----------------
# ignore belows
# ignore belows
# ignore belows
# ignore belows
# ignore belows
# ignore belows
# ignore belows



colnames(temp)
temp %>% select_if(is.character)

temp %>% select(contains("BMI")) %>% c()

%>% as.numeric()

temp$`BMI平均値_2012(男性20〜69歳)(女性40〜69歳)(単位Kg/㎡)`

temp %>% select(`BMI平均値_2012(男性20〜69歳)(女性40〜69歳)(単位Kg/㎡)`="−")



# aa<-read.csv("DataFormat.csv", fileEncoding = "cp932") %>% dim()
# aa<-read.csv("DataFormat.csv", fileEncoding = "cp932")

aa %>% select(contains("寿命")) %>% colnames()
aa<-aa %>% select(平均寿命_2015 , 健康寿命_2016, everything())

aa %>%select(-"人口")

aa %>% colnames()


#  出典

# 変数名：受療率
# 出典：患者調査
# 取得元：以下のリンク

# https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00450022&tstat=000001031167&cycle=7&tclass1=000001124800&tclass2=000001124802

# 詳細説明：
# ・「第17表　受療率（人口10万対），入院－外来・施設の種類 × 傷病分類 × 都道府県別」をダウンロード
# ・「入院_悪性新生物_2017」は、B列の中で、A列が「（悪性新生物＜腫瘍＞）（再掲）」となっているものを取得し、
# ・DataFormat.csvのH列に転記

# ・「入院_心疾患_2017」は、B列の中で、A列が「（心疾患（高血圧性のものを除く））（再掲）」となっているものを取得し、
# ・DataFormat.csvのI列に転記

# ・「入院_脳血管疾患_2017」は、B列の中で、A列が「脳血管疾患（再掲）」となっているものを取得し、
# ・DataFormat.csvのJ列に転記

# ・「外来_悪性新生物_2017」は、E列の中で、A列が「（心疾患（高血圧性のものを除く））（再掲）」となっているものを取得し、
# ・DataFormat.csvのK列に転記

# ・「外来_心疾患_2017」は、E列の中で、A列が「脳血管疾患（再掲）」となっているものを取得し、
# ・DataFormat.csvのL列に転記

# ・「外来_脳血管疾患_2017」は、E列の中で、A列が「脳血管疾患（再掲）」となっているものを取得し、
# ・DataFormat.csvのM列に転記
# ###########################################################################################################################
# 変数名：施設数
# 出典：平成 26 年(2014)医療施設（静態・動態）調査・病院報告
# の概況
# 取得元：以下のリンク

# https://www.mhlw.go.jp/toukei/saikin/hw/iryosd/14/

#   詳細説明：
# ・「統計表」をダウンロード
# ・「病院数_2014」は、39ページの「統計表1 施設の種類別にみた施設数・病床数及び人口10万人対施設数・病床数の年次推移」から、「病院（人口10万対施設数）」の「26年(′14）」から取得し、
#・DataFormat.csvのN列に転記

#・「診療所数_2014」は、39ページの統計表1 施設の種類別にみた施設数・病床数及び人口10万人対施設数・病床数の年次推移」から、「一般診療所（人口10万対施設数）」の「26年(′14）」から取得し、
#  ・DataFormat.csvのO列に転記
#  #############################################################
#  変数名：がん治療認定医数_2020
#  出典：がん治療認定医名簿（2020年4月1日現在)
#取得元：以下のリンク

#https://www.jbct.jp/general/figure.html

#詳細説明：
#・「認定医総数（2020年4月1日現在）　都道府県別認定医数一覧」をダウンロード
#・「全国都道府県別　認定医総数」の「合計」を取得、
#・DataFormat.csvのP列に転記
##############################################################
#変数名：循環器専門医数_2020
#出典：会員名簿・循環器専門医名簿（2020年4月1日現在）
#取得元：以下のリンク

#https://www.j-circ.or.jp/senmoni_kensaku/

#  詳細説明：
#・リンク先Webサイトより、「専門医名簿検索」によって各都道府県の専門医を検索、
#・DataFormat.csvのQ列に転記
##############################################################
#変数名：内視鏡専門医数_2020
#出典：会員名簿（2020年4月1日現在）
#取得元：以下のリンク

#https://www.jges.net/medical/about/list/memberlist#92

#詳細説明：
#・各都道府県の「会員名簿」を参照し、名簿に記載されている医師名の数を集計
#・DataFormat.csvのR列に転記
##############################################################
#変数名：75歳未満調整死亡率_悪性新生物_2018
#出典：がんに関する統計データのダウンロード
#取得元：以下のリンク

#https://ganjoho.jp/reg_stat/statistics/dl/index.html#pref_mortality

#詳細説明：
#・「全がん死亡率・粗死亡率・年齢調整死亡率（1995年～2018年）をダウンロード
#・シート「asr75」の「AA列」より2018年の男女計75歳未満年齢調整死亡率を取得
#・DataFormat.csvのS列に転記
##############################################################
#変数名：60歳以上人口_2015
#出典：平成27年国勢調査
#取得元：以下のリンク

#http://www.stat.go.jp/data/kokusei/2015/kekka.html

#詳細説明：
#・「人口等基本集計結果　概要（第2部　資料）」をダウンロード
#・51ページから66ページにかけて記載されている「年齢（5歳階級）、男女別人口、年齢別割合、平均年齢及び年齢中位数」より、各都道府県ごとの「60～64、65～69、70～71、75～79、80～84、85～89、90～94、95～99、100歳以上」の、総数の値を足し合わせて60歳以上人口を算出、
#・DataFormat.csvのT列に転記
##############################################################
#変数名：学習率_2016
#出典：平成28年社会生活基本調査
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200533&tstat=000001095335&cycle=0&tclass1=000001095377&tclass2=000001095378&tclass3=000001095386&tclass4=000001095387

#詳細説明：
#・「70-1　男女,学習・自己啓発・訓練の種類別行動者数（10歳以上）-全国,都道府県」をダウンロード
#・N列「行動者率　学習・自己啓発・訓練の種類　0_総数」の中で、F列において「0_総数」であり、かつH列において「0_総数」となっているものを取得、
#・DataFormat.csvのU列に転記
#############################################################
#変数名：読書率_2016
#出典：平成28年社会生活基本調査
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200533&tstat=000001095335&cycle=0&tclass1=000001095377&tclass2=000001095378&tclass3=000001095386&tclass4=000001095389

#詳細説明：
#・「86-2　男女,趣味・娯楽の種類別行動者率（10歳以上）-全国,都道府県」をダウンロード
#・AO列「行動者率　趣味・娯楽の種類　27_趣味としての読書」の中で、F列において「0_総数」であり、かつH列において「0_総数」となっているものを取得、
#・DataFormat.csvのV列に転記
#############################################################
#変数名：書籍購入代金_2017
#出典：家計調査　家計収支編　二人以上の世帯　詳細結果表
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200561&tstat=000000330001&cycle=7&year=20170&month=0&tclass1=000000330001&tclass2=000000330004&tclass3=000000330005&result_back=1

#詳細説明：
#・「第4-1表　都道府県庁所在地別　1世帯当たり年間の支出金額、購入数量及び平均価格　二人以上の世帯」をダウンロード
#・各都道府県所在市の「支出金額」の中で、「品目分類　9.3　書籍・他の印刷物」となっているものを取得
#・DataFormat.csvのW列に転記
#############################################################
#変数名：平均寿命_2015
#出典：平成27年都道府県別生命表の概況
#取得元：以下のリンク

#https://www.mhlw.go.jp/toukei/saikin/hw/life/tdfk15/index.html

#詳細説明：
#・「都道府県別にみた平均寿命の推移」をダウンロード
#・男性の平均寿命は「表5-1　平均寿命の推移（男）」より「平成27年」のものを、女性の平均寿命は「表5-2　平均寿命の推移（女）」より「平成27年」のものを取得
#・DataFormat.csvのX列に転記
#############################################################
#変数名：健康寿命_2016
#出典：厚生労働科学研究　健康寿命のページ
#取得元：以下のリンク

#http://toukei.umin.jp/kenkoujyumyou/

#  詳細説明：
#・「都道府県別健康寿命（2010～2016年）」をダウンロード
#・男性の健康寿命はシート「付表1-1」より「I列」の2016年の推定値を、女性の健康寿命はシート「付表1-2」より「I列」の2016年の推定値を取得
#・DataFormat.csvのY列に転記

#・国民生活基礎調査は熊本地震により2016年の熊本県の健康情報を調査していないため、熊本県の2016年健康寿命のデータはない
#############################################################
#変数名：75歳未満調整死亡率_悪性新生物_2018
#出典：がんに関する統計データのダウンロード
#取得元：以下のリンク

#https://ganjoho.jp/reg_stat/statistics/dl/index.html#pref_mortality

#詳細説明：
#・「全がん死亡率・粗死亡率・年齢調整死亡率（1995年～2018年）をダウンロード
#・シート「asr75」の「AA列」より2018年の男女別の75歳未満年齢調整死亡率を取得
#・DataFormat.csvのZ列に転記
#############################################################
#変数名：年齢調整死亡率_2015
#出典：平成27年度都道府県別年齢調整死亡率の概況
#取得元：以下のリンク

#https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/other/15sibou/index.html

#詳細説明：
#・「参考2　主な死因,性,都道府県別年齢調整死亡率（人口10万対）・順位　-平成27年-」をダウンロード
#・「年齢調整死亡率_心疾患_2015」は、31ページの「心疾患」列より取得
#・DataFormat.csvのAA列に転記

#・「年齢調整死亡率_脳血管疾患_2015」は、32ページの「脳血管疾患」列より取得
#・DataFormat.csvのAB列に転記
#############################################################
#変数名：60歳以上人口_2015
#出典：平成27年国勢調査
#取得元：以下のリンク

#http://www.stat.go.jp/data/kokusei/2015/kekka.html

#詳細説明：
#・「人口等基本集計結果　概要（第2部　資料）」をダウンロード
#・51ページから66ページにかけて記載されている「年齢（5歳階級）、男女別人口、年齢別割合、平均年齢及び年齢中位数」より、各都道府県ごとに男女別の「60～64、65～69、70～71、75～79、80～84、85～89、90～94、95～99、100歳以上」の値を足し合わせて60歳以上人口を算出
#・DataFormat.csvのAC列に転記
#############################################################
#変数名：学習率_2016
#出典：平成 28 年社会生活基本調査
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200533&tstat=000001095335&cycle=0&tclass1=000001095377&tclass2=000001095378&tclass3=000001095386&tclass4=000001095387

#詳細説明：
#・「70-1　男女,学習・自己啓発・訓練の種類別行動者数（10歳以上）-全国,都道府県」をダウンロード
#・男性の学習率は、N列「行動者率　学習・自己啓発・訓練の種類　0_総数」の中で、F列において「1_男」であり、かつH列において「0_総数」となっているものを取得、
#・女性の学習率は、N列「行動者率　学習・自己啓発・訓練の種類　0_総数」の中で、F列において「2_女」であり、かつH列において「0_総数」となっているものを取得、
#・DataFormat.csvのAD列に転記
#############################################################
#変数名：読書率_2016
#出典：平成28年社会生活基本調査
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200533&tstat=000001095335&cycle=0&tclass1=000001095377&tclass2=000001095378&tclass3=000001095386&tclass4=000001095389

#詳細説明：
#・「86-2　男女,趣味・娯楽の種類別行動者率（10歳以上）-全国,都道府県」をダウンロード
#・男性の読書率は、AO列「行動者率　趣味・娯楽の種類　27_趣味としての読書」の中で、F列において「1_男」であり、かつH列において「0_総数」となっているものを取得、
#・女性の読書率は、AO列「行動者率　趣味・娯楽の種類　27_趣味としての読書」の中で、F列において「2_女」であり、かつH列において「0_総数」となっているものを取得、
#・DataFormat.csvのAE列に転記
#############################################################
#変数名：人口・世帯
#出典：統計でみる都道府県のすがた2020
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200502&tstat=000001137306&cycle=0&year=20200&month=0&tclass1=000001137307

#詳細説明：
#・「A　人口・世帯」をダウンロード
#・年少人口割合は、AD列「15歳未満人口割合（対総人口）」を取得し、
#・DataFormat.csvのAF列に転記

#・老年人口割合は、AF列「65歳以上人口割合（対総人口）」を取得し、
#・DataFormat.csvのAG列に転記

#・生産年齢人口割合は、AH列「15～64歳人口割合（対総人口）」を取得し、
#・DataFormat.csvのAH列に転記

#・粗死亡率は、AX列「粗死亡率（人口千人当たり）」を取得し、
#・DataFormat.csvのAI列に転記

#・共働き世帯割合は、CH列「共働き世帯割合（対一般世帯数）」を取得し、
#・DataFormat.csvのAJ列に転記
#############################################################
#変数名：自然環境
#出典：統計でみる都道府県のすがた2020
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200502&tstat=000001137306&cycle=0&year=20200&month=0&tclass1=000001137307

#詳細説明：
#・「B　自然環境」をダウンロード
#・年平均気温は、V列「年平均気温」を取得し、
#・DataFormat.csvのAK列に転記

#・年平均相対湿度は、AB列「年平均相対湿度」を取得し、
#・DataFormat.csvのAL列に転記

#・降水量（年間）は、AF列「降水量（年間）」を取得し、
#・DataFormat.csvのAM列に転記

#・雪日数（年間）は、AL列「雪日数（年間）」を取得し、
#・DataFormat.csvのAN列に転記
#############################################################
#変数名：経済基盤
#出典：統計でみる都道府県のすがた2020
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200502&tstat=000001137306&cycle=0&year=20200&month=0&tclass1=000001137307

#詳細説明：
#・「C　経済基盤」をダウンロード
#・県民所得は、L列「１人当たり県民所得」を取得し、
#・DataFormat.csvのAK列に転記
#############################################################
#変数名：行政基盤
#出典：統計でみる都道府県のすがた2020
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200502&tstat=000001137306&cycle=0&year=20200&month=0&tclass1=000001137307

#詳細説明：
#・「D 　行政基盤」をダウンロード
#・財政力指数は、L列「財政力指数(都道府県財政)」を取得し、
#・DataFormat.csvのAP列に転記
#############################################################
#変数名：行政基盤
#出典：統計でみる都道府県のすがた2020
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200502&tstat=000001137306&cycle=0&year=20200&month=0&tclass1=000001137307

#詳細説明：
#・「D 　行政基盤」をダウンロード
#・収支比率は、N列「実質収支比率(都道府県財政)」を取得し、
#・DataFormat.csvのAQ列に転記
#############################################################
#変数名：行政基盤
#出典：統計でみる都道府県のすがた2020
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200502&tstat=000001137306&cycle=0&year=20200&month=0&tclass1=000001137307

#詳細説明：
#・「D 　行政基盤」をダウンロード
#・生活保護費割合は、AT列「生活保護費割合（対歳出決算総額）(都道府県財政)」を取得し、
#・DataFormat.csvのAR列に転記
#############################################################
#変数名：行政基盤
#出典：統計でみる都道府県のすがた2020
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200502&tstat=000001137306&cycle=0&year=20200&month=0&tclass1=000001137307

#詳細説明：
#・「D 　行政基盤」をダウンロード
#・教育費費割合は、BJ列「教育費割合（対歳出決算総額）(都道府県財政)」を取得し、
#・DataFormat.csvのAS列に転記
#############################################################
#変数名：教育
#出典：統計でみる都道府県のすがた2020
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200502&tstat=000001137306&cycle=0&year=20200&month=0&tclass1=000001137307

#詳細説明：
#・「E　教育」をダウンロード
#・最終学歴が大学・大学院卒の者の割合は、CF列「最終学歴が大学・大学院卒の者の割合（対卒業者総数）」を取得し、
#・DataFormat.csvのAT列に転記
#############################################################
#変数名：労働
#出典：統計でみる都道府県のすがた2020
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200502&tstat=000001137306&cycle=0&year=20200&month=0&tclass1=000001137307

#詳細説明：
#・「F．労働」をダウンロード
#・１次産業就業者比率は、P列「第１次産業就業者比率（対就業者）」を取得し、
#・DataFormat.csvのAU列に転記
#############################################################
#変数名：労働
#出典：統計でみる都道府県のすがた2020
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200502&tstat=000001137306&cycle=0&year=20200&month=0&tclass1=000001137307

#詳細説明：
#・「F．労働」をダウンロード
#・２次産業就業者比率は、R列「第２次産業就業者比率（対就業者）」を取得し、
#・DataFormat.csvのAV列に転記
#############################################################
#変数名：労働
#出典：統計でみる都道府県のすがた2020
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200502&tstat=000001137306&cycle=0&year=20200&month=0&tclass1=000001137307

#詳細説明：
#・「F．労働」をダウンロード
#・３次産業就業者比率は、T列「第３次産業就業者比率（対就業者）」を取得し、
#・DataFormat.csvのAW列に転記
#############################################################
#変数名：労働
#出典：統計でみる都道府県のすがた2020
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200502&tstat=000001137306&cycle=0&year=20200&month=0&tclass1=000001137307

#詳細説明：
#・「F．労働」をダウンロード
#・完全失業率は、V列「完全失業率（完全失業者数／労働力人口）」を取得し、
#・DataFormat.csvのAX列に転記
#############################################################
#変数名：文化・スポーツ
#出典：統計でみる都道府県のすがた2020
#取得元：以下のリンク

#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200502&tstat=000001137306&cycle=0&year=20200&month=0&tclass1=000001137307

#詳細説明：
#・「G．文化・スポーツ」をダウンロード
#・図書館数は、N列「図書館数（人口100万人当たり）」を取得し、
#・DataFormat.csvのAY列に転記
#############################################################
