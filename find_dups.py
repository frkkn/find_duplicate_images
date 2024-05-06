import os, sqlite3, time
from PIL import Image, ImageStat, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

t1= time.time()

con = sqlite3.connect('imgs.db')
cur = con.cursor()

cur.execute('''
    select *
      from images 
     where (mean1,mean2,mean3) in ( 
            select mean1,mean2,mean3 
              from images
             where mean1 > 0 or
                   mean2 > 0 or
                   mean3 > 0
             group by mean1,mean2,mean3 
            having count(*) >1 )
    ''');

mean1,mean2,mean3,temp = -1,-1,-1,0

for i in cur.fetchall():
    mean1_onc = mean1
    mean2_onc = mean2
    mean3_onc = mean3
    
    path = i[0]
    filename = i[1]
    mean1 = i[2]
    mean2 = i[3]
    mean3 = i[4]

    if mean1 != mean1_onc and \
       mean1 != mean1_onc and \
       mean1 != mean1_onc and \
       temp > 0:
           print('')
           
    print(path + ' ' + filename + ' ' + str(mean1) + ',' + str(mean1) + ',' + str(mean3) )
    
    temp += 1
    

