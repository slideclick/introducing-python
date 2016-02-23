# abcdefgh穿山甲到?
s=b'\xe7\xa9\xbf\xe5\xb1\xb1\xe7\x94\xb2\xe5\x88\xb0\xe7\xa9\xbf\xe5\xb1\xb1\xe7\x94\xb2\xe5\x88\xb0\xe5\xba\x95\xe8\xaf\xb4\xe4\xba\x86\xe4\xbb\x80\xe4\xb9\x88\xef\xbc\x9f'
sd = s.decode('utf-8') 
print(sd)
print()
with open('chinese.txt','wb') as fb:
    fb.write(s)#我用二进制方式写进文件，那么以UFT8打开就可以正确显示

with open('chinese.txt','r') as fb:
    pass#st= fb.read()#read会失败，以OS默认的gbk去解码会失败

with open('chinese.txt','r',encoding='utf-8') as fb:
    st= fb.read()#read会成功，因为我指定了解码格式是utf-8   
    
    
import re
rs = re.search(r'(a)\w+\1',"cabad") 
if rs:
    print(rs.group())
    print(rs.group(1))
print()    
rs = re.search(r'(山)(.*)\1',sd) 
if rs:
    print(rs.group())
    print(rs.group(0))
    print(rs.group(1))
    print(rs.group(2))
    print(rs.groups())
    print(rs.groupdict())
print()   
rs = re.search(r'(?P<shang>山)(.*)(?P=shang)',sd) 
if rs:
    print(rs.group())
    print(rs.group(0))
    print(rs.group(1))
    print(rs.group(2))
    print(rs.group(3))
    print(rs.groups())
    print(rs.groupdict())    
    