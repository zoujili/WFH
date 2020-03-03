\\15.36.180.53\MerlinShare\Users\Gaming\Video 


1. chuang server tensorflow 需要升级到1.14么
2. 加密后的网络的Debug


my: tensor 1.14 keras 2.25
troy : tensor 1.08 keras 2.1.1


我生产的model放到chuang 的server BUG  none type。。 exception
把chuang的server放在我的坏境下 修改一点代码是可以运行成功了  不加密（加密需要token）

因为chuang的tensorflow比我低， 没办法兼容  
我是ubuntu 18.04 GCC+6.0 以上 没办法装 cude9.0（gcc++）
所以需要一个chuang的环境   在另外的机器windows 安装

看chuang的server代码


.\pip.exe  --default-timeout=100 install --ignore-installed tensorflow-gpu==1.14 -i https://pypi.tuna.tsinghua.edu.cn/simple
.\pip.exe  --default-timeout=100 install --ignore-installed matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
.\pip.exe  --default-timeout=100 install --ignore-installed librosa -i https://pypi.tuna.tsinghua.edu.cn/simple
.\pip.exe  --default-timeout=100 install --ignore-installed keras==2.2.5 -i https://pypi.tuna.tsinghua.edu.cn/simple
.\pip.exe  --default-timeout=100 install --ignore-installed opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
.\pip.exe  --default-timeout=100 install --ignore-installed xxhash -i https://pypi.tuna.tsinghua.edu.cn/simple


pip --default-timeout=100 install --ignore-installed h5py==2.7.0 -i https://pypi.tuna.tsinghua.edu.cn/simple

pip --default-timeout=100 install --ignore-installed tensorflow-gpu==1.14.0 -i https://pypi.tuna.tsinghua.edu.cn/simple


python3.6.5  

setuptools 44.0.0 

 .\pip.exe install pypiwin32