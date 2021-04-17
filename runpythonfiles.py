import os
def runFiles():
    file_list = os.listdir("./samplePythonfiles")
    print(file_list)
    for file in file_list:
        os.system(f"python ./samplePythonfiles/{file}")
runFiles()