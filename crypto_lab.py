import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import rsa
import base64

class CryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptography Lab 3 & 4")
        self.root.geometry("700x650")
        self.root.configure(bg="#f4f7f6")

        # --- إعداد مفاتيح التشفير ---
        self.aes_key = Fernet.generate_key()
        self.cipher_aes = Fernet(self.aes_key)
        (self.pub_key, self.priv_key) = rsa.newkeys(512)

        # --- تصميم الواجهة ---
        tk.Label(root, text="Cryptography Labs: Symmetric vs Asymmetric", font=("Arial", 18, "bold"), bg="#f4f7f6").pack(pady=20)

        tk.Label(root, text="Enter Plain Text Here:", bg="#f4f7f6").pack()
        self.input_text = tk.Text(root, height=3, width=60)
        self.input_text.pack(pady=10)

        frame_enc = tk.Frame(root, bg="#f4f7f6")
        frame_enc.pack(pady=10)

        self.btn_aes_enc = tk.Button(frame_enc, text="Encrypt AES (Symmetric)", command=self.encrypt_aes, bg="#007bff", fg="white")
        self.btn_aes_enc.grid(row=0, column=0, padx=20)
        self.aes_cipher_box = tk.Text(frame_enc, height=5, width=35)
        self.aes_cipher_box.grid(row=1, column=0, padx=10, pady=5)

        self.btn_rsa_enc = tk.Button(frame_enc, text="Encrypt RSA (Asymmetric)", command=self.encrypt_rsa, bg="#28a745", fg="white")
        self.btn_rsa_enc.grid(row=0, column=1, padx=20)
        self.rsa_cipher_box = tk.Text(frame_enc, height=5, width=35)
        self.rsa_cipher_box.grid(row=1, column=1, padx=10, pady=5)

        # القسم السفلي: أزرار فك التشفير
        frame_dec = tk.Frame(root, bg="#f4f7f6")
        frame_dec.pack(pady=20)

        self.btn_aes_dec = tk.Button(frame_dec, text="Decrypt AES", command=self.decrypt_aes, bg="#0056b3", fg="white")
        self.btn_aes_dec.grid(row=0, column=0, padx=20)
        self.aes_plain_box = tk.Text(frame_dec, height=5, width=35)
        self.aes_plain_box.grid(row=1, column=0, padx=10, pady=5)

        self.btn_rsa_dec = tk.Button(frame_dec, text="Decrypt RSA", command=self.decrypt_rsa, bg="#1e7e34", fg="white")
        self.btn_rsa_dec.grid(row=0, column=1, padx=20)
        self.rsa_plain_box = tk.Text(frame_dec, height=5, width=35)
        self.rsa_plain_box.grid(row=1, column=1, padx=10, pady=5)

    # --- دوال التشفير وفك التشفير ---
    def encrypt_aes(self):
        try:
            data = self.input_text.get("1.0", tk.END).strip().encode()
            if not data: return
            token = self.cipher_aes.encrypt(data)
            self.aes_cipher_box.delete("1.0", tk.END)
            self.aes_cipher_box.insert(tk.END, token.decode())
        except Exception as e: messagebox.showerror("Error", str(e))

    def decrypt_aes(self):
        try:
            token = self.aes_cipher_box.get("1.0", tk.END).strip().encode()
            plain = self.cipher_aes.decrypt(token)
            self.aes_plain_box.delete("1.0", tk.END)
            self.aes_plain_box.insert(tk.END, plain.decode())
        except Exception as e: messagebox.showerror("Error", "Check Cipher Text")

    def encrypt_rsa(self):
        try:
            message = self.input_text.get("1.0", tk.END).strip().encode()
            if not message: return
            crypto = rsa.encrypt(message, self.pub_key)
            self.rsa_cipher_box.delete("1.0", tk.END)
            self.rsa_cipher_box.insert(tk.END, base64.b64encode(crypto).decode())
        except Exception as e: messagebox.showerror("Error", str(e))

    def decrypt_rsa(self):
        try:
            crypto_b64 = self.rsa_cipher_box.get("1.0", tk.END).strip().encode()
            crypto = base64.b64decode(crypto_b64)
            plain = rsa.decrypt(crypto, self.priv_key)
            self.rsa_plain_box.delete("1.0", tk.END)
            self.rsa_plain_box.insert(tk.END, plain.decode())
        except Exception as e: messagebox.showerror("Error", "Check RSA Cipher")

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoApp(root)
    root.mainloop()