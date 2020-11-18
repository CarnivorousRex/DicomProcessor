import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os, glob, stat
import pydicom
import pydicom.filewriter as fw
import pylab as pl
import sys
import matplotlib.path as mplPath
from tkinter import *
from tkinter import ttk
matplotlib.use("TkAgg")

from traverse import *
from dicomviewer import *
from getdatasets import *
from elementdicts import *
from tkinterform import *
from changesortsave import *
# data from: https://www.dicomlibrary.com/?manage=1b9baeb16d2aeba13bed71045df1bc65
# pydicom man pages: https://pydicom.github.io/pydicom/stable/index.html

# fpath = "/Users/sarahfochs/Desktop/DicomImages/"
fpath = "/Users/davidnascene/code/pythonDICOM/DICOM/knee"

# datadirs is a list of directories with DICOM data
datadirs = traverse(fpath)

# plots used to store dicom pixel data
plots = []

# datasets is a list of pydicom dictionaries
datasets, plots = getdatasets(datadirs, plots)

# elements and private_elem are dictionaries of the DICOM pre-edit
elements, private_elem = elementdicts(datasets)

# matplotlib viewer
dicomviewer(plots)

# final_elements is a dictionary of the DICOM post-edit
final = tkinterform(elements)

alterations = {}

print("Edited Dicom Elements")
print ("{:<40} {:<40}".format('KEY', 'VALUE'))
for key, val in (set(final.items())).difference(set(elements.items())):
    alterations[key] = val
    print ("{:<40} {:<40}".format(key, val[0:64]))
print ("{:<40} {:<40}".format('----------------', '----------------'))

changesortsave(datadirs, alterations)
