"""
AES-128 Encryption/Decryption Performance Analysis
Comparing ECB and CBC Modes
Student ID: 0424312042
"""

import os
import sys
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


STUDENT_ID = "0424312042"
INPUT_FILE = "../dummy_file_100mb.txt"


def generate_aes128_key(student_id):
    # AES-128 key = student ID padded with '0' to 16 bytes
    key = student_id.ljust(16, '0').encode('utf-8')
    return key


def perform_aes128_ecb(data, key):
    padded_data = pad(data, AES.block_size)

    # Encryption
    cipher_enc = AES.new(key, AES.MODE_ECB)
    start_time = time.perf_counter()
    encrypted_data = cipher_enc.encrypt(padded_data)
    enc_time = time.perf_counter() - start_time

    # Decryption
    cipher_dec = AES.new(key, AES.MODE_ECB)
    start_time = time.perf_counter()
    decrypted_padded = cipher_dec.decrypt(encrypted_data)
    decrypted_data = unpad(decrypted_padded, AES.block_size)
    dec_time = time.perf_counter() - start_time

    return encrypted_data, decrypted_data, enc_time, dec_time


def perform_aes128_cbc(data, key):
    iv = get_random_bytes(AES.block_size)
    padded_data = pad(data, AES.block_size)

    # Encryption
    cipher_enc = AES.new(key, AES.MODE_CBC, iv)
    start_time = time.perf_counter()
    encrypted_data = cipher_enc.encrypt(padded_data)
    enc_time = time.perf_counter() - start_time

    # Decryption
    cipher_dec = AES.new(key, AES.MODE_CBC, iv)
    start_time = time.perf_counter()
    decrypted_padded = cipher_dec.decrypt(encrypted_data)
    decrypted_data = unpad(decrypted_padded, AES.block_size)
    dec_time = time.perf_counter() - start_time

    return encrypted_data, decrypted_data, enc_time, dec_time, iv


def main():
    print("=" * 70)
    print("AES-128 Encryption/Decryption Performance Analysis (ECB vs CBC)")
    print("=" * 70)

    # Generate and display key
    aes_key = generate_aes128_key(STUDENT_ID)
    print("\nEncryption Details:")
    print("-" * 50)
    print(f"Student ID: {STUDENT_ID}")
    print(f"Algorithm: AES (Advanced Encryption Standard)")
    print(f"Key Size: 128-bit (16 bytes)")
    print(f"AES-128 Key (hex): {aes_key.hex()}")
    print(f"Block Size: 16 bytes")

    # Check if input file exists
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, INPUT_FILE)

    if not os.path.exists(input_path):
        print(f"\nError: Input file not found at {input_path}")
        sys.exit(1)

    # Read input file
    file_size = os.path.getsize(input_path)
    print(f"Input File Size: 100 MB")

    with open(input_path, 'rb') as f:
        plaintext = f.read()

    print("\nPerforming encryption and decryption analysis...")
    print("-" * 50)

    # ECB Mode
    print("\n[ECB Mode]")
    encrypted_ecb, decrypted_ecb, enc_time_ecb, dec_time_ecb = perform_aes128_ecb(plaintext, aes_key)
    ecb_verified = plaintext == decrypted_ecb
    ecb_enc_speed = (file_size / (1024 * 1024)) / enc_time_ecb
    ecb_dec_speed = (file_size / (1024 * 1024)) / dec_time_ecb

    print(f"  Encryption Time: {enc_time_ecb:.6f} seconds")
    print(f"  Decryption Time: {dec_time_ecb:.6f} seconds")
    print(f"  Encryption Speed: {ecb_enc_speed:.2f} MB/s")
    print(f"  Decryption Speed: {ecb_dec_speed:.2f} MB/s")
    print(f"  Data Integrity Verified: {'Yes' if ecb_verified else 'No'}")

    # CBC Mode
    print("\n[CBC Mode]")
    encrypted_cbc, decrypted_cbc, enc_time_cbc, dec_time_cbc, iv = perform_aes128_cbc(plaintext, aes_key)
    cbc_verified = plaintext == decrypted_cbc
    cbc_enc_speed = (file_size / (1024 * 1024)) / enc_time_cbc
    cbc_dec_speed = (file_size / (1024 * 1024)) / dec_time_cbc

    print(f"  IV (hex): {iv.hex()}")
    print(f"  Encryption Time: {enc_time_cbc:.6f} seconds")
    print(f"  Decryption Time: {dec_time_cbc:.6f} seconds")
    print(f"  Encryption Speed: {cbc_enc_speed:.2f} MB/s")
    print(f"  Decryption Speed: {cbc_dec_speed:.2f} MB/s")
    print(f"  Data Integrity Verified: {'Yes' if cbc_verified else 'No'}")

    # Comparative Summary
    print("\n" + "=" * 70)
    print("Comparative Summary: ECB vs CBC")
    print("=" * 70)
    print(f"{'Mode':<10} {'Enc Time(s)':<15} {'Dec Time(s)':<15} {'Enc Speed(MB/s)':<18} {'Dec Speed(MB/s)':<18} {'Verified'}")
    print("-" * 90)
    print(f"{'ECB':<10} {enc_time_ecb:<15.6f} {dec_time_ecb:<15.6f} {ecb_enc_speed:<18.2f} {ecb_dec_speed:<18.2f} {'Yes' if ecb_verified else 'No'}")
    print(f"{'CBC':<10} {enc_time_cbc:<15.6f} {dec_time_cbc:<15.6f} {cbc_enc_speed:<18.2f} {cbc_dec_speed:<18.2f} {'Yes' if cbc_verified else 'No'}")
    print("-" * 90)

    # Performance Difference
    enc_diff = ((enc_time_cbc - enc_time_ecb) / enc_time_ecb) * 100
    dec_diff = ((dec_time_cbc - dec_time_ecb) / dec_time_ecb) * 100

    print(f"\nPerformance Difference (CBC vs ECB):")
    print(f"  Encryption: CBC is {abs(enc_diff):.2f}% {'slower' if enc_diff > 0 else 'faster'} than ECB")
    print(f"  Decryption: CBC is {abs(dec_diff):.2f}% {'slower' if dec_diff > 0 else 'faster'} than ECB")


if __name__ == "__main__":
    main()
