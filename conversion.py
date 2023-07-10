import os
import glob
import pydub
from timer import Timer


def convertWavToMp3():
    path = input("Enter the path: ")
    t = Timer()
    t.start()
    totalCount = 0
    failed_files = []
    all_wav_files = []
    # walk through path and store all child directories in subdirs
    subdirs = os.listdir(path)
    for dirs in subdirs:
        counter = 0
        # join path to directory name for absolute path
        dir_path = os.path.join(path, dirs)
        os.chdir(dir_path)
        #grab all .wav and .mp3 files and store them in the corresponding list
        wav_files = glob.glob("./*.wav")
        all_wav_files = glob.glob("./*.wav")
        mp3_files = glob.glob("./*.mp3")
        print(f"Conversion of .wav files in {dirs} has begun. Please wait for the process to finish.")
        # create mp3 file name check if that mp3 already exists in the directory and skip it if so, if not convert from .wav and export to directory
        for wav_file in wav_files:
            mp3_file = os.path.splitext(wav_file)[0] + ".mp3"
            if mp3_file in mp3_files:
                print("File already converted to mp3.")
                continue
            try:
                sound = pydub.AudioSegment.from_wav(wav_file)
                sound.export(mp3_file, format="mp3")
                os.remove(wav_file)
                counter += 1
                totalCount += 1
                print(f"{counter} files out of {len(wav_files)} converted in the {dirs} directory.")
            except:
                print(f"Error decoding file {wav_file}.")
                failed_files.append(wav_file.strip(".\\"))
    elapsed_time = t.stop()
    print(f"Conversion complete. {totalCount} files were converted in total.")
    try:
        print(f"Average time for each file conversion was {elapsed_time / totalCount:04f}.")
        print(f"The following files were unable to be converted {failed_files}")
        print(f"The following wav files were found {all_wav_files}")
    except:
        print("No files were converted as no .wav files were detected.")
        print(f"The following files were unable to be converted {failed_files}")
        print(f"The following wav files were found {all_wav_files}")
    return all_wav_files

def removeWavFiles(wav_files):
    answer = input(f"Would you like to delete the following files?: {wav_files}").lower()
    if answer == "y":
        try:
            for wav_file in wav_files:
                os.remove(wav_file)
                print(f"{wav_file} has been removed.")
        except:
            print(f"The following file was unable to be removed {wav_file}.")
    else:
        quit()
