""" the commented out part was used for calibration """
#
# from matplotlib.pyplot import imshow, scatter, show
# import cv2
# import numpy as np

# def empty_function(*arg):
#     pass

# # tune canny edge detection. accept with pressing "C"
# def CannyTrackbar(img, win_name):
#     trackbar_name = win_name + "Trackbar"

#     cv2.namedWindow(win_name)
#     cv2.resizeWindow(win_name, 500,100)
#     cv2.createTrackbar("canny_th1", win_name, 0, 255, empty_function)
#     cv2.createTrackbar("canny_th2", win_name, 0, 255, empty_function)
#     cv2.createTrackbar("blur_size", win_name, 0, 255, empty_function)
#     cv2.createTrackbar("blur_amp", win_name, 0, 255, empty_function)

#     while True:
#         trackbar_pos1 = cv2.getTrackbarPos("canny_th1", win_name)
#         trackbar_pos2 = cv2.getTrackbarPos("canny_th2", win_name)
#         trackbar_pos3 = cv2.getTrackbarPos("blur_size", win_name)
#         trackbar_pos4 = cv2.getTrackbarPos("blur_amp", win_name)
#         img_blurred = cv2.GaussianBlur(img.copy(), (trackbar_pos3 * 2 + 1, trackbar_pos3 * 2 + 1), trackbar_pos4)
#         canny = cv2.Canny(img_blurred, trackbar_pos1, trackbar_pos2)
#         cv2.imshow(win_name, canny)

#         key = cv2.waitKey(1) & 0xFF
#         if key == ord("c"):
#             break

#     cv2.destroyAllWindows()
#     return canny

# def HoughTrackbar(canny, img_org, win_name):
#     trackbar_name = win_name + "Trackbar"

#     cv2.namedWindow(win_name)
#     cv2.resizeWindow(win_name, 500,100)
#     cv2.createTrackbar("canny_th1", win_name, 1, 255, empty_function)
#     cv2.createTrackbar("canny_th2", win_name, 1, 255, empty_function)
#     cv2.createTrackbar("blur_size", win_name, 1, 255, empty_function)
#     cv2.createTrackbar("4", win_name, 1, 255, empty_function)
#     cv2.createTrackbar("5", win_name, 1, 255, empty_function)
#     cv2.createTrackbar("6", win_name, 1, 255, empty_function)
#     cv2.createTrackbar("blur_amp", win_name, 50, 255, empty_function)

#     while True:
#         img_org_copy = img_org.copy()
#         trackbar_pos1 = cv2.getTrackbarPos("canny_th1", win_name)
#         trackbar_pos2 = cv2.getTrackbarPos("canny_th2", win_name)
#         trackbar_pos3 = cv2.getTrackbarPos("blur_size", win_name)
#         trackbar_pos4 = cv2.getTrackbarPos("4", win_name)
#         trackbar_pos5 = cv2.getTrackbarPos("5", win_name)
#         trackbar_pos6 = cv2.getTrackbarPos("6", win_name)
#         trackbar_pos7 = cv2.getTrackbarPos("blur_amp", win_name)
#         circles = cv2.HoughCircles(canny,cv2.HOUGH_GRADIENT, trackbar_pos1+1, trackbar_pos2+1, trackbar_pos3+1, trackbar_pos4+1, trackbar_pos5+1, trackbar_pos6+1, trackbar_pos7+1)

from matplotlib.pyplot import imshow, scatter, show, savefig
import cv2

image = cv2.imread('circles.png', 0)
image = cv2.GaussianBlur(image.copy(), (27, 27), 0)
image = cv2.Canny(image, 0, 130)
cv2.imshow("canny", image)
cv2.waitKey(0)
imshow(image, cmap='gray')

circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 22, minDist=1, maxRadius=50)
x = circles[0, :, 0]
y = circles[0, :, 1]

scatter(x, y)
savefig('result1.png')
cv2.waitKey(0)

_, cnts, _ = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)

# loop over the contours
for c in cnts:
    # compute the center of the contour
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    # draw the contour and center of the shape on the image
    cv2.drawContours(image, [c], -1, (125, 125, 125), 2)
    cv2.circle(image, (cX, cY), 3, (255, 255, 255), -1)

cv2.imshow("Image", image)
cv2.imwrite("result2.png", image)
cv2.waitKey(0)
