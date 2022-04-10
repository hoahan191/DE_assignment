-- Create schema staging with 4 tables
CREATE SCHEMA IF NOT EXISTS staging 
    CREATE TABLE IF NOT EXISTS staging_orders(
        order_id                        int,
        deal_id                         int,
        order_created_at                timestamp,   
        order_placed_at                 timestamp, 
        order_quantity_kg               decimal(18, 1),
        ordering_user_id                int,
        order_price_kg_nationalcurrency decimal(18, 6)
    )
    CREATE TABLE IF NOT EXISTS staging_deals(
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
    