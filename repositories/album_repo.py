from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repo


# CRUD

# Create / insert instance in table. This will receive a full Album() class object, without the ID.
def insert(album):
    sql = 'INSERT INTO albums (title,genre,artist) VALUES (%s,%s,%s) RETURNING *'
             # ^command    ^table   ^columns         ^to add    ^placeholder  ^return the row (for ID(?))
    values = [album.title,album.genre,album.artist]

    # at this point we can run the SQL and place these values in the respective table/columns
    # this point will generate the ID
    row = run_sql(sql,values)
    #the result of this will be the inception of semi lists that are actually dictionaries with 'hidden' keys [[]]
    #since we need to pick at it to get the id, we store it in a variable (row)
    id = row[0]['id']
    #the result will be one item so calling 0 will refer to it. if there is no item then it will result in index out of range..probably
    #now, we need to assign the id to the class object Album()
    album.id = id
    #this should now return a neat completed class which we can go wild with :)
    return album

#READ / select a piece or all of the data and show it to me
def select_all(id):
    #since we want to be friends with the machine we use ids or it gets confused
    album = None
    #for now, the album is none, we want one but we have none, so we need to get it.
    #sql = SELECT all FROM table WHERE id is Y - understanding that we select all since we want to check all the table for the one instance of id
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    #at this point we have the full SQL code and can run it
    row = run_sql(sql,values)
    #we need the result from running the sql, 
    #from here we want to check whether it returned something or not
    if row:
        #if row == [] then it's falsy
        #from here we need to create the task class object, but we need to make the artist repo first so we can pull the artist which goes in to album.artist
        #I totally did not start from here and now need to go do the artist :)
        print('got a row watchugonndoboutit')