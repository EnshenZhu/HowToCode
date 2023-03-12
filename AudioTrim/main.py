import os.path

from pydub import AudioSegment
from os import listdir
from os.path import isfile, join


def get_files(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles


def Segmentation(inputFilePath, outputFilePath):
    # importing file from location by giving its path
    sound = AudioSegment.from_mp3(inputFilePath)

    # Selecting Portion we want to cut
    StrtMin = 0
    StrtSec = 8
    EndMin = 0
    EndSec = 22

    # Time to milliseconds conversion
    StrtTime = StrtMin * 60 * 1000 + StrtSec * 1000
    EndTime = EndMin * 60 * 1000 + EndSec * 1000

    # Opening file and extracting portion of it
    extract = sound[StrtTime:EndTime]

    # Saving file in required location
    extract.export(outputFilePath, format="mp3")


if __name__ == "__main__":
    inputFolderPath = r"./input_folder"
    inputMusicList=[]
    print(get_files(inputFolderPath))
