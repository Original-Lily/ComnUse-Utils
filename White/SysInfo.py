#!/usr/bin/env python
import platform
import psutil

def system_info():
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"CPU Cores: {psutil.cpu_count(logical=True)}")
    print(f"Memory: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")

if __name__ == "__main__":
    system_info()
