import cv2

# Open webcam (use 0 for default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur (reduces noise)
    blur = cv2.GaussianBlur(gray, (5, 15), 0)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blur, 50, 50)

    # Show results
    cv2.imshow("Original Video", frame)
    cv2.imshow("Canny Edges", edges)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
