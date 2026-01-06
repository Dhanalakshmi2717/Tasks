def analyze_logs(logs):
    level_count = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    error_messages = {}

    for log in logs:
        parts = log.split()
        if len(parts) < 4:
            continue  
        level = parts[2]
        message = " ".join(parts[3:])

        if level in level_count:
            level_count[level] += 1

        if level == "ERROR":
            if message in error_messages:
                error_messages[message] += 1
            else:
                error_messages[message] = 1

    
    most_common = None
    max_count = 0
    for msg, count in error_messages.items():
        if count > max_count:
            max_count = count
            most_common = msg


    print("INFO logs:", level_count["INFO"])
    print("WARNING logs:", level_count["WARNING"])
    print("ERROR logs:", level_count["ERROR"])
    print("Most common error:", most_common if most_common else "None")


if __name__ == "__main__":
    logs = [
        "2026-01-06 10:00:00 INFO Application started",
        "2026-01-06 10:01:00 WARNING Low memory",
        "2026-01-06 10:02:00 ERROR Database connection failed",
        "2026-01-06 10:03:00 ERROR Database connection failed",
        "2026-01-06 10:04:00 INFO User logged in"
    ]

    analyze_logs(logs)
