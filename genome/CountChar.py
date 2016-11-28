#!/usr/bin/python -tt
import sys
"""
GATAGGAGTAGTGAGT
GTAGTAGAGTATGATAGTGTA
GATTAGATGATGATG
GATATATAGATATATTAGAT
GATAGATAGT
GATTAAGATATGATAGTAG
GATTAGATAGTAGTAGT
GTATAGATAGTAGTAGTGATGA
GTAGATGATGATAGTAGTAGT
GAAGTAGTGATGAGTAG

Sample output Format:

Position: 1 (A: 0%,  C: 0%, G: 100%, T: 0%)
Position: 2 (A: 80%, C: 0%, G: 0%,   T: 20%)
etc.

"""
def main():
  if len(sys.argv) < 3:
    help() 
  valueDict = {}
  resultDict = {}
  resultDict = countCharPositions(sys.argv[1],sys.argv[2])
  printOutput(resultDict)

def help():
  print "Please enter name of the input file followed by input chars file in current directory"
  exit(1)

def initializeValueDict(valueDict,charFileName):
  try:
    file = open(charFileName, "r")
  except IOError:
    print "Unable to open char input file"
    exit(1)
  for line in file:
    key = line.strip()
    valueDict[key] = 0

def countCharPositions(fileName,charFileName):
  try:
    file = open(fileName, "r")
  except IOError:
    print "Unable to open input file"
    exit(1)
  outputDict = {}
  for line in file:
    line = line.strip()
    i = 0
    for i in range(len(line)):
      key = str(i+1)
      if key != None and key in outputDict:
        tempValueDict = outputDict.get(key)
        count = int(tempValueDict[line[i]])
        count = count +1
        tempValueDict[line[i]] = count
        outputDict[key] = tempValueDict
      else:
        count = 0
        valueDict = {}
        initializeValueDict(valueDict,charFileName)
        count = int(valueDict.get(line[i]))
        count = count + 1
        valueDict[line[i]] = count
        outputDict[key] = valueDict
  return outputDict

def key_as_int(inp_key):
  try:
    return int(inp_key)
  except ValueError:
    print "Unable to convert input key to int"
    exit(1)
    

def printOutput(inputDict):
  for key in sorted(inputDict,key=key_as_int):
    outputValueDict = inputDict.get(key)
    totalCount = sum(outputValueDict.values())
    output = "("
    for k in sorted(outputValueDict.keys()):
      value = float((float(outputValueDict.get(k))/totalCount)*100)
      temp = '%s:%.2f' %(k,value)
      output = output + temp + '%'+ ", "
    output = output.strip(', ')
    output = output + ")"
    print "Position:", key, output 
      
if __name__=='__main__':
  main()


