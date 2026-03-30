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