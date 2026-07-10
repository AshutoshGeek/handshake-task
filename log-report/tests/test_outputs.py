import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load():
    return json.loads(REPORT.read_text())


def test_total_requests():
    """Success criterion 1: report.json contains total_requests equal to the number of log lines."""
    assert _load()["total_requests"] == 6


def test_unique_ips():
    """Success criterion 2: report.json contains unique_ips equal to the number of distinct client IPs."""
    assert _load()["unique_ips"] == 3


def test_top_path():
    """Success criterion 3: report.json contains top_path equal to the most-requested URL path."""
    assert _load()["top_path"] == "/index.html"
