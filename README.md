# 🔐 VulnSight — Vulnerability Assessment & Reverse Engineering

## Overview
**VulnSight** is an AI-powered cybersecurity tool designed to automate vulnerability assessment and reporting. It analyzes uploaded scan files (JSON), applies machine learning models, and generates structured vulnerability reports with severity levels and recommendations.

---

## 🎯 Objective
- Automate vulnerability detection
- Reduce manual security analysis effort
- Improve accuracy and speed of reporting
- Prioritize critical security threats efficiently

---

## ⚙️ System Architecture

### 🖥️ Frontend
- Built using **HTML/CSS**
- Pages include:
  - `index.html` → Home page
  - `scan.html` → File upload interface
  - `results.html` → Displays detected vulnerabilities
  - `history.html` → Shows past scans

---

### ⚙️ Backend
- Built with **Flask (Python)**
- Handles:
  - File uploads
  - ML pipeline execution
  - Result generation
  - Scan history management

---

### 🧰 Utilities
- `scanner.py` → Extracts key fields from scan files  
- `vulnerability_processor.py` → Cleans and prepares data for ML model  

---

### 🤖 Machine Learning Models
- **TF-IDF Vectorizer** → Converts text into numerical features  
- **Classifier (SVM / Random Forest)** → Predicts vulnerability type & severity  
- **Label Encoders** → Convert predictions into readable labels  

---

## 🔄 Workflow

1. User uploads scan file (JSON)
2. System extracts vulnerability data
3. Data is cleaned and tokenized
4. TF-IDF converts text into feature vectors
5. ML model predicts:
   - Vulnerability type
   - Severity level
   - Suggested remediation
6. Results are displayed in the web interface

---

## 🔍 Key Features
- Automated vulnerability classification  
- Severity-based ranking (Critical → Low)  
- Fast processing (< 5 seconds per scan)  
- Scan history tracking  
- User-friendly web interface  

---

## 📊 Vulnerability Processing
- Extracted features include:
  - Description
  - File references
  - Risk level
- Data is sorted by severity for prioritization
- Focus on critical vulnerabilities first

---

## 📤 Output Format
Each scan report includes:
- Vulnerability Name  
- Severity Level  
- Suggested Fix / Recommendation  

---

## ⚠️ Limitations
- Depends on quality of input scan files  
- Cannot detect unknown (zero-day) vulnerabilities  
- No integration with external CVE databases or threat intelligence APIs  

---

## 🚀 Future Improvements
- Real-time network scanning  
- Integration with tools like OWASP ZAP / Burp Suite  
- API-based threat intelligence (CVE integration)  
- User authentication system  
- Model retraining using user feedback  

---

## 🧠 Conclusion
**VulnSight** demonstrates how machine learning can enhance cybersecurity by automating vulnerability detection and reporting. It improves efficiency, reduces manual effort, and helps prioritize security risks effectively.
