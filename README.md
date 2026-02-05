# Behavioral Analysis of TLS Handshakes for Man-in-the-Middle (MITM) Attack Detection

## Overview
Transport Layer Security (TLS) is the foundation of secure communication on the Internet. While TLS provides strong encryption, Man-in-the-Middle (MITM) attacks can still occur by manipulating the TLS handshake phase without decrypting application data. Such attacks often leave detectable behavioral anomalies in handshake metadata.

This project implements a behavioral anomaly detection system that analyzes TLS handshake characteristics to identify potential MITM attacks. The approach does not rely on payload decryption, preserving privacy while enabling effective detection through statistical and machine learning–based analysis.

---

## Objectives
- Capture and analyze TLS handshake traffic from network traces
- Extract meaningful behavioral features from TLS handshakes
- Model normal TLS behavior using unsupervised machine learning
- Detect anomalies indicative of MITM attacks
- Demonstrate privacy-preserving network security analysis

---

## Key Features
- TLS handshake analysis without decrypting encrypted traffic
- Behavioral anomaly detection using Isolation Forest
- Compatible with real-world network captures (PCAP files)
- Modular and extensible Python implementation
- Suitable for academic, research, and educational use

---

## Project Architecture

PCAP (TLS Traffic)  
→ TLS Handshake Feature Extraction  
→ Baseline Behavior Modeling (Isolation Forest)  
→ Anomaly Detection  
→ MITM Suspicion Classification  

---

## Directory Structure

tls-mitm-detection/  
├── capture/  
│   └── tls_traffic.pcap  
├── extract_features.py  
├── train_baseline.py  
├── detect_mitm.py  
├── tls_features.csv  
├── mitm_detection_results.csv  
├── tls_baseline_model.pkl  
├── requirements.txt  
└── README.md  

---

## Tools and Technologies
- Python 3.9 or higher
- PyShark
- Pandas
- NumPy
- Scikit-learn
- Wireshark / TShark

---

## Installation

Clone the repository:

git clone https://github.com/RishiKrishnah/Man-in-the-Middle-MITM-Attack-Detection.git
cd tls-mitm-detection

Install dependencies:
pip install -r requirements.txt


Ensure Wireshark and TShark are installed and accessible via PATH:


tshark --version


---

## Usage

### Step 1: Capture TLS Traffic
Capture HTTPS traffic using Wireshark and save it as:


capture/tls_traffic.pcap

Apply the display filter:


tls.handshake

### Step 2: Extract TLS Handshake Features
python extract_features.py

Output file:
tls_features.csv


### Step 3: Train Baseline TLS Behavior Model
python train_baseline.py

Output file:
tls_baseline_model.pkl


### Step 4: Detect MITM Anomalies
python detect_mitm.py

Output file:
mitm_detection_results.csv

---

## Detection Methodology
The system models normal TLS handshake behavior using the following features:
- TLS handshake packet length
- Certificate length

An Isolation Forest algorithm is trained on normal traffic to establish a baseline. TLS handshakes that deviate significantly from this baseline are classified as anomalous and labeled as "MITM Suspected".

---

## Sample Output

Normal            121  
MITM Suspected      7  

This indicates that a subset of TLS handshakes exhibited abnormal behavior consistent with potential MITM interference.

---

## Limitations
- Anomalies indicate suspicion, not definitive confirmation of MITM attacks
- Detection accuracy depends on the quality and diversity of baseline traffic
- TLS 1.3 restricts visibility of certain handshake fields
- Environmental factors may introduce false positives

---

## Future Enhancements
- Real-time TLS traffic monitoring
- Cipher suite downgrade detection
- Certificate issuer and chain validation
- Support for additional TLS handshake features
- Visualization dashboard for anomaly analysis

---

## Ethical Considerations
This project analyzes only TLS handshake metadata and does not decrypt encrypted application data. It is intended strictly for educational, research, and defensive security purposes.

---

## License
MIT License

---

## Author
Rishi Krishna  
B.Tech Computer Science and Engineering  
Vellore Institute of Technology, Chennai

