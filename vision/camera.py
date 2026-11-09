import cv2
camera = cv2.VideoCapture(0)
while camera.isOpened():
    ret, frame = camera.read()
    if not ret:
        break
    cv2.imshow("test", frame)
    if cv2.waitKey(1) == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()