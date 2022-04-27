import numpy as np
import cv2 as cv


def roi(image1,vertices):
    mask = np.zeros_like(image1)
    #channel_count = image.shape[2]
    match_mask_color = 255
    cv.fillPoly(mask,vertices,match_mask_color)
    masked_image = cv.bitwise_and(image1,mask)
    return masked_image

def draw_lines(image2,lines):
    image2 = np.copy(image2)
    blank_image = np.zeros((image2.shape[0],image2.shape[1], 3),dtype=np.uint8)
    for vectors in lines:
        for x1,y1,x2,y2 in vectors:
            cv.line(blank_image, (x1,y1), (x2,y2), (256,0,256),thickness=10)
   
    image2 = cv.addWeighted(image2, 0.8, blank_image, 1, 0.0)
    return image2


def process(image3):
    height = image3.shape[0]
    width = image3.shape[1]
    roi_vertices= [(300,650),(1150,650),(730,420)]

    gray_image = cv.cvtColor(image3,cv.COLOR_RGB2GRAY)
    canny_image = cv.Canny(gray_image,200,225)
    cropped_image = roi(canny_image,np.array([roi_vertices],np.int32))
    lines = cv.HoughLinesP(cropped_image,rho = 2, theta = np.pi/60, threshold = 50, lines = np.array([]), minLineLength = 40, maxLineGap = 100)
    image_with_lines = draw_lines(image3,lines)
    return image_with_lines

cap = cv.VideoCapture('test1.mp4',0)

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
   
    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv.destroyAllWindows()