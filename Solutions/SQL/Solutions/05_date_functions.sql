-- ============================================================
-- Module 1 | Topic: Date Functions
-- Exercises: 11, 23
-- SQLite functions shown; MySQL equivalents noted in comments.
-- ============================================================

-- Exercise 11: Daily New User Count
-- Number of users who registered each day in the last 7 days.
-- MySQL:  WHERE registration_date >= CURDATE() - INTERVAL 7 DAY
SELECT registration_date,
       COUNT(user_id) AS new_users
FROM   Users
WHERE  registration_date >= DATE('now', '-7 days')
GROUP  BY registration_date
ORDER  BY registration_date;

-- ------------------------------------------------------------

-- Exercise 23: Registration Trends
-- Month-wise registration count over the past 12 months.
-- MySQL:  DATE_FORMAT(registration_date, '%Y-%m')
--         WHERE registration_date >= CURDATE() - INTERVAL 12 MONTH
SELECT strftime('%Y-%m', registration_date) AS month,
       COUNT(registration_id)               AS registrations
FROM   Registrations
WHERE  registration_date >= DATE('now', '-12 months')
GROUP  BY strftime('%Y-%m', registration_date)
ORDER  BY month;
