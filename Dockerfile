
FROM python:3.10-slim

WORKDIR /app

COPY mapper.py reducer.py ./
COPY input/ ./input/

CMD ["sh", "-c", "find input -type f -name '*.csv' -exec cat {} + | python3 mapper.py | LC_ALL=C sort -S 64M -T /tmp | python3 reducer.py"]
