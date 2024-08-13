import cv2

# Load the Haar Cascade file for face detection
face_cap = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start capturing video from the webcam
video_cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, video_data = video_cap.read()

    # Convert the frame to grayscale
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cap.detectMultiScale(col, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("video_live", video_data)

    # Break the loop if the 'a' key is pressed
    if cv2.waitKey(10) == ord("a"):
        break

# Release the webcam and close all OpenCV windows
video_cap.release()
cv2.destroyAllWindows()