# Fernet Cipher Tool

A command-line tool for encrypting and decrypting messages and files using Fernet symmetric encryption.

Built as Portfolio Piece #1 — a Python OOP rewrite of a basic crypto encoder/decoder.

---

## What it does

- Encrypt and decrypt text messages from the command line
- Encrypt and decrypt entire files in place
- Generate new Fernet keys or use an existing one

---

## Project structure

```
fernet_cipher.py   — Crypt class: core encrypt and decrypt logic
file_encrypt.py    — FileOps class: file read, encrypt/decrypt, and write
main.py            — CLI entry point: user interaction and flow control
```

---

## Requirements

Python 3.8 or higher and the `cryptography` library.

```bash
pip install cryptography
```

---

## Usage

Run the tool from the command line:

```bash
python main.py
```

You will be prompted to choose between working with a **file** or a **message**.

### Encrypt a message

```
Do you want to work with a file or just a message: m
Message you want to encrypt/decrypt: hello world
Do you want to encrypt or decrypt? (E)|(D): e
Do you have a key? (Y)es|(N)o: n
```

A new key will be generated and printed. Save it — you will need it to decrypt.

### Decrypt a message

```
Do you want to work with a file or just a message: m
Message you want to encrypt/decrypt: <your encrypted token>
Do you want to encrypt or decrypt? (E)|(D): d
Please enter key for decryption: <your key>
```

### Encrypt a file

```
Do you want to work with a file or just a message: f
Enter path: lorem.txt
Do you want to encrypt or decrypt? (E)|(D): e
Do you have a key? (Y)es|(N)o: n
```

The file is encrypted in place. Save the generated key.

### Decrypt a file

```
Do you want to work with a file or just a message: f
Enter path: lorem.txt
Do you want to encrypt or decrypt? (E)|(D): d
Please enter key for decryption: <your key>
```

---

## Important

- **Save your key.** If you lose it, encrypted data cannot be recovered.
- **Never hardcode keys** in source code or commit them to GitHub.
- Fernet uses AES-128-CBC with HMAC-SHA256 for authenticated encryption.

---

## What I learned building this

- Python OOP — classes, static methods, separation of concerns
- Applied symmetric encryption using the `cryptography` library
- Error handling with `try/except` for invalid tokens and wrong keys
- Splitting a project across multiple modules with clean imports
