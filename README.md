# 📄 iLovePDF Automation Bot

This Python script automates the **PDF compression** process using [iLovePDF](https://www.ilovepdf.com/) with Selenium. It logs into your account, opens the Compress PDF tool, and processes a file (with manual file selection support).

> Developed by **Muhammad Hammad Ashraf**, Owner of **coreXmanzoid**

---

## 🧰 Features

- 🔐 Logs into your iLovePDF account automatically
- 📁 Navigates directly to the **Compress PDF** tool
- 🖱️ Prompts for manual file selection to ensure compatibility across systems
- 📥 Automatically clicks the download button once the file is processed
- 🧾 Clean console messages guiding the user through the process

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Google Chrome browser
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) installed and added to your system PATH
- Required Python libraries:
  - `selenium`
  - `time` (built-in)

### Installation

1. **Clone this repository**

```bash
git clone https://github.com/your-username/ilovepdf-automation.git
cd ilovepdf-automation
```

2. **Install the required packages**

```bash
pip install selenium
```

3. **Update login credentials** in the script:

```python
email.send_keys("your_email_here")
password.send_keys("your_password_here")
```

4. **Run the script**

```bash
python ilovepdf.py
```

---

## 🛠 How It Works

1. Opens [iLovePDF](https://www.ilovepdf.com/) in Chrome.
2. Logs into the user account using credentials you provide.
3. Navigates to **Compress PDF** tool.
4. Prompts you to manually select the file to compress.
5. Automatically starts the compression and downloads the final file.
6. Provides helpful console messages throughout the process.

---

## 📂 Files Included

- `ilovepdf.py`: Main Python script to automate the compression process
- `sample.pdf`: Example input file (to test compression)
- `compressed_sample.pdf`: Result after compression

---

## ℹ️ Notes

- **Manual File Selection**: This script pauses to let you manually select a file using the browser file picker. You’ll be prompted in the console.
- If you want to automate file selection too, you'll need to use external tools (e.g., `pyautogui`) or run a headless file upload approach depending on your OS.
- Ensure your download settings in Chrome allow automatic downloads without prompting.

---

## 👤 Developed By

**Muhammad Hammad Ashraf**  
Owner of [coreXmanzoid](https://your-company-website.com)  
Email: manzoid@gmail.com

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

