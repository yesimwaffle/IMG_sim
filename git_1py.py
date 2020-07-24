import cv2
a = "/Users/waffle/Documents/random pic/70559da1-e676-49.jpg"
cv2.imread(a)
b = cv2.imread(a)

b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
cv2.imwrite('b.png', b)