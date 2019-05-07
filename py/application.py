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

    def __init__(self, appName, managementUrl, appId, 
     memory, usedMemory, memoryPercent, 
     heapMemory, usedHeapMemory, heapMemoryPercent, 
     nonHeapMemory, usedNonHeapMemory, nonHeapMemoryPercent
):
        self.appName = appName
        self.managementUrl = managementUrl
        self.appId = appId
        self.memory = memory
        self.usedMemory = usedMemory
        self.memoryPercent = memoryPercent
        self.heapMemory = heapMemory
        self.usedHeapMemory = usedHeapMemory
        self.heapMemoryPercent = heapMemoryPercent
        self.nonHeapMemory = nonHeapMemory
        self.usedNonHeapMemory = usedNonHeapMemory
        self.nonHeapMemoryPercent = nonHeapMemoryPercent
        
        
