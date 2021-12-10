create table if not exists genre (
	id_genre serial primary key,
	name varchar(30) not null unique
);
create table if not exists nickname (
	id_nick serial primary key,
	name varchar(30) unique,
	id_genre integer references genre(id_genre)
);
create table if not exists artist (
	id_artist serial primary key,
	name varchar(30) NOT NULL unique,
	id_nick integer references nickname(id_nick)
);
create table if not exists genre_nickname (
	id serial primary key,
	id_genre integer not null references genre(id_genre),
	id_nick integer not null references nickname(id_nick)
);
create table if not exists album (
	id_album serial primary key,
	name varchar(30) not null,
	release_year date not null,
	id_nick integer references nickname(id_nick),
	id_genre integer references genre(id_genre)
);
create table if not exists album_nickname (
	id  serial primary key,
	id_nick integer not null references nickname(id_nick),
	id_album integer not null references album(id_album),
	id_genre integer references genre(id_genre)
);
create table if not exists track (
	id_track serial primary key,
	name varchar(30) not null,
	track_length numeric(3,2) not null,
	id_album integer references album(id_album),
	id_nick integer references nickname(id_nick),
	id_genre integer references genre(id_genre)	 
);
create table if not exists collection (
	id_collection serial primary key,
	name varchar(30) not null,
	release_year integer not null,
	id_nick integer references nickname(id_nick)
);
create table if not exists collections_album_track (
	id serial primary key,
	id_collection integer not null references collection(id_collection),
	id_album integer not null references album(id_album),
	id_track integer not null references track(id_track),
	id_nick integer references nickname(id_nick)
);