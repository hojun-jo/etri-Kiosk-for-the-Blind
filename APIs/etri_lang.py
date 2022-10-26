#-*- coding:utf-8 -*-
import urllib3
import json
 
# 언어 분석 기술(구어)
openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU_spoken"
accessKey = "09bc8742-702f-4b0d-a46a-fb29c118dbf5"
analysisCode = "ner"

def etri_lang_result(text):
    requestJson = {
        "access_key": accessKey,
        "argument": {
            "text": text,
            "analysis_code": analysisCode
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
    print("===== etri lang =====")
    data = json.loads(response.data.decode("utf-8", errors='ignore'))    
    # print(data['return_object']['sentence'][0]['NE'])
    result = []
    for i in data['return_object']['sentence'][0]['NE']:
        if i['type'] == "CV_FOOD" or "AF_WARES" or "QT_COUNT":
            print(i['text'])
            result.append(i['text'])
    
    return result