fname = input('Enter File: ')

lo = 'D:\coding\pythonStudy04\\'
if len(fname) < 1 : fname = 'clown.txt'
hand = open(lo+fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        # if the key is not there the default is 0
        # idiom : retrieve/create/update
        """
        oldcount = di.get(w, 0)
        print(w, ' old: ' ,oldcount)
        newCount = oldcount +1
        di[w] = newCount
        print(w, ' new: ' ,newCount)
        """
        di[w] = di.get(w, 0) + 1

        """
        if w in di :
            di[w] = di[w] + 1
        else:
            di[w] = 1
            
        print(w, di[w])
        """

#print(di)

#now we want to find the most common word
largest = -1
theword = None
for k,v in di.items():
    if v > largest :
        largest = v
        theword = k #capture/remember the word that was largest

print(theword, largest)