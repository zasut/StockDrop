BEGIN;

CREATE TYPE location_t AS ENUM ('warehouse', 'store', 'online');

CREATE TABLE locations (
    location_id TEXT PRIMARY KEY,
    location_name TEXT NOT NULL,
    location_type location_t NOT NULL
);


CREATE TABLE products (
    sku TEXT PRIMARY KEY,
    product_name TEXT NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL CHECK (unit_price >= 0),
    unit_cost NUMERIC(10,2) NOT NULL CHECK (unit_cost >= 0),
    category TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

COMMIT;