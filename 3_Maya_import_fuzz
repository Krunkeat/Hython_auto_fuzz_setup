import maya.cmds as cmds
import ramses as ram
from mtoa.core import createStandIn


# Frank  /  Herve
chr = "Herve" 
if chr == "Frank" :
    cloths = ["CHEMISE", "PULL", "SOUS_PULL"]
    sg_chr = ["Hair_Shader_Fuzz_FRANK_FUZZ_HAIR_SHD"]
if chr == "Herve" :
    cloths = ["CHEMISE", "PULL", "MOUMOUTH"]
    sg_chr = ["Hair_Shader_Fuzz_HERVE_CLOTHS_FUZZ_HAIR_SHD","Hair_Shader_Fuzz_HERVE_LAINE_FUZZ_HAIR_SHD"]
if chr == "Mouton" :
    cloths = ["MOUMOUTH"]
    sg_chr = [""]

# get current file
current_file = cmds.file( q=True, sn=True )
filename = os.path.basename(current_file)

step = ram.RamStep.fromPath( current_file )
step = step.getShortName(step)

if not cmds.objExists(chr.upper()+"_FUZZ"):
    cmds.group(em=True,n=chr.upper()+"_FUZZ")

for cloth in cloths:
    # Duplicate a standin
    standin = createStandIn().replace("Shape","")
    
    
    cmds.setAttr(f"{standin}.scale", 0.01, 0.01, 0.01)
    cmds.setAttr(f"{standin}.rotate", 0, 0, 0)
    cmds.setAttr(f"{standin}.translate", 0, 0, 0)

    # Get path
    new_file = current_file.replace(filename, f"_published/Fuzz_{chr}/{cloth}_0001.ass")
    new_file = new_file.replace(str(step), "VFX")
    cmds.setAttr(f"{standin}.dso", new_file, type='string')  
    
    cmds.setAttr(f"{standin}.useFrameExtension", 1)
    
    cmds.parent(standin, chr.upper()+"_FUZZ")
    cmds.rename(standin, f"{cloth}_Fuzz")


# Recent Adition to del if error
def getSGfromShader(shader=None):
    if shader:
        if cmds.objExists(shader):
            sgq = cmds.listConnections(shader, d=True, et=True, t='shadingEngine')
            if sgq:
                return sgq[0]

    return None

def assignObjectListToShader(objList=None, shader=None):
    """
    Assign the shader to the object list
    arguments:
        objList: list of objects or faces
    """
    # assign selection to the shader
    shaderSG = getSGfromShader(shader)
    if objList:
        if shaderSG:
            cmds.sets(objList, e=True, forceElement=shaderSG)
            print(f"Shader Assigned {shader}")
        else:
            print('The provided shader didn\'t returned a shaderSG')
    else:
        print('Please select one or more objects')

def assignSelectionToShader(shader=None):
    sel = cmds.ls(sl=True, l=True)
    if sel:
        assignObjectListToShader(sel, shader)

imp= True


for sg in sg_chr:
    if cmds.objExists(sg):
        imp = False
        print("sg: " + sg + "  already in the scene skiped import for now import it by hand")

if imp:
    cmds.file("S:/SIC3D/SIC5/Projects/moutons/02-PROD/moutons_G_VFX/Hair_Shader_Fuzz.mb", i=True ,type="mayaBinary" ,ra=True ,rdn=True ,mergeNamespacesOnClash=False ,rpr="Hair_Shader_Fuzz" ,options="v=0;" )
    for nb in range(3):
        cmds.delete(f"Hair_Shader_Fuzz_pSphere{nb+1}")
# Connect Fuzz
if chr == "Frank" :
    for cloth in cloths:
        assignObjectListToShader(f"{cloth}_Fuzz",sg_chr[0])

if chr == "Herve" :
    assignObjectListToShader("CHEMISE_Fuzz",sg_chr[0])
    assignObjectListToShader("PULL_Fuzz",sg_chr[0])
    assignObjectListToShader("MOUMOUTH_Fuzz",sg_chr[1])


        
        
        
        
        
        
    
