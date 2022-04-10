CREATE TABLE IF NOT EXISTS orders (
    id                              SERIAL PRIMARY KEY, 
    order_id                        int,
    deal_id                         int,
    order_created_at                timestamp,   
    order_placed_at                 timestamp, 
    order_quantity_kg               decimal(18, 1),
    ordering_user_id                int,
    order_price_kg_nationalcurrency decimal(18, 6)
)