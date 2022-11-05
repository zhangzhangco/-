import jsonpath
import json
import sys, os, fnmatch
from shutil import copyfile

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

with open("/Users/John/mediastandards-registry-china/src/main/data/documents.json", encoding='utf8') as f:
    data = json.load(f)
    r = jsonpath.jsonpath(data, '$[0].docId')
for key in range(len(data)):
    if jsonpath.jsonpath(data, "$["+str(key)+"].href"):
        file = data[key]['docTitle']
        fn = find('*'+file+'*.pdf', '/Users/John/Library/Containers/com.kingsoft.wpsoffice.mac/Data/Library/Application Support/Kingsoft/WPS Cloud Files/userdata/qing/filecache/259626762/标准研究室/标准处文件共享/文献资料/标准电子版归档')
        if len(fn) > 0:
            srcfile = fn[0]
            objfile = os.path.abspath('..')+'/filmstandards/'+data[key]['docLabel'].replace('/', '')+' '+data[key]['docTitle']+'.pdf'
            copyfile(srcfile,objfile)
            data[key]['href']='file://'+objfile.replace(" ","%20")
        # for key, value in data[key].items():
        #     print(key, value)

with open("/Users/John/mediastandards-registry-china/src/main/data/documents.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(json.dumps(data, ensure_ascii=False))
