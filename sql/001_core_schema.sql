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

CREATE TABLE sales (
    ticket_id TEXT PRIMARY KEY,
    location_id TEXT NOT NULL REFERENCES locations(location_id),
    channel TEXT NOT NULL CHECK (channel IN ('in_store', 'online')),
    sold_at TIMESTAMPTZ NOT NULL,
    recorded_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE sale_lines (
    ticket_id TEXT NOT NULL REFERENCES sales(ticket_id),
    line_no INT NOT NULL,
    sku TEXT NOT NULL REFERENCES products(sku),
    quantity INT NOT NULL CHECK (quantity > 0),
    discount NUMERIC NOT NULL DEFAULT 0,
    unit_price NUMERIC(10,2) NOT NULL,
    unit_cost NUMERIC(10,2) NOT NULL,
    PRIMARY KEY(ticket_id, line_no)
);

COMMIT;