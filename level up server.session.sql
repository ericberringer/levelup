SELECT 
    e.id EventId,
    e.date EventDate,
    e.event_name EventName,
    e.time EventTime,
    gr.id GamerId,
    g.title GameName,
    u.id user_id,
    u.first_name || ' ' || u.last_name AS FullName
    FROM 
        levelupapi_event e
    JOIN 
        levelupapi_gamer gr ON gr.id = e.id
    JOIN 
        levelupapi_game g ON g.id = e.game_id
    JOIN 
        auth_user u ON u.id = gr.user_id