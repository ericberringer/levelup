CREATE VIEW EVENTS_BY_USER AS
SELECT 
    e.id event_id,
    e.date,
    e.time,
    e.event_name,
    gr.id gamer_id,
    g.title,
    u.id user_id,
    u.first_name || ' ' || u.last_name AS full_name
FROM 
    levelupapi_event e
JOIN 
    levelupapi_gamer gr ON gr.id = e.organizer_id
JOIN 
    levelupapi_game g ON g.id = e.game_id
JOIN 
    auth_user u ON u.id = gr.user_id