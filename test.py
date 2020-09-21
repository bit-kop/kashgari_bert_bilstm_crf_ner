# 中文分词
from collections import Counter

import jieba
import numpy as np

def cos_sim(str1, str2):
    str1 = fen_ci(str1)
    str2 = fen_ci(str2)

    # str1 = jieba.lcut(str1)
    # str2 = jieba.lcut(str2)
    # print('str1',str1)
    # print('str2',str2)
    co_str1 = (Counter(str1))
    co_str2 = (Counter(str2))
    p_str1 = []
    p_str2 = []
    for temp in set(str1 + str2):
        p_str1.append(co_str1[temp])
        p_str2.append(co_str2[temp])
    p_str1 = np.array(p_str1)
    p_str2 = np.array(p_str2)
    return p_str1.dot(p_str2) / (np.sqrt(p_str1.dot(p_str1)) * np.sqrt(p_str2.dot(p_str2)))

def fen_ci(string, cut_all=False, append_tag=False, filter_set=[]):
    seq = []
    if append_tag:
        seq.append('start')
    for ws in jieba.cut(string, cut_all=cut_all):
        if ws not in filter_set:
            if Chinese(ws):
                for ch in ws:
                    seq.append(ch)
            else:
                seq.append(ws)
    if append_tag:
        seq.append('end')
    return seq


def Chinese(str):
    if str >= '\u4e00' and str<= '\u9fa5':
        return True
    else:
        return False

print(fen_ci('云端业务'))
print(cos_sim('在线营销大赛报名流程是怎样的','啥是第三届营销大赛'))
print(cos_sim('在线营销大赛报名流程是怎样的','报名参加营销大赛'))