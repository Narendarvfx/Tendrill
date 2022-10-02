import nuke
import os
import sys
import posixpath
import glob

project = sys.argv[1]
# print (project)
shot_dir = sys.argv[2]
shot_name = sys.argv[3]
input = sys.argv[4]
denoise = sys.argv[5]
first_frame = sys.argv[6]
last_frame = sys.argv[7]
final_out = sys.argv[8]

# def build_shot(project,shot_dir,shot_name,input, denoise, first_frame, last_frame,final_out):
file_path = posixpath.join(shot_dir, shot_name)

if not os.path.exists(shot_dir):
    try:
        os.makedirs(shot_dir)
    except Exception as e:
        print(e)
        # return

    templatefile = r"P:\Tendrill\templates\{}.nk".format(project)
    nuke.scriptOpen(templatefile)
    nuke.root().knob("first_frame").setValue(int(first_frame))
    nuke.root().knob("last_frame").setValue(int(last_frame))

    # Adjusting mov read node knobs
    input_file= glob.glob('{}/*.exr'.format(input))
    # print("###",input_file)

    #set input
    if input_file:
        input_final = input_file[0].replace('\\', '/')
        print(">>>>", input_final)
        n = nuke.toNode("input")
        n["file"].setValue(input_final)
        n["frame_mode"].setValue("start at")
        n["frame"].setValue(first_frame)
        n["last"].setValue(int(last_frame))
    else:
        print (f'unable to find the plate sequence in the given path \n {input} ')

    # set input
    denoise_file = glob.glob('{}/*.exr'.format(denoise))
    if denoise_file:
        denoise_n = nuke.toNode("denoise_input")
        denoise_input_final = input_file[0].replace('\\', '/')
        denoise_n["file"].setValue(denoise_input_final)

        denoise_n["frame_mode"].setValue("start at")
        denoise_n["frame"].setValue(first_frame)
        denoise_n["last"].setValue(int(last_frame))
    else:
        print (f'unable to find the denoise sequence in the given path \n {denoise} ')

    # resolution = str(width + " " + height + " " + "ingestionResolution")
    # nuke.addFormat(resolution)
    # n["format"].setValue("ingestionResolution")

    # Adjusting mov write node knobs
    n = nuke.toNode("Write1")
    n["channels"].setValue("rgba")
    output_file = os.path.splitext("{}/{}".format(final_out, shot_name))[0]+".%04d.exr"
    print(output_file)
    n["file"].setValue(output_file)


    try:
        nuke.scriptSave("{}/{}".format(shot_dir, shot_name))
        nuke.scriptClose(templatefile)

    except:
        print("\n-------------------------------------------\n")
        print("Unable to save nuke script from first chunk")
        print("\n-------------------------------------------\n")

else:
    print ("shot build was already created")


