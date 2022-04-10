CREATE TABLE IF NOT EXISTS offers (
    id                              SERIAL PRIMARY KEY, 
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