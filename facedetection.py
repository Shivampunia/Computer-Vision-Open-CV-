import cv2 as cv

img=cv.imread("Resources/people.png")
cv.imshow("output",img)

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

harr_cascade= cv.CascadeClassifier("C:\\Users\\hp\\AppData\\Roaming\\JetBrains\\PyCharmCE2024.2\\scratches\\scratch.dtd")
face_rect= harr_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=7)

print(f'Number of faces detect= {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow("face detect",img)



cv.waitKey(0)