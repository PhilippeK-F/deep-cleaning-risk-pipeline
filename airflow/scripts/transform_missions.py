import pandas as pd
from pathlib import Path

RAW_PATH = Path("/opt/airflow/data/raw/deep_cleaning_missions.csv")
PROCESSED_PATH = Path("/opt/airflow/data/processed/deep_cleaning_missions_processed.csv")


def compute_risk_score(row: pd.Series) -> int:
    score = 0

    if row["zone_type"] in ["freezer", "cold_room", "food_lab"]:
        score += 3
    if row["temperature_c"] <= -18:
        score += 2
    if row["surface_m2"] >= 300:
        score += 2
    if row["estimated_duration_min"] >= 240:
        score += 2
    if row["incident_flag"]:
        score += 3
    if row["compliance_score"] < 80:
        score += 2

    return score


def main() -> None:
    if not RAW_PATH.exists():
        raise FileNotFoundError(f"Raw file not found: {RAW_PATH}")

    df = pd.read_csv(RAW_PATH)
    df["scheduled_date"] = pd.to_datetime(df["scheduled_date"])
    df["risk_score"] = df.apply(compute_risk_score, axis=1)

    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

    print(f"Processed file written to {PROCESSED_PATH}")


if __name__ == "__main__":
    main()