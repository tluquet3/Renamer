# Renamer

Initially created to reindex my holidays pictures from multiple cameras,  Renamer can also insert characters at the start or end of files, reindex files by creation date, ... 

# Help

* usage: renamer.py [-h] [-re] [-a APPEND] [-i INSERT] [-l] [-rm] [-v] selector
                  selector
* positional arguments:
	selector              Files to select in the directory, type: string

* optional arguments:
  - -h, --help | show this help message and exit
  - -re, --reindex  |  Reindex all selected files by creation date from 0 to N, n the number of files. The number will be appended at the begining of the file
  - -a APPEND, --append APPEND  |  Append string at the end of the files
  - -i INSERT, --insert INSERT  | Insert String at the start of the file
  - -l, --list  |  List files of selection
  - -rm, --remove  |  Remove files
  - -v, --verbose | Activate verbose mode

# Examples 

`python renamer.py -a "-gopro" "./testfolder/*.mp4"`   
This command will append to all my .mp4 videos in the "testfolder" directory the suffix "-gopro"

`python renamer.py -re "./testfolder/*.jpg"`   
This command will re-index all my .jpg pictures in the "testfolder" directory by creation date. Index will be inserted at the start of the filename, example : my-awesome-picture.jpg will become 01_my-awesome-picture.jpg   


