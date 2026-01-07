import platform
import psutil


def main():
    print("=" * 60)
    print("System Specifications")
    print("=" * 60)
    print(f"OS: {platform.system()} {platform.version()}")
    print(f"Processor: {platform.processor()}")
    print(f"RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    print(f"Python Version: {platform.python_version()}")
    print("=" * 60)


if __name__ == "__main__":
    main()
