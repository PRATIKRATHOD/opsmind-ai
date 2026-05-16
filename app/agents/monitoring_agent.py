def monitoring_agent(incident):

    application = incident["application"]
    issue = incident["issue"].lower()

    if "memory" in issue:
        return {
            "status": "HIGH_MEMORY_USAGE",
            "details": "Memory usage exceeded 90%"
        }

    if "latency" in issue:
        return {
            "status": "HIGH_API_LATENCY",
            "details": "API response time exceeded threshold"
        }

    if "cpu" in issue:
        return {
            "status": "HIGH_CPU_USAGE",
            "details": "CPU utilization exceeded 95%"
        }

    if "disk" in issue:
        return {
            "status": "DISK_SPACE_CRITICAL",
            "details": "Disk usage exceeded 95%"
        }

    if "kafka" in issue or "lag" in issue:
        return {
            "status": "KAFKA_CONSUMER_LAG",
            "details": "Consumer lag increasing rapidly"
        }

    return {
        "status": "HEALTHY",
        "details": "No critical alerts detected"
    }