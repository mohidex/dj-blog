-- Create Database
CREATE DATABASE test_blogapp;
\c test_blogapp;

-- Run Query
CREATE COLLATION case_insensitive (
    provider = icu,
    locale = 'und-u-ks-level2',
    deterministic = false
);
