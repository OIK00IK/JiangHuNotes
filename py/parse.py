import urllib.request
import json
import Application

def dealMemory(value):
        global tempMemory
        if value > 1000:
            value = value/1000
            if value > 1000:
                value = value/1000
                tempMemory = str('%.2f' % value) + "G"
            else:
                tempMemory = str('%.2f' % value) + "M"
        return tempMemory


def getIlogList(application,listUrl):       
    appName = application["name"]
    managementUrl = application["managementUrl"]
    url = managementUrl[7:-5], 
    appId = application["id"]
    response = urllib.request.urlopen(listUrl + appId + "/metrics")
    applicationDetail = response.read().decode("utf-8")
    json_applicationDetail = json.loads(applicationDetail)

    memory = json_applicationDetail["mem"]
    usedMemory = memory - json_applicationDetail["mem.free"]
    memoryPercent = usedMemory/memory

    heapMemory = json_applicationDetail["heap.committed"]
    usedHeapMemory = json_applicationDetail["heap.used"]
    heapMemoryPercent = usedHeapMemory/heapMemory

    nonHeapMemory = json_applicationDetail["nonheap.committed"]
    usedNonHeapMemory = json_applicationDetail["nonheap.used"]
    nonHeapMemoryPercent = usedNonHeapMemory/nonHeapMemory

    app = Application(appName, url, appId, memory, usedMemory, memoryPercent, 
     heapMemory, usedHeapMemory, heapMemoryPercent, 
     nonHeapMemory, usedNonHeapMemory, nonHeapMemoryPercent)

    return app
'''
    ilogApplication = dict(name = appName, id = appId, url = managementUrl[7:-5],
                        memory = dealMemory(memory), usedMemory = dealMemory(usedMemory),
                        memoryPercent = str('%.2f' %(memoryPercent * 100)) + "%",
                        heapMemory = dealMemory(heapMemory), usedHeapMemory = dealMemory(usedHeapMemory),
                        heapMemoryPercent = str('%.2f' %(heapMemoryPercent * 100)) + "%",
                        nonHeapMemory = dealMemory(nonHeapMemory),usedNonHeapMemory = dealMemory(usedNonHeapMemory),
                        nonHeapMemoryPercent = str('%.2f' %(nonHeapMemoryPercent * 100)) + "%"
                        )
    return ilogApplication
'''

def printIlogList(ilogList): 
    print(len(ilogList))
    for ilog in ilogList:
        print(ilog['name'] + "\t" + ilog['url']  + "\t" + ilog['memoryPercent'] + "\t("  + ilog['usedMemory'] + "/" + ilog['memory'] + ")"
          + "\t" + ilog['heapMemoryPercent'] + "\t(" + ilog['usedHeapMemory'] + "/" + ilog['heapMemory'] + ")"
          + "\t" + ilog['nonHeapMemoryPercent'] + "\t(" + ilog['usedNonHeapMemory'] + "/" + ilog['nonHeapMemory'] + ")"
        )   