import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

OUTPUT_PATH = Path("/opt/airflow/data/raw/deep_cleaning_missions.csv")

CLIENTS = ["Carrefour", "Leclerc", "Auchan", "Intermarché"]
SITES = [
    "Paris Hypermarket",
    "Lyon Hypermarket",
    "Marseille Logistics Site",
    "Lille Food Storage",
]
ZONE_TYPES = ["freezer", "cold_room", "storage", "loading_area", "food_lab"]
OPERATIONS = [
    "total deep cleaning",
    "defrost and cleaning",
    "disinfection",
    "post-incident cleaning",
]
CHEMICALS = ["degreaser", "food_safe_disinfectant", "neutral_cleaner"]
PPE = ["gloves", "non-slip shoes", "cold protection", "goggles"]


def random_date(days_back: int = 30) -> datetime:
    now = datetime.now()
    return now - timedelta(
        days=random.randint(0, days_back),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
    )


def generate_row(i: int) -> dict:
    zone_type = random.choice(ZONE_TYPES)
    temperature = random.choice([-25, -18, -5, 2, 8]) if zone_type in ["freezer", "cold_room"] else random.choice([10, 15, 20])
    surface = random.randint(50, 600)
    team_size = random.randint(2, 6)
    duration = random.randint(60, 360)
    incident_flag = random.random() < 0.08
    compliance_score = round(random.uniform(70, 100), 1)
    if incident_flag:
        compliance_score = round(random.uniform(40, 85), 1)

    return {
        "mission_id": f"MISSION-{i:04d}",
        "client_name": random.choice(CLIENTS),
        "site_name": random.choice(SITES),
        "zone_type": zone_type,
        "operation_type": random.choice(OPERATIONS),
        "temperature_c": temperature,
        "surface_m2": surface,
        "team_size": team_size,
        "estimated_duration_min": duration,
        "chemical_used": random.choice(CHEMICALS),
        "ppe_required": ", ".join(random.sample(PPE, k=random.randint(2, 4))),
        "incident_flag": incident_flag,
        "compliance_score": compliance_score,
        "scheduled_date": random_date().strftime("%Y-%m-%d %H:%M:%S"),
    }


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    rows = [generate_row(i) for i in range(1, 301)]

    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "mission_id",
                "client_name",
                "site_name",
                "zone_type",
                "operation_type",
                "temperature_c",
                "surface_m2",
                "team_size",
                "estimated_duration_min",
                "chemical_used",
                "ppe_required",
                "incident_flag",
                "compliance_score",
                "scheduled_date",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"{len(rows)} missions generated in {OUTPUT_PATH}")


if __name__ == "__main__":
    main()