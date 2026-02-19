# SVD Görüntü Sıkıştırma Web Uygulaması

Görüntü kalitesini korurken dosya boyutlarını küçültmek için **Tekil Değer Ayrışımı (SVD - Singular Value Decomposition)** yöntemini kullanan, profesyonel ve web tabanlı bir görüntü sıkıştırma aracı. Bu proje, lineer cebir ve sinyal işleme konseptlerinin modern ve kullanıcı dostu bir arayüz üzerinden pratik bir uygulamasını sunar.

## 🚀 Özellikler

* **Toplu İşlem (Batch Processing):** Aynı anda birden fazla görüntüyü yükleme ve işleme imkanı.
* **Dinamik Rank Seçimi (k değeri):** Kullanıcılar, tutulacak tekil değer sayısını (k) belirleyerek, görüntü kalitesi ile sıkıştırma oranı arasındaki dengeyi gerçek zamanlı olarak gözlemleyebilir.
* **Detaylı Analiz:** Sistem her görsel için şunları otomatik olarak hesaplar ve gösterir:
    * Orijinal vs. Sıkıştırılmış Matris Boyutu
    * Sıkıştırma Oranı
    * Toplam Boyut Kazancı (%)
* **Modern Arayüz (UI/UX):** Duyarlı (responsive) Flexbox ızgara yapısı, animasyonlu SVG geri bildirimleri ve temiz tasarım.

## 🧮 Matematiksel Altyapı

Bu uygulamanın temeli Tekil Değer Ayrışımı (SVD) teoremine dayanır. Gri tonlamalı görüntümüzü temsil eden herhangi bir reel A matrisi, üç farklı matrisin çarpımı şeklinde ifade edilebilir:

A = U Σ V^T

Σ köşegen matrisindeki yalnızca en büyük k adet tekil değeri (k < rank(A) olacak şekilde) tutarak, "kesilmiş" (truncated) bir SVD oluştururuz. Bu işlem, orijinal görüntü matrisine en uygun yaklaşımı sağlarken, onu saklamak için gereken veri miktarını da önemli ölçüde azaltır.

## 🛠️ Kullanılan Teknolojiler

* **Arka Plan (Backend):** Python, Flask, Werkzeug
* **Matematik & Görüntü İşleme:** NumPy, scikit-image, Matplotlib
* **Ön Yüz (Frontend):** HTML5, CSS3 (Flexbox), Saf JavaScript (DOM manipülasyonu ve SVG animasyonları)

## ⚙️ Kurulum ve Kullanım

1. **Projeyi bilgisayarınıza indirin (Klonlayın):**
   git clone https://github.com/KULLANICI_ADIN/svd-image-compression.git
   cd svd-image-compression

2. **Gerekli kütüphaneleri yükleyin:**
   pip install -r requirements.txt

3. **Uygulamayı çalıştırın:**
   python app.py

4. **Web arayüzüne erişin:**
   Tarayıcınızı açın ve http://127.0.0.1:5000 adresine gidin.
