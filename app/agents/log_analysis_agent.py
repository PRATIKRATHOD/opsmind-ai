from pathlib import Path


LOG_PATTERNS = {

    "OutOfMemoryError": {
        "status": "MEMORY_FAILURE",
        "details": "JVM memory exhaustion detected"
    },

    "ExpiredJwtException": {
        "status": "JWT_TOKEN_EXPIRED",
        "details": "JWT token expiration detected"
    },

    "DisabledException": {
        "status": "ACCOUNT_DISABLED",
        "details": "User account disabled or locked"
    },

    "InsufficientAuthenticationException": {
        "status": "AUTHENTICATION_FAILURE",
        "details": "Authentication required for access"
    },

    "Connection timeout": {
        "status": "DATABASE_TIMEOUT",
        "details": "Database connection timeout detected"
    },

    "HikariPool": {
        "status": "DB_CONNECTION_POOL_EXHAUSTED",
        "details": "Database connection pool exhausted"
    },

    "Consumer lag": {
        "status": "KAFKA_CONSUMER_LAG",
        "details": "Kafka consumer lag increasing"
    },

    "CrashLoopBackOff": {
        "status": "K8S_CRASH_LOOP",
        "details": "Kubernetes pod crash loop detected"
    },

    "GC overhead limit exceeded": {
        "status": "HIGH_GC_ACTIVITY",
        "details": "High JVM garbage collection activity"
    }
}


def log_analysis_agent(incident):

    application = incident["application"]

    log_path = Path(f"logs/{application}.log")

    print(f"Checking logs: {log_path}")

    if not log_path.exists():

        return {
            "status": "LOG_NOT_FOUND",
            "details": "Log file missing"
        }

    content = log_path.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    for pattern, result in LOG_PATTERNS.items():

        if pattern in content:

            print(f"Matched log pattern: {pattern}")

            return result

    return {
        "status": "NO_CRITICAL_ERRORS",
        "details": "No major operational errors detected"
    }