def find_elem_hash(inputArray,targetElem):
    match = {}
    found = 0
    for i in xrange(len(inputArray)):
        if inputArray[i] in match.keys():
            match[inputArray[i]].append(i)
        else:
            match[inputArray[i]] = [i]
    return match[targetElem]

def main():
    inputArray = [1,4,5,6,7,4,9,6,6,6]
    targetElem = 6
    indexArray =  find_elem_hash(inputArray, targetElem)
    if len(indexArray) == 0:
        print "Elem %d not found" % (targetElem)
    elif len(indexArray) == 1:
        print "One occunrence of Elem %d at index %d" % (targetElem,indexArray[0])
    else:
        print "StartIndex %d and EndIndex %d for Elem %d" % (indexArray[0],indexArray[-1],targetElem)

if __name__ == '__main__':
    main()

