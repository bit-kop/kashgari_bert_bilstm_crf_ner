import os
cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
yun_duan_ye_wu_gong_zuo_shi_entity_path = os.path.join(cur_dir, 'dict/'+'云端业务工作室'+'.txt')
print(yun_duan_ye_wu_gong_zuo_shi_entity_path)
print(cur_dir)