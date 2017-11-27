DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id integer PRIMARY KEY AUTOINCREMENT,
	username varchar,
	password varchar
);

DROP TABLE IF EXISTS events;
CREATE TABLE events (
	id integer PRIMARY KEY AUTOINCREMENT,
	title varchar,
	description varchar,
	start_time datetime,
	end_time datetime,
	reminder boolean,
	color integer
);

DROP TABLE IF EXISTS notes;
CREATE TABLE notes (
	id integer PRIMARY KEY AUTOINCREMENT,
	title varchar,
	description varchar,
	color integer
);

DROP TABLE IF EXISTS user_events;
CREATE TABLE user_events (
	id integer PRIMARY KEY AUTOINCREMENT,
	user integer,
	event integer
);

DROP TABLE IF EXISTS user_notes;
CREATE TABLE user_notes (
	id integer PRIMARY KEY AUTOINCREMENT,
	user integer,
	notes integer
);

DROP TABLE IF EXISTS colors;
CREATE TABLE colors (
	id integer PRIMARY KEY AUTOINCREMENT,
	name varchar
);

