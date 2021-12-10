import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:user@localhost:5432/database')

connection = engine.connect()

 1. Название и год выхода альбомов, вышедших в 2018 году;

connection.execute('''SELECT  name, release_yaer FROM album
WHERE release_yaer BETWEEN '2018-01-01' AND '2018-12-31';
''').fetchall()

 2. Название и продолжительность самого длительного трека;

connection.execute('''SELECT   name, track_length FROM track
ORDER BY track_length DESC;
''').fetchone()

 3. Название треков, продолжительность которых не менее 3,5 минуты;

connection.execute('''SELECT  name FROM track
WHERE track_length >= 03.50;
''').fetchall()

 4. Названия сборников, вышедших в период с 2018 по 2020 год включительно;

connection.execute('''SELECT name FROM collection
WHERE release_year BETWEEN '2018-01-01' AND '2020-12-31';
''').fetchall()

 5. Исполнители, чье имя состоит из 1 слова;

connection.execute('''SELECT name FROM nickname
WHERE name NOT LIKE '%% %%';
''').fetchall()

 6. Название треков, которые содержат слово "мой"/"my";

connection.execute('''SELECT name FROM track
WHERE name iLIKE '%%my%%';
''').fetchall()

" 6. Название треков, которые содержат слово "мой"/"my";

connection.execute('''SELECT name FROM track
WHERE name LIKE '%%My%%';
''').fetchall()"
