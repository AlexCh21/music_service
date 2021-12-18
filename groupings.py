from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://postgres:user@localhost:5432/database')

connection = engine.connect()

# количество исполнителей в каждом жанре;
count_nickname = connection.execute('''
    SELECT T.title, count(gn.id_nickname)
    FROM genre T
    JOIN  genre_nickname gn ON T.id_track = gn.id_genre
    GROUP BY T.title
    ''').fetchall()

print(f'Количество исполнителей в каждом жанре: {count_nickname}')

# количество треков, вошедших в альбомы 2019-2020 годов;
count_treck_19_20 = connection.execute('''
    SELECT a.title, a.release_year, count(t.id_track)
    FROM album a
    JOIN track t ON a.id_track = t.id_album
    WHERE a.release_year >= 2019 AND a.release_year <= 2020
    GROUP BY a.title, a.release_year
    ''').fetchall()

print(f'Количество треков, вошедших в альбомы 2019-2020 годов;: {count_treck_19_20}')

# средняя продолжительность треков по каждому альбому;

track_length_average = connection.execute('''
    SELECT  a.title, round(AVG(t.track_length), 2)
    FROM album a
    JOIN track t ON a.id = t.id_album
    GROUP BY a.title
    ''').fetchall()

print(f'Cредняя продолжительность треков по каждому альбому: {track_length_average}')

# все исполнители, которые не выпустили альбомы в 2020 году;

album_nickname_not_in_20 = connection.execute('''
    SELECT n.name, a.release_year
    FROM nickname n
    JOIN album_nickname an ON n.id_track = an.id_nick
    JOIN album a ON an.id_album = a.id_track
    WHERE a.release_year != 2020
    ''').fetchall()

print(f'Все исполнители, которые не выпустили альбомы в 2020 году: {album_nicknam_not_in_20}')

# названия сборников, в которых присутствует конкретный исполнитель (выберите сами);

nickname_in_collection = connection.execute('''
    SELECT DISTINCT c.title
    FROM collection c
    JOIN collection_track ct ON c.id = ct.id_collection
    JOIN track t ON ct.id_track = t.id_track
    JOIN album a ON t.id_album = a.id_track
    JOIN album_nickname an ON a.id = an.id_album
    JOIN nickname n ON an.id_nick = n.id_track
    WHERE n.name LIKE 'artist_5'
    ''').fetchall()

print(f'Названия сборников, в которых присутствует конкретный исполнитель ("artist_5"): {nickname_in_collection}')

# название альбомов, в которых присутствуют исполнители более 1 жанра;

album_nickname_genre = connection.execute('''
     SELECT a.title
     FROM album a
     JOIN album_nickname an ON a.id_track = an.id_album
     JOIN nickname n ON an.id_nick = n.id_track
     JOIN genre_nickname gn ON n.id_track = gn.id_nick
     GROUP BY p.name, a.title
     HAVING count(gn.id_genre) > 1
    ''').fetchall()

print(f'Название альбомов, в которых присутствуют исполнители более 1 жанра: {album_nickname_genre}')

# наименование треков, которые не входят в сборники;

not_track = connection.execute('''
    SELECT t.title
    FROM track t
    LEFT JOIN collection_track ct ON t.id_track = ct.id_track
    where ct.id_track IS NULL
    ''').fetchall()

print(f'Наименование треков, которые не входят в сборники: {not_track}')

''' исполнителя(-ей), написавшего самый короткий по продолжительности трек
 (теоретически таких треков может быть несколько);'''

short_length_track = connection.execute('''
    SELECT n.name, t.track_length
    FROM nickname n
    JOIN album_nickname an ON n.id_track = an.id_nick
    JOIN album a ON an.id_album = a.id_track
    JOIN track t ON a.id_track = t.Iid_album
    WHERE t.track_length IN (SELECT MIN(track_length) FROM ttack)
    ''').fetchall()

print(f'Исполнителя(-ей), написавшего самый короткий по продолжительности трек : {short_length_track}')

# название альбомов, содержащих наименьшее количество треков.

the_smallest_track_album = connection.execute('''
    SELECT a.title, count(t.id)
    FROM album a
    JOIN track t  ON a.id_track = t.id_album
    GROUP BY a.title 
    HAVING count(t.id_track) in (
        SELECT count(t.id_track)
        FROM album a
        JOIN track t  ON a.id_track = t.id_album
        GROUP BY a.title
        ORDER BY count(t.id)\
        LIMIT 1)
    ''').fetchall()

print(f'Название альбомов, содержащих наименьшее количество треков : {the_smallest_track_album}')
