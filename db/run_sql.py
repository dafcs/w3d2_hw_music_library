import psycopg2
import psycopg2.extras as ext 
# psycopg2 for python/sql relation, extras for cursor(?)
def run_sql(sql,values = None):
    conn = None  #connection
    results = [] #will be added to, one [] per row with , separator
    try:
        #error handling, if it fails it goes for exceptions provided error, if it does not
        #succeed it will return exception, if it succeeds it will pass to finally.
        conn = psycopg2.connect(dbname='music_lib')
            #conn is the connection, we are making the connection between python and the database
        cur = conn.cursor(cursor_factory=ext.DictCursor) #cursor - something we get from a connection
            # cursor '|' is something that iterates 1 character in a row at a time (or steps through), 
            # dict is the dictionary, the column is the key and the value in row is the value
            # return some data in python form
        cur.execute(sql, values)
            #running the SQL, this also sanitizes the data, meaning that it will not run in case of injection but treat it as info to store
        conn.commit()
            #committing the run
        results = cur.fetchall()
            #tells the cursor to fetch all that it iterates through (also exists fetchone and fetchmany)
            #and puts the result into results, which is then returned
            #it starts with [],and for each row creates another [],
            #stage one will be [[]], when it iterates the values in row, it 'appends'
            #stage one will result in [[val1,val2,val3]]
            #stage three will then go to the next row and add a new 'list', [[[val1,val2,val3],[val4,val5,val6]] it will repeat the process until it has ran the whole table
        cur.close()
            #terminating cursor because we're cool like that
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"My error handling: {error}")
            #error handling
            #handles all exceptions, including database errors from psycopg2
            #it is then printing str + error type
    finally:
        if conn is not None:
            conn.close()
            #terminating connection if one exists
    return results