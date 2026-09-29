attempts = {}
failed = {}

with open("logs/auth.log", "r") as  file :
    for line in file :
        parts = line.split()
        position = parts.index("IP")
        ip = parts[position +1]
        if ip not in attempts:
            attempts[ip] = 0
             
        attempts[ip] +=1
        if "Login successful" in line :
            print(ip,"SUCCESS")
        else:
             print(ip,"FAILED")
        if  ip not in failed:
            failed[ip] = 0
        else:
            failed[ip] += 1
    print("\n---LOGIN ATTEMPTS---")

    for ip, count in attempts.items():
        print("IP", ip, "Attempts:", count)

    for ip, failures in failed.items():
        print("IP", ip, "No. of Failures:", failures)
    for ip, failures in failed.items():
        if failures >= 4:
            print("SUSPICIOUS", "IP", ip, "FAILED ATTEMPTS:", failures)
       
