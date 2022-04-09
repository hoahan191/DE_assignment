import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_orders_table_drop = "DROP TABLE IF EXISTS staging_orders;"
staging_deals_table_drop = "DROP TABLE IF EXISTS staging_deals;"
staging_invites_table_drop = "DROP TABLE IF EXISTS staging_invites;"
staging_offers_table_drop = "DROP TABLE IF EXISTS staging_offers;"
orders_table_drop = "DROP TABLE IF EXISTS orders;"
deals_table_drop = "DROP TABLE IF EXISTS deals;"
invites_table_drop = "DROP TABLE IF EXISTS invites;"
offers_table_drop = "DROP TABLE IF EXISTS offers;"


# CREATE TABLES

staging_orders_table_create= ("""
CREATE TABLE IF NOT EXISTS staging_orders (
    order_id                        int,
    deal_id                         int,
    order_created_at                timestamp,   
    order_placed_at                 timestamp, 
    order_quantity_kg               decimal(18, 1),
    ordering_user_id                int,
    order_price_kg_nationalcurrency decimal(18, 6)
)
diststyle auto
sortkey auto;
""")

staging_deals_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_deals (
    dead_id                         int,
    invite_id                       int,
    deal_created_at                 timestamp,
    deal_status                     varchar(50),
    deal_material_id                int,
    deal_quantity_kg                decimal(18, 1),
    deal_price_kg_nationalcurrency  decimal(18, 2),
    deal_valid_from                 timestamp,
    deal_valid_to                   timestamp
)
diststyle auto
sortkey auto;
""")

staging_invites_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_invites (
    invite_id                       int,
    offer_id                        int,
    invite_created_at               timestamp,
    invite_invitation_state         varchar(50),
    invite_state                    varchar(50),
    invite_first_viewed_at          timestamp,
    invite_material_id              int,
    invite_min_deal_quantity_kg     decimal(18, 1),
    invite_max_deal_quantity_kg     decimal(18, 1),
    selling_company_id	            int,
    buying_org_id                   int
)
diststyle auto
sortkey auto;
""")

staging_offers_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_offers (
    offer_id                        int,
    offer_created_at                timestamp,
    offer_valid_from                timestamp,
    offer_valid_until               timestamp,
    offer_state                     varchar(50),
    offer_national_currency         varchar(50),
    offer_total_quantity_kg         decimal(18, 1),
    transaction_type	            varchar(50),
    seller_user_id                  int,
    unit_price_nationalcurrency     decimal(18, 6)
)
diststyle auto
sortkey auto;
""")

orders_table_create = ("""
CREATE TABLE IF NOT EXISTS orders (
    order_id                        int     NOT NULL PRIMARY KEY,
    deal_id                         int,
    order_created_at                timestamp,   
    order_placed_at                 timestamp, 
    order_quantity_kg               decimal(18, 1),
    ordering_user_id                int,
    order_price_kg_nationalcurrency decimal(18, 6)
)
diststyle all
sortkey(deal_id);
""")

deals_table_create = ("""
CREATE TABLE IF NOT EXISTS deals (
    dead_id                         int     NOT NULL PRIMARY KEY,
    invite_id                       int,
    deal_created_at                 timestamp,
    deal_status                     varchar(50),
    deal_material_id                int,
    deal_quantity_kg                decimal(18, 1),
    deal_price_kg_nationalcurrency  decimal(18, 2),
    deal_valid_from                 timestamp,
    deal_valid_to                   timestamp
)
diststyle all
sortkey(invite_id);
""")

invites_table_create = ("""
CREATE TABLE IF NOT EXISTS invites (
    invite_id                       int     NOT NULL PRIMARY KEY,
    offer_id                        int,
    invite_created_at               timestamp,
    invite_invitation_state         varchar(50),
    invite_state                    varchar(50),
    invite_first_viewed_at          timestamp,
    invite_material_id              int,
    invite_min_deal_quantity_kg     decimal(18, 1),
    invite_max_deal_quantity_kg     decimal(18, 1),
    selling_company_id	            int,
    buying_org_id                   int
)
diststyle all
sortkey(deal_id);
""")

offers_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    offer_id                        int     NOT NULL PRIMARY KEY,
    offer_created_at                timestamp,
    offer_valid_from                timestamp,
    offer_valid_until               timestamp,
    offer_state                     varchar(50),
    offer_national_currency         varchar(50),
    offer_total_quantity_kg         decimal(18, 1),
    transaction_type	            varchar(50),
    seller_user_id                  int,
    unit_price_nationalcurrency     decimal(18, 6)
)
diststyle all
sortkey(offer_id);
""")

# STAGING TABLES

staging_orders_copy = ("""
COPY staging_orders
FROM {0}
iam_role {1}
region 'us-west-2'
json {2}
BLANKSASNULL
EMPTYASNULL
TRUNCATECOLUMNS
""").format(config['S3']['LOG_DATA'], config['IAM_ROLE']['ARN'], config['S3']['LOG_JSONPATH'])

staging_deals_copy = ("""
COPY staging_deals
FROM {0}
iam_role {1}
region 'us-west-2'
json 'auto'
BLANKSASNULL
EMPTYASNULL
TRUNCATECOLUMNS
""").format(config['S3']['SONG_DATA'], config['IAM_ROLE']['ARN'])

staging_invites_copy = ("""
COPY staging_invites
FROM {0}
iam_role {1}
region 'us-west-2'
json 'auto'
BLANKSASNULL
EMPTYASNULL
TRUNCATECOLUMNS
""").format(config['S3']['SONG_DATA'], config['IAM_ROLE']['ARN'])

staging_offers_copy = ("""
COPY staging_offers
FROM {0}
iam_role {1}
region 'us-west-2'
json 'auto'
BLANKSASNULL
EMPTYASNULL
TRUNCATECOLUMNS
""").format(config['S3']['SONG_DATA'], config['IAM_ROLE']['ARN'])

# FINAL TABLES

songplay_table_insert = ("""
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
SELECT DISTINCT timestamp 'epoch' + ts / 1000 * interval '1 second' AS start_time,
                user_id,
                level,
                song_id,
                artist_id,
                session_id,
                location,
                user_agent
           FROM staging_events, staging_songs
          WHERE staging_events.song = staging_songs.title
            AND staging_events.artist = staging_songs.artist_name
            AND user_id IS NOT NULL
            AND song_id IS NOT NULL
            AND artist_id IS NOT NULL
            AND ts IS NOT NULL
            AND staging_events.length IS NOT NULL
            AND staging_events.length = staging_songs.duration
            AND staging_events.page = 'NextSong';
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
SELECT DISTINCT user_id, first_name, last_name, gender, level
           FROM staging_events
          WHERE user_id IS NOT NULL 
            AND first_name IS NOT NULL
            AND last_name IS NOT NULL
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
SELECT DISTINCT song_id, title, artist_id, year, duration
           FROM staging_songs
          WHERE song_id IS NOT NULL
            AND title IS NOT NULL
            AND duration IS NOT NULL;
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, lattitude, longitude)
SELECT DISTINCT artist_id, artist_name, artist_location, artist_latitude, artist_longitude
           FROM staging_songs
          WHERE artist_id IS NOT NULL
            AND artist_name IS NOT NULL;
""")

time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
SELECT DISTINCT timestamp 'epoch' + ts / 1000 * interval '1 second' AS start_time,
                extract(hour from (timestamp 'epoch' + ts / 1000 * interval '1 second')),
                extract(day from (timestamp 'epoch' + ts / 1000 * interval '1 second')),
                extract(week from (timestamp 'epoch' + ts / 1000 * interval '1 second')),
                extract(month from (timestamp 'epoch' + ts / 1000 * interval '1 second')),
                extract(year from (timestamp 'epoch' + ts / 1000 * interval '1 second')),
                extract(weekday from (timestamp 'epoch' + ts / 1000 * interval '1 second'))
           FROM staging_events
          WHERE ts IS NOT NULL;
""")

# QUERY LISTS

create_table_queries = [staging_orders_table_create, staging_deals_table_create, staging_invites_table_create, staging_offers_table_create, orders_table_create, deals_table_create, invites_table_create, offers_table_create, time_table_create]
drop_table_queries = [staging_orders_table_drop, staging_deals_table_drop, staging_invites_table_drop, staging_offers_table_drop, orders_table_drop, deals_table_drop, invites_table_drop, offers_table_drop]
copy_table_queries = [staging_orders_copy, staging_deals_copy, staging_invites_copy, staging_offers_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
