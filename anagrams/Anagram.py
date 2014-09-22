#!/usr/bin/python -tt
import sys

input = ['cat','dog','rats','moon','god','star','tsar']

def main():
  outputDict ={}
  outputDict = findAnagrams(input)
  printResult(outputDict)
  
def findAnagrams(inputList):
  resultDict = {}
  for i in range(len(inputList)):
    key = str(sorted(inputList[i]))
    if key in resultDict:
      value = resultDict.get(key)
      value.append(inputList[i])
      resultDict[key] = value
    else:
      myList = list()
      myList.append(inputList[i])
      resultDict[key] = myList
    
  return resultDict
      
      
def printResult(outputDict):
  for key in outputDict.keys():
    currValueList = outputDict.get(key)
    if len(currValueList) > 1:
      print currValueList[:]
  
  
if __name__=='__main__':
  main()
