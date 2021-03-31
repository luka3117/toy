# -*- coding: utf-8 -*-
# List 7-13  リンゴとミカンの好き嫌いの相関
import numpy as np
apple = [0,1,0,0,1,0,1,1,0,0]
orange= [1,1,0,0,0,0,1,1,0,0]
print('リンゴの平均値', np.mean(apple), 'ミカンの平均値', np.mean(orange))
print('相関係数', np.corrcoef(apple, orange)[0,1].round(4))
#
# 実行結果は
# リンゴの平均値 0.4 ミカンの平均値 0.4
# 相関係数 0.5833


