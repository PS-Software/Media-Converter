import os

def fileConversionTask(inputPath, outputDirectory, inputExtension, outputExtension):
    #we will be using ffmpeg with the os module to convert the file
    os.popen("ffmpeg -i " + inputPath + inputExtension + outputDirectory + outputExtension)
    return

def convertTask(inPath, outDir, inExt, outExt):
    return fileConversionTask(inPath, outDir, inExt, outExt)