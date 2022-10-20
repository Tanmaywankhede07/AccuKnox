# logs = 'E1 I1\nE1 I2\nE1 I3\nE2 I2\nE1 I4\nE2 I3\nE3 I2\nE2 I4'
file = open("data.txt", "r")
fileRead = file.read()
# print(fileRead)

loglist = fileRead.split('\\n')
# print(loglist)
def checkDuplicate(loglist):
    dup = {}
    for entry in loglist:
        eater, item = entry.split(' ')
        if eater not in dup.keys():
            dup[eater] = set()
            dup[eater].add(item)
        else:
            if item in dup[eater]:
                return True
            else:
                dup[eater].add(item)
    return False

def findTop3Items(loglist):
    itcount = {}
    for entry in loglist:
        eater, item = entry.split(' ')
        if item in itcount.keys():
            itcount[item] += 1
        else:
            itcount[item] = 1

    itcount = sorted(itcount.items(), key=lambda x: x[1], reverse=True)
    i = 0
    ret = []
    for key, value in itcount:
        if i < 3:
            ret.append(key)
        i += 1
    return ret

if checkDuplicate(loglist):
    print("Error: Duplicate fooditem for same eater found!")
else:
    print("Top 3 items are: ")
    top3Items = findTop3Items(loglist)
    for item in top3Items:
        print(item)
