FROM python:3.11-slim-bookworm@sha256:247656641b9c748cb151e3604f86d81c4e7ee54226fcf9b5b271d4bf597ba156

WORKDIR /app

# Install pinned testing frameworks at image build time
RUN pip install --no-cache-dir \
    pytest==8.4.1 \
    pytest-json-ctrf==0.3.5

# Copy only the input raw log data file
COPY access.log /app/access.log

# Ensure standard verifier logging mount point exists
RUN mkdir -p /logs/verifier

CMD ["/bin/bash"]