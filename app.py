import cv2;
image = cv2.imread("./assets/demo2.png")

grey_filter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("graysacle.png",grey_filter)

invert = cv2.bitwise_not(grey_filter)
cv2.imwrite("invert.png",invert)

blur = cv2.GaussianBlur(invert,(21,21),0)
cv2.imwrite("blur.png",blur)

invertedBlur = cv2.bitwise_not(blur)
cv2.imwrite("invBlur.png",invertedBlur)

sketch = cv2.divide(grey_filter,invertedBlur,scale=256.0)
cv2.imwrite("sketch.png",sketch)