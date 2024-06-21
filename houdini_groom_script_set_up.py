#
#
#

from optparse import OptionParser
import os
import hou
import subprocess
from datetime import datetime

def do_the_thing(new_hip, frame_start, frame_end, cam_path, mouton):
    # update the path of the ABC file
    import hou
    import ramses as ram
    import os

    #if mouton != None :


    hou.parm("obj/Import/alembic_CHR//reload").pressButton()

    # Set cam
    hou.parm("obj/Cam_esta//objectPath").set(cam_path)
    hou.parm("obj/Cam_esta//buildHierarchy").pressButton()

    current_file = hou.hipFile.name()
    dir = "/".join(current_file.split("/")[0:-1])
    abc_dir = dir + "/abc"

    #No cam mask
    #hou.parm("obj/GROOM/SPR_cameraRayMask3//camera_path").set("/obj/Cam_esta"+cam_path.replace(":", "_"))

    # check if a set.abc exist
    for abc in os.listdir(abc_dir):
        if "set" in abc:
            hou.parm("obj/Import/switch_set//input").set(0)
            hou.parm("obj/Import/alembic_SET//reload").pressButton()
        else:
            hou.parm("obj/Import/switch_set//input").set(1)

    # Set Path to render
    myShot = ram.RamShot.fromPath(current_file)

    shotname = myShot.getShortName(myShot)
    pathNode = hou.node("obj/ropnet5/path_to_current_shot")
    pathNode.parm("Seq_N_Shot").set(shotname)
    hou.playbar.setFrameRange(int(frame_start.split(".")[0]), int(frame_end.split(".")[0]))
    # render .ASS cache
    hou.parm("obj/ropnet5/arnold3_PULL//execute").pressButton()

    print("All done Fuzz " + shotname)

    shot = new_hip.split("/")[-1].split("_")[-2]
    current_time = datetime.now()
    print(f"Fuzz {shot} finished at {current_time}")

    # Dummy file to say it's done
    # To do : check file date and compare it to ass export
    path = "/".join(new_hip.split("/")[0:-1])
    if not os.path.exists(path + "/Fuzz_Done.txt"):
        os.mkdir(path + "/Fuzz_Done.txt")

if __name__ == "__main__":
    # this gets run when called via the commandline
    # parse commandline arguments here and pass to the main function
    parser = OptionParser()
    parser.add_option("-i", "--hip", dest="hipfile", help="path to .hip file")
    parser.add_option("-n", "--newfile", dest="newfile", help="path to save the new .hip file")
    parser.add_option("-p", "--path", dest="path", help="dir path to save the new .hip file")
    parser.add_option("-s", "--start", dest="start", help="start frame")
    parser.add_option("-e", "--end", dest="end", help="end frame")
    parser.add_option("-c", "--cam", dest="cam", help="cam path")
    (options, args) = parser.parse_args()

    # load the scene
    current_hip = options.hipfile
    new_hip = options.newfile
    path = options.path
    hou.hipFile.load(current_hip)

    print(options.mouton)
    # now do the thing with the scene
    hou.hipFile.save(new_hip)
    do_the_thing(new_hip, options.start, options.end, options.cam)
    hou.hipFile.save(new_hip)

    # now open the scene
    # env Problems  houdini doesn't fin path to side_fx_paint module and others maybe
    #os.system("\"C:\\Program Files\\Side Effects Software\\Houdini 19.5.682\\bin\\houdinifx.exe\" {}".format(new_hip))

    # now open the scene path in folder explorer
    path = path.replace("/","\\")
    subprocess.Popen(r'explorer /select,{}'.format(path))

