attempts = {}
failed = {}
threshold = 5

with open("logs/auth.log", "r") as file:
    for line in file:
        if not line.strip():
            continue

        parts = line.split()
        position = parts.index("IP")
        ip = parts[position + 1]

        if ip not in attempts:
            attempts[ip] = 0

        attempts[ip] += 1
        if "Login successful" in line :
            print(ip,"SUCCESS")
        else:
             print(ip,"FAILED")
             if  ip not in failed:
                 failed[ip] = 1
             else:
                  failed[ip] += 1
    print("\n---LOGIN ATTEMPTS---")

    for ip, count in attempts.items():
        print("IP", ip, "Attempts:", count)
print("---SECURITY FINDINGS---")
print("---Suspicious IPs---")

for ip, failures in failed.items():
    if failures >= threshold:
        print("SUSPICIOUS", "IP", ip, "FAILED ATTEMPTS:", failures)
print("---SECURITY FINDINGS---")
            
