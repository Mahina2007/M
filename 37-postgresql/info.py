# # CREATE TABLE IF NOT EXISTS users
# # (
# #     id         SERIAL PRIMARY KEY,
# #     first_name VARCHAR(128) NOT NULL,
# #     last_name  VARCHAR(128) NOT NULL,
# #     age        SMALLINT     NOT NULL,
# #     about      TEXT,
# #     birthdate  DATE,
# #     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

# #
#
# \! cls - clear
# \l - databaselar royxati
# CREATE USER name WITH PASSWORD "password"
# \du - barcha userlarni korsatish
# CREATE DATABASE n68 owner n68; - user da db yaratish
# psql -u username -d db name
#
# Numeric Types
#     INTEGER: A standard integer.
#     BIGINT: A larger integer.
#     SMALLINT: A smaller integer.
#     SERIAL: Auto-incrementing integer (commonly used for primary keys).
#     DECIMAL or NUMERIC: Exact numeric values with specified precision and scale.
#     REAL: Single-precision floating point.
#     DOUBLE PRECISION: Double-precision floating point.
#
#
# Character Types
#     CHAR(n): Fixed-length character string.
#     VARCHAR(n): Variable-length character string.
#     TEXT: Variable-length character string with unlimited length.
#
# Date and Time Types
#     DATE: Stores only the date.
#     TIME: Stores only the time (no date).
#     TIMESTAMP: Stores both date and time.
#     TIMESTAMPTZ: Timestamp with time zone.
#     INTERVAL: Stores a time period, like '2 days' or '3 hours 10 minutes'.
#
# Boolean Type
#     BOOLEAN: Stores TRUE, FALSE, or NULL.
#
# Binary Data Types
#     BYTEA: Stores binary data (useful for images, files, etc.).
#
# UUID Type
#     UUID: Stores Universally Unique Identifiers.
#
# JSON Types
#     JSON: Stores JSON data.
#     JSONB: Stores binary JSON data (more efficient for some operations).
#
# Arrays
# PostgreSQL supports arrays for any data type. You can create arrays like this:
#     datatype[]
