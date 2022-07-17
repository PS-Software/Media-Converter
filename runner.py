import os

def file_conversion_task(input_path, output_directory, output_extension):
    #we will be using ffmpeg with the os module to convert the file
    
    filename_extensionless = os.path.splitext(input_path)[0]
    os.popen("ffmpeg -i " + input_path + " " + output_directory + "/"+ filename_extensionless + output_extension)
    return

def convert_Task(in_path, out_dir, in_name, out_ext):
    return file_conversion_task(in_path, out_dir, in_name, out_ext)