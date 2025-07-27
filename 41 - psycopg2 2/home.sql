create type  payment_status AS ENUM ('paid', 'pending', 'delayed');

create table salaries (
    id SERIAL PRIMARY KEY,
    employee_name VARCHAR(64),
    month_name  VARCHAR(64),
    base_salary NUMERIC,
    bonus NUMERIC,
    penalty NUMERIC,
    net_salary NUMERIC GENERATED ALWAYS AS (base_salary + bonus - penalty) STORED,
    status payment_status
)

Maosh yozuvi qo‘shish – foydalanuvchi ma’lumot kiritadi, net_salary avtomatik hisoblanadi.
INSERT INTO salaries (
     employee_name,
     month_name,
     base_salary,
     bonus,
     penalty,
     status
) VALUES
('Ali Valiyev', '2025-07', 5000, 500, 100, 'paid'),
('Malika Karimova', '2025-07', 4500, 300, 0, 'pending'),
('Shoxrux Ergashev', '2025-07', 6000, 700, 200, 'delayed');
('Ali Valiyev', '2025-04', 4800, 300, 50, 'paid'),
('Ali Valiyev', '2025-05', 4900, 400, 0, 'paid'),
('Ali Valiyev', '2025-06', 5000, 450, 100, 'pending');

Muayyan ishchining oylik maoshlarini ko‘rish (filtr: ism, oy).
select month_name, net_salary from salaries where employee_name = 'Ali Valiyev' order by month_name;

Biror oy uchun barcha ishchilarning maosh ro‘yxatini chiqarish.
select employee_name, net_salary from salaries where month_name = '2025-07';

To‘lanmagan (pending) yoki kechiktirilgan (delayed) yozuvlarni ko‘rish.
select employee_name, status from salaries where status = 'pending' or status = 'delayed';

Maosh statusini o‘zgartirish (pending → paid).
update salaries set status = 'paid' where status = 'pending';

Statistika:
Bir oyda to‘langan umumiy maosh summasi.
select month_name, sum(net_salary) as total_salary from salaries group by month_name order by month_name;

Eng ko‘p ustama olgan ishchi.
select employee_name, bonus from salaries where bonus = (select max(bonus) from salaries);

Eng ko‘p jarima qilingan ishchi.
select employee_name, penalty from salaries where penalty = (select max(penalty) from salaries);


