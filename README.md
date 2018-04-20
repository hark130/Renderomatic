# RENDEROMATIC

## NAME

	print_PID_libraries.exe - list files loaded into memory by a PID

## SYNOPSIS

	renderomatic.py [-h] -f LIST_OF_FILES -s LIST_OF_SIZES -m LIST_OF_MOLDS

## DESCRIPTION

TBD

NOTE: No spaces are permitted in any of the argument lists.  ```... -f art123, more_art ...``` will cause an error.

## DOWNLOAD

1. Download and install a git client
	* [Linux/Unix](https://git-scm.com/download/linux)
	* [Mac OS X](https://git-scm.com/download/mac)
	* [Windows](https://git-scm.com/download/win)
2. ```git clone https://github.com/hark130/Renderomatic.git```
3. ```cd Renderomatic```
4. Copy renderomatic.py to wherever you process combinations of Adobe input

## EXAMPLE

```$ python renderomatic.py -h```

	usage: renderomatic.py [-h] -f FILE -s SIZES -m MOLDS

	optional arguments:
	  -h, --help            show this help message and exit
	  -f FILE, --file FILE  Input art file
	  -s SIZES, --sizes SIZES
	                        List of sizes to render in
	  -m MOLDS, --molds MOLDS
	                        List of mouldings to render in

```$ python renderomatic.py -f art123,more_art -s 10x10,20x20,30x30 -m brown,black,white```


