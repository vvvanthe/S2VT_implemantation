import glob
import numpy as np
import h5py
import os



#input_path='./features/MSVD_incep4_recon.hdf5'
input_path='hdf5/VGG_str_1.hdf5'

Vid2Url = eval(open('url_to_vidId.txt').read())

#out_path='Output/EDSR/LR47_EDSR/'

#out_path='Output/unkv6/unkv6_EDSR/'
out_path='Output/VGG_stride/'

os.makedirs(out_path,exist_ok=True)

f1 = open(out_path+'vgg_feat_test_str1.txt', 'w')


with h5py.File(input_path,'r') as ff:
	for vid, c in enumerate(sorted(ff.keys())):
		for frame, feat in enumerate(ff[c]):
			#print(ff[c].shape)
			#print("vid%d_frame_%d transform.." % (vid+1, frame+1))
			#print(feat.shape)
			#print(ff[c])
			d=Vid2Url[c]
			d1 = "%s_frame_%d," % (d, frame + 1)
			#print(d1)
			#print(feat)
			d2 = ','.join(map(str, feat))
			data = d1 + d2 + '\n'
			#if vid >= 1300:
			f1.write(data)
			
			#print("shape %d" %(feat.shape))
		print("%s : %d"%(d, vid+1301))
f1.close()

print("FINISH")
