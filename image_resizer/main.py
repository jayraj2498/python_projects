import cv2

image=cv2.imread("transformer.jpeg",  cv2.IMREAD_UNCHANGED)

# cv2.imshow('title', image)
# cv2.waitKey(0)

scale_percentage = 200
new_width= int(image.shape[1] * scale_percentage /100)
new_height= int(image.shape[0] * scale_percentage /100)

# resize_image

output_img =cv2.resize(image, (new_width,new_height))
cv2.imwrite('newLarger_trans.png',output_img)
cv2.waitKey(0)
