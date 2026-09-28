attempts = {}

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
    print("\n---LOGIN ATTEMPTS---")
    for ip,count in attempts.items():
        print("IP",ip,"Attempts:",count)



