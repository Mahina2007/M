# CREATE TABLE patients (
#     patient_id INTEGER PRIMARY KEY,
#     full_name VARCHAR(50),
#     age INTEGER,
#     disease VARCHAR(50),
#     hospital VARCHAR(50),
#     admission_year INTEGER,
#     treatment_cost DECIMAL(10,2)
# );
#
# INSERT INTO patients (patient_id, full_name, age, disease, hospital, admission_year, treatment_cost) VALUES
# (1, 'John Smith', 45, 'Flu', 'City Hospital', 2021, 150.50),
# (2, 'Mary Johnson', 32, 'Cold', 'General Hospital', 2020, 120.75),
# (3, 'James Brown', 60, 'Diabetes', 'City Hospital', 2022, 300.00),
# (4, 'Patricia Wilson', 28, 'Flu', 'General Hospital', 2021, 140.25),
# (5, 'Robert Davis', 55, 'Hypertension', 'City Hospital', 2020, 250.50),
# (6, 'Linda Martinez', 39, 'Cold', 'General Hospital', 2023, 130.99),
# (7, 'Michael Clark', 47, 'Diabetes', 'City Hospital', 2021, 320.75),
# (8, 'Susan Lee', 25, 'Flu', 'General Hospital', 2022, 145.00),
# (9, 'William Taylor', 62, 'Hypertension', 'City Hospital', 2020, 270.25),
# (10, 'Elizabeth White', 34, 'Cold', 'General Hospital', 2021, 125.50),
# (11, 'David Harris', 50, 'Diabetes', 'City Hospital', 2023, 310.00),
# (12, 'Jennifer Lewis', 29, 'Flu', 'General Hospital', 2020, 135.75),
# (13, 'Thomas Walker', 58, 'Hypertension', 'City Hospital', 2022, 260.99),
# (14, 'Sarah Adams', 36, 'Cold', 'General Hospital', 2021, 128.25),
# (15, 'Charles Moore', 64, 'Diabetes', 'City Hospital', 2020, 330.50),
# (16, 'Karen Young', 31, 'Flu', 'General Hospital', 2023, 142.00),
# (17, 'Steven King', 53, 'Hypertension', 'City Hospital', 2021, 255.75),
# (18, 'Nancy Scott', 27, 'Cold', 'General Hospital', 2022, 132.50),
# (19, 'Daniel Green', 59, 'Diabetes', 'City Hospital', 2020, 325.25),
# (20, 'Laura Hall', 33, 'Flu', 'General Hospital', 2021, 138.99);

# Vazifa 1: Barcha bemorlar ro'yxatini ularning yoshiga ko'ra kamayish tartibida olish so'rovini yozing.
# select * from patients order by age desc;
# Vazifa 2: Muayyan shifoxonadagi (masalan, "City Hospital") va ma'lum bir kasallikdan (masalan, "Diabetes") davolanayotgan bemorlarni topish so'rovini yozing.
# select * from patients where hospital='City Hospital' and disease='Diabetes';
# Vazifa 3: Har bir bemorning davolanish xarajatlarini umumiy o'rtacha xarajat bilan solishtirish so'rovini yozing.
#select full_name, treatment_cost, (select(treatment_cost) from patients) as average_cost from patients;
# Vazifa 4: Har bir kasallik turi bo'yicha bemorlar sonini va ularning umumiy davolanish xarajatlarini aniqlash so'rovini yozing.
# select distinct disease count(*) from patients;
# Vazifa 5: Eng yuqori davolanish xarajatiga ega bo'lgan bemorni topish so'rovini yozing.
# select * from patients where max(treatment_cost);
# Vazifa 6: Har bir shifoxonada davolanayotgan bemorlarning o'rtacha yoshini chiqaruvchi so'rovini yozing.
#
# Vazifa 7: Muayyan yilda (masalan, 2021) ro'yxatdan o'tgan va "Flu" kasalligidan davolanayotgan bemorlar ro'yxatini olish so'rovini yozing.
#
# Vazifa 8: Eng past davolanish xarajatiga ega bo'lgan bemorni aniqlash so'rovini yozing.
#
# Vazifa 9: Har bir yilda va har bir kasallik bo'yicha ro'yxatdan o'tgan bemorlar sonini ko'rsatish so'rovini yozing.
#
# Vazifa 10: Davolanish xarajati o'rtacha xarajatlardan yuqori bo'lgan va yoshi 40 dan katta bemorlar ro'yxatini chiqaruvchi so'rovini yozing.
#
# Vazifa 11: Har bir kasallik bo'yicha eng yuqori va eng past davolanish xarajatiga ega bo'lgan bemorlarni aniqlash so'rovini yozing.
#
# Vazifa 12: Har bir shifoxonada eng ko'p bemor davolanadigan kasallik turini aniqlash so'rovini yozing.
#
# Vazifa 13: Yosh bo'yicha eng yosh 5 ta bemorni topish so'rovini yozing.
#
# Vazifa 14: Har bir kasallik bo'yicha davolanish xarajati o'rtacha xarajatlardan past bo'lgan bemorlarning foizini hisoblash so'rovini yozing.
