import os

# 用于ner的人民日报语料
cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
path_ner_people_train = os.path.join(cur_dir, 'data/corpus/people_daily/people.train')
path_ner_people_dev = os.path.join(cur_dir, 'data/corpus/people_daily/people.dev')
path_ner_people_test = os.path.join(cur_dir, 'data/corpus/people_daily/people.test')

# path of BertMode
model_dir = os.path.join(cur_dir, 'data/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12')
config_name = os.path.join(model_dir, '/bert_config.json')
ckpt_name = os.path.join(model_dir, '/bert_model.ckpt')
vocab_file = os.path.join(model_dir, '/vocab.txt')
