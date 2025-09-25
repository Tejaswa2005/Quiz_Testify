CREATE TABLE questions(
    id serial primary key,
    text varchar(500) not null,
    option1 varchar(100) not null,
    option2 varchar(100) not null,
    option3 varchar(100) not null,
    option4 varchar(100) not null,
    correct int not null
);

CREATE TABLE results (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) not null,
    roll_no VARCHAR(50) not null,
    class VARCHAR(50) not null,
    school VARCHAR(100) not null,
    score INT,
    percentage NUMERIC(5,2)
);