import cv2

img = cv2.imread('DL/OpenCV_ex/card.png')
target_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# contours, hierarchy = cv2.findContours(otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# contours, hierarchy = cv2.findContours(otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

COLOR = (0, 200, 0)
# cv2.drawContours(target_img, contours, -1, COLOR, 2)

idx = 1
for cnt in contours:
  if cv2.contourArea(cnt) > 25000:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(target_img, (x, y), (x+w, y+h), COLOR, 2)

    crop = img[y:y+h, x:x+w]
    cv2.imshow('crop_{}'.format(idx), crop)
    cv2.imwrite('DL/OpenCV_ex/card_crop_{}.png'.format(idx), crop)
    idx += 1

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('otsu', otsu)
cv2.imshow('contour', target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
