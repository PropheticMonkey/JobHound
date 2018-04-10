import json

leadList = [
            {'name':"Test Job 1", 'description':"A pretty good job."}, 
            {'name':"Test Job 2", 'description':"An ok job."}, \
            {'name':"Test Job 3", 'description':"A not very fun job."} 
            ]

def getLeadListJson():
    return json.dumps({'data': leadList})

def setLeadList(jsonString):
    return json.loads(jsonString)