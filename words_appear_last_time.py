#coding=gbk
import wordEachyear as wy

es = range(32)#��ͬ�ʻ���
esr1 = range(32)#������ƽ���ʻ���Ϊ��׼
esr2 = range(32)#�Ե���
esr3 = range(32)#����һ��
for i in range(32):
    es[i] = len(set(wy.eywords[i]) & set(wy.eywords[i+1]))
    esr1[i] = float(es[i]) * 2 / (wy.eywords_volume[i] + wy.eywords_volume[i+1])
    esr2[i] = float(es[i]) / wy.eywords_volume[i+1]
    esr3[i] = float(es[i]) / wy.eywords_volume[i]

