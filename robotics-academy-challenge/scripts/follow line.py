import GUI
import HAL
import cv2
import numpy as np

# Enter sequential code!

Kp = 0.5
Ki = 0.01
Kd = 0.1

prev_error = 0
integral = 0


def process_image(image):
    """Detects the red line and returns the error from the center."""
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
        else:
            cx = image.shape[1] // 2

        error = cx - (image.shape[1] // 2)
        return error, mask

    return 0, mask


while True:
    # Enter iterative code!
    image = HAL.getImage()
    error, processed_mask = process_image(image)

    integral += error
    derivative = error - prev_error
    correction = Kp * error + Ki * integral + Kd * derivative
    prev_error = error

    HAL.setV(1.0)
    HAL.setW(-correction / 100)

    GUI.showImage(processed_mask)
