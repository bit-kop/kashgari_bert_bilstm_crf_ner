import os
import pathlib
import sys

import kashgari
from kashgari.embeddings import BERTEmbedding
from kashgari.tasks.labeling import BiLSTM_CRF_Model

projectdir = str(pathlib.Path(os.path.abspath(__file__)).parent)
sys.path.append(projectdir)
data_dir = projectdir+'/data/corpus/people_daily'

train_path = data_dir+'/example.train'
dev_path = data_dir+'/example.dev'
test_path = data_dir+'/example.test'
bert_path = projectdir+'/data/chinese_wwm_ext_L-12_H-768_A-12'
model_path = projectdir+'/model/my_ner.h5'

def get_sequenct_tagging_data(file_path):
    data_x, data_y = [], []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

        x, y = [], []
        for line in lines:
            rows = line.split(' ')
            if len(rows) == 1:
                data_x.append(x)
                data_y.append(y)
                x = []
                y = []
            else:
                x.append(rows[0])
                y.append(rows[1])
    return data_x, data_y

train_x, train_y = get_sequenct_tagging_data(train_path)
dev_x, dev_y = get_sequenct_tagging_data(dev_path)
test_x,test_y = get_sequenct_tagging_data(test_path)

print(f"train data count: {len(train_x)}")
print(f"validate data count: {len(dev_x)}")
print(f"test data count: {len(test_x)}")

bert_embed = BERTEmbedding(bert_path,
                           task=kashgari.LABELING,
                           sequence_length=100)

# 创建模型并训练
model = BiLSTM_CRF_Model(bert_embed)
model.fit(train_x,
          train_y,
          x_validate=dev_x,
          y_validate=dev_y,
          epochs=20,
          batch_size=512)

model.save(model_path)

# 模型评估
model.evaluate(test_x,test_y)