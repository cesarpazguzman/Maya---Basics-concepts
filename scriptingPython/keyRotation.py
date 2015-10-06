#keyRotation.py. This script can be used when I want rotate a object like an animation. 
import maya.cmds as cmds

#p in the parameters. Functions for define the keys
def keyFullRotation(pObjectName, pStartTime, pEndTime, pTargetAttribute):
    #The keys are deleted
    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    #Define new keys for the animations (rotation in the axis Y). 
    cmds.setKeyframe(pObjectName, time= pStartTime, attribute=pTargetAttribute, value = 0)
    
    cmds.setKeyframe(pObjectName,time=pEndTime, attribute=pTargetAttribute, value = 360)

    #In order to mantain a constant rate of rotation with linear tangents
    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)
    cmds.keyTangent( inTangentType='linear', outTangentType='linear')
    
    
    
selectionObjects = cmds.ls( selection = True, type='transform')

if len(selectionObjects) >= 1:
    #print 'Selected items: %s' % (selectionObjects)
    
    #query = true for indicate that the frames used in the interface. 
    #start in 0 seconds and in the first frame
    startTime = cmds.playbackOptions( query = True, minTime = True)
    #end in 48 seconds and in the last frame (24)
    endTime = cmds.playbackOptions( query = True, maxTime = True)
    
    for objectName in selectionObjects:
        
        #Obtain the type of the object selected
        #objectTypeResult = cmds.objectType(objectName)
        
        #print '%s type: %s' % (objectName, objectTypeResult)  
        keyFullRotation(objectName, startTime, endTime, 'rotateY')
        
else:
    print 'Select at least one object'
