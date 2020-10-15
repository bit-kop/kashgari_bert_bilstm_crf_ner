一，基于kashgari的命名实体识别
1，bert+bilstm+crf
2，bert，提供了两个模型，分别是chinese-bert与Chinese-BERT-wwm（哈工大讯飞）
3，下载地址为：https://gitee.com/natural-language-processing/Chinese-BERT-wwm?_from=gitee_search
4，模型代码封装的比较简单，后续将尝试修改kashgari包的源码

二，代码说明：
1，my_model.py 训练模型并保存
2，my_model_predict.py 对输入文本找出实体，并预测其实体类别