# Stamp Image Retrieval System

## 📌 Project Description

This project implements a content-based image retrieval system for postage stamps using classical computer vision methods.

The system retrieves visually similar postage stamps based on local feature descriptors and keypoint matching techniques implemented with OpenCV. The proposed approach relies on classical computer vision algorithms without using deep learning models.

---

## ⚙️ Technologies Used

- Python 3.x
- OpenCV
- NumPy

---

## 🧠 System Overview

The system consists of three main modules:

- **StampDescriptor** – extracts key visual features from images
- **StampMatcher** – performs feature matching between query and dataset images
- **Search Engine (search.py)** – manages search pipeline and ranking results

---

## 📁 Project Structure

```text
stamp-image-search/
│
├── stamp_dataset/     # Reference stamp images
├── query/             # Query images and distortion tests
├── stampdescriptor.py # Feature extraction
├── stampmatcher.py    # Image matching
├── search.py          # Search logic
├── main.py            # Entry point
├── stamps.csv         # Metadata
├── requirements.txt
└── README.md
```

---

## 🚀 Features

- Postage stamp matching using local feature descriptors
- Robustness to image transformations:
  - rotation
  - scaling
  - cropping
  - Gaussian blur
- Retrieval under real-world conditions (stamp placed on envelope)
- Support for BRISK and SIFT descriptors

---

## 📊 Experimental Results

The system was evaluated using multiple image distortions, including rotation, scaling, cropping, Gaussian blur, and real-world scene testing.

Experimental results demonstrated high robustness of the proposed approach, maintaining correct stamp retrieval in most test scenarios, even under significant image transformations.

---

## ▶️ How to Run

Run the search system using:

```bash
python main.py --db stamps.csv --stamp_dataset stamp_dataset --query query/test_original.jpg --sift 0
```

### Parameters

- `--db` – path to metadata CSV file
- `--stamp_dataset` – path to dataset images
- `--query` – query image for matching
- `--sift` – descriptor mode:
  - `0` – BRISK
  - `1` – SIFT

---
## 📌 Notes

This project was developed as part of a diploma thesis on image retrieval systems based on computer vision methods.


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

## 🇺🇦 Опис українською

Система пошуку поштових марок за зображенням, реалізована з використанням методів комп’ютерного зору на базі Python та OpenCV.

Система виконує пошук найбільш схожої марки на основі локальних дескрипторів ознак (BRISK/SIFT) та алгоритмів зіставлення ключових точок.

У межах дослідження проведено серію експериментів із поворотом, масштабуванням, обрізкою, розмиттям зображень, а також тестуванням у реальній сцені (марка на конверті).

Проєкт розроблено в рамках дипломної роботи.