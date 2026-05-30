-- ============================================================
-- ANSI SQL Using MySQL - Module 1 | 25 Exercises
-- Database: event_management
-- ============================================================

USE event_management;

-- ------------------------------------------------------------
-- Exercise 1: User Upcoming Events
-- Show all upcoming events a user is registered for in their
-- city, sorted by event start date.
-- ------------------------------------------------------------
SELECT
    u.user_id,
    u.full_name,
    e.title        AS event_title,
    e.city,
    e.start_date
FROM Users u
JOIN Registrations r ON r.user_id  = u.user_id
JOIN Events        e ON e.event_id = r.event_id
WHERE e.status = 'upcoming'
  AND e.city   = u.city
ORDER BY e.start_date;

-- ------------------------------------------------------------
-- Exercise 2: Top Rated Events
-- Events with highest average rating having at least 10
-- feedback submissions.
-- ------------------------------------------------------------
SELECT
    e.event_id,
    e.title,
    AVG(f.rating)      AS avg_rating,
    COUNT(f.feedback_id) AS feedback_count
FROM Events   e
JOIN Feedback f ON f.event_id = e.event_id
GROUP BY e.event_id, e.title
HAVING COUNT(f.feedback_id) >= 10
ORDER BY avg_rating DESC;

-- ------------------------------------------------------------
-- Exercise 3: Inactive Users
-- Users who have not registered for any event in the last
-- 90 days.
-- ------------------------------------------------------------
SELECT
    u.user_id,
    u.full_name,
    u.email
FROM Users u
WHERE u.user_id NOT IN (
    SELECT r.user_id
    FROM   Registrations r
    WHERE  r.registration_date >= CURDATE() - INTERVAL 90 DAY
);

-- ------------------------------------------------------------
-- Exercise 4: Peak Session Hours
-- Count of sessions scheduled between 10 AM and 12 PM
-- for each event.
-- ------------------------------------------------------------
SELECT
    e.event_id,
    e.title,
    COUNT(s.session_id) AS peak_hour_sessions
FROM Events   e
JOIN Sessions s ON s.event_id = e.event_id
WHERE HOUR(s.start_time) >= 10
  AND HOUR(s.start_time) <  12
GROUP BY e.event_id, e.title;

-- ------------------------------------------------------------
-- Exercise 5: Most Active Cities
-- Top 5 cities with the highest distinct user registrations.
-- ------------------------------------------------------------
SELECT
    u.city,
    COUNT(DISTINCT r.user_id) AS distinct_registrations
FROM Users         u
JOIN Registrations r ON r.user_id = u.user_id
GROUP BY u.city
ORDER BY distinct_registrations DESC
LIMIT 5;

-- ------------------------------------------------------------
-- Exercise 6: Event Resource Summary
-- Number of PDFs, images, and links uploaded per event.
-- ------------------------------------------------------------
SELECT
    e.event_id,
    e.title,
    SUM(CASE WHEN r.resource_type = 'pdf'   THEN 1 ELSE 0 END) AS pdf_count,
    SUM(CASE WHEN r.resource_type = 'image' THEN 1 ELSE 0 END) AS image_count,
    SUM(CASE WHEN r.resource_type = 'link'  THEN 1 ELSE 0 END) AS link_count,
    COUNT(r.resource_id)                                        AS total_resources
FROM Events    e
LEFT JOIN Resources r ON r.event_id = e.event_id
GROUP BY e.event_id, e.title;

-- ------------------------------------------------------------
-- Exercise 7: Low Feedback Alerts
-- Users who gave a rating less than 3, with their comments
-- and the associated event name.
-- ------------------------------------------------------------
SELECT
    u.user_id,
    u.full_name,
    e.title     AS event_title,
    f.rating,
    f.comments,
    f.feedback_date
FROM Feedback f
JOIN Users  u ON u.user_id  = f.user_id
JOIN Events e ON e.event_id = f.event_id
WHERE f.rating < 3;

-- ------------------------------------------------------------
-- Exercise 8: Sessions per Upcoming Event
-- All upcoming events with their session count.
-- ------------------------------------------------------------
SELECT
    e.event_id,
    e.title,
    COUNT(s.session_id) AS session_count
FROM Events e
LEFT JOIN Sessions s ON s.event_id = e.event_id
WHERE e.status = 'upcoming'
GROUP BY e.event_id, e.title;

-- ------------------------------------------------------------
-- Exercise 9: Organizer Event Summary
-- For each organizer, count of events per status.
-- ------------------------------------------------------------
SELECT
    u.user_id     AS organizer_id,
    u.full_name   AS organizer_name,
    e.status,
    COUNT(e.event_id) AS event_count
FROM Users  u
JOIN Events e ON e.organizer_id = u.user_id
GROUP BY u.user_id, u.full_name, e.status
ORDER BY u.user_id, e.status;

-- ------------------------------------------------------------
-- Exercise 10: Feedback Gap
-- Events that had registrations but received no feedback.
-- ------------------------------------------------------------
SELECT
    e.event_id,
    e.title,
    COUNT(DISTINCT r.registration_id) AS total_registrations
FROM Events        e
JOIN Registrations r  ON r.event_id  = e.event_id
LEFT JOIN Feedback f  ON f.event_id  = e.event_id
WHERE f.feedback_id IS NULL
GROUP BY e.event_id, e.title;

-- ------------------------------------------------------------
-- Exercise 11: Daily New User Count
-- Number of users who registered each day in the last 7 days.
-- ------------------------------------------------------------
SELECT
    registration_date,
    COUNT(user_id) AS new_users
FROM Users
WHERE registration_date >= CURDATE() - INTERVAL 7 DAY
GROUP BY registration_date
ORDER BY registration_date;

-- ------------------------------------------------------------
-- Exercise 12: Event with Maximum Sessions
-- Event(s) with the highest number of sessions.
-- ------------------------------------------------------------
SELECT
    e.event_id,
    e.title,
    COUNT(s.session_id) AS session_count
FROM Events   e
JOIN Sessions s ON s.event_id = e.event_id
GROUP BY e.event_id, e.title
HAVING COUNT(s.session_id) = (
    SELECT MAX(cnt)
    FROM (
        SELECT COUNT(session_id) AS cnt
        FROM Sessions
        GROUP BY event_id
    ) AS sub
);

-- ------------------------------------------------------------
-- Exercise 13: Average Rating per City
-- Average feedback rating of events held in each city.
-- ------------------------------------------------------------
SELECT
    e.city,
    ROUND(AVG(f.rating), 2) AS avg_rating
FROM Events   e
JOIN Feedback f ON f.event_id = e.event_id
GROUP BY e.city
ORDER BY avg_rating DESC;

-- ------------------------------------------------------------
-- Exercise 14: Most Registered Events
-- Top 3 events by total registration count.
-- ------------------------------------------------------------
SELECT
    e.event_id,
    e.title,
    COUNT(r.registration_id) AS total_registrations
FROM Events        e
JOIN Registrations r ON r.event_id = e.event_id
GROUP BY e.event_id, e.title
ORDER BY total_registrations DESC
LIMIT 3;

-- ------------------------------------------------------------
-- Exercise 15: Event Session Time Conflict
-- Sessions within the same event whose time ranges overlap.
-- ------------------------------------------------------------
SELECT
    s1.event_id,
    s1.session_id  AS session_a,
    s1.title       AS title_a,
    s1.start_time  AS start_a,
    s1.end_time    AS end_a,
    s2.session_id  AS session_b,
    s2.title       AS title_b,
    s2.start_time  AS start_b,
    s2.end_time    AS end_b
FROM Sessions s1
JOIN Sessions s2
  ON  s1.event_id   = s2.event_id
  AND s1.session_id < s2.session_id
  AND s1.start_time < s2.end_time
  AND s1.end_time   > s2.start_time;

-- ------------------------------------------------------------
-- Exercise 16: Unregistered Active Users
-- Users who signed up in the last 30 days but have not
-- registered for any event.
-- ------------------------------------------------------------
SELECT
    u.user_id,
    u.full_name,
    u.registration_date
FROM Users u
WHERE u.registration_date >= CURDATE() - INTERVAL 30 DAY
  AND u.user_id NOT IN (
      SELECT DISTINCT user_id FROM Registrations
  );

-- ------------------------------------------------------------
-- Exercise 17: Multi-Session Speakers
-- Speakers handling more than one session across all events.
-- ------------------------------------------------------------
SELECT
    speaker_name,
    COUNT(session_id) AS session_count
FROM Sessions
GROUP BY speaker_name
HAVING COUNT(session_id) > 1
ORDER BY session_count DESC;

-- ------------------------------------------------------------
-- Exercise 18: Resource Availability Check
-- Events that have no resources uploaded.
-- ------------------------------------------------------------
SELECT
    e.event_id,
    e.title
FROM Events e
LEFT JOIN Resources r ON r.event_id = e.event_id
WHERE r.resource_id IS NULL;

-- ------------------------------------------------------------
-- Exercise 19: Completed Events with Feedback Summary
-- For completed events: total registrations + average rating.
-- ------------------------------------------------------------
SELECT
    e.event_id,
    e.title,
    COUNT(DISTINCT r.registration_id)  AS total_registrations,
    ROUND(AVG(f.rating), 2)            AS avg_rating
FROM Events e
LEFT JOIN Registrations r ON r.event_id = e.event_id
LEFT JOIN Feedback      f ON f.event_id = e.event_id
WHERE e.status = 'completed'
GROUP BY e.event_id, e.title;

-- ------------------------------------------------------------
-- Exercise 20: User Engagement Index
-- For each user: events registered + feedbacks submitted.
-- ------------------------------------------------------------
SELECT
    u.user_id,
    u.full_name,
    COUNT(DISTINCT r.event_id)    AS events_registered,
    COUNT(DISTINCT f.feedback_id) AS feedbacks_submitted
FROM Users u
LEFT JOIN Registrations r ON r.user_id = u.user_id
LEFT JOIN Feedback      f ON f.user_id = u.user_id
GROUP BY u.user_id, u.full_name
ORDER BY events_registered DESC, feedbacks_submitted DESC;

-- ------------------------------------------------------------
-- Exercise 21: Top Feedback Providers
-- Top 5 users by number of feedback entries submitted.
-- ------------------------------------------------------------
SELECT
    u.user_id,
    u.full_name,
    COUNT(f.feedback_id) AS feedback_count
FROM Users    u
JOIN Feedback f ON f.user_id = u.user_id
GROUP BY u.user_id, u.full_name
ORDER BY feedback_count DESC
LIMIT 5;

-- ------------------------------------------------------------
-- Exercise 22: Duplicate Registrations Check
-- Detect users registered more than once for the same event.
-- ------------------------------------------------------------
SELECT
    user_id,
    event_id,
    COUNT(*) AS registration_count
FROM Registrations
GROUP BY user_id, event_id
HAVING COUNT(*) > 1;

-- ------------------------------------------------------------
-- Exercise 23: Registration Trends
-- Month-wise registration count over the past 12 months.
-- ------------------------------------------------------------
SELECT
    DATE_FORMAT(registration_date, '%Y-%m') AS month,
    COUNT(registration_id)                  AS registrations
FROM Registrations
WHERE registration_date >= CURDATE() - INTERVAL 12 MONTH
GROUP BY DATE_FORMAT(registration_date, '%Y-%m')
ORDER BY month;

-- ------------------------------------------------------------
-- Exercise 24: Average Session Duration per Event
-- Average duration (in minutes) of sessions in each event.
-- ------------------------------------------------------------
SELECT
    e.event_id,
    e.title,
    ROUND(AVG(TIMESTAMPDIFF(MINUTE, s.start_time, s.end_time)), 2) AS avg_duration_minutes
FROM Events   e
JOIN Sessions s ON s.event_id = e.event_id
GROUP BY e.event_id, e.title;

-- ------------------------------------------------------------
-- Exercise 25: Events Without Sessions
-- All events that have no sessions scheduled.
-- ------------------------------------------------------------
SELECT
    e.event_id,
    e.title,
    e.status
FROM Events e
LEFT JOIN Sessions s ON s.event_id = e.event_id
WHERE s.session_id IS NULL;
