# load json and create model

from __future__ import division
# import os
# os.environ['TF_MIM_LOG_LEVEL']='2'
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import model_from_json
import numpy
import os
import numpy as np
import cv2
import time
#loading the model
class FaceEmotion():
    def __init__(self,photo_folder_path,save_path):
        self.photo_folder_path = photo_folder_path
        self.save_path = save_path
    def filterPhoto(self):
        photo_arr=[]
        for root, dirs,files in os.walk(self.photo_folder_path):
            for folder_path in dirs:
                    initial_count=0
                    for file_name in os.listdir(self.photo_folder_path+'\\'+str(folder_path)):
                            file_path=self.photo_folder_path+'\\'+folder_path+"\\"+str(file_name)
                            if os.path.isfile(os.path.join(file_path)):
                                    initial_count += 1
                    if initial_count<=2:
                            photo_arr.append(folder_path) 
        return photo_arr
    def predictFace(self):
        json_file = open('fer.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("fer.h5")
        print("Loaded model from disk")
        #setting image resizing parameters
        WIDTH = 48
        HEIGHT = 48
        x=None
        y=None
        labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
        start = time.time()
        file_name=''
        photo_arr=self.filterPhoto()
        print('Filter folder :',photo_arr)
        #loading image
        for folder_path in photo_arr:
                for file_name in os.listdir(self.photo_folder_path+'\\'+str(folder_path)):
                        file_path=self.photo_folder_path+'\\'+folder_path+"\\"+str(file_name)
                        full_size_image = cv2.imread(file_path)
                        # full_size_image = cv2.resize(full_size_image, interpolation=cv2.INTER_AREA)
                        print("Image Loaded",file_path)
                        gray=cv2.cvtColor(full_size_image,cv2.COLOR_RGB2GRAY)
                        face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                        faces = face.detectMultiScale(gray, 1.3  , 5)
                        print('--------',faces)
                        #detecting faces
                        is_face=False
                        for (x, y, w, h) in faces:
                                roi_gray = gray[y:y + h, x:x + w]
                                cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (WIDTH, HEIGHT)), -1), 0)
                                cv2.normalize(cropped_img, cropped_img, alpha=0, beta=1, norm_type=cv2.NORM_L2, dtype=cv2.CV_32F)
                                cv2.rectangle(full_size_image, (x, y), (x + w, y + h), (0, 255, 0), 1)
                                #predicting the emotion
                                yhat= loaded_model.predict(cropped_img)
                                print(yhat)
                                cv2.putText(full_size_image, labels[int(np.argmax(yhat))], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
                                print("Emotion: "+labels[int(np.argmax(yhat))])
                                is_face = True
                                # cv2.imshow('Emotion', full_size_image)
                                # print('final',path)
                        if(is_face):
                                file_path=self.save_path+str(folder_path)+'\\'+file_name
                                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                                print('save path',file_path)
                                cv2.imwrite(os.path.join(file_path), full_size_image)
        end = time.time()
        print('執行時間',end - start)
        cv2.waitKey()
folder_path = "yolo_cut"
save_path = 'C:\\Users\\user\\Desktop\\project_code\\face\\fer2013\\result\\'
res=FaceEmotion(folder_path,save_path)
res.predictFace()