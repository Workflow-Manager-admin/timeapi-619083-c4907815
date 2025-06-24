#!/bin/bash
cd /tmp/kavia/workspace/code-generation/timeapi-619083-c4907815/time_api_backend_workspace/time_api_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

