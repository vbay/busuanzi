import json
import numpy as np
# lo_fs = json.load(open("/Users/wangxiaolei/Projects/dajing-group/dajing-services/api-docs/services-sql/dataset/location.json",encoding='utf-8'))
# print(lo_fs)
# print(type(lo_fs))
filep = "/Users/wangxiaolei/Projects/dajing-group/dajing-services/api-docs/services-sql/dataset/location.json"

fp = json.dumps(filep, ensure_ascii=False)

print (fp)

# f = open(filep)
# for line in f:
#     print(line)

# print(filep,'w')
#
# fp = open(filep,'w')
# js =json.dump(filep,lo_fs)
# fs = json.dump(open(filep,'w'),lo_fs)
# d = {'a': 'aaa', 'b': ['b1', 'b2', 'b3'], 'c': 100}
# json_str = json.dumps(d)
# print (json_str)
# print(type(json_str))

# json.dump(lo_fs,open('/Users/wangxiaolei/Projects/dajing-group/dajing-services/api-docs/services-sql/dataset/location1.json','w',encoding='utf-8'))