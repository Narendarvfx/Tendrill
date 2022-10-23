import nuke
import os
import sys
import posixpath
import glob

project = sys.argv[1]
shot_dir = sys.argv[2]
shot_name = sys.argv[3]
input = sys.argv[4]
denoise = sys.argv[5]
first_frame = sys.argv[6]
last_frame = sys.argv[7]
final_out = sys.argv[8]

# def build_shot(project,shot_dir,shot_name,input, denoise, first_frame, last_frame,final_out):
paint_shot_dir = shot_dir + '/scripts/nuke/'
print(paint_shot_dir)
file_path = posixpath.join(paint_shot_dir, shot_name)

if not os.path.exists(paint_shot_dir):
    default_folder_structure = r'P:\Tendrill\folder_structure\{}'.format('paint')
    base_dir = shot_dir
    cmd = f"robocopy /e  {default_folder_structure} {base_dir} /MIR"

    try:
        os.system(cmd)
        folders_to_remove = ['annotations', 'feedback', 'final_renders']
        for i in folders_to_remove:
            os.rmdir(os.path.join(base_dir, i))
        print("Folder structure Created {}".format(base_dir))
    except Exception as e:
        print(e)
        print("Failed to create folder structure")

    templatefile = r"P:\Tendrill\templates\{}.nk".format(project)

    if templatefile:

        nuke.scriptOpen(templatefile)
        nuke.root().knob("first_frame").setValue(int(first_frame))
        nuke.root().knob("last_frame").setValue(int(last_frame))

        # Adjusting mov read node knobs
        input_file= glob.glob('{}/*.exr'.format(input))


        #set input
        if input_file:
            input_final = input_file[0].replace('\\', '/')

            n = nuke.toNode("input")
            n["file"].setValue(input_final)
            n["frame_mode"].setValue("start at")
            n["frame"].setValue(first_frame)
            n["last"].setValue(int(last_frame))
        else:
            print (f'unable to find the plate sequence in the given path \n {input} ')

        # set input
        denoise_file = glob.glob('{}/*.exr'.format(denoise))
        print (">>>>",denoise_file)
        if denoise_file:
            denoise_n = nuke.toNode("denoise_input")
            denoise_input_final = input_file[0].replace('\\', '/')
            denoise_n["file"].setValue(denoise_input_final)

            denoise_n["frame_mode"].setValue("start at")
            denoise_n["frame"].setValue(first_frame)
            denoise_n["last"].setValue(int(last_frame))
        else:
            print (f'unable to find the denoise sequence in the given path \n {denoise} ')


        # Adjusting mov write node knobs
        n = nuke.toNode("Write1")
        n["channels"].setValue("rgba")
        output_file = os.path.splitext("{}/{}".format(final_out, shot_name))[0]+".%04d.exr"
        print(output_file)
        n["file"].setValue(output_file)



        print("?>>",os.path.join(paint_shot_dir, shot_name))
        nuke.scriptSave("{}/{}".format(paint_shot_dir, shot_name))
        nuke.scriptClose(templatefile)

    else:
        print ('Unable to find the template')

else:
    print ("shot build was already created")


