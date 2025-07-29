#  Diatics - Hayvan Simülasyonu Projesi

Bu proje, farklı hayvan türlerinin doğal ortamda etkileşimlerini simüle eden bir Python uygulamasıdır. Proje, koyun, kurt, inek, tavuk, horoz, aslan ve avcı gibi çeşitli hayvan türlerinin davranışlarını modeller ve onların hayatta kalma stratejilerini görselleştirir.

##  Projeyi İndirme ve Kurulum

### 1. Depoyu İndirin
Projeyi yerel bilgisayarınıza indirmek için aşağıdaki yöntemlerden birini kullanabilirsiniz:

#### Git ile klonlama (önerilen):
```bash
git clone <repository-url>
cd diatics
```

#### ZIP dosyası olarak indirme:
- GitHub sayfasındaki "Code" butonuna tıklayın
- "Download ZIP" seçeneğini seçin
- İndirilen dosyayı istediğiniz klasöre çıkarın

### 2. Python Sanal Ortamı Oluşturun (Önerilen)
Projenin bağımlılıklarını izole etmek için sanal ortam kullanmanız önerilir:

```bash
# Sanal ortam oluştur
python -m venv diatics

# Sanal ortamı aktifleştir (Windows)
diatics\Scripts\activate

# Sanal ortamı aktifleştir (Linux/Mac)
source diatics/bin/activate
```

### 3. Gerekli Kütüphaneleri Kurun
Proje için gerekli Python kütüphanelerini yüklemek için:

```bash
pip install -r requirements.txt
```

Bu komut aşağıdaki kütüphaneleri yükleyecektir:
- **numpy**: Sayısal hesaplamalar için
- **matplotlib**: Grafik ve görselleştirme için
- **contourpy**: Kontur çizimi için
- **pillow**: Görüntü işleme için
- Ve diğer yardımcı kütüphaneler

## 🎮 Programı Çalıştırma

### Ana Simülasyonu Başlatın
Simülasyonu başlatmak için terminal/komut satırında:

```bash
python Main.py
```

### 📊 Beklenen Çıktı
Program çalıştırıldığında terminalde şu tür çıktıları göreceksiniz:

```
Toplam hayvan sayısı: 79

--- Adım 1 ---
[Hayvan hareketleri ve etkileşimleri]

--- Adım 2 ---
[Hayvan hareketleri ve etkileşimleri]

...

--- Adım 1000 ---
[Simülasyon tamamlandı]
```

Program 1000 adım boyunca çalışır ve her adımda:
- Hayvanların hareketlerini simüle eder
- Avcı-av ilişkilerini işler
- Üreme ve ölüm olaylarını yönetir
- Sonuçları terminal çıktısı olarak görüntüler

## 📁 Proje Yapısı

```
diatics/
├── Main.py           # Ana simülasyon dosyası
├── Animals.py        # Hayvan sınıfları tanımları
├── util.py          # Yardımcı fonksiyonlar
├── counts.json      # Başlangıç hayvan sayıları
├── requirements.txt # Gerekli kütüphaneler
└── README.md        # Bu dosya
```

## 🐺 Hayvan Türleri

Simülasyonda yer alan hayvan türleri:
- **Koyun** (Sheep): 30 adet (15 erkek, 15 dişi)
- **Kurt** (Wolf): 10 adet (5 erkek, 5 dişi)
- **İnek** (Cow): 10 adet (5 erkek, 5 dişi)
- **Aslan** (Lion): 8 adet (4 erkek, 4 dişi)
- **Tavuk** (Hen): 10 adet
- **Horoz** (Cockerel): 10 adet
- **Avcı** (Hunter): 1 adet

## ⚙️ Konfigürasyon

Hayvan sayılarını değiştirmek için `counts.json` dosyasını düzenleyebilirsiniz:

```json
[
    {"class": "Sheep", "count": 15, "gender": "Male"},
    {"class": "Sheep", "count": 15, "gender": "Female"},
    ...
]
```

## 🔧 Sorun Giderme

### Kütüphane Yükleme Sorunları
Eğer `pip install` komutu çalışmıyorsa:
```bash
pip install --upgrade pip
pip install -r requirements.txt --user
```

### Python Versiyonu
Bu proje Python 3.6 ve üzeri sürümlerle uyumludur. Python versiyonunuzu kontrol etmek için:
```bash
python --version
```

### Sanal Ortam Sorunları
Sanal ortamı deaktive etmek için:
```bash
deactivate
```

## 📄 Lisans

Bu proje MIT lisansı altında yayınlanmıştır.

