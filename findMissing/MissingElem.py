import sys
def findMissing(A):
    lenA = len(A)
    if lenA == 0:
        return 1
    if lenA == 1:
        if A[0] == 1:
            return int(A[0]) + 1
        else:
            return int(A[0]) - 1
    else:
        totalSum = 0
        setA = set(A)
        setA = sorted(setA)
        totalSum = (int(setA[-1]) * (int(setA[-1]) + 1))/2
        checkSum = 0
        for idx in range(len(setA)):
            checkSum = checkSum + int(setA[idx])
        missingElem = totalSum - checkSum
        if missingElem == 0:
            missingElem = int(setA[-1]) + 1
    return missingElem


def main():
    #A = [2,2,3,1,5]
    #A = [2,2]
    #A = []
    A = sys.argv[1].split(',')
    y = findMissing(A)
    print y

if __name__=='__main__':
    main()   
