import cv2

pathOut = "<folder_path>"
count = 0
counter = 1
vid = "<video_file_name>"
vid = "<video_file_path>"+vid
cap = cv2.VideoCapture(vid)
success = True
while success:
    success,image = cap.read()
    #capturing the images for every 2 seconds
    if count%2 == 0 :
         cv2.imwrite(pathOut + 'frame%d.jpg'%count,image)
    count+=1