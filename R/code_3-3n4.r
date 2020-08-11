## データ読み込み
d <- read.csv("地産地消データ.csv")
x <- d[, 4:15]

## 単純集計
barplot(sort(colSums(x), decreasing=T), ylab="購入者数", las=3)

## 距離計算
distx <- dist(t(x), method="binary")
print(distx)

## 多次元尺度法
library(maptools)
res.cmds <- cmdscale(distx)
plot(res.cmds, xlab="", ylab="")
pointLabel(res.cmds, labels=rownames(res.cmds))

## 階層的クラスタリング
plot(hclust(distx, method="ward.D"),
     main="デンドログラム", ylab="結合距離", sub="", xlab="")

## グラフ抽出
library(network)
cutoff <- quantile(distx, 0.2)
adj <- 1 * (as.matrix(distx) <= cutoff)
plot(network(adj, directed=FALSE), displaylabels=TRUE)
