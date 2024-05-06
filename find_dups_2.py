import os, sqlite3, time

t1= time.time()

con = sqlite3.connect('imgs.db')
cur = con.cursor()

cur.execute('''

	select path, filename, md5, row_number() over (partition by md5 order by md5) rn
          from images2
         where md5 in 
            (select md5
               from (select *, row_number() over (partition by md5 order by md5) rn
                       from images2
                      where processed = 1) t0 
              where rn > 1 ) 
        order by md5
        
    ''')

dups_path = r'D:\dups_all'


while True:
    
    result = cur.fetchone()

    if not result:
        break
    
    filename = result[2] + "_" + str(result[3]) + "_" + result[1]

    orig_file = os.path.join(result[0],result[1])
    new_file = os.path.join(dups_path, filename)

    if os.path.isfile(orig_file):
        os.rename(orig_file, new_file)


cur.execute('''


          select path, filename, md5, rn
            from (select *, row_number() over (partition by md5 order by md5) rn
                    from images2
                   where processed = 1) t0 
           where rn > 1 
           order by md5
        
    ''')

dups_delete_path = r'D:\dups_to_delete'

while True:
    result = cur.fetchone()

    if not result:
        break
    
    filename = result[2] + "_" + str(result[3]) + "_" + result[1]

    orig_file = os.path.join(dups_path, filename)
    new_file = os.path.join(dups_delete_path, filename)

    if os.path.isfile(orig_file):
        os.rename(orig_file, new_file)

