# Python Security Log Analyzer
# Analyzes login attempts and identifies suspicious IPs

successful = 0
failed = 0
failed_ips = {}

# Read the security log
with open("log.txt", "r") as log_file:
    for line in log_file:
        parts = line.split()

        # Skip blank or incomplete lines
        if len(parts) < 4:
            continue

        ip = parts[2]
        status = parts[3]

        if status == "SUCCESS":
            successful += 1

        elif status == "FAILED":
            failed += 1

            if ip in failed_ips:
                failed_ips[ip] += 1
            else:
                failed_ips[ip] = 1

# Display login summary
print("LOGIN SECURITY REPORT")
print("---------------------------")
print("Successful logins:", successful)
print("Failed logins:", failed)

# Display failed attempts by IP
print("\nFAILED LOGIN ATTEMPTS BY IP")
print("---------------------------")

for ip in failed_ips:
    print(ip, "-", failed_ips[ip], "failed attempts")

# Identify suspicious activity
print("\nSECURITY ALERTS")
print("---------------------------")

alerts_found = False

for ip in failed_ips:
    if failed_ips[ip] >= 3:
        print("ALERT:", ip, "has", failed_ips[ip], "failed login attempts!")
        alerts_found = True

if not alerts_found:
    print("No suspicious activity detected.")
