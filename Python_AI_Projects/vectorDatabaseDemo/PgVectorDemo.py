import os
import psycopg2
from pgvector.psycopg2 import register_vector

# 1. Connect to your PostgreSQL database.
# When using a Docker container, set DATABASE_URL or PGHOST/PGPORT/PGUSER/PGPASSWORD/PGDATABASE.

def get_connection():
    database_url = os.environ.get("DATABASE_URL")
    if database_url:
        print("Connecting to PostgreSQL via DATABASE_URL")
        return psycopg2.connect(database_url)

    pg_host = os.environ.get("PGHOST", "localhost")
    pg_port = os.environ.get("PGPORT", "5432")
    pg_user = os.environ.get("PGUSER", "postgres")
    pg_password = os.environ.get("PGPASSWORD", "admin")
    pg_database = os.environ.get("PGDATABASE", "postgres")

    print(f"Connecting to PostgreSQL at {pg_host}:{pg_port} as {pg_user} to database {pg_database}")
    return psycopg2.connect(
        dbname=pg_database,
        user=pg_user,
        password=pg_password,
        host=pg_host,
        port=pg_port,
    )

conn = get_connection()

print("Successfully connected to PostgreSQL : ", conn)

def get_pgvector_info(cursor):
    cursor.execute(
        "SELECT name, default_version, installed_version FROM pg_available_extensions WHERE name = 'pgvector';"
    )
    return cursor.fetchone()


def ensure_pgvector_extension(cursor):
    info = get_pgvector_info(cursor)
    if info is None:
        raise RuntimeError(
            "The PostgreSQL server does not expose the pgvector extension. "
            "Verify you are connected to the pgvector-enabled container or image, "
            "and that it contains pgvector extension files."
        )

    print(f"pgvector extension available: name={info[0]}, default_version={info[1]}, installed_version={info[2]}")

    try:
        cursor.execute("CREATE EXTENSION IF NOT EXISTS pgvector;")
        conn.commit()
    except psycopg2.Error as exc:
        conn.rollback()
        message = str(exc).lower()
        if "extension \"pgvector\" is not available" in message or "control file" in message:
            raise RuntimeError(
                "The PostgreSQL server does not have the pgvector extension installed. "
                "Use a pgvector-enabled image such as `pgvector/pgvector:pg16`, "
                "or install the pgvector server package inside your container."
            ) from exc
        raise

try:
    cur = conn.cursor()

    # 2. Ensure the pgvector extension is installed and available
    ensure_pgvector_extension(cur)

    # 3. Register pgvector to handle the vector type automatically
    register_vector(conn)

    # 4. Ensure the sample table exists
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            embedding vector(3) NOT NULL
        );
        """
    )
    conn.commit()

    # 5. Insert sample data if the table is empty
    cur.execute("SELECT COUNT(*) FROM items;")
    row_count = cur.fetchone()[0]
    if row_count == 0:
        sample_items = [
            ("Apple", [1.0, 0.0, 0.0]),
            ("Banana", [0.0, 1.0, 0.0]),
            ("Cherry", [0.0, 0.0, 1.0]),
            ("Apricot", [0.9, 0.1, 0.0]),
            ("Berry", [0.1, 0.0, 0.9])
        ]
        cur.executemany(
            "INSERT INTO items (name, embedding) VALUES (%s, %s);",
            sample_items,
        )
        conn.commit()

    # 6. Define the query vector and run a similarity search
    query_vector = [1.0, 0.0, 0.0]
    sql = """
    SELECT id, name, embedding
    FROM items
    ORDER BY embedding <-> %s::vector
    LIMIT 5;
    """

    cur.execute(sql, (query_vector,))
    results = cur.fetchall()

    print("Top 5 nearest neighbors:")
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Embedding: {row[2]}")

finally:
    cur.close()
    conn.close()