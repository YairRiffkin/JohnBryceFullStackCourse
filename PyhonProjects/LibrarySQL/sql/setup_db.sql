
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS details;
DROP TABLE IF EXISTS warehouse;
DROP TABLE IF EXISTS movements;

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    value  FLOAT,
    val_unit TEXT NOT NULL
);

CREATE TABLE details (
    id INTEGER PRIMARY KEY,
    detail0 TEXT,
    detail1 TEXT,
    detail2 TEXT,
    detail3 TEXT,
    detail4 TEXT,
    detail5 TEXT,
    detail6 TEXT,
    detail7 TEXT,
    detail8 TEXT,
    detail9 TEXT
);

CREATE TABLE warehouse (
    location INTEGER NOT NULL,
    loc_bin TEXT,
    item_in_loc INTEGER NOT NULL,
    quantity FLOAT NOT NULL,
    store_unit TEXT NOT NULL,
    value FLOAT,
    val_unit TEXT NOT NULL,
    time_stamp TEXT
);

CREATE TABLE movements (
    time_stamp TEXT NOT NULL,
    item INTEGER NOT NULL,
    quantity FLOAT NOT NULL,
    item_unit TEXT NOT NULL,
    value FLOAT,
    val_unit TEXT NOT NULL,
    source INTEGER NOT NULL,
    source_bin TEXT NOT NULL,
    destination INTEGER NOT NULL,
    dest_bin TEXT NOT NULL
);

