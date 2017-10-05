create table users(
	id serial,
	login varchar(15) unique,
	full_name varchar(20),
	hobby varchar(15),
	password varchar(256)
		);
