import requests
import execjs
import os
import re
session=requests.Session()
headers={
    'Host':'www.scholat.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
}
os.environ["EXECJS_RUNTIME"] = "PhantomJs"
node = execjs.get()
file=r'C:\Users\Leo\Desktop\xuezhewang.js'
ctx=node.compile(open(file).read())
res=session.get('http://www.scholat.com/Auth.html').text
pattern=re.compile(r'session_value = "(.*?)";',re.S)
session_value=re.search(pattern,res).group(1)
js="strEnc('%s','%s','%s','%s')"%('123456',session_value,'userc','pfir')
data=ctx.eval(js)
params={'urlBeforeLogin':'',
        'j_username':'zhenguoleo@163.com',
        'j_password_ext':'123456',
        'j_passdec':data}
r=session.post('http://www.scholat.com/Auth.html',headers=headers,data=params)
response=session.get('http://www.scholat.com/Phomepage.html')
print(response.text)


