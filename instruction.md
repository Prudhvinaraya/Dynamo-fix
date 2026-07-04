# Web Server Log Parser

Please parse the web server access log located at `/app/access.log` and generate a summary traffic metrics report.

The final output must be saved exactly at `/app/report.json`. The file must be formatted as a single JSON object containing exactly three fields:
1. `total_requests`: An integer tracking the total number of non-empty log entries.
2. `unique_ips`: An integer tracking the number of unique client IP addresses found in the log.
3. `top_path`: A string specifying the most frequently requested HTTP URL path block.

## Success Criteria:
1. The task must output a valid JSON report file precisely at `/app/report.json`.
2. The JSON object must contain accurate counts for total requests and unique client IPs.
3. The JSON object must identify the correct string name of the top requested path with no additional data pollution.