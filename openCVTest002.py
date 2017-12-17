import cv2

import numpy as np



text = "Funny text inside the box"
fontFace = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
fontScale = 1
thickness = 1

height = 400
width=1000

img = np.zeros((height,width,3), np.uint8)

baseline=0
(textSize, baseline) = cv2.getTextSize(text, fontFace,fontScale, thickness)
print("text size", textSize)

baseline += thickness

# center the text
textOrg = (int((width - textSize[0])/2),int((height - textSize[1])/2))

print(textOrg)
# draw the box

lu = (textOrg[0], textOrg[1])
rd =  (textOrg[0]+ textSize[0], textOrg[1]-textSize[1])
print(lu)
print(rd)


cv2.rectangle(img, lu,rd ,(0,0,255))


# then put the text itself
cv2.putText(img, text, textOrg, fontFace, fontScale,(255,255,255), thickness, cv2.LINE_AA)

cv2.imshow('Faces found',img)

cv2.waitKey(0)
cv2.destroyAllWindows()