import os
import glob
import h5py

Input_path='hdf5/inv4_f80_stride_compression/RA/'
Output_path='Output/inv4_f80_stride_compression_txt/RA/'
os.makedirs(Output_path,exist_ok=True)

Vid2Url = eval(open('url_to_vidId.txt').read())
for i, feature_file in enumerate(sorted(glob.glob(Input_path+'/*.hdf5'))):
    name = os.path.basename(feature_file)
    filename, extension = os.path.splitext(name)
    f1 = open(Output_path + '{}.txt'.format(filename), 'w')
    with h5py.File(feature_file, 'r') as ff:
        for vid, c in enumerate(sorted(ff.keys())):
            for frame, feat in enumerate(ff[c]):
                d = Vid2Url[c]
                d1 = "%s_frame_%d," % (d, frame + 1)
                d2 = ','.join(map(str, feat))
                data = d1 + d2 + '\n'
                f1.write(data)
    print('Complete: {}'.format(name))
    f1.close()
