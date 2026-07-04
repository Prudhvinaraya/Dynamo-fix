# Web Server Log Parser (Dynamo-fix)

An automated data processing task designed for the Harbor benchmark framework. This task parses standard web server access logs to generate structured JSON metrics summarizing request profiles.

## Task Objective
The system extracts information from an active server log to determine traffic usage patterns, measuring overall volume, distinct user footprints, and traffic density spikes.

The solution generates a payload file at `/app/report.json` containing exactly three fields:
1. `total_requests`: An integer count of all non-empty log lines.
2. `unique_ips`: An integer count of distinct client IP instances.
3. `top_path`: A string identifying the most heavily requested request endpoint.

---

## Directory Structure

```text
log-report/
├── environment/
│   └── Dockerfile      # Pinned base image environment containing dependencies
├── solution/
│   ├── solve.py        # Reference log processing python engine
│   └── solve.sh        # Bash wrapper executing the processing routine
├── tests/
│   ├── test.sh         # Verifier execution pipeline mapping metrics to reward file
│   └── test_outputs.py # Strict pytest suite validating 1:1 criteria assertions
├── access.log          # Raw sample web server log file
├── instruction.md      # Ground-truth success criteria specification
└── task.toml           # Harbor evaluation orchestration configuration
