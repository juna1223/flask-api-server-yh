import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'yh-db.c4kkyzo02io2.us-east-2.rds.amazonaws.com',
        database = 'recipe_db',
        user = 'recipe_user',
        password = '1223'
    )
    return connection