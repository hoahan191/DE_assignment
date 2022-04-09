class SqlQueries:
    songplay_table_select = ("""
        SELECT
                md5(events.sessionid || events.start_time) songplay_id,
                events.start_time, 
                events.userid, 
                events.level, 
                songs.song_id, 
                songs.artist_id, 
                events.sessionid, 
                events.location, 
                events.useragent
                FROM (SELECT TIMESTAMP 'epoch' + ts/1000 * interval '1 second' AS start_time, *
            FROM staging_events
            WHERE page='NextSong') events
            LEFT JOIN staging_songs songs
            ON events.song = songs.title
                AND events.artist = songs.artist_name
                AND events.length = songs.duration
    """)

    user_table_select = ("""
        SELECT distinct userid, firstname, lastname, gender, level
        FROM staging_events
        WHERE page='NextSong'
    """)

    song_table_select = ("""
        SELECT distinct song_id, title, artist_id, year, duration
        FROM staging_songs
    """)

    artist_table_select = ("""
        SELECT distinct artist_id, artist_name, artist_location, artist_latitude, artist_longitude
        FROM staging_songs
    """)

    time_table_select = ("""
        SELECT start_time, extract(hour from start_time), extract(day from start_time), extract(week from start_time), 
               extract(month from start_time), extract(year from start_time), extract(dayofweek from start_time)
        FROM songplays
    """)
    
    
    ### SQL for check quality
    
    ### 1. songplays table
    
    # check null data
    songplays_nulls_check = ("""
        SELECT COUNT(*)
        FROM songplays
        WHERE userid IS NULL
              OR songid IS NULL
              OR artistid IS NULL
              OR sessionid IS NULL;
    """)
    
    # count number of data was stored
    songplays_count_check = ("""
        SELECT COUNT(*)
        FROM songplays;
    """)
    
    
    ### 2. users table ###
    
    # check null data
    users_nulls_check = ("""
        SELECT COUNT(*)
        FROM users
        WHERE userid IS NULL;
    """)
    
    # count number of data was stored
    users_count_check = ("""
        SELECT COUNT(*)
        FROM users;
    """)
    
    ### 3. songs table ###
    
    # check null data
    songs_nulls_check = ("""
        SELECT COUNT(*)
        FROM songs
        WHERE songid IS NULL;
    """)
    
    # count number of data was stored
    songs_count_check = ("""
        SELECT COUNT(*)
        FROM songs;
    """)
    
     ### 4. artists table###
    
    # check null data
    artists_nulls_check = ("""
        SELECT COUNT(*)
        FROM artists
        WHERE artistid IS NULL;
    """)
    
    # count number of data was stored
    artists_count_check = ("""
        SELECT COUNT(*)
        FROM artists;
    """)
    
    ### 5. time table###
    
    # check null data
    time_check_nulls = ("""
        SELECT COUNT(*)
        FROM time
        WHERE start_time IS NULL;
    """)
    
    # count number of data was stored
    time_check_count = ("""
        SELECT COUNT(*)
        FROM time;
    """)