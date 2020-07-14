import os
from os import listdir
from os.path import isfile,isdir, join
import numpy as np
import cv2
import time
import sys
from imageai.Detection import ObjectDetection
import json
from exiftool_custom import exiftool


def getDetectedObject(detector, inputfile, outputfile, twicefile):
    
    detections = detector.detectObjectsFromImage(input_image=inputfile, output_image_path=outputfile)
    objects = []
    for eachObject in detections:
 
        objectone = {}
        objectone[eachObject["name"]] = eachObject['box_points']
        objects.append(objectone)
        
    with exiftool.ExifTool() as et:
        et.copy_tags(inputfile, outputfile)    
    return objects
 
 
def main(argv):
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "models/resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    inputdir = argv[0]
    outputdir = 'detect_' + inputdir
    if isdir(outputdir):
        pass
    else:
        os.mkdir(outputdir)
    inputfiles = [f for f in listdir(inputdir) if isfile(join(inputdir, f))]
    # print(inputdir, outputdir, inputfiles)
    detectedobjects = []
    for inputfile in inputfiles:
        onefile = {}
        infile = inputdir + '/' + inputfile
        outfile = outputdir + '/' + 'detect_' + inputfile
        twicefile = outputdir + '/' + 'twice_' + inputfile
        objects = getDetectedObject(detector, infile,outfile, twicefile)
        onefile[inputfile] = objects
        detectedobjects.append(onefile)  
    with open(inputdir+'.json', 'w') as json_file:
        json.dump(detectedobjects, json_file)
        json_file.close()
if __name__ == "__main__":
   main(sys.argv[1:])