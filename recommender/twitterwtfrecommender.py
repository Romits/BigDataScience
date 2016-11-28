#!/usr/bin/python -tt
import json
import sys
import numpy as np
import math
import pandas as pd
from collections import OrderedDict

class TwitterWTFRecommender:

    def __init__(self):
        self.indexLookup = {}
        self.accountLookup = {}
        self.reco_matrix = self.create_pairwise_matrix()

    def generateWTFReco(self,inputFile, aggFactor, outputFile):
    # Read single line from the file at a time

        fp = open(inputFile, "r")
        fout = open(outputFile, "w")
        support = self.find_support_value(aggFactor)
        for line in fp:
            data = json.loads(line)
            newData = OrderedDict()
            reco_dict = {}
            handle_dict = {}
            user_dict = {}
            currHandles = data['handles']
            # Call the recommender to get the output.
            recoList = self.get_wtf_recommendations(self.reco_matrix,currHandles,support)
            reco_dict['recommendations'] = recoList
            handle_dict['handles'] = currHandles
            currUser = data['userId']
            user_dict['userId'] = currUser
            newData.update(user_dict)
            newData.update(handle_dict)
            newData.update(reco_dict)
            json.dump(newData, fout)
            fout.write('\n')
        return 0

    def find_support_value(self,aggvFactor):
        aggFactor = float(aggvFactor)
        if aggFactor < 0.1:
            support = 90.0
        elif aggFactor >=0.1 and aggFactor <0.2:
            support = 80.0
        elif aggFactor >=0.2 and aggFactor <0.3:
            support = 70.0
        elif aggFactor >=0.3 and aggFactor <0.4:
            support = 60.0
        elif aggFactor >=0.4 and aggFactor <0.5:
            support = 50.0
        elif aggFactor >=0.5 and aggFactor <0.6:
            support = 40.0
        elif aggFactor >=0.6 and aggFactor <0.7:
            support = 30.0
        elif aggFactor >=0.7 and aggFactor <0.8:
            support = 20.0
        elif aggFactor >=0.8 and aggFactor <0.9:
            support = 10.0
        else:
            support = 1.0
        return support

    def scale_pairwise_matrix(self,pcount_matrix):
        #Need to take as input and modify accordingly
        newMax = 100.0
        pcount_matrix_scaled = (pcount_matrix/pcount_matrix.max())*newMax
        return pcount_matrix_scaled
    
    def create_lookup_tables(self,allAccountArray, countVal):
        indexLookup = {}
        accountLookup = {}
        for index in range(0,countVal):
            indexLookup[allAccountArray[index]] = index
            accountLookup[index] = allAccountArray[index]
        return (indexLookup,accountLookup)

    def create_pairwise_matrix(self):

        # Loading data from file
        twitterDataset = pd.read_table('../data/TwitterData.csv', delimiter=',', \
                                index_col=False, names=['pairCount', 'Account1','Account2'], header=None)

        account1Array = np.asarray(twitterDataset['Account1'])
        account2Array = np.asarray(twitterDataset['Account2'])
        allAccountArray = np.union1d(account1Array,account2Array)
        countVal = allAccountArray.size
        lookupTables = tuple()
        lookupTables = self.create_lookup_tables(allAccountArray, countVal)
        self.indexLookup = lookupTables[0]
        self.accountLookup = lookupTables[1]
        #Create a matrix with pairwise count for the accounts --two dimensional matrix...
        pcount_matrix = np.zeros(shape=((countVal),(countVal)), dtype=np.float64)
        pcount_matrix.shape
        for val,acc1,acc2 in twitterDataset.itertuples(index=False):
            rowVal = self.indexLookup[acc1]
            colVal = self.indexLookup[acc2]
            pcount_matrix[rowVal,colVal] = float(val)
        pcount_matrix_scaled = self.scale_pairwise_matrix(pcount_matrix)
        return pcount_matrix_scaled

    def get_wtf_recommendations(self,pcount_matrix_scaled,currHandles,support):
        newHandleList = []
        recoList = []
        outList = []
        sortedHandleList = []
        sortedNewHandleList = []
        countVal = pcount_matrix_scaled.shape[0]
        for handle in currHandles:
            if handle in self.indexLookup:
                rowIndex = self.indexLookup[handle]
                for idx in range(0,countVal):
                    checkVal = pcount_matrix_scaled[rowIndex,idx]
                    if checkVal >=support:
                        tuppleToAdd = (checkVal,self.accountLookup[idx])
                        newHandleList.append(tuppleToAdd)
            else:
                continue;
            sortedNewHandleList = sorted(newHandleList, key = lambda t: t[0], reverse=True)
        if sortedNewHandleList:
            for listIndex in range(0,len(sortedNewHandleList)):
                if (sortedNewHandleList[listIndex])[1] not in currHandles:
                    sortedHandleList.append(sortedNewHandleList[listIndex][1])
             
            for item in sortedHandleList:
                if item not in recoList:
                    recoList.append(item)
            if len(recoList) > 20:
                outList = recoList[:20]
            else:
                outList = recoList
        return outList
