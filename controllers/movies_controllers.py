from fastapi import FastAPI, HTTPException, status, APIRouter
from models import Movies, Movies_Update, Movies_Delete
from datetime import date
import psycopg2

router = APIRouter()
 
######### PARAMETERS OF THE DATABASE ####
#########################################
 
db_params = {
    'dbname':'postgres',
    'user':'postgres',
    'password':'aleymigle',
    'host':'localhost',
    'port':'5432'
}

conn = psycopg2.connect(**db_params)
cursor = conn.cursor()
print("Successful connection!")

######## CREATION OF THE TABLE ###########
##########################################
with conn.cursor() as cursor:
        try: 
            #define the SQL statement to create a table
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS "my_movies" (
                id SERIAL PRIMARY KEY,
                author VARCHAR(255),
                description VARCHAR(255),
                release_date DATE
            );
            '''
            #execute the SQL statement to create the table
            cursor.execute(create_table_query)

            #commit changes
            conn.commit()


        except Exception as e:
            print(f"Error:{e}")

   
################ METHODS ###############
########################################
        
## GET
@router.get('/movies')
def get_movies(db_name:str):
    temporal_list = []

    with conn.cursor() as cursor:
        try: 
            get_data_query = f'''
            SELECT * FROM {db_name}
            '''
            print(get_data_query)
            cursor.execute(get_data_query)
            rows = cursor.fetchall()
            conn.commit()

            #process the data
            for row in rows:
                print(row)
                temporal_list.append(row)

        except Exception as e:
            print(f"Error:{e}")

    return {'message':temporal_list}

## POST
@router.post('/movies')
def create_movies(movie:Movies):
    print(movie.author)
    print(movie.description)
    print(movie.release_date)

    with conn.cursor() as cursor:
        try:
            insert_data_query=f'''
            INSERT INTO {movie.db_name} (author,description,release_date) VALUES (%s,%s,%s)
            '''

            data_to_insert = (movie.author, movie.description,movie.release_date)
            print(data_to_insert)
            cursor.execute(insert_data_query,data_to_insert)
            conn.commit()
 
        except Exception as e:
            print(f'Error: {e}') 

    return {'message':'movie aggregated correctly'} 
 
## PUT
@router.put('/movies')
def update_movies(movie_update: Movies_Update):
    print(f'The register with id {movie_update.id_to_update} will be updated!')

    with conn.cursor() as cursor:
        try:
           #query to update a register
           update_query=f'''
           UPDATE {movie_update.db_name_to_update}
           SET author = %s , description =%s , release_date = %s
           WHERE id = {movie_update.id_to_update}
           '''
           data_to_update = (movie_update.author_updated,movie_update.description_updated,movie_update.release_date_updated)
           #print(update_query)
           cursor.execute(update_query,data_to_update)
           conn.commit()

        except Exception as e:
            print('Error:{e}')

    return {'message':f'register with id {movie_update.id_to_update} has been updated!'}

## DELETE
@router.delete('/movies')
def delete_data(movie_delete:Movies_Delete):
    print(f'The register with id {movie_delete.id_to_delete} will be deleted')

    with conn.cursor() as cursor:
        try:
            #query to delete
            query_to_delete = f'''
            DELETE FROM {movie_delete.db_name_to_delete}
            WHERE id = {movie_delete.id_to_delete}
            '''
            cursor.execute(query_to_delete)
            conn.commit()

        except Exception as e:
            print('Error:{e}')

    return {'message':'The register with id {movie_delete.id_to_delete} has been deleted!'} 