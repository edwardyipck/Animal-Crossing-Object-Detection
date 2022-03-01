import xml.etree.ElementTree as ET
from math import *
villager = "Stitches"

folder = r"D:\Current Work\Python\PROJECTS\Animal Crossing image processing\output photos\\" + villager + "\\"

fields = ["xmin","ymin","xmax","ymax"]
# xmd - x coordinate mid and difference (between mid and edge)
# tr - transition differences from angles 0->1 and 1->2
def dimcalc(dims):
    xdif = []
    ydif = []
    for i in range(2):
        xdif.append([dims[i+1][0]-dims[i][0],dims[i+1][2]-dims[i][2]])
        ydif.append([dims[i+1][1]-dims[i][1],dims[i+1][3]-dims[i][3]])
    
    return xdif,ydif
    
for e in range(4):
    for a in range(3):
        dims = []
        for p in [0,8,16]:
            tree = ET.parse(folder + villager+ " photo " + str(e) + "-" + str(a) + "-" + str(p)+".xml")
            root = tree.getroot()
            
            dimline = []
            for field in fields:
    
                dimline.append(int(root.find(".//"+field).text))
                
            dims.append(dimline)
            
        xdif,ydif = dimcalc(dims)
        
        xcoord = []
        ycoord = []
        for i in range(17):
            if i<9:
                x1 = dims[0][0] + (xdif[0][0]/8)*i
                x2 = dims[0][2] + (xdif[0][1]/8)*i
                xcoord.append([x1,x2])
                
                y1 = dims[0][1] + (ydif[0][0]/8)*i
                y2 = dims[0][3] + (ydif[0][1]/8)*i
                ycoord.append([y1,y2])
            else:
                j = i-8
                x1 = dims[1][0] + (xdif[1][0]/8)*j
                x2 = dims[1][2] + (xdif[1][1]/8)*j
                xcoord.append([x1,x2])
                
                y1 = dims[1][1] + (ydif[1][0]/8)*j
                y2 = dims[1][3] + (ydif[1][1]/8)*j
                ycoord.append([y1,y2])                  
                
        
        tree = ET.parse(folder + villager+ " photo " + "0-0-0.xml")
        root = tree.getroot()
        
        xcoord = xcoord+xcoord[::-1]
        ycoord = ycoord+ycoord[::-1]
        for n in range(34):            
            name = villager + " photo " + str(e) + "-" + str(a) + "-" + str(n) + ".png"
            xmlname = villager + " photo " + str(e) + "-" + str(a) + "-" + str(n) + ".xml"
            root.find("filename").text = name
            root.find("path").text = folder+name
            root.find(".//xmin").text = str(xcoord[n][0])
            root.find(".//xmax").text = str(xcoord[n][1])
            root.find(".//ymin").text = str(ycoord[n][0])
            root.find(".//ymax").text = str(ycoord[n][1])

                
            
            tree.write(folder+xmlname)
        