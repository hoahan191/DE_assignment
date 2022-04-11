CREATE TABLE IF NOT EXISTS deals (
    id                              SERIAL PRIMARY KEY, 
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