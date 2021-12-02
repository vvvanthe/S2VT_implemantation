# S2VT_implemantation
To implement S2VT

## 1. Create docker images from existed image. 
We have a images like that.
![img1](https://user-images.githubusercontent.com/42643830/144418725-fdddbe4e-70c4-42a8-878b-2af42d9e234e.PNG)


We need to copy caffe-py27-cuda80 to run S2VT:

_docker save -o /home/levanthe/caffe.tar 9ab5517db338_

==> This create a tar file. 

Load image from tar file: _docker load -i caffe.tar _

One different way: using docker pull if the image had in hub.docker.com
![2](https://user-images.githubusercontent.com/42643830/144420203-29734d40-6b24-42c3-868c-8d17d0bbfc3c.png)
 ## 2. Create container
 
 _docker run --gpus all --shm-size 128gb --name s2vt -it 9ab5517db338_
 
 ##3. Copy caffe folder to container
 _docker cp caffe s2vt:/home/_
 
 
 ## 3. Install required package:
 _apt-get update
 docker attach s2vt_
 % To run video caption-val
_ apt-get install python-tk
 apt-get install openjdk-8-jdk
 apt install vim
 _
 
 ## 4. Training S2VT
 make directory to extract hdf5 file when trainng:
 mkdir rawcorpus
 mkdir rawcorpus/train
 mkdir rawcorpus/val
 mkdir rawcorpus/val
 
 Change dimension of training data in **framefc7_stream_text_to_hdf5_data.py** file. 4096 for VGG, and 1053 for Inperceptionv4
 
 copy training data to data directory:
 yt_allframes_vgg_fc7_train.txt
 yt_allframes_vgg_fc7_val.txt
 yt_allframes_vgg_fc7_test.txt
 
extract data: 
python framefc7_stream_text_to_hdf5_data.py

Change parameters, such as save directory, iteration, learning rate,..



train: **_/usr/local/bin/caffe train –solver ./s2vt_solver.prototxt_**

## 4. Testing
Copy extracted feature txt file to data/yt_allframes_vgg_fc7_test.txt

Change testing feature demension in: vim s2vt.words_to_preds.deploy.prototxt 

## 5. Evaluation

cd caption-eval
python run_evaluations.py -i ../results/test.s2vt_youtube_inv4_iter_10000_beam_size_1.txt -r data/references_test.json 
 
