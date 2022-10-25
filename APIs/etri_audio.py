#-*- coding:utf-8 -*-
import urllib3
import json
import base64
openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
accessKey = "09bc8742-702f-4b0d-a46a-fb29c118dbf5"
audioFilePath = "./test.wav"
languageCode = "korean"


def etri_audio_result(): 
    file = open(audioFilePath, "rb")
    audioContents = base64.b64encode(file.read()).decode("utf8")
    file.close()
    
    requestJson = {
        "access_key": accessKey,
        "argument": {
            "language_code": languageCode,
            "audio": audioContents
        }
    }
    
    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )
    
    # print("[responseCode] " + str(response.status))
    # print("[responBody]")
    # print(str(response.data,"utf-8"))
    print("===== etri adio =====")
    data = json.loads(response.data.decode("utf-8", errors='ignore'))
    result = data['return_object']['recognized']
    print(result)
    return result