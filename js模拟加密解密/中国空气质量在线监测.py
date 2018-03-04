import requests
import execjs
import os
import json
# Init environment
os.environ["EXECJS_RUNTIME"] = "PhantomJs"
node = execjs.get()
# Params
method = 'GETCITYWEATHER'
city = '北京'
type = 'HOUR'
start_time = '2018-02-27 00:00:00'
end_time = '2018-02-27 23:00:00'
# Compile javascript
file = r'C:\Users\Leo\Desktop\javascript.js'
ctx = node.compile(open(file).read())
# Get params
js = 'getEncryptedData("%s","%s","%s","%s","%s")'%(method, city, type, start_time, end_time)
params = ctx.eval(js)
api = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
response = requests.post(api, data={'d': params})
js = 'decodeData("%s")'%response.text
decrypted_data = ctx.eval(js)
data = json.loads(decrypted_data)
print(data)
