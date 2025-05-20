

import pandas as pd
import csv
from mediapipe.tasks import python
from mediapipe.tasks.python import text

# STEP 1: Create a LanguageDetector object using MediaPipe's Language Detector model
base_options = python.BaseOptions(model_asset_path="detector.tflite")
options = text.LanguageDetectorOptions(base_options=base_options)
detector = text.LanguageDetector.create_from_options(options)

# Function to detect language of the entire text (row) with >50% probability for English or Spanish
def detect_english_spanish(text):
    detection_result = detector.detect(text)

    # If detections are found, check if English or Spanish has >50% probability
    if detection_result.detections:
        for detection in detection_result.detections:
            language = detection.language_code
            probability = detection.probability

            # Return only if it's English or Spanish with a probability > 0.90
            if language in ['en', 'es'] and probability > 0.97:
                return language, probability

    return "N/A", 0  # Return "N/A" if the condition is not met

# Function to process a CSV and output results for entire rows
def process_csv(input_file, output_file, batch_size=100):
    # Read input CSV
    df = pd.read_csv(input_file)
    sandesh = df.columns[0]
    # Write results to output CSV
    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Original Text', 'Detected Language', 'Probability'])

        # Process in batches for efficiency
        for i in range(0, len(df), batch_size):
            batch_df = df[i:i+batch_size]

            # Process each row of text
            for index, row in batch_df.iterrows():
                text = row[sandesh]  # Assuming a 'Text' column in the input CSV

                # Detect language for the entire row (text)
                language, probability = detect_english_spanish(text)

                # Write the result for the row
                csv_writer.writerow([
                    text,
                    language,
                    f"{probability:.2f}" if language != "N/A" else "N/A"  # Show probability only if valid language
                ])

# Example usage
input_csv = 'input.csv'  # Path to the input CSV file
output_csv = 'output_language_detection.csv'  # Path to save the output CSV file

# Process the CSV file
process_csv(input_csv, output_csv, batch_size=500)

print(f"Language detection results saved to {output_csv}")