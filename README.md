# 🫀 Bulanık Üç Değerli Mantık ile Kalp Hastalığı Risk Tahmini

> Makine Öğrenmesi Ödevi — Khushal & Fatima (2025) makalesinin uygulaması

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📋 Proje Hakkında

Bu proje, **Khushal & Fatima (2025)** tarafından önerilen *Fuzzy Three-Valued Logic* (Bulanık Üç Değerli Mantık) mimarisini kalp hastalığı risk tahminine uygular.

Geleneksel makine öğrenmesi yalnızca **0 (risk yok)** veya **1 (risk var)** çıktısı üretirken, bu çalışma **0.5 (risk olabilir)** sınıfını ekleyerek belirsizlikleri de kapsayan üç değerli bir tahmin sistemi sunar.

**Referans Makale:**
> Khushal, R. & Fatima, U. (2025). *A novel fuzzy three-valued logic computational framework in machine learning for medicine dataset.* Computers in Biology and Medicine, 186, 109636.

---

## 🗂️ Proje Yapısı

```
📦 proje/
├── 📓 MLU2.ipynb          # Ana Colab not defteri (veri işleme + model eğitimi)
├── 🖥️  app.py              # Streamlit arayüzü
├── 🗄️  heart_disease.db    # SQLite veritabanı (otomatik oluşturulur)
├── 📊 cardio_train.csv    # Ham veri seti (Kaggle'dan indirilir)
└── 📄 README.md
```

---

## ⚙️ Kurulum

### 1. Gereksinimler

```bash
pip install pandas numpy scikit-learn matplotlib streamlit sqlite3
```

### 2. Veri Setini İndir

Kaggle'dan veri setini indirin:
[🔗 Cardiovascular Disease Dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset)

`cardio_train.csv` dosyasını proje klasörüne koyun.

### 3. Not Defterini Çalıştır

Google Colab'da `MLU2.ipynb` dosyasını açın ve tüm hücreleri sırayla çalıştırın.

### 4. Streamlit Arayüzünü Başlat

```bash
streamlit run app.py
```

Tarayıcınızda `http://localhost:8501` adresine gidin.

---

## 🔬 Metodoloji

### Veri Seti
| Özellik | Değer |
|---|---|
| Ham kayıt sayısı | 70.000 |
| Temizleme sonrası | 68.614 |
| Girdi değişkeni | 11 |
| Çıktı değişkeni | İkili (0/1) |

### Bulanık Dönüşüm (Fuzzification)

Sigara **(x)**, Alkol **(y)** ve Fiziksel Aktivite **(¬z)** değişkenleri karşılaştırılarak **Diğer Faktörler (θ)** oluşturulur:

```
θ = 0    →  x = y = ¬z = 0   (hiçbir risk faktörü yok)
θ = 1    →  x = y = ¬z = 1   (tüm risk faktörleri mevcut)
θ = 0.5  →  diğer tüm durumlar (belirsizlik)
```

| θ Değeri | Anlam | Kayıt Sayısı |
|---|---|---|
| 0.0 | Risk Yok | 48.513 |
| 0.5 | Belirsiz | 19.824 |
| 1.0 | Risk Var | 277 |

### 12 Karar Kuralı

| Cinsiyet | Yaş | Diğer Faktörler | Sonuç |
|---|---|---|---|
| Kadın | < 55 | 0 | Risk Yok |
| Kadın | < 55 | 0.5 | Risk Olabilir |
| Kadın | < 55 | 1 | Risk Var |
| Kadın | ≥ 55 | 0 | Risk Olabilir |
| Kadın | ≥ 55 | 0.5 | Risk Olabilir |
| Kadın | ≥ 55 | 1 | Risk Var |
| Erkek | < 45 | 0 | Risk Yok |
| Erkek | < 45 | 0.5 | Risk Olabilir |
| Erkek | < 45 | 1 | Risk Var |
| Erkek | ≥ 45 | 0 | Risk Olabilir |
| Erkek | ≥ 45 | 0.5 | Risk Olabilir |
| Erkek | ≥ 45 | 1 | Risk Var |

---

## 📊 Sonuçlar

### Doğruluk Karşılaştırması

| Model | Normal | Modified |
|---|---|---|
| GNB | 0.71 | 1.00 |
| SVM | 0.73 | 1.00 |
| AdaBoost | 0.73 | 1.00 |
| DT | 0.73 | 1.00 |
| KNN | 0.72 | 1.00 |
| RF | 0.74 | 1.00 |
| GB | 0.74 | 1.00 |

### Hesaplama Süresi Karşılaştırması (saniye)

| Model | Normal | Modified |
|---|---|---|
| GNB | 0.05s | 0.01s |
| SVM | 469.52s | 0.08s |
| AdaBoost | 1.76s | 1.00s |
| DT | 0.11s | 0.01s |
| KNN | 0.89s | 1.27s |
| RF | 1.34s | 0.14s |
| GB | 3.51s | 2.11s |

---

## 🖥️ Streamlit Arayüzü

Kullanıcıdan 5 girdi alınır:

- **Cinsiyet** — Kadın / Erkek
- **Yaş**
- **Sigara** — Evet / Hayır
- **Alkol** — Evet / Hayır
- **Fiziksel Aktivite** — Evet / Hayır

Sistem 12 bulanık kuralı uygulayarak üç sonuçtan birini döndürür:

| Sonuç | Renk | Anlam |
|---|---|---|
| ✅ RİSK YOK | Yeşil | Kalp hastalığı riski tespit edilmedi |
| ⚠️ RİSK OLABİLİR | Sarı | Eksik sağlıklı alışkanlıkları hayatınıza ekleyin |
| 🔴 RİSK VAR | Mor | Lütfen en kısa sürede doktora başvurun |

---

## 🗄️ Veritabanı Yapısı

SQLite veritabanı (`heart_disease.db`) üç tablo içerir:

| Tablo | İçerik |
|---|---|
| `raw_data` | Ham veri (70.000 kayıt) |
| `processed_data` | Temizlenmiş + fuzzify edilmiş veri (68.614 kayıt) |
| `model_results` | 7 modelin accuracy, precision ve süre sonuçları |

---

## 📚 Referans

```bibtex
@article{khushal2025fuzzy,
  title={A novel fuzzy three-valued logic computational framework 
         in machine learning for medicine dataset},
  author={Khushal, Rabia and Fatima, Ubaida},
  journal={Computers in Biology and Medicine},
  volume={186},
  pages={109636},
  year={2025},
  publisher={Elsevier}
}
```
