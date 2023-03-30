import docker
import tempfile
import zipfile
import tarfile
import os
import shutil


client = docker.from_env()


def prepareFile(working_dir):
    filePath = input(
        "Enter the path of the file or directory to be analyzed: \n")

    if os.path.isdir(filePath):
        shutil.copytree(filePath, working_dir)
    # elif tarfile.is_tarfile(filePath):
    #     file = tarfile.open(filePath)
    #     file.extractall(working_dir)
    #     file.close()
    elif zipfile.is_zipfile(filePath):
        with zipfile.ZipFile(filePath, 'r') as zip_ref:
            zip_ref.extractall(working_dir)
            zip_ref.close()
    else:
        print("The file is not a zip or tar file")


def runPlasoAnalysis(client, working_dir):
    container = client.containers.run('log2timeline/plaso', 'log2timeline --storage-file /data/evidences.plaso /data/',
                                      volumes={working_dir: {'bind': '/data', 'mode': 'rw'}}, detach=True, remove=True)

    output = container.attach(stdout=True, stream=True, logs=True)

    for line in output:
        print(line)


def runPlasoExport(client, working_dir, outputDir):
    container = client.containers.run('log2timeline/plaso', 'psort -o l2tcsv -w /data/timeline.csv /data/evidences.plaso',
                                      volumes={working_dir: {'bind': '/data', 'mode': 'rw'}}, detach=True, remove=True)

    output = container.attach(stdout=True, stream=True, logs=True)

    for line in output:
        print(line)

    shutil.copyfile(working_dir + "/timeline.csv", outputDir + "/timeline.csv")


def savePlasoFile(working_dir):
    shutil.copyfile(working_dir + "/evidences.plaso",
                    outputDir + "/evidences.plaso")


working_dir = tempfile.mkdtemp()

print('created temporary directory', working_dir)

prepareFile(working_dir)

print("The file has been copied to the directory: " + working_dir)
print("Starting the analysis...")

runPlasoAnalysis(client, working_dir)

print("The analysis has been completed")

response = input(
    "Do you want to save the plaso file? (Press Y to continue or any other key to exit) \n")
if (response == 'Y'):
    outputDir = input(
        "Enter the path of the directory where you want to save the plaso file: \n")
    savePlasoFile(working_dir)


response = input(
    "Do you want to export the Super Timeline on csv? (Press Y to continue or any other key to exit) \n")
if (response == 'Y'):
    outputDir = input(
        "Enter the path of the directory where you want to save the csv file: \n")
    runPlasoExport(client, working_dir, outputDir)
else:
    print("Exiting the program")
    exit()
