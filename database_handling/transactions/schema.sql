DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    fname VARCHAR(255),
    lname VARCHAR(255),
    pin SMALLINT NOT NULL
);


DROP TYPE IF EXISTS account_type CASCADE;
CREATE TYPE account_type AS ENUM ('checking', 'savings');

DROP TABLE IF EXISTS accounts CASCADE;
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    type account_type,
    owner_id INTEGER NOT NULL,
    balance NUMERIC DEFAULT 0.0,
    CONSTRAINT positive_balance CHECK (balance >= 0),
    FOREIGN KEY (owner_id) REFERENCES users (id)
);

DROP TYPE IF EXISTS ledger_type CASCADE;
CREATE TYPE ledger_type AS ENUM ('credit', 'debit');

DROP TABLE IF EXISTS ledger;
CREATE TABLE ledger (
    id SERIAL PRIMARY KEY,
    account_id INTEGER NOT NULL,
    date DATE NOT NULL DEFAULT CURRENT_DATE,
    type ledger_type NOT NULL,
    amount NUMERIC NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts (id)
);
