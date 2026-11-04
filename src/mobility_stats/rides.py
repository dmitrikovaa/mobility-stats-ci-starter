import csv
import os
from collections import defaultdict


def load_rides(csv_path: str) -> list[dict[str, object]]:
    """Load ride data from rides CSV file."""
    rides = []
    if os.path.exists(csv_path) == False:
        raise FileNotFoundError(f"Could not find file: {csv_path}")
    with open(csv_path, newline="", encoding="utf-8") as f:
        rided = csv.DictReader(f)
        for rid in rided:
            rid.copy()
            rides.append(
                {
                    "ride_id": rid["ride_id"],
                    "start_station": rid["start_station"],
                    "end_station": rid["end_station"],
                    "duration_min": float(rid["duration_min"]),
                    "rider_type": rid["rider_type"],
                }
            )
    return rides


def average_duration(rid):
    """Return the average ride duration in minutes."""
    if len(rid) == 0:
        return 0.0
    counts = 0.0
    for ride in rid:
        counts += ride["duration_min"]
    return counts / len(rid)


def count_by_rider_type(rid):
    """Count rides for each rider type."""
    counts = defaultdict(int)
    for ride in rid:
        counts[ride["rider_type"]] += 1
    return dict(counts)


def busiest_start_station(rid):
    """Return the start station with the most rides."""
    if rid == None:
        raise ValueError("rides must not be None")
    if len(rid) == 0:
        raise ValueError("rides must not be empty")
    counts = {}
    for ride in rid:
        station = ride["start_station"]
        counts[station] = counts.get(station, 0) + 1
    return max(counts, key=counts.get)


def filter_long_rides(rid, counts=30):
    """Return all rides with duration greater than or equal to counts minutes."""
    long_rides = []
    for ride in rid:
        if ride["duration_min"] >= counts:
            long_rides.append(ride)
    return long_rides
