from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text

DB_URL = "postgresql+psycopg2://cleaning:cleaning@postgres:5432/deep_cleaning"
CSV_PATH = Path("/opt/airflow/data/processed/deep_cleaning_missions_processed.csv")


def main() -> None:
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"Processed file not found: {CSV_PATH}")

    df = pd.read_csv(CSV_PATH)
    df["scheduled_date"] = pd.to_datetime(df["scheduled_date"], errors="coerce")

    engine = create_engine(DB_URL)

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS deep_cleaning_missions (
        mission_id TEXT PRIMARY KEY,
        client_name TEXT,
        site_name TEXT,
        zone_type TEXT,
        operation_type TEXT,
        temperature_c INTEGER,
        surface_m2 INTEGER,
        team_size INTEGER,
        estimated_duration_min INTEGER,
        chemical_used TEXT,
        ppe_required TEXT,
        incident_flag BOOLEAN,
        compliance_score DOUBLE PRECISION,
        scheduled_date TIMESTAMP,
        risk_score INTEGER
    );
    """

    with engine.begin() as conn:
        conn.execute(text(create_table_sql))
        conn.execute(text("TRUNCATE TABLE deep_cleaning_missions;"))

    df.to_sql("deep_cleaning_missions", engine, if_exists="append", index=False)
    print(f"{len(df)} rows loaded into PostgreSQL")


if __name__ == "__main__":
    main()