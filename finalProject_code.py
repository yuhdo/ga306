import maya.cmds as mc
def Upgrade():
    mc.selectMode( co=True )
    Hard=mc.ls(sl=True) #gets selection
    mc.polySelectConstraint( m=3, t=0x8000, sm=1) #constraints hard edges and selects them
    mc.polyBevel3 (fraction=0.5, offsetAsFraction=1,depth=1,chamfer=0 ,segments=1,subdivideNgons=1 ,mergeVertices=1);
    mc.polySelectConstraint( sm=0 ) # turn off edge smoothness constraint
Upgrade()