# Mini-SOC: Authentication Log Analyzer

This is a small Python project I built while learning cybersecurity. The idea was to take a real-world SOC task — looking through authentication logs — and make a simple tool that can point out login activity worth checking.

It is still a learning project, not a full SIEM or a production security tool. I wanted to understand the logic behind basic detection rules instead of only running tools and looking at their output.

## What it does

- Reads authentication log entries from `logs/auth.log`.
- Groups login activity by source IP address.
- Counts login attempts and failed logins.
- Flags IP addresses that reach the configured failed-login threshold.
- Checks for IPs with a high proportion of failed logins.
- Looks for repeated failed logins followed by a successful login, which can be worth investigating.

The exact findings depend on the entries in the log file and the detection rules configured in `src/analyzer.py`.

## Running it

You need Python 3 installed.

Clone the repository and move into the project folder:

```bash
git clone https://github.com/aryandarne/Soc.git
cd Soc
```

Make sure the input file exists at `logs/auth.log`, then run:

```bash
python3 src/analyzer.py
```

The analyzer prints a summary of login activity and any findings triggered by its rules. It does not need any third-party Python packages at the moment.

## Project structure

```text
Soc/
├── logs/
│   └── auth.log
└── src/
    └── analyzer.py
```

## Why I made it

I'm working toward a cybersecurity internship and wanted a project that would make me practise Python while learning how a SOC analyst might investigate authentication events. Building this helped me work with files, strings, dictionaries, counters, conditions, and simple detection logic.

## Current limitations

- It analyses a local log file; it does not monitor a machine in real time.
- The parser expects log entries in the format the code currently handles, so other log formats may need changes.
- Its rules are deliberately simple. A flagged IP is something to investigate, not proof that an attack happened.
- It is a learning project and should not be relied on as a production security system.

## What I'd like to improve next

- Add test cases for normal and suspicious login patterns.
- Make log parsing more robust and easier to extend.
- Move detection thresholds into a configuration file.
- Add clearer reports so the reason for each alert is easy to understand.

This is my first version of the project, and I'll keep improving it as I learn more about Python, networking, and security monitoring.
