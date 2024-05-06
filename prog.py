import os, sqlite3, time
from PIL import Image, ImageStat, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

t1= time.time()

con = sqlite3.connect('imgs.db')
cur = con.cursor()

print('calculating means...')

i = 0
while True:
    i += 1
    
    cur.execute('select path,filename from images where processed = 0 limit 1000')
    result = cur.fetchall()

    print(str(i) + ' ' + str(len(result)))
    if len(result) == 0:
        break

    for res in result:
        cur.execute('update images set processed = 1 where path = ? and filename = ?'
                        ,(res[0],res[1]))
        con.commit()

        
    for res in result:
        img = Image.open(os.path.join(res[0],res[1]))
        img_mean = ImageStat.Stat(img).mean
        
        if len(img_mean) == 1:
            print(os.path.join(res[0],res[1]))
            continue
        
        cur.execute('update images set mean1 = ?, mean2 = ?, mean3 = ? where path = ? and filename = ?'
                    ,(img_mean[0]
                    ,img_mean[1]
                    ,img_mean[2]
                    ,res[0]
                    ,res[1]))
        con.commit()

        
t2 = time.time()
print('calculated' + str(t2-t1))

con.commit()

print('committed')
