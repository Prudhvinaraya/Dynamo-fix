import os
import json
import pytest

REPORT_PATH = "/app/report.json"

@pytest.fixture(scope="module")
def load_report():
    assert os.path.exists(REPORT_PATH), f"Output file missing at {REPORT_PATH}"
    with open(REPORT_PATH, "r") as f:
        return json.load(f)

def test_criterion_1_file_and_format(load_report):
    """
    Verifies Success Criterion 1:
    The task must output a valid JSON report file precisely at /app/report.json.
    """
    assert isinstance(load_report, dict), "The root of report.json must be a JSON object."

def test_criterion_2_log_metrics(load_report):
    """
    Verifies Success Criterion 2:
    The JSON object must contain accurate counts for total requests and unique client IPs.
    """
    assert "total_requests" in load_report, "Missing field: total_requests"
    assert "unique_ips" in load_report, "Missing field: unique_ips"
    assert isinstance(load_report["total_requests"], int), "total_requests must be an integer"
    assert isinstance(load_report["unique_ips"], int), "unique_ips must be an integer"
    # Ground-truth metric checks derived from access.log
    assert load_report["total_requests"] == 11, "total_requests count is incorrect"
    assert load_report["unique_ips"] == 4, "unique_ips count is incorrect"

def test_criterion_3_top_endpoint(load_report):
    """
    Verifies Success Criterion 3:
    The JSON object must identify the correct string name of the top requested path with no additional data pollution.
    """
    assert "top_path" in load_report, "Missing field: top_path"
    assert isinstance(load_report["top_path"], str), "top_path must be a string"
    # Ground-truth path check derived from access.log
    assert load_report["top_path"] == "/index.html", "top_path target calculation is incorrect"