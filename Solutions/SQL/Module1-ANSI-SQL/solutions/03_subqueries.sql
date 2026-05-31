-- ============================================================
-- Module 1 | Topic: Subqueries & NOT IN
-- Exercises: 3, 12, 16, 22
-- ============================================================

-- Exercise 3: Inactive Users
-- Users who have not registered for any event in the last 90 days.
-- Note: DATE('now','-90 days') is SQLite; use CURDATE()-INTERVAL 90 DAY in MySQL.
SELECT u.user_id, u.full_name, u.email
FROM   Users u
WHERE  u.user_id NOT IN (
    SELECT r.user_id
    FROM   Registrations r
    WHERE  r.registration_date >= DATE('now', '-90 days')
);

-- ------------------------------------------------------------

-- Exercise 12: Event with Maximum Sessions
-- Event(s) with the highest number of sessions.
SELECT e.event_id, e.title,
       COUNT(s.session_id) AS session_count
FROM   Events   e
JOIN   Sessions s ON s.event_id = e.event_id
GROUP  BY e.event_id, e.title
HAVING COUNT(s.session_id) = (
    SELECT MAX(cnt)
    FROM (
        SELECT COUNT(session_id) AS cnt
        FROM   Sessions
        GROUP  BY event_id
    )
);

-- ------------------------------------------------------------

-- Exercise 16: Unregistered Active Users
-- Users who signed up in the last 30 days but haven't registered for any event.
SELECT u.user_id, u.full_name, u.registration_date
FROM   Users u
WHERE  u.registration_date >= DATE('now', '-30 days')
  AND  u.user_id NOT IN (
      SELECT DISTINCT user_id FROM Registrations
  );

-- ------------------------------------------------------------

-- Exercise 22: Duplicate Registrations Check
-- Detect users registered more than once for the same event.
SELECT user_id, event_id,
       COUNT(*) AS registration_count
FROM   Registrations
GROUP  BY user_id, event_id
HAVING COUNT(*) > 1;
