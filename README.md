# Executable-File-Analysis

This Python script calculates hashes and extracts strings from an executable file (.exe) using a combination of hashlib, subprocess, and strings64.exe. It is designed for analyzing executable files by providing valuable information like MD5, SHA-1, and SHA-256 hashes, as well as extracting readable strings from the file.

# Features
Hash Calculation: Generates MD5, SHA-1, and SHA-256 hashes for any specified file.
String Extraction: Uses the strings utility (via strings64.exe) to extract readable ASCII strings from an executable file, which is often helpful in digital forensics and malware analysis.

# Prerequisites
Python 3.x
strings64.exe from the Sysinternals Suite:
Download it from Microsoft Sysinternals.
Ensure the path to strings64.exe is correctly specified in the script.
