#keyRotationWithGui.py. I learned to create an interface. It could be used for generating a simple animation.

import maya.cmds as cmds
import functools


#name of window, and a callback function 
def createUI( pWindowTitle, pApplyCallback):
    
    #each window have a id unique for sure one instance at a time
    windowID= 'myWindowID'
    
    #Checked if in Maya there is another window with this ID. 
    if cmds.window( windowID, exists=True):
        cmds.deleteUI(windowID)
      
    #Create the new window
    cmds.window(windowID, title=pWindowTitle, sizeable=False, resizeToFitChildren=True)
    
    #To determine how the interface elements will be colocated in the window. 75, 60, 60 are the pixels
    cmds.rowColumnLayout(numberOfColumns = 3, columnWidth=[ (1,75), (2,60), (3,60)], columnOffset=[(1,'right',3)])
    
    #Now we have to add the fields and buttons. When an interface element is created, it's placed 
    #in the next available position in the current layout. 
    cmds.text( label='Time Range:' )
    
    #We put a int in the next fields
    startTimeField = cmds.intField(value = cmds.playbackOptions( q = True, minTime = True))
    endTimeField = cmds.intField(value = cmds.playbackOptions( q = True, maxTime= True))
    
    cmds.text(label='Attribute:' )
    
    #We put a string in the next field
    targetAttributeField = cmds.textField(text='rotateY')
    
    cmds.separator( h = 10, style = 'none')
    cmds.separator( h = 10, style = 'none')
    cmds.separator( h = 10, style = 'none')
    cmds.separator( h = 10, style = 'none')
    
    #To align the buttons
    cmds.separator( h = 10, style = 'none')
    
    #Create the first button. When this button is pressed, the callback function will be called.
    cmds.button(label = 'Apply', command=functools.partial( pApplyCallback,
                                                    startTimeField,
                                                    endTimeField,
                                                    targetAttributeField)) 
                                                    #pApplyCallback(startTimeField,endTimeField,targetAttributeField)
    
    #Create the function, which takes an unspecifed number of arguments
    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists=True):
            cmds.deleteUI(windowID)
            
            
    #create the cancel button
    cmds.button(label='Cancel', command=cancelCallback)
    
    #To display de window
    cmds.showWindow()

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
    
#Callback function with an unspecified number of arguments
def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, *pArgs):
    
    startTime = cmds.intField(pStartTimeField, query = True, value = True)
    
    endTime = cmds.intField( pEndTimeField, query=True, value=True)
    
    targetAttribute = cmds.textField( pTargetAttributeField, query=True, text=True)
    
    print 'Start Time: %s' % (startTime)
    print 'End Time: %s' % (endTime)
    print 'Attribute: %s' % (targetAttribute)

    #Obtaing all objects selected and filter with the type transform. 
    selectionList = cmds.ls(selection=True, type='transform')
    
    for objectSelected in selectionList:
        keyFullRotation(objectSelected, startTime, endTime, targetAttribute)
        
createUI('My Title',applyCallback)
    
