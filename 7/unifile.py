# abcdefgh穿山甲到
s=b'\xe7\xa9\xbf\xe5\xb1\xb1\xe7\x94\xb2\xe5\x88\xb0\xe7\xa9\xbf\xe5\xb1\xb1\xe7\x94\xb2\xe5\x88\xb0\xe5\xba\x95\xe8\xaf\xb4\xe4\xba\x86\xe4\xbb\x80\xe4\xb9\x88\xef\xbc\x9f'
sd = s.decode('utf-8') 
print(sd)

import re
rs = re.search(r'(a)\w+\1',"cabad") 
if rs:
    print(rs.group())
    print(rs.group(1))
    
rs = re.search(r'(山).*\1',sd) 
if rs:
    print(rs.group())