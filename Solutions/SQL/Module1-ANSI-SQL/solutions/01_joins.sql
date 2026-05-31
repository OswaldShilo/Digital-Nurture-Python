-- ============================================================
-- Module 1 | Topic: JOINs
-- Exercises: 1, 7, 8, 9
-- ============================================================

-- Exercise 1: User Upcoming Events
-- Show all upcoming events a user is registered for in their city,
-- sorted by start date.
SELECT u.user_id, u.full_name,
       e.title AS event_title, e.city, e.start_date
FROM   Users u
JOIN   Registrations r ON r.user_id  = u.user_id
JOIN   Events        e ON e.event_id = r.event_id
WHERE  e.status = 'upcoming'
  AND  e.city   = u.city
ORDER  BY e.start_date;

-- ------------------------------------------------------------

-- Exercise 7: Low Feedback Alerts
-- Users who gave a rating less than 3, with their comments
-- and the associated event name.
SELECT u.user_id, u.full_name,
       e.title AS event_title,
       f.rating, f.comments, f.feedback_date
FROM   Feedback f
JOIN   Users  u ON u.user_id  = f.user_id
JOIN   Events e ON e.event_id = f.event_id
WHERE  f.rating < 3;

-- ------------------------------------------------------------

-- Exercise 8: Sessions per Upcoming Event
-- All upcoming events with the count of sessions scheduled.
SELECT e.event_id, e.title,
       COUNT(s.session_id) AS session_count
FROM   Events e
LEFT JOIN Sessions s ON s.event_id = e.event_id
WHERE  e.status = 'upcoming'
GROUP  BY e.event_id, e.title;

-- ------------------------------------------------------------

-- Exercise 9: Organizer Event Summary
-- For each organizer, count of events per status.
SELECT u.user_id   AS organizer_id,
       u.full_name AS organizer_name,
       e.status,
       COUNT(e.event_id) AS event_count
FROM   Users  u
JOIN   Events e ON e.organizer_id = u.user_id
GROUP  BY u.user_id, u.full_name, e.status
ORDER  BY u.user_id, e.status;
