from config import user, db_name, password, host
import psycopg2


def user_input():
    try:
        connection = None
        connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user,
            password=password
        )

        with connection.cursor() as cursor:
            cursor.execute(
                """select food_name from food_info"""
            )

            all_info = cursor.fetchall()
            all_food = [i[0] for i in all_info]

        food_information = "food_name", "proteins", "fats ", "carbohydrates"
        user_data_food = [input(f"Enter products {i}: ").lower() for i in food_information]

    except Exception as _ex:
        print(f"[INFO] Error:", _ex)
    finally:
        connection.close()

    return user_data_food



