-- ============================================================
-- Module 1 | Topic: Aggregations (GROUP BY, COUNT, AVG, SUM)
-- Exercises: 2, 4, 5, 6, 13, 14, 17, 21, 24
-- ============================================================

-- Exercise 2: Top Rated Events
-- Events with the highest average rating (min 10 feedback submissions).
SELECT e.event_id, e.title,
       ROUND(AVG(f.rating), 2) AS avg_rating,
       COUNT(f.feedback_id)    AS feedback_count
FROM   Events   e
JOIN   Feedback f ON f.event_id = e.event_id
GROUP  BY e.event_id, e.title
HAVING COUNT(f.feedback_id) >= 10
ORDER  BY avg_rating DESC;

-- ------------------------------------------------------------

-- Exercise 4: Peak Session Hours
-- Sessions scheduled between 10 AM and 12 PM per event.
-- Note: strftime('%H') is SQLite syntax; use HOUR() in MySQL.
SELECT e.event_id, e.title,
       COUNT(s.session_id) AS peak_hour_sessions
FROM   Events   e
JOIN   Sessions s ON s.event_id = e.event_id
WHERE  CAST(strftime('%H', s.start_time) AS INTEGER) >= 10
  AND  CAST(strftime('%H', s.start_time) AS INTEGER) <  12
GROUP  BY e.event_id, e.title;

-- ------------------------------------------------------------

-- Exercise 5: Most Active Cities
-- Top 5 cities by distinct user registrations.
SELECT u.city,
       COUNT(DISTINCT r.user_id) AS distinct_registrations
FROM   Users         u
JOIN   Registrations r ON r.user_id = u.user_id
GROUP  BY u.city
ORDER  BY distinct_registrations DESC
LIMIT  5;

-- ------------------------------------------------------------

-- Exercise 6: Event Resource Summary
-- Number of PDFs, images, and links uploaded per event.
SELECT e.event_id, e.title,
       SUM(CASE WHEN r.resource_type = 'pdf'   THEN 1 ELSE 0 END) AS pdf_count,
       SUM(CASE WHEN r.resource_type = 'image' THEN 1 ELSE 0 END) AS image_count,
       SUM(CASE WHEN r.resource_type = 'link'  THEN 1 ELSE 0 END) AS link_count,
       COUNT(r.resource_id)                                        AS total_resources
FROM   Events    e
LEFT JOIN Resources r ON r.event_id = e.event_id
GROUP  BY e.event_id, e.title;

-- ------------------------------------------------------------

-- Exercise 13: Average Rating per City
-- Average feedback rating of events conducted in each city.
SELECT e.city,
       ROUND(AVG(f.rating), 2) AS avg_rating
FROM   Events   e
JOIN   Feedback f ON f.event_id = e.event_id
GROUP  BY e.city
ORDER  BY avg_rating DESC;

-- ------------------------------------------------------------

-- Exercise 14: Most Registered Events
-- Top 3 events by total registration count.
SELECT e.event_id, e.title,
       COUNT(r.registration_id) AS total_registrations
FROM   Events        e
JOIN   Registrations r ON r.event_id = e.event_id
GROUP  BY e.event_id, e.title
ORDER  BY total_registrations DESC
LIMIT  3;

-- ------------------------------------------------------------

-- Exercise 17: Multi-Session Speakers
-- Speakers handling more than one session across all events.
SELECT speaker_name,
       COUNT(session_id) AS session_count
FROM   Sessions
GROUP  BY speaker_name
HAVING COUNT(session_id) > 1
ORDER  BY session_count DESC;

-- ------------------------------------------------------------

-- Exercise 21: Top Feedback Providers
-- Top 5 users by number of feedback entries submitted.
SELECT u.user_id, u.full_name,
       COUNT(f.feedback_id) AS feedback_count
FROM   Users    u
JOIN   Feedback f ON f.user_id = u.user_id
GROUP  BY u.user_id, u.full_name
ORDER  BY feedback_count DESC
LIMIT  5;

-- ------------------------------------------------------------

-- Exercise 24: Average Session Duration per Event
-- Average duration (in minutes) of sessions in each event.
-- Note: julianday() is SQLite; use TIMESTAMPDIFF(MINUTE,...) in MySQL.
SELECT e.event_id, e.title,
       ROUND(AVG(
           (julianday(s.end_time) - julianday(s.start_time)) * 24 * 60
       ), 2) AS avg_duration_minutes
FROM   Events   e
JOIN   Sessions s ON s.event_id = e.event_id
GROUP  BY e.event_id, e.title;
