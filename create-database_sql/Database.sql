create DATABASE eating owner Somwl encoding "utf8";

create TABLE users(
    user_id serial primary key,  -- unique user id
    user_full_name varchar(50) not null --the full name cannot be longer than 50 letters and cannot be null
);

create TABLE food(
    food_id serial primary key, -- unique food id
    food_name varchar(50) not null, --the food name cannot be longer than 50 letters and cannot be null
    grams integer check ( grams > 0 ) not null -- grams cannot be equal zero, grams always is integer, cannot be null
);

create TABLE food_intake(
    intake_id serial primary key, -- unique food id
    user_id integer references users(user_id) on delete cascade, --  id  in int, references takes the user id from -->
    --> the users table, delete cascade - If the user_id was deleted in the users table, it will be deleted in the -->
    --> food_intake table as well.
    user_food integer references food(food_id) on delete cascade,--  id  in int, references takes the user_food from -->
    --> the food table, delete cascade - If the food_id was deleted in the food table, it will be deleted in the -->
    --> food_intake table as well.
    amount integer check ( amount > 0 ) not null -- amount cannot be equal zero, amount always is integer cannot be null
)