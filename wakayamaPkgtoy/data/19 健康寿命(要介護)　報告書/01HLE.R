# data import
library(readxl)
library(RColorBrewer)

d<-read_excel("./data1.xlsx",1); d<-d[-95,] #男女データ

HLE<-d[, c("pref.J","sex", "HLE.CSS.13", "LE.75","LE.85","LE.90","LE.95","LE.00","LE.05","LE.10","LE.15")]
pref<-d$pref.J[1:47]
HLE<-split(HLE, HLE$sex)

m<-HLE$`1`
f<-HLE$`0`



jc.m <- function(year){
  tt<-eval(parse(text=paste0("m","$",year)))
  names(tt)<-m$pref.J
  tt<-tt[order(tt)]
  return(tt)}

jc.f <- function(year){
  tt<-eval(parse(text=paste0("f","$",year)))
  names(tt)<-f$pref.J
  tt<-tt[order(tt)]
  return(tt)}


colfunc <- colorRampPalette(c("gray90","black"))
aa<-colfunc(47)


pdf("./res/kenko.pdf", family="Japan1")
par(mfrow=c(1,2))
dotchart(main="健康寿命(2013年, 男性)",jc.m("HLE.CSS.13"),cex = 0.7,
         lcolor = "gray90", pch=19, col=aa, pt.cex=1.5)
abline(v=79, lty=2)

dotchart(main="健康寿命(2013年, 女性)",jc.f("HLE.CSS.13"),cex = 0.7,
         lcolor = "gray90", pch=19, col=aa, pt.cex=1.5)
abline(v=83.5, lty=2)
par(mfrow=c(1,1))
dev.off()


#  ------------------------------------------------------------------------


pdf("./res/kenko.pdf", family="Japan1")
par(mfrow=c(1,2))
dotchart(main="健康寿命(2013年, 男性)",jc.m("HLE.CSS.13"),cex = 0.7,
         lcolor = "gray90", pch=19, pt.cex=1.5)
abline(v=79, lty=2)

dotchart(main="健康寿命(2013年, 女性)",jc.f("HLE.CSS.13"),cex = 0.7,
         lcolor = "gray90", pch=19, pt.cex=1.5)
abline(v=83.5, lty=2)
par(mfrow=c(1,1))
dev.off()

male<-sort(jc.m("HLE.CSS.13"), decreasing = T)
write.csv(male[male>quantile(male, 0.75)],"./res/male.kenko.csv")

female<-sort(jc.f("HLE.CSS.13"), decreasing = T)
write.csv(female[female>quantile(female, 0.75)],"./res/female.kenko.csv")

