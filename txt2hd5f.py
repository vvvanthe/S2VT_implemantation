import glob
import numpy as np
import h5py
import os


Url2Vid = eval(open('Vid2Url_Full.txt').read())

file = h5py.File("VGG_train.hdf5")
lines = []
with open('yt_allframes_vgg_fc7_train.txt') as f:
    lines = f.readlines()


count = 0

feats = None
pre_name='vid1'
name=''
for line in lines:

    line1=line.replace('\n','')
    arr=line1.split(',')
    id=arr[0]
    name=id.split('_')[0]

    feats_batch=np.array(arr[1:],dtype='f4')
    feats_batch=np.expand_dims(feats_batch, axis=0)

    if name.find(pre_name) ==-1:

        print('completed: {}/{}'.format(pre_name,count))
        file[Url2Vid[pre_name]] = feats
        count =1
        feats = feats_batch

    else:
        count+=1
        feats = feats_batch if feats is None else np.concatenate([feats, feats_batch], axis=0)
    pre_name = name
    #if count >1: break

if feats is not None:
    print('completed: {}'.format(pre_name))
    file[Url2Vid[pre_name]] = feats
    #print(feats.shape)
    #file[Url2Vid[name]] = feats
    #.create_dataset(Url2Vid[pre_name], data=feats)
file.close()