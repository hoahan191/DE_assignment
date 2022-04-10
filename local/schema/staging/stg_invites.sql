CREATE TABLE IF NOT EXISTS invites (
    id                              SERIAL PRIMARY KEY, 
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