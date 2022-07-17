import os

def fileConversionTask(input_path, output_directory, input_extension, output_extension):
    #we will be using ffmpeg with the os module to convert the file
    os.popen("ffmpeg -i " + input_path + input_extension + output_directory + output_extension)
    return

def convertTask(in_path, out_dir, in_ext, out_ext):
    return fileConversionTask(in_path, out_dir, in_ext, out_ext)