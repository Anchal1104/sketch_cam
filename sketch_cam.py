import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    inverted = 255 - gray
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    inverted_blur = 255 - blurred
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)

    cv2.imshow('Original', frame)
    cv2.imshow('Pencil Sketch', sketch)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()
    
    cv2.imshow('Original (Paused)', frame)
    cv2.imshow('Final Sketch(Paused)', sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()