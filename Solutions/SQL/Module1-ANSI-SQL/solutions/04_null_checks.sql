-- ============================================================
-- Module 1 | Topic: NULL Checks (LEFT JOIN … IS NULL)
-- Exercises: 10, 18, 25
-- ============================================================

-- Exercise 10: Feedback Gap
-- Events that had registrations but received no feedback at all.
SELECT e.event_id, e.title,
       COUNT(DISTINCT r.registration_id) AS total_registrations
FROM   Events        e
JOIN   Registrations r  ON r.event_id = e.event_id
LEFT JOIN Feedback   f  ON f.event_id = e.event_id
WHERE  f.feedback_id IS NULL
GROUP  BY e.event_id, e.title;

-- ------------------------------------------------------------

-- Exercise 18: Resource Availability Check
-- Events that have no resources uploaded.
SELECT e.event_id, e.title
FROM   Events e
LEFT JOIN Resources r ON r.event_id = e.event_id
WHERE  r.resource_id IS NULL;

-- ------------------------------------------------------------

-- Exercise 25: Events Without Sessions
-- Events that currently have no sessions scheduled.
SELECT e.event_id, e.title, e.status
FROM   Events e
LEFT JOIN Sessions s ON s.event_id = e.event_id
WHERE  s.session_id IS NULL;
