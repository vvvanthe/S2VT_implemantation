import glob
import numpy as np
import h5py
import os

txt_file='txt/inv4_feat_test_f80.txt'
stride_list=[1,2,3,4,5,6,8,10,12,16,20,24,28,32]
out_dir='hdf5/Inv4_f80_stride'

os.makedirs(out_dir,exist_ok=True)

for stride_para in stride_list:


    out_path=out_dir+'/Inv4_str_{}.hdf5'.format(stride_para)

    Url2Vid = eval(open('Vid2Url_Full.txt').read())

    file = h5py.File(out_path)
    lines = []


    with open(txt_file) as f:
        lines = f.readlines()


    count = 0

    feats = None
    pre_name='vid1301'
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
            count = 1
            feats = feats_batch

        else:
            count += 1
            if (count-1)%stride_para==0:
                feats = feats_batch if feats is None else np.concatenate([feats, feats_batch], axis=0)
        pre_name = name
        #if count >1: break

    if feats is not None:
        print('completed: {}'.format(pre_name))
        file[Url2Vid[pre_name]] = feats
    file.close()