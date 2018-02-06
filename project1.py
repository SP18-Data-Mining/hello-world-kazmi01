import csv
import sys
import math
terms = []
dataObjectCount = 0
testData = []
trainingData = []
with open('fruit_data_with_colors.txt','r') as tsv:

	for line in tsv : 
		if dataObjectCount % 5 == 0 :
			# Ignoring the first row - containing header info
			if dataObjectCount != 0 :
				testData.append(line.strip().split('\t'))
		else :
			trainingData.append(line.strip().split('\t'))
		dataObjectCount = dataObjectCount + 1

#print("Test Data " + str(testData))
#print("\n\n\n\n")
#print("Training Data " + str(trainingData))


# We have two datasets, training dataset - training data
# And we have the test dataset - testData
# each line -  ['element', "element'.... n ]

#trainingFeatures [ [ width, height], [width,height] ..]
trainingFeatures = []
testFeatures = []
trainingLabels = []
for line in trainingData :
	dataObject = []
	dataObject.append(float(line[5]))
	dataObject.append(float(line[6]))
	trainingLabels.append(line[0]) 
	trainingFeatures.append(dataObject)
for line in testData:
     dataObject=[]
     dataObject.append(float(line[5]))
     dataObject.append(float(line[6]))
     testFeatures.append(dataObject)
mindistance=10000


for i,testdataitem in enumerate(testData):
    
    for j,tdataitem in enumerate(trainingData):
          
            distance=math.sqrt(sum([(a-b)**2 for a,b in zip(testFeatures[i],trainingFeatures[j])]))
            if(distance < mindistance):
                  mindistance=distance
                  neighbor=j
                  print "distance=",distance
                  print("label index=",trainingLabels[neighbor])
                  print("test data=",(testdataitem))
                  print("nearest neighbor=",(j,tdataitem))
                  print("\n\n\n\n")
                      
                  
                  
                  
                    
                  

                  
             
                     
                      
                                               
                                   
                                                 
                              
                        
                             
                        
                

                     
                    
                     
                
                
                         
 
             
               
              
             
                    



# For each test data object find the nearest neighbor 
# Have some structure that contains the neighrest training data neighbor for each test data object


# Get the label index for the nearest neighbor training data
# So the nearest training data label is the prediction for the test dataObject

# So the assignment is output the predication label

