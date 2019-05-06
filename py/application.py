import parse

class Application:
    appName = ""
    managementUrl = ""
    appId = ""
    
    memory = ""
    usedMemory = ""
    memoryPercent = ""

    heapMemory = ""
    usedHeapMemory = ""
    heapMemoryPercent = ""

    nonHeapMemory = ""
    usedNonHeapMemory = ""
    nonHeapMemoryPercent = ""

    def dealMemory(self, value):
        global tempMemory
        if value > 1000:
            value = value/1000
            if value > 1000:
                value = value/1000
                tempMemory = str('%.2f' % value) + "G"
            else:
                tempMemory = str('%.2f' % value) + "M"
        return tempMemory

    def __init__(self, appName, managementUrl, appId, 
     memory, usedMemory, memoryPercent, 
     heapMemory, usedHeapMemory, heapMemoryPercent, 
     nonHeapMemory, usedNonHeapMemory, nonHeapMemoryPercent
):
        self.name = appName,  
        self.id = appId,  
        self.url = managementUrl[7:-5], 
        self.memory = dealMemory(memory) 
        self.usedMemory = dealMemory(usedMemory), 
        self.memoryPercent = str('%.2f' %(memoryPercent * 100)) + "%", 
        self.heapMemory = dealMemory(heapMemory),  
        self.usedHeapMemory = dealMemory(usedHeapMemory), 
        self.heapMemoryPercent = str('%.2f' %(heapMemoryPercent * 100)) + "%", 
        self.nonHeapMemory = dealMemory(nonHeapMemory), 
        self.usedNonHeapMemory = dealMemory(usedNonHeapMemory), 
        self.nonHeapMemoryPercent = str('%.2f' %(nonHeapMemoryPercent * 100)) + "%"
        
