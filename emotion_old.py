#OKOKOKOK

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, sys
import json

import numpy
import cv2
headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '50e0e7d55b584047b950d812d5d65c09',
}

params = urllib.parse.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
#body = "{ 'url': 'https://upload.wikimedia.org/wikipedia/commons/1/1b/%E8%94%A1%E8%8B%B1%E6%96%87%E5%AE%98%E6%96%B9%E5%85%83%E9%A6%96%E8%82%96%E5%83%8F%E7%85%A7.png' }"
image_path = 'https://upload.wikimedia.org/wikipedia/commons/1/1b/%E8%94%A1%E8%8B%B1%E6%96%87%E5%AE%98%E6%96%B9%E5%85%83%E9%A6%96%E8%82%96%E5%83%8F%E7%85%A7.png'
image_path = "https://www.bestcouplesworkshops.com/wp-content/uploads/2015/06/couple-3.png"
body = "{ 'url': '" + image_path +"'}"


#辨識結果呈現
faces = []
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
fontScale=1
thickness=1
parsed =""
try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
    #   URL below with "westcentralus".
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read().decode("utf-8")

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)

    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    conn.close()


    # for item in parsed:
    #     face = []
    #     face.append(item['faceRectangle']['left'])
    #     face.append(item['faceRectangle']['top'])
    #     face.append(item['faceRectangle']['width'])
    #     face.append(item['faceRectangle']['height'])
    #
    #     text = 'anger:' + str(item['scores']['anger'])
    #     face.append(text)
    #     text = 'contempt:' + str(item['scores']['contempt'])
    #     face.append(text)
    #     text = 'disgust:' + str(item['scores']['disgust'])
    #     face.append(text)
    #     text = 'fear:' + str(item['scores']['fear'])
    #     face.append(text)
    #     text = 'happiness:' + str(item['scores']['happiness'])
    #     face.append(text)
    #     text = 'neutral:' + str(item['scores']['neutral'])
    #     face.append(text)
    #     text = 'sadness:' + str(item['scores']['sadness'])
    #     face.append(text)
    #     text = 'surprise:' + str(item['scores']['surprise'])
    #     face.append(text)
    #     #print(face)
    #     faces.append(face)

    #print(parsed[0]['faceRectangle']['height'])
    #print(faces)
except Exception as e:
    print(e.args)


# Read the image
req = urllib.request.urlopen(image_path)
arr = numpy.asarray(bytearray(req.read()), dtype=numpy.uint8)
image = cv2.imdecode(arr,-1) # 'load it as it is'

for item in parsed:

    x= item['faceRectangle']['left']
    y= item['faceRectangle']['top']
    w = item['faceRectangle']['width']
    h = item['faceRectangle']['height']

    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    t1 = 'anger:' + str("%.2f" % item['scores']['anger'])
    t2 = 'contempt:' + str("%.2f" % item['scores']['contempt'])
    t3 = 'disgust:' + str("%.2f" % item['scores']['disgust'])
    t4 = 'fear:' + str("%.2f" % item['scores']['fear'])
    t5 = 'happiness:' + str("%.2f" % item['scores']['happiness'])
    t6 = 'neutral:' + str("%.2f" % item['scores']['neutral'])
    t7 = 'sadness:' + str("%.2f" % item['scores']['sadness'])
    t8 = 'surprise:' + str("%.2f" % item['scores']['surprise'])

    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, t1, (x, y + h + 20), font, fontScale, (255, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(image, t2, (x, y + h + 40), font, fontScale, (0, 255, 0), 1, cv2.LINE_AA)
    cv2.putText(image, t3, (x, y + h + 60), font, fontScale, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.putText(image, t4, (x, y + h + 80), font, fontScale, (255, 255, 0), 1, cv2.LINE_AA)
    cv2.putText(image, t5, (x, y + h + 100), font, fontScale, (255, 0, 255), 1, cv2.LINE_AA)
    cv2.putText(image, t6, (x, y + h + 120), font, fontScale, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(image, t7, (x, y + h + 140), font, fontScale, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(image, t8, (x, y + h + 160), font, fontScale, (0, 0, 0), 1, cv2.LINE_AA)




















# for face in faces:
#     print(face)
#     for (x, y, w, h, t1, t2, t3, t4, t5, t6, t7, t8) in face:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         cv2.putText(image, t1, (x, y + h + 20), font, fontScale, (255, 0, 0), 1, cv2.LINE_AA)
#         cv2.putText(image, t2, (x, y + h + 40), font, fontScale, (0, 255, 0), 1, cv2.LINE_AA)
#         cv2.putText(image, t3, (x, y + h + 60), font, fontScale, (0, 0, 255), 1, cv2.LINE_AA)
#         cv2.putText(image, t4, (x, y + h + 80), font, fontScale, (255, 255, 0), 1, cv2.LINE_AA)
#         cv2.putText(image, t5, (x, y + h + 100), font, fontScale, (255, 0, 255), 1, cv2.LINE_AA)
#         cv2.putText(image, t6, (x, y + h + 120), font, fontScale, (0, 255, 255), 1, cv2.LINE_AA)
#         cv2.putText(image, t7, (x, y + h + 140), font, fontScale, (255, 255, 255), 1, cv2.LINE_AA)
#         cv2.putText(image, t8, (x, y + h + 160), font, fontScale, (0, 0, 0), 1, cv2.LINE_AA)


cv2.imshow('Faces found',image)
cv2.imwrite("face_detection.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

####################################
