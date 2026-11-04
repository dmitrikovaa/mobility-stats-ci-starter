from mobility_stats.rides import average_duration, busiest_start_station, count_by_rider_type


def build_summary(rid):
    """Build rides compact dictionary with headline statistics."""
    counts = {
        "ride_count": len(rid),
        "average_duration": average_duration(rid),
        "rider_types": count_by_rider_type(rid),
    }
    if rid:
        counts["busiest_start_station"] = busiest_start_station(rid)
    else:
        counts["busiest_start_station"] = None
    return counts


def format_summary(rid):
    """Create rides human-readable text summary."""
    title = "Mobility summary"
    line1 = f"Rides: {rid['ride_count']}"
    line2 = f"Average duration: {rid['average_duration']:.1f} min"
    line3 = f"Busiest start: {rid['busiest_start_station']}"
    return title + "\n" + line1 + "\n" + line2 + "\n" + line3
