# spark_video

![SparkPhoto-功能架構](https://user-images.githubusercontent.com/35889113/203204055-d14abac6-c199-4f7f-ab1a-656eaed86ff8.png)

## installation
* git clone https://github.com/fdsf53451001/spark_video.git
* cd spark_video
* pip install -r requirements.txt

## usage
### with web interface
* cd web/senior_project
* python app.py
* upload your video, and enjoy :D

### with command line
* cd spark_video
* create video_database folder and set it in main6.py
* set video_path in main6.py
* python main6.py

### with music model training 
* download [lpd_5_cleansed](https://drive.google.com/uc?id=1yz0Ma-6cWTl6mhkrLnAVJ7RNzlQRypQ5)
* download [id_lists_amg](https://drive.google.com/uc?id=1hp9b_g1hu_dkP4u8h46iqHeWMaUoI07R)
* unzip lpd_5_cleansed and id_list_amg
* set the dataset_root = lpd_5_cleansed path
* set the amg_path = id_lists_amg path (or spark_muse_amg we provide)
* run the MuseGan_train.ipynb
* [for other details](https://docs.google.com/document/d/1wRIa2ytVwF7eDj8QByU8rGlP5a3uXZ-g2mNeFwsE-As/edit?usp=sharing)

## team
<img width="329" alt="如影隨形" src="https://user-images.githubusercontent.com/35889113/203204415-81beb247-d41d-4199-bfaa-0614864dae0d.png">

## structure
![SparkPhoto-程式架構_多線程優化](https://user-images.githubusercontent.com/35889113/208694384-e4c8a7f3-b72a-4810-9036-4f73ef410909.png)
