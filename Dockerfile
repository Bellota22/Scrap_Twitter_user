FROM python:3.10-bullseye

WORKDIR /app


# Install OS dependencies
RUN apt-get update && apt-get install -y \
    bash \
    curl \
    jq \
    unzip \
    wget \
    apt-transport-https \
    ca-certificates \
    gnupg \
    --no-install-recommends \
 && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install latest ChromeDriver
RUN CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Copy and install Python dependencies

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy application files
COPY . .

# Expose default port
EXPOSE 80

# Set the entrypoint
CMD ["uvicorn", "main:app", "--port", "80" ]
