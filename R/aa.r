# source('aa.R')

args <- commandArgs()  # パラメータのベクトル

name <- args[6]      # ６番めの要素が最初のパラメータ
n.block <- args[7]   # ７番めは２つめのパラメータ
  
#   
# name <- "file"
# n.block <- 5

for (i in 1:n.block) {
  file <-  sprintf("%s_%03d.txt", name, i)
  cat(file) # 画面に出力
  cat("\n")  # 改行コード
}




