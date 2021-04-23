# # setwd("C:\\Users\\ds-pcr113a\\Dropbox\\00000健康衛生(滋賀県)\\data\\R")
# load("HL.Rdata")

# data import
library(readxl)

# system("open .")
d<-read_excel("./data1.xlsx",1); d<-d[-95,] #男女データ
f<-d[d$sex==0,];m<-d[d$sex==1,] # 男女別分けデータ

getwd()


LE<-d[, c("LE.75","LE.85","LE.90","LE.95","LE.00","LE.05","LE.10","LE.15")]





tt<-Wakayama::pref %>% bind_rows(Wakayama::pref) %>% bind_cols(LE) %>% tbl_df()

tt1<-tt %>% bind_cols(sex=d$sex) %>% select(sex, everything())

tt2<-tt1 %>% pivot_longer(cols=5:12, names_to="year", values_to="LE") %>%
        group_by(year, sex) %>% mutate(rank=rank(-LE)) %>% ungroup()

tt2 %>% filter(tt2$pref.E=="Wakayama")


wakayama_m<-tt2 %>% filter(tt2$pref.E=="Wakayama") %>% select(5, 6, 7) %>%
  .[1:8, ]


wakayama_f<-tt2 %>% filter(tt2$pref.E=="Wakayama") %>% select(5, 6, 7) %>%
  .[9:16, ]


zwakayama_m %>% bind_cols(wakayama_f) %>% xtable::xtable()

wakayama_f

tt2 %>% plot_ly() %>%
  add_lines(x=~year, y=~LE, color=~interaction(sex, pref.J),
            hoverinfo="text",
            text=paste("平均寿命", tt2$LE, tt2$pref.J)
          )

tt2$pref.E








#----- plot 開始--------------------
pdf("WakayamaTrend.pdf", family = "Japan1")


# par(family= "HiraKakuProN-W3")
matplot(t(LE) ,  xlab="", ylab="", type="n", axes=F, xlim=c(0.5, 8.5))
matpoints(t(LE) ,  xlab="", ylab="", type="l",
          col=rgb(26/255,26/255,26/255, alpha=0.05),
          lty=rep(1,47),
          lwd=3)
axis(side=1,
     labels=c("1975年", "1985年", "1990年", "1995年", "2000年", "2005年", "2010年", "2015年"),
     at=1:8,
     las=3,
     cex.axis = 1.5)
axis(side=2,
     labels=c("70歳", "75歳", "80歳", "85歳", "90歳"),
     at=seq(70,90,5),
     cex.axis=1.5)
text(2, 85, "女性", cex=2)
text(4, 80, "男性", cex=2)

# 和歌山県
matpoints(t(LE[c(30,30+47),]) , type="l",
          col=rgb(0,0,1, alpha=0.7),
          lty=rep(1,47), lwd=2)

# 滋賀県
matpoints(t(LE[c(25,25+47),]) , type="l",
          col=rgb(0,1,0, alpha=0.7),
          lty=rep(1,47), lwd=1)
# 長野県
matpoints(t(LE[c(20,20+47),]) , type="l",
          col=rgb(1,0,0, alpha=0.7),
          lty=rep(2,2), lwd=1)
legend("bottomright", c("和歌山", "長野", "滋賀", "その他(44都道府県)"),
       lty=c(1,2,1, 1),
       col=c("blue","red", "green", "gray"),
       lwd=c(2,2,2), cex=1.5)


#　男性の順位
text(c(1,2,3,4,5,6,7,8),
     c(71.51, 75.34, 76.36, 77.13, 78.19,  79.6, 80.58, 81.78)-1,
     c("28位","40位","44位","44位","41位","42位","37位","44位"),#<-和歌山県順位
     # c("22位", "11位", "12位", "12位", "6位","2位","2位","1位") ,
     cex=1.5)

#　女性の順位
text(c(1,2,3,4,5,6,7,8),
     c(76.47, 80.63, 81.88,  83.2, 84.92, 86.17, 86.69, 87.57)-0.5,
     # c("37位",  "30位",  "37位",  "30位",  "15位",  "12位",  "12位",   "4位"),
     c("22.5位","43位","40位","44位","41位","41位","45位","41位"),#<-和歌山県順位
     cex=1.5)
title(main="和歌山県の平均寿命順位推移", cex.main=2)
dev.off()

#----- plot end--------------------




#----- plot end--------------------



