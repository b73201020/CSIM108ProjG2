#OK 成功
# 使用 Microsoft Azure Emotion API
#https://azure.microsoft.com/en-us/services/cognitive-services/emotion/

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

#照片集
images=["https://upload.wikimedia.org/wikipedia/commons/1/1b/%E8%94%A1%E8%8B%B1%E6%96%87%E5%AE%98%E6%96%B9%E5%85%83%E9%A6%96%E8%82%96%E5%83%8F%E7%85%A7.png",
    "https://www.bestcouplesworkshops.com/wp-content/uploads/2015/06/couple-3.png",
    "http://www.mtv.com/news/wp-content/uploads/2015/10/Plastics-1445283863.jpg",
    "https://media.licdn.com/mpr/mpr/AAEAAQAAAAAAAAc1AAAAJDYyYTg4OTk2LTY2NjQtNDJiNy05MjgwLWNlZDlkZDFmODI5Ng.jpg",
    "https://marketingland.com/wp-content/ml-loads/2015/12/people-customers-emotions-ss-1920-800x450.jpg",
    "https://marketingland.com/wp-content/ml-loads/2015/12/people-customers-emotions-ss-1920-800x450.jpg",
    "http://3.bp.blogspot.com/_0AyNA9sRlIs/TFB5NfKfhnI/AAAAAAAAJLU/tCZDBe-KQ2I/s1600/propagation031.jpg"
    ]


# Replace the example URL below with the URL of the image you want to analyze.
#body = "{ 'url': 'https://www.example.com/1.jpg' }"
image_path =images[6]
body = "{ 'url': '%s'}"%image_path


#辨識結果呈現
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

except Exception as e:
    print(e.args)


# 從URL讀照片
req = urllib.request.urlopen(image_path)
arr = numpy.asarray(bytearray(req.read()), dtype=numpy.uint8)
image = cv2.imdecode(arr,-1) # 'load it as it is'

cv2.imshow('orginal image',image)
#辨識結果
for item in parsed:
    #faceRectangle and scores for each faces
    faceRect = item['faceRectangle']
    scores = item['scores']
    #座標&寬高
    x= faceRect['left']
    y= faceRect['top']
    w = faceRect['width']
    h = faceRect['height']

    #畫臉外框
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


    i = 0
    color = (0, 0, 230)  # BGR
    baseline = 5

    #分數
    for emotion, score in scores.items():
        if(float(score)>0.01): #分數大於0.01則輸出文字

            outputText = emotion + ':' + str("%.2f" % score)
            i = i + 1
            cv2.rectangle(image, (x, y + h + baseline + 20 * (i - 1)),
                                (x + 180, y + h + baseline + 20 * i),
                                (200, 200, 200), -1)
            cv2.putText(image, outputText, (x, y + h + 20 * i), font, fontScale, color, 1, cv2.LINE_AA)


from time import gmtime, strftime
now = strftime("%Y%m%d_%H%M%S", gmtime())
print(now)  #現在時間

cv2.imshow('Faces found',image)
cv2.imwrite("face_detection%s.jpg"%now, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

####################################
