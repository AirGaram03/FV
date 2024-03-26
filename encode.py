import cv2 as cv
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials, db
from firebase_admin import storage
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred,{
'databaseURL':"https://fv-project-81f32-default-rtdb.firebaseio.com/",
'storageBucket':"fv-project-81f32.appspot.com"
})


imageMode = 'images'
imgpath = os.listdir(imageMode)
print(imgpath)
imgList = []
stdID = []

for path in imgpath:
    imgList.append(cv.imread(os.path.join(imageMode, path)))    
    fileName = f'{imageMode}/{path}'
    print(fileName)
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # print(path)
    # print(os.path.splitext(path)[0])
    stdID.append(os.path.splitext(path)[0])
print(stdID)

def findEncoding(imagelist):
    encodeList = []
    for img in imagelist:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
        
    return encodeList

print("encode start")
knownEncode = findEncoding(imgList)
knownEncodeID = [knownEncode, stdID]
print(knownEncodeID)
print("encoding complete")
# print(knownEncode)

file = open("encodefile.p", 'wb')
pickle.dump(knownEncodeID, file)
file.close()
print("file saved")