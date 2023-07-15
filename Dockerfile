FROM nikolaik/python-nodejs:python3.9-nodejs17
RUN sodo apt-get update \
    && sudo apt-get install -y --no-install-recommends ffmpeg \
    && sudo apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD bash start
