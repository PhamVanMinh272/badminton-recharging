-- Name is unique to avoid duplicate
INSERT INTO player (id, name, weight) VALUES (1, 'Giao', 0.8);
INSERT INTO player (id, name, weight) VALUES (2, 'C Ân', 0.8);
INSERT INTO player (id, name, weight) VALUES (3, 'Minh', 1);
INSERT INTO player (id, name, weight) VALUES (4, 'Đạt', 1);
INSERT INTO player (id, name, weight) VALUES (5, 'Thảo', 1);
INSERT INTO player (id, name, weight) VALUES (6, 'Tú', 1);
INSERT INTO player (id, name, weight) VALUES (7, 'Văn', 1);
INSERT INTO player (id, name, weight) VALUES (8, 'Tuyến', 1);
INSERT INTO player (id, name, weight) VALUES (9, 'Thịnh', 1);
INSERT INTO player (id, name, weight) VALUES (10, 'Thoại', 1);
INSERT INTO player (id, name, weight) VALUES (11, 'Toàn', 1);
INSERT INTO player (id, name, weight) VALUES (12, 'Thiên', 1);
INSERT INTO player (id, name, weight) VALUES (13, 'Tâm', 1);
INSERT INTO player (id, name, weight) VALUES (14, 'Tấn', 1);
INSERT INTO player (id, name, weight) VALUES (15, 'Thanh', 1);

-- Name is unique to avoid duplicate
INSERT INTO billing_type (id, name) VALUES (1, 'Equally');
INSERT INTO billing_type (id, name) VALUES (2, 'Weight');
INSERT INTO billing_type (id, name) VALUES (3, 'Custom');

-- Name is unique to avoid duplicate
INSERT INTO template (name, billing_type_id, rental_cost, shuttleAmount, shuttlePrice) VALUES ('Wednesday', 1, 220, 4, 310);
INSERT INTO template (name, billing_type_id, rental_cost, shuttleAmount, shuttlePrice) VALUES ('Friday', 2, 280, 4, 310);
INSERT INTO template (name, billing_type_id, rental_cost, shuttleAmount, shuttlePrice) VALUES ('Sunday', 1, 200, 4, 310);

-- Link players to templates
INSERT INTO template_player (template_id, player_id) VALUES (1, 3);
INSERT INTO template_player (template_id, player_id) VALUES (1, 4);
INSERT INTO template_player (template_id, player_id) VALUES (1, 5);
INSERT INTO template_player (template_id, player_id) VALUES (1, 6);
INSERT INTO template_player (template_id, player_id) VALUES (1, 7);
INSERT INTO template_player (template_id, player_id) VALUES (1, 9);

INSERT INTO template_player (template_id, player_id) VALUES (2, 3);
INSERT INTO template_player (template_id, player_id) VALUES (2, 4);
INSERT INTO template_player (template_id, player_id) VALUES (2, 10);
INSERT INTO template_player (template_id, player_id) VALUES (2, 11);
INSERT INTO template_player (template_id, player_id) VALUES (2, 12);
INSERT INTO template_player (template_id, player_id) VALUES (2, 13);
INSERT INTO template_player (template_id, player_id) VALUES (2, 14);
INSERT INTO template_player (template_id, player_id) VALUES (2, 15);
INSERT INTO template_player (template_id, player_id) VALUES (2, 1);
INSERT INTO template_player (template_id, player_id) VALUES (2, 2);

INSERT INTO template_player (template_id, player_id) VALUES (1, 3);
INSERT INTO template_player (template_id, player_id) VALUES (1, 4);
INSERT INTO template_player (template_id, player_id) VALUES (1, 5);
INSERT INTO template_player (template_id, player_id) VALUES (1, 6);
INSERT INTO template_player (template_id, player_id) VALUES (1, 7);
INSERT INTO template_player (template_id, player_id) VALUES (1, 8);
INSERT INTO template_player (template_id, player_id) VALUES (1, 9);
