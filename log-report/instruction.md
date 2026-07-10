An Apache-style access log is at /app/access.log. Parse it and write a JSON report to /app/report.json.

The report must be a single JSON object with exactly these keys:

- "total_requests": integer — total number of log lines
- "unique_ips": integer — number of distinct client IP addresses
- "top_path": string — the URL path that appears most often in requests

Success criteria:
1. /app/report.json exists and is valid JSON.
2. "total_requests" equals the exact count of log entries in /app/access.log.
3. "unique_ips" equals the exact count of distinct client IP addresses in the log.
4. "top_path" equals the URL path with the highest request count in the log.
