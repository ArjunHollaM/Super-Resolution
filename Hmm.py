import cv2
img=cv2.imread("\\Users\\HOLLA-PC\\Downloads\\IMG_C.jpg", cv2.IMREAD_UNCHANGED)

print("Original Dimensions: ",img.shape)
scale_percent = 200
a = int(img.shape[1] * scale_percent / 100)
b = int(img.shape[0] * scale_percent / 100)
d = (a,b)
new=cv2.resize(img,d,interpolation=cv2.INTER_AREA)
print("New Dimensions: ",new.shape)
cv2.imshow("New Image: ",new)
cv2.waitKey(0)
cv2.destroyAllWindows()
