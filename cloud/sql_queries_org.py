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

offers_table_insert = ("""
SELECT DISTINCT offer_id, title, artist_id, year, duration
           FROM staging_songs
          WHERE song_id IS NOT NULL
            AND title IS NOT NULL
            AND duration IS NOT NULL;
""")