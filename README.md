# 📸 Screenshot Uploader

This script captures a screenshot of the active window, uploads it to Imgur, copies the URL to the clipboard, and logs the upload history in a CSV file.

## 🚀 Features
- Captures the active window screenshot
- Uploads the screenshot to Imgur
- Copies the Imgur URL to the clipboard
- Saves upload history in a `uploads.csv` file
- Provides desktop notifications

## 🛠 Installation

Ensure you have the following dependencies installed:

```sh
sudo apt install maim xdotool libnotify-bin
pip install imgurpython pyperclip
```

## 🔧 Configuration

1. Clone this repository or copy the script.
2. Set up your `ImgurClient` credentials in the script. Replace `ABC123` with your own Imgur API key.

## ▶️ Usage

Run the script using:

```sh
python screenshot_uploader.py
```

## 📂 Output
- The screenshot is saved temporarily in `~/imgur/imgur.png`.
- The uploaded image link is copied to the clipboard.
- A record of uploads is stored in `~/imgur/history/uploads.csv`.

## 📢 Notifications
The script provides desktop notifications when:
- A screenshot is taken
- The upload is successful or fails

## ⚡ Author
Made with ❤️ for easy screenshot sharing!

---
📌 *Tip: You can set a keyboard shortcut to run this script for faster screenshots!*
