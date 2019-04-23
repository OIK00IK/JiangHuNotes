import urllib.request
import json
import parse

iapplicationListUrl = "http://support.icore.ccic-net.com.cn/ui/boot-admin/api/applications/"
applicationListUrl = "http://support.core.ccic-net.com.cn/ui/boot-admin/api/applications/"

serviceCode = ""

listUrl = iapplicationListUrl

ilogList = []

response = urllib.request.urlopen(listUrl)
applicationList = response.read().decode("utf-8")
json_applicationList = json.loads(applicationList)

def takeUrl(elem):
    return elem['url']

def takeName(elem):
    return elem['name']



for application in json_applicationList:
    if application["name"].startswith("ILOG"):
        if -1 == str(ilogList).find(str(application["id"]) ):
            ilogApplication = parse.getIlogList(application,listUrl)
            ilogList.append(ilogApplication)

ilogList.sort(key=takeName)

lifeApplicationCount = 0
nvApplicationCount = 0
vehicleApplicationCount = 0

for ilog in ilogList:
    if ilog["name"].startswith("ILOG-LIFE"):
        lifeApplicationCount = lifeApplicationCount + 1
    elif ilog["name"].startswith("ILOG-NV"):
        nvApplicationCount = nvApplicationCount + 1
    else:
        vehicleApplicationCount = vehicleApplicationCount + 1

ilogList = [
            ilogList[0:lifeApplicationCount],
            ilogList[lifeApplicationCount:-vehicleApplicationCount],
            ilogList[-vehicleApplicationCount:]
            ]

for ilogType in ilogList:
        parse.printIlogList(ilogType)




#print(str(ilogList))


#parse.printIlogList(ilogList)


         

