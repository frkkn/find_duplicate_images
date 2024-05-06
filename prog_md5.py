import os, sqlite3, time, hashlib
from PIL import Image, ImageStat, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

t1= time.time()

con = sqlite3.connect('imgs.db')
cur = con.cursor()

cur.execute('select count(*) from images3 where processed = 0')
i = cur.fetchone()[0]


while True:
    print(i)
    i -= 1

    cur.execute('select path,filename from images3 where processed = 0')
    result = cur.fetchone()

    if not result:
        break
        
    t1 = time.time()
    file = open(os.path.join(result[0],result[1]), 'rb')
    file_data = file.read()
    file.close()
    md5 = hashlib.md5(file_data).hexdigest()
    process_time = time.time() - t1
    
    cur.execute('update images3 set processed = 1, processtime = ?, md5 = ? \
                  where path = ? and filename = ?'
                ,(process_time
                ,md5
                ,result[0]
                ,result[1]))
    con.commit()

        
t2 = time.time()
print('calculated' + str(t2-t1))

con.commit()

print('committed')
