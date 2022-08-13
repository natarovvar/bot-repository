from os import curdir
import sqlite3 as sq




def sql_database_start():
    global base, cur
    base = sq.connect('paperclip_database.db')
    cur = base.cursor()
    if base:
        print('data base is connected')
    base.execute('CREATE TABLE IF NOT EXISTS loaded(img TEXT, description TEXT )')
    base.execute('CREATE TABLE IF NOT EXISTS geolocation(user TEXT, latitude TEXT, longitude TEXT )')
    base.commit()
    
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO loaded VALUES (?,?)', tuple(data.values()))
        base.commit()

async def sql_add_geopostition(username, lat, lon):
        cur.execute('INSERT INTO geolocation VALUES (?,?,?)', (username, lat, lon))
        base.commit()
        




        
        