# -*- coding: utf-8 -*-
import os
import pathlib
import sys

import kashgari
import re

projectdir = str(pathlib.Path(os.path.abspath(__file__)).parent)
sys.path.append(projectdir)
data_dir = projectdir+'/data/corpus/people_daily'

model_path = projectdir+'/model/my_ner.h5'
loaded_model = kashgari.utils.load_model(model_path)

def cut_text(text, lenth):
    textArr = re.findall('.{' + str(lenth) + '}', text)
    textArr.append(text[(len(textArr) * lenth):])
    return textArr

def extract_labels(text, ners):
    ner_reg_list = []
    if ners:
        new_ners = []
        for ner in ners:
            new_ners += ner
        for word, tag in zip([char for char in text], new_ners):
            if tag != 'O':
                ner_reg_list.append((word, tag))

    # 输出模型的NER识别结果
    labels = {}
    if ner_reg_list:
        for i, item in enumerate(ner_reg_list):
            if item[1].startswith('B'):
                label = ""
                end = i + 1
                while end <= len(ner_reg_list) - 1 and ner_reg_list[end][1].startswith('I'):
                    end += 1

                ner_type = item[1].split('-')[1]

                if ner_type not in labels.keys():
                    labels[ner_type] = []

                label += ''.join([item[0] for item in ner_reg_list[i:end]])
                labels[ner_type].append(label)

    return labels

text_input = '周某某与周某某和刘某某经事先商量（由周某某提出，其余两人同意）后，来到甘霖镇大王庙孔村农科所园区内空地旁边，' \
             '趁四下无人之际，盗走4个棕色大花盆（直径约50公分）、3个青色大花盆（直径约70公分）'

texts = cut_text(text_input,100)
ners = loaded_model.predict([[char for char in text] for text in texts])
print(ners)
labels = extract_labels(text_input,ners)
print(labels)
