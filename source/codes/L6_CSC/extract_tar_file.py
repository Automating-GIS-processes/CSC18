# -*- coding: utf-8 -*-
"""
Download Tiff files.

Created on Sun Jan 14 10:44:51 2018

@author: Henrikki Tenkanen
"""
import os
import urllib

def get_filename(url):
    """
    Parses filename from given url
    """
    if url.find('/'):
        return url.rsplit('/', 1)[1]

# Filepaths
outdir = r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\Data\CSC_Lesson6"

# File locations
url_list = ["http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4133A.tif",
            "http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4133B.tif",
            "http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4133C.tif",
            "http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4133D.tif",
            "https://etsin.avointiede.fi/storage/f/paituli/ehdot/Latuviitta_ehdot.pdf",
            "https://etsin.avointiede.fi/storage/f/paituli/ehdot/MML_ehdot_CC.txt",            
            "https://github.com/Automating-GIS-processes/CSC18/raw/master/data/Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif"
            ]

# Create folder if it does no exist
if not os.path.exists(outdir):
    os.makedirs(outdir)

# Download files
for url in url_list:
    # Parse filename
    fname = get_filename(url)
    outfp = os.path.join(outdir, fname)
    # Download the file if it does not exist already
    if not os.path.exists(outfp):
        print("Downloading", fname)
        r = urllib.request.urlretrieve(url, outfp)
    