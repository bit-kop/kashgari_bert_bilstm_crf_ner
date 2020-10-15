import os
import pathlib
import sys

projectdir = str(pathlib.Path(os.path.abspath(__file__)).parent.parent)
sys.path.append(projectdir)
corpus_dir = projectdir+'/data/corpus/people_daily'

train_path = corpus_dir+'/example.train'
dev_path = corpus_dir+'/example.dev'
test_path = corpus_dir+'/example.test'
bert_path = projectdir+'/data/chinese_wwm_ext_L-12_H-768_A-12'
model_path = projectdir+'/model/my_ner.h5'

print(model_path)