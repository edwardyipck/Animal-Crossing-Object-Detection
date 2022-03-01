import cv2
import numpy as np
import pandas as pd
import random
import os
import xml.etree.ElementTree as ET

villager_list = ["Aurora","Ozzie","Hamlet"]

for villager in villager_list:
    photofolder = r"D:\Current Work\Python\PROJECTS\Animal Crossing image processing\output photos\\" + villager + "\\"
    sceneryfolder = r"D:\Current Work\Python\PROJECTS\Animal Crossing image processing\sceneries\\"
    outputfolder = r"D:\Current Work\Python\PROJECTS\Animal Crossing image processing\output photos\bgtest\\" + villager + "\\"   

    kelvin_table = pd.read_csv("whitebalance-rgb.csv")
    kelvin_table = dict(zip(kelvin_table["temp"], zip(kelvin_table["R"],kelvin_table["G"],kelvin_table["B"])))
    
    temps = list(kelvin_table.keys())
    brights = [-12,34]
    blurs = [1,4]   
    
    def convert_temp(image, temp):
        image = cv2.convertScaleAbs(image)
        r, g, b = kelvin_table[temp]
        matrix = np.array([[ b / 255.0, 0.0, 0.0, 0.0],
                          [0.0, g / 255.0, 0.0, 0.0],
                          [0.0, 0.0, r / 255.0, 0.0],
                          [0.0, 0.0, 0.0       ,1.0]])      
        output = np.tensordot(image,matrix, axes=([2,0]))
        return output
    
    def brightness(image,val):
        image = cv2.convertScaleAbs(image)
        inc_matrix = np.ones(image.shape,dtype="uint8")*val
        
        if image.shape[2] == 4:
            keep_alpha = np.array([[1.0, 0.0, 0.0, 0.0],
                               [0.0, 1.0, 0.0, 0.0],
                               [0.0, 0.0, 1.0, 0.0],
                               [0.0, 0.0, 0.0, 0.0]])
            inc_matrix = np.tensordot(inc_matrix,keep_alpha, axes=([2,0]))
            
        else:
            keep_alpha = np.array([[1.0, 0.0, 0.0],
                               [0.0, 1.0, 0.0],
                               [0.0, 0.0, 1.0]])
            inc_matrix = np.tensordot(inc_matrix,keep_alpha, axes=([2,0]))     
        inc_matrix = cv2.convertScaleAbs(inc_matrix)
        if val < 0:
            output = cv2.subtract(image,inc_matrix)
        else:
            output = cv2.add(image,inc_matrix)
        return output

    def blur(image,val):
        if val ==0:
            return image
        else:
            output = cv2.blur(image, (val, val))
            return output
        
    tree = ET.parse("blank.xml")
    root = tree.getroot()
    def createxml(name,k,root,villager,bgsize,coords):
        root.find("filename").text = villager+"-"+str(k)+".jpg"
        root.find(".//name").text = villager
        root.find("path").text = name
        root.find(".//width").text = str(bgsize[1])
        root.find(".//height").text = str(bgsize[0])
        root.find(".//xmin").text = str(coords[0])
        root.find(".//xmax").text = str(coords[1])
        root.find(".//ymin").text = str(coords[2])
        root.find(".//ymax").text = str(coords[3])
        
        tree.write(outputfolder+villager+"-"+str(k)+".xml")
        
    photos = os.listdir(photofolder)
    backgrounds = os.listdir(sceneryfolder)
    
    for k in range(1000):
        if k== 500 or k == 999:
            print(villager+"halfway")
        
        randpng = random.choice(photos)
        randbg = random.choice(backgrounds)
        
        temp = random.choice(temps)
        bright = random.randrange(brights[0],brights[1])
        blur_n = random.randrange(blurs[0],blurs[1])
        
        img = cv2.imread(photofolder+randpng, cv2.IMREAD_UNCHANGED)
        bg = cv2.imread(sceneryfolder+randbg)
        
        bg = brightness(bg,random.randrange(-30,30))
        bg = blur(bg,blur_n)
        
        if random.random() < .5:
            randmult = random.uniform(1.5,1)
            randdim = [int(bg.shape[1]*randmult),int(bg.shape[0]*randmult)]
            bg = cv2.resize(bg, randdim, interpolation = cv2.INTER_LINEAR)
            
        else:
            randmult = random.uniform(1,0.5)
            randdim = [int(bg.shape[1]*randmult),int(bg.shape[0]*randmult)]
            bg = cv2.resize(bg, randdim, interpolation = cv2.INTER_AREA)           
        
        scale = (bg.shape[1]*random.uniform(0.05, 0.15))/img.shape[1]
        
        if scale>1:
            dim = [int(bg.shape[1]*(1/scale)),int(bg.shape[0]*(1/scale))]
            bg = cv2.resize(bg, dim, interpolation = cv2.INTER_LINEAR)
            
        else:
            dim = [int(img.shape[1]*scale),int(img.shape[0]*scale)]
            img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
          
        img = convert_temp(img,temp)
        img = brightness(img,bright)
        img = blur(img,blur_n)
        
        bgx = random.randint(0,max(0,bg.shape[1]-512))
        bgy = random.randint(0,max(0,bg.shape[0]-512))
        
        bg = bg[bgy:bgy+min(512,bg.shape[1]), bgx:bgx+min(512,bg.shape[0])]
            
        x1 = random.randint(10, bg.shape[1]-img.shape[1]-10)
        y1 = random.randint(10, bg.shape[0]-img.shape[0]-10)
        x2 = x1 + img.shape[1]
        y2 = y1 + img.shape[0]
        
        name = outputfolder+villager+"-"+str(k)+".jpg"
        createxml(name,k,root,villager,bg.shape,(x1,x2,y1,y2))
        
        output = bg.copy()
        output[y1:y2, x1:x2] =  output[y1:y2, x1:x2] * (1 - img[:, :, 3:] / 255) + \
                            img[:, :, :3] * (img[:, :, 3:] / 255)
        
           
        cv2.imwrite(name, output,[int(cv2.IMWRITE_JPEG_QUALITY), random.randrange(50,100)])