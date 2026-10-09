# Mini-SOC — Python Security Log Analyzer

A small Python project I'm building to learn how SOC analysts detect suspicious authentication activity from logs.

Right now, the analyzer reads authentication logs, tracks login attempts by IP address, and flags patterns that could indicate suspicious behavior. I'm building it step by step and testing each detection rule with sample logs.

## What it detects

* **Repeated failed logins** — flags IPs with multiple failed attempts.
* **High failure rate** — identifies IPs with a high proportion of failed logins.
* **Failed login followed by success** — flags an IP after repeated failures followed by a successful login.
* **Multiple accounts targeted** — detects an IP attempting to log in to three or more unique usernames.

These alerts highlight suspicious patterns; they don't automatically prove an attack occurred.

## Built with

* Python
* Linux / Kali Linux
* Git and GitHub

## Project structure

```text
Soc/
├── logs/
│   └── auth.log
└── src/
    └── analyzer.py
```

## Run it

Clone the repository and move into the project directory:

```bash
git clone https://github.com/aryandarne/Soc.git
cd Soc
python3 src/analyzer.py
```

The analyzer uses the sample authentication log at `logs/auth.log`.

## Current status

The initial detection rules are implemented and have been tested against simulated authentication logs. I'm working on improving the reliability of the detections, adding automated tests, and cleaning up the output.

## What's next

* Add automated tests for each detection rule.
* Improve alert formatting and severity levels.
* Make detection thresholds configurable.
* Explore storing alerts in SQLite.

## Disclaimer

This is a learning project for defensive security and detection engineering. The sample logs are simulated, and the tool is intended for authorized analysis only.
