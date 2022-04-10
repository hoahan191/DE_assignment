CREATE TABLE IF NOT EXISTS dim_date (
    date                date PRIMARY KEY,
    week                varchar(8),
    month               varchar(5),
    quarter             varchar(2),
    year                int,
    weekdate            varchar(5),
)