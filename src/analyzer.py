attempts = {}
failed = {}
threshold = 5
success = {}
users = {}

with open("logs/auth.log", "r") as file:
    for line in file:

        # Skip empty lines
        if not line.strip():
            continue

        parts = line.split()
        if "user" not in parts :
           continue
        user = parts.index("user")
        username = parts[user + 1]
       

        # Skip malformed entries that don't contain an IP
        if "IP" not in parts:
            continue

        position = parts.index("IP")
        ip = parts[position + 1]
        if ip not in users:
           users[ip] = []

        # Count total login attempts
        if ip not in attempts:
            attempts[ip] = 0
        users[ip].append(username)    
        
        

        attempts[ip] += 1
        # Track successful and failed logins
        if "Login successful" in line:
            print(ip, "SUCCESS")

            if ip not in success:
                success[ip] = 1
            else:
                success[ip] += 1

        else:
            print(ip, "FAILED")

            if ip not in failed:
                failed[ip] = 1
            else:
                failed[ip] += 1

    print("\n---LOGIN ATTEMPTS---")

    for ip, count in attempts.items():
        print("IP", ip, "Attempts:", count)

    print("\n---FAILURE COUNTS---")

    for ip, failures in failed.items():
        print("IP", ip, "No. of Failures:", failures)

    print("\n---SECURITY FINDINGS---")
    print("---Suspicious IPs---")

    # Detect IPs with repeated failed logins
    for ip, failures in failed.items():
        if attempts[ip] >= 3 and (failed[ip] / attempts[ip]) * 100 > 80:
            print(
                "SUSPICIOUS",
                "IP", ip,
                "Failure percentage:", (failed[ip]/attempts[ip]) * 100 , 
            )

    # Detect IPs that failed repeatedly and eventually succeeded
    print("\n---FAILED THEN SUCCESS---")

    for ip, failures in failed.items():
        if failures >= threshold and ip in success:
            print(
                "ALERT",
                "IP", ip,
                "had", failures,
                "failed attempts and",
                success[ip],
                "successful login(s)"
            )
    print(users)
