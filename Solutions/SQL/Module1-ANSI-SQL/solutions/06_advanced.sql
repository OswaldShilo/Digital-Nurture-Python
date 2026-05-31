-- ============================================================
-- Module 1 | Topic: Advanced Queries
-- Exercises: 15 (self-join), 19, 20
-- ============================================================

-- Exercise 15: Event Session Time Conflict
-- Pairs of sessions within the same event whose times overlap.
SELECT s1.event_id,
       s1.session_id AS session_a, s1.title AS title_a,
       s1.start_time AS start_a,  s1.end_time AS end_a,
       s2.session_id AS session_b, s2.title AS title_b,
       s2.start_time AS start_b,  s2.end_time AS end_b
FROM   Sessions s1
JOIN   Sessions s2
  ON   s1.event_id   = s2.event_id
 AND   s1.session_id < s2.session_id
 AND   s1.start_time < s2.end_time
 AND   s1.end_time   > s2.start_time;

-- ------------------------------------------------------------

-- Exercise 19: Completed Events with Feedback Summary
-- For completed events: total registrations and average feedback rating.
SELECT e.event_id, e.title,
       COUNT(DISTINCT r.registration_id) AS total_registrations,
       ROUND(AVG(f.rating), 2)           AS avg_rating
FROM   Events e
LEFT JOIN Registrations r ON r.event_id = e.event_id
LEFT JOIN Feedback      f ON f.event_id = e.event_id
WHERE  e.status = 'completed'
GROUP  BY e.event_id, e.title;

-- ------------------------------------------------------------

-- Exercise 20: User Engagement Index
-- For each user: events registered and feedbacks submitted.
SELECT u.user_id, u.full_name,
       COUNT(DISTINCT r.event_id)    AS events_registered,
       COUNT(DISTINCT f.feedback_id) AS feedbacks_submitted
FROM   Users u
LEFT JOIN Registrations r ON r.user_id = u.user_id
LEFT JOIN Feedback      f ON f.user_id = u.user_id
GROUP  BY u.user_id, u.full_name
ORDER  BY events_registered DESC, feedbacks_submitted DESC;
