from glob import glob
from sklearn.model_selection import train_test_split
import yaml


img_list = glob('./dataset/train/images/*.jpg')

print(len(img_list))

train_img_list, val_img_list = train_test_split(img_list, test_size=0.2, random_state=3000)

print(len(train_img_list), len(val_img_list))
with open('./dataset/train.txt', 'w') as f:
  f.write('\n'.join(train_img_list) + '\n')

with open('./dataset/val.txt', 'w') as f:
  f.write('\n'.join(val_img_list) + '\n')

with open('./dataset/data.yaml', 'r') as f:
  data = yaml.safe_load(f)

print(data)

data['train'] = './dataset/train.txt'
data['val'] = './dataset/val.txt'

with open('./dataset/data.yaml', 'w') as f:
  yaml.dump(data, f)

print(data)