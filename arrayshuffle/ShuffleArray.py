import random
import sys

def shuffleArray(inputArray):
    origLen = len(inputArray) - 1
    for i in range(origLen):
        modLen = origLen - i
        for j in range(0,(modLen)):
            rand = random.randint(0,j)
            lastVal = inputArray[modLen]
            currVal = inputArray[rand]
            inputArray[modLen] = currVal
            inputArray[rand] = lastVal
            
    
def main():
    #inputArray = [1,2,3,4,5,6]
    inputArray = (sys.argv[1]).split(',')
    shuffleArray(inputArray)
    print inputArray
    
if __name__=='__main__':
    main()
