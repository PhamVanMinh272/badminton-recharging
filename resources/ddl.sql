CREATE TABLE IF NOT EXISTS player (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    weight REAL NOT NULL DEFAULT 1.0
);

CREATE TABLE IF NOT EXISTS template (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    rental_cost REAL NOT NULL DEFAULT 0.0,
    shuttle_amount INTEGER NOT NULL DEFAULT 0,
    shuttle_price REAL NOT NULL DEFAULT 0.0,
    billing_type_id INTEGER NOT NULL,
    day_index INTEGER NOT NULL,
    shift_time TEXT NOT NULL,
    location TEXT NOT NULL,
    FOREIGN KEY (billing_type_id) REFERENCES billing_type(id)
);

CREATE TABLE IF NOT EXISTS template_player (
    template_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (template_id) REFERENCES templates(id)
);

CREATE TABLE IF NOT EXISTS billing_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS practice_session (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    session_date DATETIME NOT NULL,
    shift_time TEXT NOT NULL,
    location TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS practice_session_player (
    practice_session_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (practice_session_id) REFERENCES practice_sessions(id)
);

CREATE TABLE IF NOT EXISTS bill (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    practice_session_id INTEGER NOT NULL,
    expense_date DATETIME NOT NULL,
    rental_cost REAL NOT NULL DEFAULT 0.0,
    shuttle_amount INTEGER NOT NULL DEFAULT 0,
    shuttle_price REAL NOT NULL DEFAULT 0.0,
    billing_type_id INTEGER NOT NULL,
    FOREIGN KEY (billing_type_id) REFERENCES billing_type(id)
);

CREATE TABLE IF NOT EXISTS bill_share (
    bill_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    amount REAL NOT NULL DEFAULT 0.0,
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (bill_id) REFERENCES bills(id)
);
