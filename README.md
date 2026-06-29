# Lesson 3: StegoGuard Image Forensics with GitHub Actions

## Project Title

**StegoGuard: Detecting Suspicious Hidden Data in Images Using GitHub Actions**

## Goal

In this lab, students learn how GitHub Actions can automatically check image files for suspicious hidden data.

This project connects cybersecurity concepts from:

- Steganography
- Digital forensics
- File signatures
- Automated security scanning
- GitHub Actions

---

## Important Safety Note

This project is for educational and defensive cybersecurity learning only.

Do not use steganography to hide illegal content, bypass monitoring, or exfiltrate sensitive data.

In this lab, we only use harmless demo text to understand how hidden appended data can be detected.

---

## Repository Structure

```text
stegoguard-image-forensics/
├── lab_mode.txt
├── make_demo_image.py
├── scanner.py
├── images/
│   └── README.md
└── .github/
    └── workflows/
        └── stegoguard.yml
```

---

## How the System Works

```text
Student edits lab_mode.txt
        ↓
GitHub Actions starts automatically
        ↓
Python creates a demo PNG image
        ↓
StegoGuard scans the generated image
        ↓
If hidden appended data is found, the workflow fails
        ↓
If no suspicious data is found, the workflow passes
```

---

## What StegoGuard Detects

StegoGuard performs simple image-forensics checks:

1. Checks whether PNG, JPG, and GIF files have the correct file signature.
2. Checks whether extra data exists after the real image ending marker.
3. Checks whether suspicious keywords appear inside the image file bytes.

In this lab, the suspicious image contains harmless appended text after the PNG ending marker.

This simulates one simple way data can be hidden inside a file.

---

# Student Instructions

## Step 1: Fork the Instructor Repository

Open the instructor repository in your browser:

```text
https://github.com/RafikHamza/stegoguard-image-forensics
```

Then:

```text
1. Click Fork
2. Select your GitHub account
3. Keep the repository name, or rename it to:
   stegoguard-image-forensics-student
4. Click Create fork
```

Do not use terminal commands.

---

## Step 2: Check the Initial Scan

Open your forked repository.

Go to:

```text
Actions
```

Select:

```text
StegoGuard Image Forensics
```

Run the workflow if needed.

Expected result:

```text
Passed
```

This means the generated image is clean.

The file `lab_mode.txt` currently contains:

```text
clean
```

---

## Step 3: Create a Suspicious Image

Open:

```text
lab_mode.txt
```

Click the pencil icon.

Change:

```text
clean
```

to:

```text
suspicious
```

Click:

```text
Commit changes
```

---

## Step 4: See the Failed Scan

Go to:

```text
Actions
```

Click the latest:

```text
StegoGuard Image Forensics
```

Expected result:

```text
Failed
```

This is good.

It means StegoGuard detected suspicious hidden data inside the generated image.

The log should show something like:

```text
Status: SUSPICIOUS
- Extra data found after PNG ending marker
- Suspicious keyword found inside file: hidden_message
```

Take a screenshot of the failed scan.

---

## Step 5: Fix the Problem

Open:

```text
lab_mode.txt
```

Change:

```text
suspicious
```

back to:

```text
clean
```

Click:

```text
Commit changes
```

---

## Step 6: See the Passed Scan

Go back to:

```text
Actions
```

Open the latest workflow run.

Expected result:

```text
Passed
```

Take a screenshot of the passed scan.

---

# Explanation of the Main Files

## `lab_mode.txt`

This file controls the lab.

If it contains:

```text
clean
```

then the workflow creates a normal PNG image.

If it contains:

```text
suspicious
```

then the workflow creates a PNG image with harmless hidden demo text appended after the image ending marker.

---

## `make_demo_image.py`

This script creates a small valid PNG image.

When `lab_mode.txt` is set to `suspicious`, the script appends hidden demo text to the image file.

---

## `scanner.py`

This is the StegoGuard scanner.

It checks image files in the `images/` folder and prints a report.

If suspicious hidden data is found, the script exits with an error code, causing GitHub Actions to fail.

---

## `.github/workflows/stegoguard.yml`

This is the GitHub Actions workflow.

It runs automatically when students commit changes.

The workflow:

```text
1. Checks out the repository
2. Reads lab_mode.txt
3. Creates the demo image
4. Runs the StegoGuard scanner
5. Passes or fails based on the scanner result
```

---

# What Students Learn

By completing this lab, students learn:

1. What steganography is
2. What image forensics is
3. How image files have signatures and ending markers
4. How hidden appended data can be detected
5. How GitHub Actions can automate cybersecurity checks
6. How a workflow can block suspicious files before they are accepted

---

# Submission Requirements

Submit:

```text
1. Your forked GitHub repository link
2. Screenshot of the initial passed scan
3. Screenshot of the failed scan after changing lab_mode.txt to suspicious
4. Screenshot of the final passed scan after changing lab_mode.txt back to clean
5. Short report
```

---

# Short Report Requirements

Write 1 page answering:

```text
1. What is steganography?
2. What is image forensics?
3. What did StegoGuard detect?
4. Why can hidden data inside files be dangerous?
5. How did GitHub Actions help automate the check?
6. How did you fix the suspicious image?
```

---

# Important Reminder

This lab is for learning and defensive cybersecurity only.

Do not use steganography to hide harmful content, leak data, or bypass security systems.
