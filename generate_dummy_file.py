"""
Dummy File Generator for Cryptography Assignment
Generates a 100MB test file with random alphanumeric characters
Student ID: 0424312042
"""

import os
import string
import random


def generate_100mb_file(output_file_path):
    """
    Generate a 100MB file with random alphanumeric characters.
    Writes data in 1MB chunks for memory efficiency.
    """
    # 100 MB in bytes
    target_size = 100 * 1024 * 1024
    chunk_size = 1024 * 1024  # 1 MB chunks

    # Characters to use (A-Z, a-z, 0-9)
    characters = string.ascii_letters + string.digits

    print(f"Generating 100MB dummy file: {output_file_path}")
    print(f"Target size: {target_size / (1024 * 1024):.0f} MB")
    print(f"Characters used: A-Z, a-z, 0-9")
    print("-" * 50)

    bytes_written = 0
    with open(output_file_path, 'w', encoding='utf-8') as f:
        while bytes_written < target_size:
            # Generate 1MB chunk of random characters
            chunk = ''.join(random.choices(characters, k=chunk_size))
            f.write(chunk)
            bytes_written += chunk_size

            # Progress indicator
            progress = (bytes_written / target_size) * 100
            print(f"\rProgress: {progress:.1f}% ({bytes_written // (1024 * 1024)} MB / {target_size // (1024 * 1024)} MB)", end="")

    print(f"\n\nFile generated successfully!")
    print(f"File path: {output_file_path}")
    print(f"Actual size: {os.path.getsize(output_file_path) / (1024 * 1024):.2f} MB")


def main():
    print("=" * 60)
    print("Dummy File Generator for Cryptography Assignment")
    print("=" * 60)

    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, "dummy_file_100mb.txt")

    # Check if file already exists
    if os.path.exists(output_file):
        print(f"\nFile already exists: {output_file}")
        print(f"Current size: {os.path.getsize(output_file) / (1024 * 1024):.2f} MB")
        response = input("\nDo you want to regenerate the file? (y/n): ").strip().lower()
        if response != 'y':
            print("File generation skipped.")
            return

    print()
    generate_100mb_file(output_file)

    print("\n" + "=" * 60)
    print("Done! You can now run the encryption analysis scripts.")
    print("=" * 60)


if __name__ == "__main__":
    main()
