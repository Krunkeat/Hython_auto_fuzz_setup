## Update loaded asset to lastest  between dependent job
# 
#    Select the Character you want the fuzz On (the GEO grpwould be best)
#

import sys, os
import ramses as ram
import maya.cmds as cmds

# Constant
hython = '"C:\\Program Files\\Side Effects Software\\Houdini 19.5.682\\bin\\hython.exe"'
script = r"D:\Hython_script.py"
hip = r"S:\SIC3D\SIC5\Projects\moutons\02-PROD\moutons_G_VFX\TEMPLATE_groom_{}.hipnc".format(name) # hipFile


current_file = cmds.file(q=True, sn=True)
myRamses = ram.Ramses.instance()
currentItem = ram.RamItem.fromPath( current_file )
currentStep = ram.RamStep.fromPath( current_file )

export_cam = True
export_CHR = True

if currentItem.itemType() == "S":
    
    CHR = cmds.ls(sl=True, l=True)[0]
    if "MOUTON" in CHR:
        name = "Mouton"
    if "FRANK" in CHR:
        name = "Frank"
    if "HERVE" in CHR:
        name = "Herve"
        
    # Construct New_file
    short_name = currentStep.getShortName( currentStep )
    
    filepath = os.path.dirname(current_file)
    path = filepath.replace("_{}".format(short_name), "_VFX")
    newfile = path + "/" + cmds.file(q=True, sn=True, shn=True).split(".")[0] + f"_{name}_FUZZ" + ".hip"
    
    start = cmds.playbackOptions(q=True, min=True)
    end = cmds.playbackOptions(q=True, max=True)
    

    if not os.path.isdir(path):
        os.mkdir(path)
    
    # Export Abc file
    # Cam abc
    if export_cam:
        abc_dir = path + "/abc"
        if not os.path.isdir(abc_dir):
            os.mkdir(abc_dir)
        
        
        cameras = cmds.ls(type=('camera'), l=True)
        root = [cam for cam in cameras if "camera" in cam][0]
        root = "|".join(root.split("|")[0:-1])
        save_name = path + "\\abc\cam.abc"
    
        command = "-frameRange " + str(start) + " " + str(end) +" -uvWrite -worldSpace -dataFormat ogawa " + "-root " + root + " -file " + save_name
        cmds.AbcExport ( j = command )
        
        

    if export_CHR:
        # CHR abc
        save_name = "{}\\abc\{}.abc".format(path,name)

        command = "-frameRange " + str(start) + " " + str(end) +" -uvWrite -worldSpace -dataFormat ogawa " + "-root " + CHR + " -file " + save_name
        cmds.AbcExport ( j = command )

    
    # Command build up
    cameras = cmds.ls(type=('camera'), l=True)
    root = [cam for cam in cameras if "camera" in cam][0]
    path_cam = "/" + "/".join(root.split("|")[-2:])
    hython_cmd = "{hython} {script} -i {hipfile} -n {newfile} -p {path} -s {start} -e {end} -c {path_cam}".format(hython= hython, script= script, hipfile= hip, newfile= newfile, path= path, end= end, start= start, path_cam= path_cam)
    print(hython_cmd)
    import csv

    # open the file in the write mode
    with open( path + f'/{name}_csv_file.csv', 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
    
        # write a row to the csv file
        writer.writerow([hython_cmd])
    
