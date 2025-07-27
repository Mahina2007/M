"""
Vazifa 1: Barcha xodimlar ro'yxatini ularning maoshiga ko'ra o'sish tartibida olish so'rovini yozing.
select * from staff order by salary;
Vazifa 2: M uayyan bo'limdagi (masalan, "Development") va ma'lum bir lavozimdag (masalan, "Senior Developer") xodimlarni topish so'rovini yozing.
select * from staff where department='Development' and position='Senior Developer';
Vazifa 3: Har bir xodimning maoshini kompaniyadagi o'rtacha maosh bilan solishtirish so'rovini yozing.
select full_name, salary, (select avg(salary) from staff) as average_cost from staff;
Vazifa 4: Har bir bo'lim bo'yicha xodimlar sonini va ularning umumiy maoshlarini aniqlash so'rovini yozing.
select distinct department, count(*) as employee_num, sum(salary) as total_salary from staff group by department;
Vazifa 5: Eng yuqori maoshga ega bo'lgan xodimni topish so'rovini yozing.
select full_name, salary from staff where salary = (select max(salary) from staff);
Vazifa 6: Har bir lavozimdagi xodimlarning o'rtacha tajribasini (yillarda) chiqaruvchi so'rovini yozing.
select distinct position, avg(experience_years) from staff group by position;
Vazifa 7: Muayyan yilda (masalan, 2020) ishga qabul qilingan va "Development" bo'limida ishlaydigan xodimlar ro'yxatini olish so'rovini yozing.
select * from staff where hire_year = '2020' and department = 'Development';
Vazifa 8: Eng kam tajribaga ega bo'lgan xodimni aniqlash so'rovini yozing.
select full_name, experience_years from staff where experience_years = (select min(experience_years) from staff);
Vazifa 9: Har bir yilda va har bir bo'lim bo'yicha ishga qabul qilingan xodimlar sonini ko'rsatish so'rovini yozing.
select hire_year, department, count(*) as employee_num from staff group by hire_year, department order by hire_year, department;
Vazifa 10: Maoshi o'rtacha maoshdan past bo'lgan va tajribasi 5 yildan kam xodimlar ro'yxatini chiqaruvchi so'rovini yozing.
select * from staff where experience_years<5 and salary < (select avg(salary) from staff);
Vazifa 11: Har bir lavozim bo'yicha eng yuqori va eng past maoshga ega bo'lgan xodimlarni aniqlash so'rovini yozing.
select * from staff where salary = (select max(salary) from staff) or salary = (select min(salary) from staff);
Vazifa 12: Har bir bo'limda eng ko'p xodim ishlaydigan lavozimni aniqlash so'rovini yozing.
select department, count(*) as employee_num from staff group by department;
Vazifa 13: Tajribasi bo'yicha eng tajribali 5 ta xodimni topish so'rovini yozing.
select * from staff order by experience_years desc limit 5;

CREATE TABLE staff (
    staff_id INTEGER PRIMARY KEY,
    full_name VARCHAR(50),
    department VARCHAR(50),
    position VARCHAR(50),
    hire_year INTEGER,
    salary DECIMAL(10,2),
    experience_years INTEGER
);

INSERT INTO staff (staff_id, full_name, department, position, hire_year, salary, experience_years) VALUES
(1, 'John Doe', 'Development', 'Senior Developer', 2019, 75000.00, 8),
(2, 'Jane Smith', 'Marketing', 'Marketing Manager', 2020, 65000.50, 5),
(3, 'Michael Brown', 'Development', 'Junior Developer', 2022, 55000.75, 2),
(4, 'Emily Davis', 'HR', 'HR Specialist', 2021, 60000.25, 4),
(5, 'Robert Wilson', 'Development', 'Team Lead', 2018, 80000.00, 10),
(6, 'Laura Martinez', 'Marketing', 'Content Creator', 2023, 52000.99, 3),
(7, 'David Clark', 'Development', 'Senior Developer', 2020, 78000.50, 7),
(8, 'Susan Lee', 'HR', 'Recruiter', 2022, 58000.00, 3),
(9, 'William Taylor', 'Development', 'Junior Developer', 2021, 56000.25, 2),
(10, 'Elizabeth White', 'Marketing', 'SEO Specialist', 2020, 62000.50, 4),
(11, 'Thomas Harris', 'Development', 'Team Lead', 2019, 82000.75, 9),
(12, 'Jennifer Lewis', 'HR', 'HR Manager', 2020, 70000.00, 6),
(13, 'Charles Walker', 'Development', 'Senior Developer', 2021, 77000.99, 8),
(14, 'Sarah Adams', 'Marketing', 'Content Creator', 2022, 53000.25, 2),
(15, 'James Moore', 'Development', 'Junior Developer', 2023, 54000.50, 1),
(16, 'Karen Young', 'HR', 'Recruiter', 2021, 59000.75, 4),
(17, 'Steven King', 'Development', 'Senior Developer', 2020, 79000.00, 7),
(18, 'Nancy Scott', 'Marketing', 'Marketing Manager', 2022, 68000.50, 5),
(19, 'Daniel Green', 'Development', 'Team Lead', 2019, 83000.25, 10),
(20, 'Laura Hall', 'HR', 'HR Specialist', 2021, 61000.99, 3);

"""