from config import user, db_name, password, host
import psycopg2

connection = None

try:
    connection = psycopg2.connect(
        host=host,
        database=db_name,
        user=user,
        password=password
    )

    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """select * from food_info"""
        )
        all_info = cursor.fetchall()
        print(all_info)

        cursor.execute(
            """select * from all_user"""
        )
        user_info = cursor.fetchall()
        print(user_info)

        cursor.execute(
            """select * from user_food_intake"""
        )
        user_info_intake = cursor.fetchall()
        print(user_info_intake)


except Exception as _ex:
    print(f"[INFO] Error:", _ex)
finally:
    connection.close()
