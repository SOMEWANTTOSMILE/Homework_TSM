from config import host, db_name, user, password
import psycopg2

connection = None

try:
    connection = psycopg2.connect(
        host=host,
        database=db_name,
        password=password,
        user=user
    )

    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """Create table food_info(
            id serial primary key ,
            food_name varchar(50) not null,
            proteins integer check ( proteins > 0 ) not null,
            fats integer check ( fats > 0 ) not null,
            carbohydrates integer check ( carbohydrates > 0 ) not null
            )"""
        )
        cursor.execute(
            """Create table all_user(
            user_id serial primary key,
            name varchar(50) not null
            )"""
        )
        cursor.execute(
            """Create table user_food_intake(
            food_intake_id serial primary key,
            name varchar(50) not null,
            food_intake varchar(50) not null
            )"""
        )

        print(f"[INFO] Table successful was created")


except Exception as _ex:
    print(f"[INFO], _ex")
finally:
    connection.close()
    print(f"[INFO] database was close")
