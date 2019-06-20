# iNaturalist image loader
'''
本程序用来产生 trainlist, vallist, testlist三个文件
'''
import sys
sys.path.append(r'/home/jiancaiqing/python_code/iNaturalist19/INaturalist/data')

from PIL import Image
import os
import json
import numpy as np

def default_loader(path):
    return Image.open(path).convert('RGB')

def gen_list(prefix):
	ann_file = '%s2019.json'%prefix #2019.5.10:ann_file是注释文件
	train_out = '%s.lst'%prefix
	# load annotations
	print('Loading annotations from: ' + os.path.basename(ann_file))
	with open('/home/jiancaiqing/python_code/iNaturalist19/INaturalist/data/'+ann_file) as data_file:
		ann_data = json.load(data_file) #ann_data是json文件的数据

	# set up the filenames and annotations
	imgs = [aa['file_name'] for aa in ann_data['images']]
	im_ids = [aa['id'] for aa in ann_data['images']]
	if 'annotations' in ann_data.keys():
		# if we have class labels
		classes = [aa['category_id'] for aa in ann_data['annotations']]
	else:
		# otherwise dont have class info so set to 0
		classes = [0]*len(im_ids)

#	idx_to_class = {cc['id']: cc['name'] for cc in ann_data['categories']} #索引到类别
#   上句只是为显示类别数

	print('\t' + str(len(imgs)) + ' images')
#	print('\t' + str(len(idx_to_class)) + ' classes')

	for index in range(10):
		path = imgs[index]
		target = str(classes[index])
		im_id = str(im_ids[index]-1)
		print(im_id + '\t' + target + '\t' + path)

	import pandas as pd
	from sklearn.utils import shuffle

	df = pd.DataFrame(classes)
	df[1] = imgs  #prefix为train时，len(imgs)为265213,为val时len(imgs)为3030
	df = shuffle(df)

	df.to_csv(train_out, sep='\t', header=None, index=False)
	df = pd.read_csv(train_out, delimiter='\t', header=None)
	df.to_csv(train_out, sep='\t', header=None)

if __name__ == '__main__':  #2019.5.10：在if __name__ == 'main': 下的代码只有在文件作为脚本直接执行时才会被执行，而import到其他脚本中是不会被执行的
	set_names = ['train', 'val', 'test']
	for name in set_names:
		gen_list(name) #逐句调试时，遇到函数调用、实例调用等，不要直接执行，要手动传入参数并跳转至函数定义处逐句执行










