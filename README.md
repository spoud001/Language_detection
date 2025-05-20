# Language Detection Script (MediaPipe)

This script detects whether text entries are written in English or Spanish with high confidence using MediaPipe's TFLite language detection model.

## 📌 Features
- Uses a compact MediaPipe TFLite model
- Classifies text as English or Spanish with ≥ 97% confidence
- Processes large datasets in batches
- Outputs results to a new CSV file with language and probability

## 🛠 Technologies
- Python
- MediaPipe
- pandas

## 📂 Input Format
The input file should be a CSV containing a column of text values (e.g., place names).

**Example:**
```
Place Name
San Pedro Sula
Pine Ridge
Tikal
```

## 📈 Output Format
The script generates a new CSV with:
- Detected language (`en`, `es`, or `N/A`)
- Confidence probability

**Example Output:**
```
Place Name         | Language | Probability
------------------ | -------- | -----------
San Pedro Sula     | es       | 0.99
Pine Ridge         | en       | 0.98
Unknown Settlement | N/A      | N/A
```

## 🚀 How to Use



1. **Download the MediaPipe TFLite model**
```bash
wget -O detector.tflite https://storage.googleapis.com/mediapipe-models/language_detector/language_detector/float32/latest/language_detector.tflite
```

2. **Run the script**
```bash
python language_detection.py
```

Make sure your `input.csv` file is in the same directory.

## 📘 Project Context
This script was originally developed as part of a broader project exploring **Meso-American Landscapes**, but can be used for any language classification task involving English and Spanish.

