import cv2
import numpy as np 
import os

orb = cv2.ORB_create(nfeatures=1000)

path = "D:\\Python_XLA\\nhandangdoituong_xacdinhlabai\\img_Query"
images = []
classNames = []
myList = os.listdir(path)


for cl in myList:
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])
    
def findDes(image):
    desList = []
    for img in image:
        kp1, des1 = orb.detectAndCompute(img,None)    #Tìm các điểm chính trong một hình ảnh và tính toán các bộ mô tả của chúng
        desList.append(des1)
    return desList

def finID(img, desList, thres = 15):
    kp2, des2 = orb.detectAndCompute(img,None)   #Tìm các điểm chính trong một hình ảnh và tính toán các bộ mô tả của chúng
    bf = cv2.BFMatcher()
    matchList = []
    findVal = -1
    
    try:
        for des1 in desList:
            matches = bf.knnMatch(des1, des2, k=2)
            good = []
            for m,n in matches:
                if m.distance < 0.75*n.distance:
                    good.append([m])
                matchList.append(len(good))
    except:
        pass
    if len(matchList) != 0:
        if max(matchList)>thres:
                findVal = matchList.index(max(matchList))
    return findVal

desList = findDes(images)


img2 = cv2.imread('D:\\Python_XLA\\nhandangdoituong_xacdinhlabai\\img_Query\\A_ro.png')

imgOriginal = img2.copy()
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)        #Chuyển sang ảnh xám

id = finID(img2,desList)
imgOriginal = cv2.resize(imgOriginal,(500,500))     #Thay đổi kích thước của ảnh

if id != -1:
    cv2.putText(imgOriginal,classNames[id],(200,30),cv2.FONT_HERSHEY_COMPLEX,1,(255,15,255),1)
    #Vẽ một chuỗi văn bản lên ảnh

cv2.imshow('img2',imgOriginal)      
cv2.waitKey(0)
