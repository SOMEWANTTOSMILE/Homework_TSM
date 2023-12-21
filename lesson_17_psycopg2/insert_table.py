from config import user, db_name, password, host
import psycopg2
from data_insert_table import user_input

connection = None

try:
    connection = psycopg2.connect(
        user=user,
        database=db_name,
        password=password,
        host=host
    )

    connection.autocommit = True

    user_data = user_input()
    print(user_data)

    with connection.cursor() as cursor:
        cursor.execute(
            """insert into food_info(
            food_name, proteins, fats, carbohydrates) VALUES (%s,%s,%s,%s ) RETURNING food_name;""",
            (user_data[0], user_data[1], user_data[2], user_data[3])
        )
        food_name = cursor.fetchone()[0]

        user_name = input("Enter your name: ")

        cursor.execute(
            f"""insert into all_user(
            name) VALUES ('{user_name}') RETURNING name;"""
        )

        user_name = cursor.fetchone()[0]

        cursor.execute(
            """insert into user_food_intake(
            name, food_intake) VALUES (%s, %s);""",
            (user_name, food_name)
        )


except Exception as _ex:
    print(f"[INFO] Error:", _ex)
finally:
    connection.close()
    print(f"[INFO] database was close")
