# Created by Gaurav Shankar --github : <gauravsh02.github.io> -- emailid : <gauravshankar.bk@gmail.com>
# This is a Python script to arrange your video songs into directories according to Band name
# If the songs are in format BAND_NAME - SONG_NAME --- .mp4 OR .MKV
# Directories will be created according to BAND name and files will me moved accordingly
# Further changes will be made to provide more flexibility

import os, shutil
cpath = os.getcwd()

flist = os.listdir()
vlist = []
slist=[]

def mov(source, di):
    dsst = di+"/"+source
    shutil.move(source, dsst)

for i in flist:
    if(i[len(i)-3:]=="MKV" or i[len(i)-3:]=="mp4"):
        slist.append(i)
        if '&' in i:
            if i.index('-') < i.index('&') :
                pt = i.index('-')
                vlist.append(i[:pt-1])
            else:
                pt = i.index('&')
                vlist.append(i[:pt-1])
        else:
            pt = i.index('-')
            vlist.append(i[:pt-1])

vlist = set(vlist)

for di in vlist:
    if os.path.exists(di):
        for song in slist:
            if song.startswith(di):
                mov(song, di)
    else:
        os.makedirs(di)
        for song in slist:
            if song.startswith(di):
                mov(song, di)


print("Done")
