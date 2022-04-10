
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

# CREATE TABLES
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
CREATE TABLE IF NOT EXISTS dim_date (
    date                         int     NOT NULL PRIMARY KEY,
    week                       int,
    month                timestamp,
    quarter                     varchar(50),
    year                int,
    weekdat                decimal(18, 1),
)
""")


# FIND SONGS
fact_sales_data_query = (""" SELECT --sales_id,
	                                ofs.offer_id as sales_key,
	                                TO_DATE(order_created_at date) as sales_date, -- Datetime to Date
	                                order_quantity_kg as sales_quantity,
	                                offer_national_currency as material_id,
	                                CASE 
		                                WHEN ord.deal_id not null THEN "ORDER" --- ???
		                                WHEN invite_state not null THEN 'INVITE'
		                                WHEN deal_status not null THEN 'DEAL'
		                                WHEN offer_state not null THEN 'OFFER'
		                                ELSE NULL
	                                END as sales_stage,
	                                order_price_kg_nationalcurrency as order_price,
	                                deal_price_kg_nationalcurrency as deal_price,
	                                unit_price_nationalcurrency as offer_price,
	                                offer_national_currency as currency,
	                                CASE 
		                                WHEN ord.deal_id not null THEN "ORDER" --- ??? NULL
		                                WHEN invite_state not null THEN CONCAT('INVITE_', invite_state)
		                                WHEN deal_status not null THEN CONCAT('DEAL_', deal_status)
		                                WHEN offer_state not null THEN CONCAT('OFFER_', offer_state)
		                                ELSE NULL
	                                END as sales_status
                            FROM public.offers ofs 
                            LEFT JOIN public.invites ivt on ofs.offer_id = ivt.offer_id
                            LEFT JOIN public.deals dls on ivt.invite_id = dls.invite_id
                            LEFT JOIN public.orders ord on dls.deal_id = ord.deal_id
                        """)


# INSERT RECORDS
fact_sales_table_insert = ("INSERT INTO fact_sales\n" + fact_sales_data_query)
dim_date_table_insert = ()

# QUERY LISTS
create_table_queries = [staging_orders_table_create, staging_deals_table_create, staging_invites_table_create, staging_offers_table_create, fact_sales_table_create, dim_date_table_create]
drop_table_queries = [staging_orders_table_drop, staging_deals_table_drop, staging_invites_table_drop, staging_offers_table_drop, fact_sales_table_drop, dim_date_table_drop]