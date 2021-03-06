import cv2

img_file = 'car_image.jpg'
video = cv2.VideoCapture('#your video file name#')
#video = cv2.VideoCapture('g20.mp4')

car_tracker_file = 'cars.xml'

pedestrian_tracker_file =('haarcascade_fullbody.xml')
car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)
while True:
    (read_successful, frame) = video.read()
    if read_successful:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrian = pedestrian_tracker.detectMultiScale(grayscaled_frame)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3 )
    for (x, y, w, h) in pedestrian:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 3 )    
    cv2.imshow('car detection', frame)

    cv2.waitKey(1)


""""        

img = cv2.imread(img_file)

car_tracker = cv2.CascadeClassifier(classifier_file) 

black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
car_tracker = cv2.CascadeClassifier(classifier_file)
cars = car_tracker.detectMultiScale(black_n_white)
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 5 )

 

cv2.imshow('car detection', img)

cv2.waitKey()



"""""
print('code completed')
