'''
Created on 23 Feb 2017
@author: dghosh
'''

def getRmsdAvg(filename):
    cmd.load(filename)
    rmsdarray = cmd.intra_rms_cur(filename[:-6], 1)
    rmsdAvg = (sum(rmsdarray) + 1.0) / len(rmsdarray)
    #cmd.delete(filename[:-6])
    return rmsdAvg
# import __main__
# __main__.pymol_argv = [ 'pymol', '-qc']
import os
import pymol
import random
from pymol import cmd
from dockingPipeline import pathCollections as pc
targetDir = pc.vinaOutputDir
os.chdir(targetDir)
pymol.finish_launching()
#for filename in os.listdir("."):
filenames = random.sample(os.listdir("."), 100)
for filename in filenames:
#filename = "14718841.ouput.pdbqt"
    rmsdAvg = getRmsdAvg(filename)
    print rmsdAvg