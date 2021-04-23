system("open .")


Wakayama::d %>% dim()

Wakayama::JpnEng %>% tbl_df() %>% xtable::xtable()



Wakayama::d_m %>% select(LE_2015) %>% bind_cols(Wakayama::pref["pref.J"]) %>% dplyr::arrange(LE_2015) %>% mutate(rank=row_number()) %>%
  xtable::xtable()


Wakayama::d_f %>% select(LE_2015) %>% bind_cols(Wakayama::pref["pref.J"]) %>% dplyr::arrange(LE_2015) %>% mutate(rank=row_number()) %>%
  xtable::xtable()


Wakayama::d_m %>% select(HLE_2016) %>%
  bind_cols(Wakayama::pref["pref.J"]) %>%
  dplyr::arrange(HLE_2016) %>% mutate(rank=row_number()) %>%
  xtable::xtable()

Wakayama::d_f %>% select(HLE_2016) %>%
  bind_cols(Wakayama::pref["pref.J"]) %>%
  dplyr::arrange(HLE_2016) %>% mutate(rank=row_number()) %>%
  xtable::xtable()






jc.dotplot <- function(x) {
  # x is HLE or LE in c()　vector
  names(x)<-Wakayama::pref$pref.J
  x<-x[order(x)]

}

colfunc <- colorRampPalette(c("gray90","black"))

par(family= "HiraKakuProN-W3")


pdf("./fig/wakayama_LE_M.pdf", family="Japan1")

dotchart(
  main = paste("平均寿命(2015年, 男性), 全国平均",
               mean(Wakayama::d_m$LE_2015) %>% round(2),
               "歳"),
  jc.dotplot(Wakayama::d_m$LE_2015),
  cex = 0.7,
  lcolor = "gray90",
  pch = 19,
  col = colfunc(47),
  pt.cex = 1.5
)

abline(v = mean(Wakayama::d_m$LE_2015), lty = 2)

dev.off()



pdf("./fig/wakayama_LE_F.pdf", family="Japan1")

dotchart(
  main = paste("平均寿命(2015年, 女性), 全国平均",
               mean(Wakayama::d_f$LE_2015) %>% round(2),
               "歳"),
  jc.dotplot(Wakayama::d_f$LE_2015),
  cex = 0.7,
  lcolor = "gray90",
  pch = 19,
  col = colfunc(47),
  pt.cex = 1.5
)

abline(v = mean(Wakayama::d_f$LE_2015), lty = 2)

dev.off()



pdf("./fig/wakayama_HLE_M.pdf", family="Japan1")

dotchart(
  main = paste("健康寿命(2016年, 男性), 全国平均",
               mean(Wakayama::d_m$HLE_2016) %>% round(2),
               "歳"),
  jc.dotplot(Wakayama::d_m$HLE_2016),
  cex = 0.7,
  lcolor = "gray90",
  pch = 19,
  col = colfunc(47),
  pt.cex = 1.5
)

abline(v = mean(Wakayama::d_m$HLE_2016), lty = 2)

dev.off()



pdf("./fig/wakayama_HLE_F.pdf", family="Japan1")

dotchart(
  main = paste("健康寿命(2016年, 女性), 全国平均",
               mean(Wakayama::d_f$HLE_2016) %>% round(2),
               "歳"),
  jc.dotplot(Wakayama::d_f$HLE_2016),
  cex = 0.7,
  lcolor = "gray90",
  pch = 19,
  col = colfunc(47),
  pt.cex = 1.5
)

abline(v = mean(Wakayama::d_f$HLE_2016), lty = 2)

dev.off()



Wakayama::d_common %>% dplyr::select_if(is.numeric) %>% sapply(rank) %>%
  tbl_df() %>%dplyr::filter(key==30) %>% t() %>% as.data.frame() %>%
  tibble::rownames_to_column() %>% tbl_df()
  tibble::rowid_to_column("key") %>% tbl_df()
#
# Wakayama::JpnEng %>% class()
#
# Wakayama::JpnEng %>% as.data.frame()

# system("open .")




