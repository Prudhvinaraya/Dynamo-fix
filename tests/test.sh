#!/bin/bash
set -e

VERIFIER_LOG_DIR="/logs/verifier"
mkdir -p "$VERIFIER_LOG_DIR"

# Execute plain pytest natively using pre-baked dependencies with CTRF mapping outputs
python3 -m pytest /app/tests/test_outputs.py --json-ctrf="$VERIFIER_LOG_DIR/ctrf.json" > "$VERIFIER_LOG_DIR/pytest.log" 2>&1
RC=$?

if [ $RC -eq 0 ]; then
    echo "1" > "$VERIFIER_LOG_DIR/reward.txt"
else
    echo "0" > "$VERIFIER_LOG_DIR/reward.txt"
fi

exit $RC