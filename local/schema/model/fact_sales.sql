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