
# DROP TABLES

staging_orders_table_drop = "DROP TABLE IF EXISTS staging_orders;"
staging_deals_table_drop = "DROP TABLE IF EXISTS staging_deals;"
staging_invites_table_drop = "DROP TABLE IF EXISTS staging_invites;"
staging_offers_table_drop = "DROP TABLE IF EXISTS staging_offers;"
fact_sales_table_drop = "DROP TABLE IF EXISTS fact_sales;"
dim_date_table_drop = "DROP TABLE IF EXISTS dim_date;"

# CREATE STAGING TABLES

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
""")

# CREATE DATA WAREHOUSE (DW) TABLES
fact_sales_table_create = ("""
CREATE TABLE IF NOT EXISTS fact_sales (
    sales_id            int IDENTITY(0, 1) PRIMARY KEY,
    sales_date          date,
    sales_quantity_kg   decimal(18, 1),   
    material_id         int, 
    sales_stage         varchar(10),
    order_price         decimal(18, 6),
    deal_price          decimal(18, 2),
    offer_price         decimal(18, 6)
    currency            varchar(10),
    sales_status        varchar(50)
)
""")

dim_date_table_create = ("""
CREATE TABLE IF NOT EXISTS deals (
    deal_id                         int     NOT NULL PRIMARY KEY,
    invite_id                       int,
    deal_created_at                 timestamp,
    deal_status                     varchar(50),
    deal_material_id                int,
    deal_quantity_kg                decimal(18, 1),
    deal_price_kg_nationalcurrency  decimal(18, 2),
    deal_valid_from                 timestamp,
    deal_valid_to                   timestamp
)
""")

# QUERY LISTS
create_table_queries = [staging_orders_table_create, staging_deals_table_create, staging_invites_table_create, staging_offers_table_create, fact_sales_table_create, dim_date_table_create]
drop_table_queries = [staging_orders_table_drop, staging_deals_table_drop, staging_invites_table_drop, staging_offers_table_drop, fact_sales_table_drop, dim_date_table_drop]