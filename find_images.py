import os, sqlite3, time
from PIL import Image, ImageStat, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

t1= time.time()

con = sqlite3.connect('imgs.db')
cur = con.cursor()

t2 = time.time()
print('connected to imgs.db' + str(t2-t1))


##image_folders_ = [
##    r'E:\fotoğraflar-iphone',
##    r'E:\iCloud',
##    r'E:\iphone-manuel-20210711'    
##    ]
##
##image_folders = []
##
##for i in image_folders_:
##    for j in os.listdir(i):
##        if os.path.isdir(os.path.join(i,j)):
##            image_folders.append(os.path.join(i,j))

##folders = [
##    r'D:\fotoğraflar-iphone',
##    r'D:\fotoğraflar-iphone\100APPLE',
##    r'D:\fotoğraflar-iphone\101APPLE',
##    r'D:\fotoğraflar-iphone\102APPLE',
##    r'D:\fotoğraflar-iphone\103APPLE',
##    r'D:\fotoğraflar-iphone\104APPLE',
##    r'D:\fotoğraflar-iphone\105APPLE',
##    r'D:\fotoğraflar-iphone\106APPLE',
##    r'D:\fotoğraflar-iphone\107APPLE',
##    r'D:\fotoğraflar-iphone\108APPLE',
##    r'D:\fotoğraflar-iphone\109APPLE',
##    r'D:\fotoğraflar-iphone\116APPLE',
##    r'D:\fotoğraflar-iphone\20171203',
##    r'D:\fotoğraflar-iphone\2019-03-13',
##    r'D:\fotoğraflar-iphone\2020-09-29',
##    r'D:\fotoğraflar-iphone\2020-10-04',
##    r'D:\fotoğraflar-iphone\2020-10-05',
##    r'D:\fotoğraflar-iphone\2020-10-06',
##    r'D:\fotoğraflar-iphone\2020-10-07',
##    r'D:\fotoğraflar-iphone\2020-10-08',
##    r'D:\fotoğraflar-iphone\2020-10-09',
##    r'D:\fotoğraflar-iphone\2020-10-10',
##    r'D:\fotoğraflar-iphone\2020-10-11',
##    r'D:\fotoğraflar-iphone\2020-10-12',
##    r'D:\fotoğraflar-iphone\2020-10-13',
##    r'D:\fotoğraflar-iphone\2020-10-14',
##    r'D:\fotoğraflar-iphone\2020-10-15',
##    r'D:\fotoğraflar-iphone\2020-10-16',
##    r'D:\fotoğraflar-iphone\2020-10-17',
##    r'D:\fotoğraflar-iphone\2020-10-18',
##    r'D:\fotoğraflar-iphone\2020-10-19',
##    r'D:\fotoğraflar-iphone\2020-10-20',
##    r'D:\fotoğraflar-iphone\2020-10-21',
##    r'D:\fotoğraflar-iphone\2020-10-23',
##    r'D:\fotoğraflar-iphone\Hepsi',
##    r'D:\fotoğraflar-iphone\Video Projeleri',
##    r'D:\fotoğraflar-iphone\20171203\2018-05-12',
##    r'D:\iCloud',
##    r'D:\iCloud\dub',
##    r'D:\iCloud\Hepsi',
##    r'D:\iphone-manuel-20210711',
##    r'D:\iphone-manuel-20210711\aynıisimli',
##    r'D:\iphone-manuel-20210711\aynıisimli2',
##    r'D:\iphone-manuel-20210711\heic'
##    
##    ]

folders = [r'd:\cleaned']
            
files = []

for folder in folders:
    files.append([(folder,file) for file in os.listdir(folder) if os.path.isfile(os.path.join(folder,file))])

for i in files:
    cur.executemany('insert into images3 values (?,?,\'xx\',0,0)', i)

t3 = time.time()
print('inserted to images3' + str(t3-t2))

con.commit()

t4 = time.time()
print('committed' + str(t4-t3))
