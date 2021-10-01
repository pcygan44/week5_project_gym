DROP TABLE bookings;
DROP TABLE members;
DROP TABLE sesions;


CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    membership BOOLEAN,
    active_status BOOLEAN
);

CREATE TABLE sesions(
    id SERIAL PRIMARY KEY,
    class_name VARCHAR(255),
    duration INT,
    class_date FLOAT,
    class_time FLOAT,
    capacity INT,
    active_status BOOLEAN

);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    members_id INT REFERENCES members(id) ON DELETE CASCADE,
    sesions_id INT REFERENCES sesions(id) ON DELETE CASCADE,
    review TEXT
);










