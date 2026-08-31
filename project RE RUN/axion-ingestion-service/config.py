"""
Axion Ingestion Service - Configuration
Loads database connection string from environment variable.
"""

import os
from dataclasses import dataclass


@dataclass
class Settings:
    # PostgreSQL connection string
    # Format: postgresql://<user>:<password>@<host>:<port>/<database>
    # Example: postgresql://postgres:postgres@localhost:5432/axiondb
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://myuser:mypassword@postgresqlsvc:5432/mydatabase"  # Default value if environment variable is not set,
    )

settings = Settings()
