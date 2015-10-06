#aim.py. This script can be used when several objects have to look at their target. 

import maya.cmds as cmds

#Obtain the objects selected ordered. 
selectionObjects = cmds.ls(orderedSelection = True)

#If we selected more or equal two objects (one of the will be the target)
if len(selectionObjects) >= 2:
    #print 'Selection List %s' % (selectionObjects)
    
    #We obtain the aim where the other objects will be oriented
    TargetName = selectionObjects[0]
    selectionObjects.remove(TargetName)
    
    #The other objects will rotate in the axis Y when the target is moved
    for otherObject in selectionObjects:
        cmds.aimConstraint(TargetName, otherObject, aimVector=[0,1,0])
else:
    print 'You have to select more objects'




 

    
