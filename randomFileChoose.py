'''
Created on 21 Feb 2017

@author: dghosh
'''
import os,random
from shutil import copyfile
import pathCollections as pc
targetDir = pc.pdbDir
randomSelDir = pc.randomSelDir
pc.createFolder(randomSelDir)
if __name__ == "__main__":
    filenames = random.sample(os.listdir(targetDir), 2500)    
    for fname in filenames:
        #srcpath = os.path.join(randomSelDir, fname)
        copyfile(targetDir+fname, randomSelDir+fname)
        print fname