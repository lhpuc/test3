from operator import attrgetter
class report:
    def __init__(self,logId, employeeId,location,checkin,checkout):
        self.logId = logId
        self.employeeId = employeeId
        self.location = location
        self.checkin = checkin
        self.checkout = checkout
    def __repr__(self):
            return '({}, {}, {}, {})'.format(self.logId,self.employeeId,self.location,self.checkin)

def travelTime(a,b):
    if a==b: return 0
    else:
        if a == 'BuildingA': return 150 if b == 'BuildingB' else 200
        if a == 'BuildingB': return 150 if b == 'BuildingA' else 100
        if a == 'BuildingC': return 200 if b == 'BuildingA' else 100

def impossibleCheckin(reports):
    impossible = []
    idOfEm = []
    for x in reports:
        if x.employeeId not in idOfEm: idOfEm += [x.employeeId]
    print(idOfEm)
    for x in idOfEm:
        emInfo = []
        numofInfo=0
        for i in reports:
            if i.employeeId == x: 
                emInfo += [i]
                numofInfo+=1

        emInfo.sort(key = attrgetter('checkin'))
        for j in range(0,numofInfo):
            i = j
            while (i<numofInfo - 1):
                if (emInfo[i].checkout + travelTime(emInfo[i].location,emInfo[i+1].location) > emInfo[i+1].checkin):
                    impossible+=[emInfo[i+1].logId]
                i+=1
    return impossible


        
    
a= report('AFCK',1,'BuildingA',120,200)
b= report('BGFC',2,'BuildingB',300,400)
c= report('FECD',1,'BuildingA',120,200)
d= report('HGFD',2,'BuildingB',300,200)

print(impossibleCheckin([a,b,c,d]))




