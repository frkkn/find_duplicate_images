import os, sqlite3, time

t1= time.time()

con = sqlite3.connect('imgs.db')
cur = con.cursor()

sql = """
    select path,filename from
    (select path,filename,row_number() over (partition by md5 order by md5) rn
      from images2) t
    where rn = 1
"""

sql2 = """
    select path,count(*) from
    (select path,filename,row_number() over (partition by md5 order by md5) rn
      from images2) t
    where rn = 1
    group by path
"""

cur.execute(sql)

while True:
    res = cur.fetchone()

    if not res:
        break

    if os.path.isfile(os.path.join(res[0],res[1])) \
        and not os.path.isfile(os.path.join(r'd:\cleaned',res[1])) :

        os.rename(os.path.join(res[0],res[1]), os.path.join(r'd:\cleaned',res[1]))

    elif os.path.isfile(os.path.join(res[0],res[1])) and os.path.isfile(os.path.join(r'd:\cleaned',res[1])):
        new_filename = res[1][:res[1].rindex('.')] + "_2" + res[1][res[1].rindex('.'):]
        
        if os.path.isfile(os.path.join(r'd:\cleaned',new_filename)):
            new_filename = res[1][:res[1].rindex('.')] + "_3" + res[1][res[1].rindex('.'):]
                          
        if os.path.isfile(os.path.join(r'd:\cleaned',new_filename)):
            new_filename = res[1][:res[1].rindex('.')] + "_4" + res[1][res[1].rindex('.'):]
            
        if os.path.isfile(os.path.join(r'd:\cleaned',new_filename)):
            new_filename = res[1][:res[1].rindex('.')] + "_5" + res[1][res[1].rindex('.'):]
                          
        os.rename(os.path.join(res[0],res[1]), os.path.join(r'd:\cleaned',new_filename))

    else:
        pass

