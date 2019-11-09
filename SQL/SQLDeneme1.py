import sqlite3 as sql
import os
try:
    DByol = os.getcwd() + os.sep + "SQL" + os.sep + "chinook" + os.sep+"chinook.db"
    db = sql.connect(DByol)
    cur = db.cursor()
    query = """
    INSERT INTO artists (Name) VALUES ('{}');
    """
    isim = input("Sanatçının İsmi Giriniz")
    query = query.format(isim)
    cur.execute(query)
    # print(*cur.fetchall(),sep="\n")
    if input("Değişikliği Onaylıyor musunuz") == "e":
        db.commit()
    else:
        print("Onaylamadın")
except:
    pass
finally:
    db.close()


