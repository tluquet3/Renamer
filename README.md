# Renamer

Initially created to reindex my holidays pictures from multiple cameras,  Renamer can also insert characters at the start or end of files, reindex files by creation date, ... 

## Help

* usage: renamer.py [-h] [-v] [-d] [-a APPEND] [-i INSERT] [-l] [-re] [-rm]
                  selector
* positional arguments:
	selector              Files to select in the directory, type: string

* optional arguments:
	- -h, --help | show this help message and exit
  - -v, --verbose | Activate verbose mode
  - -d, --debug  |  Activate debug mode
  - -a APPEND, --append APPEND  |  Append string at the end of the files
  - -i INSERT, --insert INSERT  | Insert String at the start of the file
  - -l, --list  |  List files of selection
  - -re, --reindex  |  Reindex all selected files by creation date from 0 to N, n the number of files. The number will be appended at the begining of the file
  - -rm, --remove  |  Remove files
