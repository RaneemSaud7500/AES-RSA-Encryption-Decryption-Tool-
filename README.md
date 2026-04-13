# AES & RSA Encryption & Decryption Tool 

A Python-based graphical user interface (GUI) application designed to demonstrate and compare the implementation of **Symmetric** and **Asymmetric** encryption algorithms. 

---

##  Project Overview
This tool provides a hands-on experience with modern cryptography standards. It allows users to encrypt and decrypt text using two of the most widely used algorithms in the industry: **AES** and **RSA**.

###  Symmetric Encryption (AES)
* **Algorithm:** AES-128 (Advanced Encryption Standard).
* **Mode:** Fernet (CBC/HMAC).
* **Key Concept:** Uses a single secret key for both encryption and decryption.
* **Feature:** Implements **Initialization Vectors (IV)** to ensure that the same plaintext produces different ciphertexts each time (Semantic Security).

###  Asymmetric Encryption (RSA)
* **Algorithm:** RSA (Rivest–Shamir–Adleman).
* **Key Size:** 512-bit (for demonstration purposes).
* **Key Concept:** Uses a **Public Key** for encryption and a **Private Key** for decryption.
* **Feature:** Implemented with **PKCS1 Padding** to enhance security against pattern recognition.

---

##   Tech Stack
* **Language:** Python 
* **Libraries:**
    *  `cryptography`: For high-level AES implementation.
    * `rsa`: For asymmetric key generation and processing.
    * `Tkinter`: For the graphical user interface.

---

##  Features
* **Dual Encryption Modes:** Toggle between AES and RSA seamlessly.
* **Real-time Ciphertext Generation:** Watch the ciphertext change even for the same input due to randomized padding/IV.
* **Base64 Encoding:** Binary cipher data is automatically encoded to Base64 for human-readable display.
* **User-Friendly GUI:** Simple and intuitive layout for educational demonstrations.

---

##  Installation & Setup

1. **Clone the repository:**
   ```bash
   https://github.com/RaneemSaud7500/AES-RSA-Encryption-Decryption-Tool-.git
