import numpy as np
import cv2
import math
def color(imgSize):
    cornerSize = int(math.floor(imgSize/8));
    img = np.ones((imgSize,imgSize,3));
    img[:cornerSize, :cornerSize] = (0,0,1); #(b,g,r)
    img[:cornerSize:, -cornerSize:] = (0,1,0);
    img[-cornerSize:, :cornerSize] = (1,0,0);
    img[-cornerSize:, -cornerSize:] = (0,0,0);
    cv2.imshow('img',img);
    cv2.waitKey(0);
    return;
color(500);
