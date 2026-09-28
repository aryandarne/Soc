Mini-SOC — Security Log Analyzer & Detection Platform

A Python-based security monitoring project that analyzes authentication logs, detects suspicious activity, and generates security alerts.

The goal of this project is to build a small Security Operations Center (SOC)-style detection system while learning Python, cybersecurity concepts, data analysis, databases, testing, and Git/GitHub.

«Status: 🚧 In Development»

🎯 Project Goal

The system will analyze authentication events such as successful and failed logins and identify potentially suspicious behavior.

The project will progressively evolve from a simple log parser into a small security monitoring platform.

Planned pipeline

Authentication Logs
        ↓
    Log Parser
        ↓
 Detection Engine
        ↓
  Risk Scoring
        ↓
     Alerts
        ↓
   SQLite Database
        ↓
     Dashboard

🔍 Planned Detection Rules

The detection engine will eventually identify patterns such as:

- Repeated failed login attempts
- Brute-force-like activity
- Multiple accounts targeted from the same IP
- Successful login following repeated failures
- Suspicious authentication patterns
- Other configurable authentication-based detections

Detection rules will be documented and tested as the project develops.

🛠️ Technology

Current/planned technologies:

- Python — core application
- Linux — development and testing environment
- SQLite — event and alert storage
- Git & GitHub — version control
- HTML/CSS/JavaScript or a Python web framework — planned dashboard
- pytest — planned automated testing

📁 Project Structure

mini-soc/
├── README.md
├── .gitignore
├── logs/
│   └── auth.log
├── src/
│   └── analyzer.py
├── tests/
└── docs/
    └── learning-log.md

The structure will expand as new components are added.

🚀 Current Progress

Phase 1 — Log Analysis

- [ ] Create authentication log dataset
- [ ] Read log files with Python
- [ ] Parse authentication events
- [ ] Count failed logins
- [ ] Track failed attempts by IP
- [ ] Implement first suspicious-login detection

Phase 2 — Detection Engine

- [ ] Add multiple detection rules
- [ ] Detect brute-force-like behavior
- [ ] Detect attacks against multiple accounts
- [ ] Improve event parsing
- [ ] Make detection thresholds configurable

Phase 3 — Risk & Alerts

- [ ] Add severity levels
- [ ] Implement risk scoring
- [ ] Generate structured alerts
- [ ] Store detection results

Phase 4 — Database

- [ ] Add SQLite database
- [ ] Store authentication events
- [ ] Store alerts
- [ ] Query security events

Phase 5 — Dashboard

- [ ] Display authentication statistics
- [ ] Display detected threats
- [ ] Display severity levels
- [ ] Add filtering/search

Phase 6 — Testing & Documentation

- [ ] Add automated tests
- [ ] Test detection rules
- [ ] Improve error handling
- [ ] Document architecture
- [ ] Add example datasets
- [ ] Document limitations

🧪 Example Detection

A future detection rule might identify repeated failed logins from the same source:

Source IP: 192.168.1.50
Failed attempts: 7
Target accounts: admin, root

Detection: Repeated authentication failures
Severity: HIGH

The exact thresholds and scoring rules will be documented as the detection engine develops.

🔐 Security & Ethics

This project is intended for defensive security learning and authorized environments.

The initial datasets will use simulated authentication logs rather than targeting real systems.

The project focuses on:

- Security monitoring
- Log analysis
- Detection engineering
- Incident investigation concepts
- Defensive automation

📚 Learning Goals

This project is also a practical Python learning exercise.

Topics covered will include:

- Variables and data types
- Conditions and loops
- Functions
- Lists and dictionaries
- File handling
- String parsing
- Regular expressions
- Error handling
- Object-oriented programming
- SQLite and SQL
- Testing
- Git/GitHub
- Basic web development
- Security event analysis

📌 Why I'm Building This

Rather than building isolated beginner projects, I'm using one project to progressively learn how real security-monitoring software is structured.

The emphasis is on understanding the code, building incrementally, testing the detection logic, and documenting the decisions behind the system.

⚠️ Disclaimer

This project is for educational and defensive security purposes.

It should only be used with systems, logs, and data that you are authorized to analyze.
