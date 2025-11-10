FROM python:3.10-slim

WORKDIR /app

# 1️⃣ Устанавливаем системные зависимости + Chrome
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \
    curl \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libasound2 \
    libxshmfence1 \
    libgbm-dev \
    libgtk-3-0 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# 2️⃣ Добавляем репозиторий Google Chrome и ставим браузер
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# 3️⃣ Устанавливаем ChromeDriver соответствующей версии
RUN CHROME_VERSION=$(google-chrome --version | grep -oE '[0-9.]+' | head -1) && \
    DRIVER_VERSION=$(wget -qO- "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_${CHROME_VERSION%.*}") && \
    wget -O /tmp/chromedriver.zip "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${DRIVER_VERSION}/linux64/chromedriver-linux64.zip" && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver.zip /usr/local/bin/chromedriver-linux64

# 4️⃣ Устанавливаем Python зависимости
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5️⃣ Копируем весь проект
COPY . .

# 6️⃣ Переменные окружения
ENV PYTHONUNBUFFERED=1
ENV PATH="/usr/local/bin:$PATH"

# 7️⃣ Точка входа — запуск pytest
CMD ["pytest", "-v", "--maxfail=1"]