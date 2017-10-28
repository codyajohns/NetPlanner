CREATE TABLE users (
	id integer PRIMARY KEY AUTOINCREMENT,
	username varchar,
	password varchar
);

CREATE TABLE events (
	id integer PRIMARY KEY AUTOINCREMENT,
	title varchar,
	description varchar,
	start_time datetime,
	end_time datetime,
	reminder boolean,
	color integer
);

CREATE TABLE notes (
	id integer PRIMARY KEY AUTOINCREMENT,
	title varchar,
	description varchar,
	color integer
);

CREATE TABLE user_events (
	id integer PRIMARY KEY AUTOINCREMENT,
	user integer,
	event integer
);

CREATE TABLE user_notes (
	id integer PRIMARY KEY AUTOINCREMENT,
	user integer,
	notes integer
);

CREATE TABLE colors (
	id integer PRIMARY KEY AUTOINCREMENT,
	name varchar
);

