# Stamp Image Retrieval System

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.x-blue" />
  <img src="https://img.shields.io/badge/OpenCV-CV2-green" />
  <img src="https://img.shields.io/badge/Status-Educational-lightgrey" />
</p>

### Content-Based Image Retrieval using classical Computer Vision (BRISK / SIFT)

Lightweight image retrieval system for matching postage stamps under real-world distortions and transformations.

## 📌 Project Description

This project implements a content-based image retrieval (CBIR) system for postage stamps using classical computer vision methods.

The system retrieves visually similar images based on local feature descriptors and keypoint matching techniques implemented with OpenCV. The proposed approach relies on classical computer vision algorithms without using deep learning models.

---

## ⚙️ Technologies Used

- Python 3.x
- OpenCV
- NumPy

---

## 🧠 System Architecture

The system consists of three main components:

- **StampDescriptor** – extraction of local visual features
- **StampMatcher** – feature matching and similarity estimation
- **Search Engine (search.py)** – search pipeline and ranking of results

---

## 📁 Project Structure

```text
stamp-image-search/
│
├── stamp_dataset/     # Reference stamp images
├── query/             # Query images and distortion tests
├── stampdescriptor.py # Feature extraction module
├── stampmatcher.py    # Feature matching module
├── search.py          # Search pipeline logic
├── main.py            # Entry point
├── stamps.csv         # Dataset metadata
├── requirements.txt
└── README.md
```

---

## 🚀 Key Features

- Content-based image retrieval using local feature descriptors
- Robustness to image transformations:
  - rotation
  - scaling
  - cropping
  - Gaussian blur
- Retrieval under real-world conditions (stamp placed on envelope)
- Support for BRISK and SIFT descriptors

---

## 📊 Experimental Evaluation

The system was evaluated on multiple test cases, including synthetic distortions and real-world scenes.

Experiments demonstrate that the proposed approach maintains high retrieval accuracy under significant geometric transformations and noise conditions.

---

## ▶️ How to Run

Run the system using:

```bash
python main.py --db stamps.csv --stamp_dataset stamp_dataset --query query/test_original.jpg --sift 0
```

### Parameters

- `--db` – path to metadata CSV file
- `--stamp_dataset` – path to dataset images
- `--query` – query image for matching
- `--sift` – descriptor selection:
  - `0` – BRISK
  - `1` – SIFT

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Required libraries:

```txt
opencv-python
numpy
```

---
## 📌 Notes

This project was developed as part of a diploma thesis focused on image retrieval systems based on computer vision methods.

---

## 🇺🇦 Опис українською

Розроблена система забезпечує пошук схожих зображень поштових марок із використанням методів комп’ютерного зору на базі Python та бібліотеки OpenCV.

Пошук виконується на основі локальних дескрипторів ознак (BRISK та SIFT) із застосуванням алгоритмів зіставлення ключових точок та оцінки схожості між зображеннями.

У межах дослідження проведено експериментальну перевірку роботи системи на наборах зображень із різними типами спотворень, зокрема поворотом, масштабуванням, обрізкою та розмиттям. Окремо проведено тестування системи в умовах, наближених до реальних сцен, із зображенням поштової марки на конверті, з додатковим застосуванням геометричних та фотометричних спотворень, зокрема повороту, масштабування та розмиття.

Отримані результати підтверджують стійкість та ефективність запропонованого підходу до геометричних перетворень та шумових спотворень.

Проєкт виконано в рамках дипломної роботи з комп’ютерного зору.