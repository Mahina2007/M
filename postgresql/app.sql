CREATE TABLE IF NOT EXISTS teachers
(
    id         SERIAL PRIMARY KEY,
    full_name  VARCHAR(128) NOT NULL,
    age        SMALLINT CHECK(age>0) NOT NULL,
    gender     BOOLEAN,
    subject    VARCHAR,
    email      VARCHAR NOT NULL,
    birthdate  DATE NOT NULL,
    phone_num  VARCHAR(13)
);
