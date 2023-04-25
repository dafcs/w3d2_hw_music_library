from db.run_sql import run_sql
from models.artist import Artist

#we do not need to import album for now since it is not inside the artist table, however the artists is inside album

# CRUD

#Create - send/insert/save
def insert(artist):
    sql = 'INSERT INTO artists (name) VALUES (%s) RETURNING *'
    values = [artist.name]
    row = run_sql(sql,values)
    artist.id = row[0]['id']
    return artist

#Read - select

#single
def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    row = run_sql(sql,values)
    if row is not None:
        artist = Artist(row.name)
    return artist

#all
def select_all():
    result = []
    sql = "SELECT * FROM artists"
    rows = run_sql(sql)
    for row in rows:
        artist = Artist(row["name"])
        result.append(artist)
    return result


#Update - modify
    #single
def update(artist):
    sql = 'UPDATE artists SET (name) = (%s) WHERE id=%s'
    values = (artist.name,artist.id)
    run_sql(sql,values)

    #all(?)
def update_all(artist):
    sql = 'UPDATE artists SET (name) = (%s)'
    values = (artist.name)
    run_sql(sql,values)

#Delete - poof
    #single
def delete(id):
    sql = 'DELETE FROM artists WHERE id = %s'
    values = [id]
    run_sql(sql,values)
    #all
def delete_all():
    sql = 'DELETE * FROM artists'
    run_sql(sql)
