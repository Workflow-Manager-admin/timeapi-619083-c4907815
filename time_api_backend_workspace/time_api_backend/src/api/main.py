from datetime import datetime, timezone
from typing import Dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI(
    title="Time API",
    description="API service providing real-time server time information",
    version="1.0.0",
    openapi_tags=[{
        "name": "time",
        "description": "Endpoints for retrieving current server time"
    }]
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TimeResponse(BaseModel):
    """Response model for time endpoints."""
    timestamp: int
    iso_time: str
    timezone: str

    class Config:
        json_schema_extra = {
            "example": {
                "timestamp": 1646956800,
                "iso_time": "2024-03-11T00:00:00Z",
                "timezone": "UTC"
            }
        }


@app.get("/")
def health_check() -> Dict[str, str]:
    """
    Health check endpoint to verify API is running.
    Returns:
        Dict containing health status message
    """
    return {"message": "Healthy"}


@app.get("/time", response_model=TimeResponse, tags=["time"])
def get_current_time() -> TimeResponse:
    """
    Get the current server time.
    Returns:
        TimeResponse object containing:
        - Unix timestamp (seconds since epoch)
        - ISO 8601 formatted time string
        - Timezone (always UTC)
    """
    now = datetime.now(timezone.utc)
    return TimeResponse(
        timestamp=int(now.timestamp()),
        iso_time=now.isoformat(),
        timezone="UTC"
    )


@app.get("/time/timestamp", response_model=Dict[str, int], tags=["time"])
def get_unix_timestamp() -> Dict[str, int]:
    """
    Get current Unix timestamp (seconds since epoch).
    Returns:
        Dict containing Unix timestamp
    """
    return {"timestamp": int(datetime.now(timezone.utc).timestamp())}


@app.get("/time/iso", response_model=Dict[str, str], tags=["time"])
def get_iso_time() -> Dict[str, str]:
    """
    Get current time in ISO 8601 format.
    Returns:
        Dict containing ISO 8601 formatted time string
    """
    return {"iso_time": datetime.now(timezone.utc).isoformat()}
