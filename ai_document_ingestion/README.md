

# Intelligent Document Processing with OCR + Gemini

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tWN--oRQcN2vS7RXWpqAwTB-h1jh5sfe?usp=sharing)


This project demonstrates how to build an **Intelligent Document Processing (IDP) pipeline** using **image preprocessing, OCR, and Google Gemini**.

It focuses on extracting structured information from **receipt images** by combining:
1. Image preprocessing with OpenCV  
2. Text extraction using Tesseract OCR  
3. AI-powered information extraction using Gemini  

The project uses the **SROIE receipt dataset** to simulate a real-world document understanding workflow.

These steps help you understand how modern AI systems process scanned documents, invoices, receipts, and forms in practical business settings.

---

## What This Project Covers

- Download and explore a receipt dataset  
- Preprocess document images for better OCR accuracy  
- Apply grayscale conversion, noise reduction, thresholding, and deskewing  
- Extract raw text using Tesseract OCR  
- Use Gemini to convert raw document content into structured information  
- Save extracted outputs for further use and analysis  

---

## Tech Stack Used

- **LLM**: Google Gemini  
- **OCR Engine**: Tesseract OCR  
- **Computer Vision**: OpenCV  
- **Language**: Python  
- **Environment**: Google Colab / Jupyter Notebook  
- **Dataset**: SROIE Receipt Dataset  

---

## Dataset Used

### SROIEv2: Receipt Dataset

The project works on the **SROIE receipt dataset**, which contains scanned receipt images and corresponding entity labels.

### What the dataset includes
- Train and test folders  
- Receipt images  
- Text/entity annotation files  

### Why this dataset is useful
It is a practical dataset for learning:
- OCR pipelines  
- receipt understanding  
- document AI  
- structured information extraction  

---

## Project 1: Document Image Preprocessing

### What it does
Improves receipt images before sending them to OCR.

### Features
- Converts image to grayscale  
- Reduces noise using Gaussian blur  
- Applies adaptive thresholding for binarization  
- Corrects skew in rotated receipts  
- Processes one image or all images in batch  

### Workflow
1. Load receipt image  
2. Convert to grayscale  
3. Apply noise reduction  
4. Perform binarization  
5. Correct image skew  
6. Save processed image  

### Why preprocessing matters
OCR works much better when images are clean, sharp, and properly aligned.  
This stage improves the readability of receipt text and increases extraction quality.

---

## Project 2: OCR-Based Text Extraction

### What it does
Uses **Tesseract OCR** to convert processed receipt images into machine-readable text.

### Features
- Reads processed receipt images  
- Extracts raw textual content  
- Saves OCR text output  
- Supports batch processing across multiple files  

### Workflow
1. Load processed image  
2. Pass image to Tesseract OCR  
3. Extract text  
4. Save text to output folder  

### Output generated
- Raw OCR text files for each receipt  
- Intermediate content ready for AI processing  

---

## Project 3: Structured Information Extraction with Gemini

### What it does
Uses **Google Gemini** to extract key business information from receipt content.

### Target fields
- Company  
- Date  
- Address  
- Total amount  

### Features
- Uses OCR text as input  
- Sends a structured prompt to Gemini  
- Generates clean extracted fields  
- Saves final result as structured JSON  

### Workflow
1. Read processed image and OCR text  
2. Create information extraction prompt  
3. Send content to Gemini  
4. Receive structured output  
5. Save extracted data in JSON format  

### Why this step is important
OCR only gives raw text.  
Gemini helps transform noisy document text into **usable structured data** that can power downstream systems like analytics, automation, and document search.

---

## End-to-End Pipeline

This project follows a complete IDP workflow:

1. Download receipt dataset  
2. Preprocess receipt images  
3. Extract text with Tesseract  
4. Send extracted content to Gemini  
5. Generate structured JSON output  

---

## Output Generated

- Preprocessed receipt images  
- OCR-extracted text files  
- Structured JSON outputs with receipt fields  
- Intermediate files for debugging and evaluation  

---

## Use Cases

- Receipt data extraction  
- Invoice processing  
- Expense management automation  
- Document digitization  
- Financial document understanding  
- Enterprise Intelligent Document Processing systems  

---

## Learning Outcome

By completing this project, you will understand:

- How document AI pipelines work  
- Why image preprocessing is important before OCR  
- How OCR converts document images into raw text  
- How LLMs can convert noisy text into structured information  
- How to combine computer vision + OCR + LLMs in one workflow  

This forms the foundation for building advanced systems like:

- AI invoice processors  
- Resume parsers  
- KYC document extractors  
- Automated document validation systems  
- End-to-end enterprise IDP pipelines  

---

## Notebook Highlights

The notebook includes:

- Dataset download and inspection  
- Image preprocessing step-by-step  
- OCR extraction using Tesseract  
- Prompt-based structured extraction with Gemini  
- Batch processing for multiple receipt images  

---

## 👤 Credits

Made with ❤️ by [Ashish Jangra](https://github.com/AshishJangra27)  
Powered by OpenCV, Tesseract OCR, and Google Gemini
