--1. books nomli jadval yarating, unda quyidagi ustunlar boвЂlsin:
--    kitob nomi, muallif ismi, chop etilgan yili, va narxi.
CREATE TABLE IF NOT EXISTS books
(
    title      VARCHAR(100) NOT NULL,
    author     VARCHAR  NOT NULL,
    published  DATE NOT NULL,
    price      VARCHAR
);
--
--2. employees nomli jadval tuzing, u xodim ID raqami, toвЂliq ism, lavozimi,
--    ishga kirgan sana va oylik maosh ustunlarini oвЂz ichiga olsin.
CREATE TABLE IF NOT EXISTS employees
(
    id         SERIAL PRIMARY KEY,
    full_name  VARCHAR(100) NOT NULL,
    job        VARCHAR  NOT NULL,
    started_on DATE NOT NULL,
    salary     VARCHAR
);

--
--3. products jadvalini yarating, bu jadvalda mahsulot nomi, toifasi, zaxiradagi
--    soni va mahsulot faol (boolean) ekanligini bildiruvchi ustun boвЂlsin.
CREATE TABLE IF NOT EXISTS products
(
    product  VARCHAR NOT NULL,
    type     VARCHAR(100) NOT NULL,
    quantity SMALLINT,
    activity BOOLEAN
);
--
--4. students jadvalini tuzing, unda talabalar ID raqami (avto-inkrement), ism,
--    tugвЂilgan sana, sevimli fanlar (array koвЂrinishida) va oвЂqishga kirgan sana boвЂlsin.
CREATE TABLE IF NOT EXISTS students
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR NOT NULL,
    birth        DATE,
    fav_subjects TEXT[],
    admitted     DATE
);
--
--5. orders jadvali yarating, u buyurtma ID, mijoz ID, mahsulot ID, buyurtma sanasi
--    va umumiy summa ustunlarini oвЂz ichiga olsin (umumiy summani aniq decimal turida saqlang).
CREATE TABLE IF NOT EXISTS orders
(
    order_id          SERIAL PRIMARY KEY,
    client_id         SERIAL PRIMARY KEY,
    product_id        SERIAL PRIMARY KEY,
    ordered           DATE,
    total_sum         DECIMAL
);
--
--6. movies nomli jadval yarating, unda film nomi, rejissyor, chiqish sanasi, janr
--    va reyting (bir oвЂnlik kasr koвЂrinishida) boвЂlsin.
CREATE TABLE IF NOT EXISTS movies
(
    movie          VARCHAR NOT NULL,
    director       VARCHAR,
    film_date      DATE,
    genre          VARCHAR,
    rating         DECIMAL(3,1)
);
--7. payments jadvalini tuzing, bu jadval toвЂlov IDsi, toвЂlovchi ismi,
--    miqdori, toвЂlov usuli va vaqt belgisini (timestamp) oвЂz ichiga olsin.
CREATE TABLE IF NOT EXISTS payments
(
    id              PRIMARY KEY,
    name            VARCHAR,
    payment_type    VARCHAR,
    time_of_payment TIMESTAMP
);
--8. vehicles nomli jadval yarating, unda transport vositasi IDsi, ishlab chiqaruvchi,
--    model, yil, roвЂyxatdan oвЂtgan sana va kuzatuv uchun UUID ustuni boвЂlsin.
CREATE TABLE IF NOT EXISTS vehicles
(
    id                 PRIMARY KEY,
    manufacturer       VARCHAR,
    model              VARCHAR,
    year_of_production DATE,
    approved           DATE,
    monitoring         UUID
);
--9. appointments jadvalini tuzing, unda uchrashuv IDsi, bemor ismi, shifokor ismi,
--    uchrashuv sanasi va vaqti, va davomiyligi (interval turi) boвЂlsin.
CREATE TABLE IF NOT EXISTS appointments
(
    id           PRIMARY KEY,
    patient_name VARCHAR,
    doctor_name  VARCHAR,
    meeting_date TIMESTAMP,
    duration     INTERVAL
);
--10. weather_logs jadvalini yarating, unda log ID, sana, harorat
--    (real turi), namlik (real turi), va izohlar (text) boвЂlsin.
CREATE TABLE IF NOT EXISTS weather_logs
(
    log_id           PRIMARY KEY,
    date_of_logs     DATE,
    temperature      REAL,
    humidity         REAL,
    comments         TEXT[]
);
--11. invoices nomli jadval yarating, unda quyidagi ustunlar boвЂlsin:
--    hisob-faktura raqami, mijoz ismi, sana, umumiy summa (decimal), va toвЂlanganmi (boolean).
CREATE TABLE IF NOT EXISTS invoices
(
    invoice_num         INT,
    client_name         VARCHAR,
    date_of_invoice     DATE,
    total_sum           DECIMAL,
    is_paid             BOOLEAN
);
--12. teachers jadvalini tuzing, u yerda oвЂqituvchi IDsi (avto-inkrement),
--    ism, mutaxassislik, yillik tajribasi (integer), va tugвЂilgan sanasi boвЂlsin.
CREATE TABLE IF NOT EXISTS TEACHERS
(
    ID                  SERIAL PRIMARY KEY,
    name                VARCHAR,
    specification       VARCHAR,
    experience          INT,
    birth_date          DATE
);
--13. feedbacks nomli jadval yarating, foydalanuvchi ismi, baho (1 dan 5 gacha),
--    sharh (text), va yuborilgan sana/vaqt (timestamp) ustunlarini oвЂz ichiga olsin.
CREATE TABLE IF NOT EXISTS feedbacks
(
    name                VARCHAR,
    rate                NUMERIC(2,1),
    comments            TEXT[],
    time_of_feedback    TIMESTAMP
);
--14. flights jadvalini tuzing, bu jadvalda reys raqami, manzil,
--    uchish vaqti (TIMESTAMP), kelish vaqti, va parvoz davomiyligi (INTERVAL) boвЂlsin.
CREATE TABLE IF NOT EXISTS flights
(
    flight_num              VARCHAR,
    destination             VARCHAR,
    flight_time           TIMESTAMP,
    time_of_arrival       TIMESTAMP,
    duration              INTERVAL
);
--15. subscriptions nomli jadval yarating, unda foydalanuvchi IDsi,
--    obuna turi (masalan: "basic", "premium"), boshlanish sanasi, tugash sanasi (DATE), va faol (boolean) ustunlari boвЂlsin.
CREATE TABLE IF NOT EXISTS SUBSCRIPTIONS
(
    user_id               SERIAL PRIMARY KEY,
    subscription_type     VARCHAR,
    start_time            DATE,
    finish_time           DATE,
    is_active             BOOLEAN
);