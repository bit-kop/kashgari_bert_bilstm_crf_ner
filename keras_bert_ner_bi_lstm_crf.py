
from config.path_config import *


class BertNerBiLstmModel():
    def __init__(self):
        print('BertNerBiLstmModel init start !')
        self.dict_path, self.max_seq_len, self.keep_prob, self.is_training = vocab_file,args.

'''
读取人民日报语料，类似txt阅读器
获取语料与label的list：x,y，列表中每个元素是一个list，按照之前语料文件（比如train）中的' '切分
'''
def get_sequence_tagging_data_from_chinese_people_daily_ner_corpus(file_path):
    _x_,_y_ = [],[]
    with open(file_path,'r',encoding='utf-8') as fr:
        lines = fr.read().splitlines()
        x,y = [],[]
        for line_one in lines:
            rows = line_one.split(' ')
            if len(rows) == 1:
                _x_.append(x),_y_.append(y)
                x,y = [],[]
            else:
                x.append(rows[0]),y.append(rows[1])
    return _x_,_y_


if __name__ == '__main__':
    path_dev = path_ner_people_dev
    x,y = get_sequence_tagging_data_from_chinese_people_daily_ner_corpus(path_dev)
    # print(len(x))
    # print(x[1])