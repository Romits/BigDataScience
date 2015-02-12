def find_sum_hash(inputArray,targetSum):
    match = {}
    found = 0
    for i in xrange(len(inputArray)):
        if targetSum-inputArray[i] in match.keys():
            for t in match[targetSum-inputArray[i]]:
                found += 1
                print "%d: [%d]=%d - [%d]=%d"%(found, t, inputArray[t], i, inputArray[i])
        if inputArray[i] in match.keys():
            match[inputArray[i]].append(i)
        else:
            match[inputArray[i]] = [i]
    return found

def main():
    inputArray = [1,4,5,6,7,8,9]
    targetSum = 12
    retVal =  find_sum_hash(inputArray, targetSum)
    print "Number of Pairs found %d\n" % (retVal)

if __name__ == '__main__':
    main()

