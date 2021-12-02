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
 apt-get install openjdk-8-jdk_
