# -*- coding: utf-8 -*-
# List 5-4  ���K��W�c�̕W�{���U�̐���i�ꕪ�U�����m�̏ꍇ�j
import scipy.stats

popmean = 50   # V
popvar = 25    # sigma^2
n = 10
v = ((n-1)*popmean)/popvar
print(v, 1-scipy.stats.chi2.cdf(v, n-1).round(4))
# �o�͌��ʂ� 18.0    0.0352

