#randomInstances.py

import maya.cmds as cmds
import random

#the same seed for the same results
random.seed(1234)

result = cmds.ls(orderedSelection = True)

#transformName = name of the object
transformName = result[0]

#Create a group for the cubes
instanceGroupName = cmds.group( empty = True, name = transformName + '_group#')

#create 10 duplicates of myCube1 with instance(same shape in all). 
for i in range(1,50):
    
    #Duplicate for instance the transformName
    instanceResult = cmds.instance(transformName, name = transformName + '_instance#')
    
    cmds.parent(instanceResult,instanceGroupName )
    
    #Define the transform
    x = random.uniform(-10,10)
    y = random.uniform(0,20)
    z = random.uniform(-10, 10)
    
    cmds.move(x,y,z,instanceResult)
    
    xRot = random.uniform(0,360)
    yRot = random.uniform(0,360)
    zRot = random.uniform(0,360)
    cmds.rotate(xRot, yRot, zRot, instanceResult)
    
    scalingFactor = random.uniform(0.5, 1.5)
    cmds.scale(scalingFactor,scalingFactor,scalingFactor,instanceResult)

#Hide the initial cube in the scene. 
cmds.hide(transformName)

#Center de pivot of the group
cmds.xform(instanceGroupName, centerPivots = True)

    