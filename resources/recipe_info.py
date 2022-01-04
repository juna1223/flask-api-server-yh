from flask import request
from flask.json import jsonify
from flask_restful import Resource
from http import HTTPStatus

from mysql_connection import get_connection
from mysql.connector.errors import Error

class RecipeResource(Resource) :

   def get(self, recipe_id) :
        # 클라이언트에서, 경로에 들어있는 데이터를 받고 싶을때는
        # app.py에서 연결한 변수로 처리할 수 있다.
        # 이 변수는 get 함수의 파라미터로 받는다.

        print(recipe_id)

        # 1. db 접속recipe 테이블에서 select 
        try :
            connection = get_connection()

            query = ''' select * 
                        from recipe where id = %s ; '''
            
            param = (recipe_id, )
            
            cursor = connection.cursor(dictionary = True)

            cursor.execute(query, param)

            # select 문은 아래 내용이 필요하다.
            record_list = cursor.fetchall()
            print(record_list)

            ### 중요. 파이썬의 시간은, JSON으로 보내기 위해서
            ### 문자열로 바꿔준다.
            i = 0
            for record in record_list:
                record_list[i]['created_at'] = record['created_at'].isoformat()
                record_list[i]['updated_at'] = record['updated_at'].isoformat()
                i = i + 1
            
        # 위의 코드를 실행하다가, 문제가 생기면, except를 실행하라는 뜻.
        except Error as e :
            print('Error while connecting to MySQL', e)
            return {'error' : str(e)} , HTTPStatus.BAD_REQUEST
        # finally 는 try에서 에러가 나든 안나든, 무조건 실행하라는 뜻.
        finally :
            print('finally')
            cursor.close()
            if connection.is_connected():
                connection.close()
                print('MySQL connection is closed')
            else :
                print('connection does not exist')


        return {'data' : record_list}, HTTPStatus.OK

   def put(self, recipe_id) :

       data = request.get_json()

       try :
            connection = get_connection()

            query = ''' update recipe 
                        from recipe where id = %s ; '''
            
            param = (recipe_id, )
            
            cursor = connection.cursor(dictionary = True)

            cursor.execute(query, param)

            # select 문은 아래 내용이 필요하다.
            record_list = cursor.fetchall()
            print(record_list)

            ### 중요. 파이썬의 시간은, JSON으로 보내기 위해서
            ### 문자열로 바꿔준다.
            i = 0
            for record in record_list:
                record_list[i]['created_at'] = record['created_at'].isoformat()
                record_list[i]['updated_at'] = record['updated_at'].isoformat()
                i = i + 1
            
        # 위의 코드를 실행하다가, 문제가 생기면, except를 실행하라는 뜻.
        except Error as e :
            print('Error while connecting to MySQL', e)
            return {'error' : str(e)} , HTTPStatus.BAD_REQUEST
        # finally 는 try에서 에러가 나든 안나든, 무조건 실행하라는 뜻.
        finally :
            print('finally')
            cursor.close()
            if connection.is_connected():
                connection.close()
                print('MySQL connection is closed')
            else :
                print('connection does not exist')


       return()     