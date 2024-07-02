# Zip-Instrument-Data

An imporved version of this CLI application can be found [here](https://github.com/Jack-Coutts/rust_zipper_CLI) and this newer version should be used by members of the proteomics STP.

This repository contains a python script that can be used to zip (compress) all subdirectories within a given directory. The script now gives the option to individually zip all the files in the directory as well. 

## How to download the script

If you are a member of the Proteomics STP using the VM, you DO NOT need to download the script. It is already on the VM and you can skip to the instructions below.

You can download this README file, the License and the Python script [here](https://github.com/Jack-Coutts/Zip-Instrument-Data/archive/refs/tags/v2.0.0.zip). This
will download a zipped folder containing the three files mentioned above but the only that you will need is the Python script 
[zipping_instrument_raw_data.py](https://github.com/Jack-Coutts/Zip-Instrument-Data/blob/main/zipping_instrument_raw_data.py). 

## How to run the script - Proteomics STP user

You can run this script from the Proteomics STP virtual machine (VM) assuming you have your data stored on drive E under your name. NOTE: The version of this script on the proteomics VM does not give the option to zip files. Assuming this is the case, follow the instructions below:

1. Open the command prompt application.
2. Copy the following command and press enter: `python E:\Jack\zipping_instrument_raw_data.py`
3. The command prompt will then show the following message: `Please enter directory path:`. Here you must type in the file path to the data you would like zipped. 
Assuming the data is in Jack's folder on drive E in a folder called `example_data`, the file path would be `E:\Jack\example_data`. Enter the file path and press enter. The program will then begin to run.  

## How to run the script - General

*For this script to run, you must first ensure you have python installed on your machine. It can be downloaded [here](https://www.python.org/downloads/).*

To run this script you should move the `zipping_instrument_raw_data.py` file to a location on you machine where you can access it easily E.g. `Users -> Name -> Documents -> Zipping`.
In this case the file path would be `Users/Name/Documents/Zipping/zipping_instrument_raw_data.py` and will be used as the example below. 

NOTE: On windows computers, backslashes are used instead of forward slashes so the file path might look more like this: `C:\Users\Name\Documents\Zipping\zipping_instrument_raw_data.py`

To run the file you need to know the file path of your target directory and the fle path of the `zipping_instrument_raw_data.py` file.

Here we will use `Users/Name/Documents/data/instrument` as the example target directory, meaning all directories within the instrument folder will be zipped and the option for the files withing this directory to be zipped will be presented.

1. Open the command prompt (Windows) or Terminal (Mac).
2. Type the following command and press enter to run the script:<br/>`python Users/Name/Documents/Zipping/zipping_instrument_raw_data.py`. If you are a mac user you may need to use `python3` rather than `python`.
3. In the command prompt/terminal you will then be asked for the file path of your target directory. For our example you would type `Users/Name/Documents/data/instrument` and press enter.
4. You will be asked if you want files in the given directory to be zipped, answer with yes or no.
5. The script will then run and in the terminal you will see the progress of the script as it zips each file/directory.
6. When the compression is complete, the command prompt/terminal will display the message `Zipping complete.`.


