# 📧 Email Automation with Python

Automate Gmail cold emails with Python and Excel — includes **personalized messages** and **resume attachments**.  
This project demonstrates how to send bulk emails safely and efficiently using Python, Excel, and Gmail SMTP.

---

## 🚀 Features
- Reads contacts (Name, Email, Company) from Excel file  
- Sends **personalized emails** (e.g., "Hi John")  
- Attaches a resume or any file automatically  
- Uses Gmail SMTP with secure **App Passwords**  
- Includes **sample Excel** and **dummy resume** for testing  

---

## 📂 Project Structure
```
Email-Automation/
│
├── emails_automate.py     # Main Python script
├── sample emails data.xlsx     # Dummy contact list (safe for demo)
├── sample resume.pdf       # Example resume (safe for demo)
└── README.md              # Project documentation
```

---

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/email-automation-python.git
cd email-automation-python
```

### 2️⃣ Install Dependencies
```bash
pip install pandas openpyxl
```

### 3️⃣ Configure Gmail
1. Enable **2-Step Verification** in your Google account  
2. Generate an **App Password** ([Guide](https://myaccount.google.com/apppasswords))  
3. Replace your email & app password in `emails_automate.py`  

```python
your_email = "yourgmail@gmail.com"
your_password = "your_app_password"
```

---

## ▶️ Usage
1. Add your own `emails.xlsx` (not included in repo for privacy).  
   - Format should be:  

| Name        | Email                 | Company           |
|-------------|-----------------------|------------------|
| John Doe    | john.doe@testmail.com | TestCorp Ltd     |
| Jane Smith  | jane.smith@demo.com   | DemoWorks Inc    |

2. Run the script:
```bash
python emails_automate.py
```

3. Emails will be sent to all contacts in the Excel file with your **resume attached**.

---

## ⚠️ Important Notes
- Do **NOT** upload your real Excel or resume to GitHub.  
- Only use the provided **sample_emails.xlsx** and **Dummy_Resume.pdf** for demonstration.  
- Use responsibly — avoid spamming or violating Gmail policies.  

---

## 📌 Example Email Body
```
Hi John,

I hope this email finds you well.

I am reaching out to express my interest in any available opportunities in Data Science / Machine Learning. 
Please find my resume attached for your consideration.

Looking forward to hearing from you.

Best regards,
Your Name
```

---

## 🌟 Contributing
Feel free to fork this repo and enhance it — for example:
- Add HTML email templates  
- Integrate Gmail API for OAuth login  
- Add logging / error handling  

--- 

## ✍️ Author

**Rohit Yadav**  
📧 Email: rohityadavofficial.06@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/rohit-yadav-datascientist/) | [GitHub](https://github.com/rohityadav-06)