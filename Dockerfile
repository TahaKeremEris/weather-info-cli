# Python 3.9-slim tabanlı bir imaj kullanıyoruz
FROM python:3.9-slim

# Çalışma dizini oluştur ve ayarla
WORKDIR /app

# Proje dosyalarını kopyala
COPY . .

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Varsayılan komut: python dosyanızı çalıştırmak
ENTRYPOINT ["python", "WeatherInfoCLI.py"]