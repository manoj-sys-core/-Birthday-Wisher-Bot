# 🎉 Birthday Wisher Bot 🎂

Automate birthday wishes like a pro! This Python script reads a list of birthdays from a CSV file and sends personalized birthday emails automatically using Gmail.

## ✨ Features

- ✅ Reads birthday data from a CSV file  
- ✅ Picks a random letter template  
- ✅ Personalizes each message with the recipient's name  
- ✅ Sends emails using your Gmail account  
- ✅ Easy to set up and customize!

## 📁 Project Structure

\`\`\`
Birthday-Wisher-Bot/
├── main.py                  # Main script that checks today's birthdays and sends emails
├── birthdays.csv            # Your list of birthday people
└── letter_templates/        # Folder containing 3 customizable letter templates
    ├── letter_1.txt
    ├── letter_2.txt
    └── letter_3.txt
\`\`\`

## 🛠 Requirements

- Python 3.x  
- `pandas`  
- `smtplib` (built-in)  
- Gmail account with "Less secure app access" turned on (or App Passwords if 2FA is enabled)

Install the required package:

\`\`\`bash
pip install pandas
\`\`\`

## 📌 Setup Instructions

1. **Clone the repository:**
   \`\`\`bash
   git clone https://github.com/your-username/birthday-wisher-bot.git
   cd birthday-wisher-bot
   \`\`\`

2. **Add your email credentials in `main.py`:**
   \`\`\`python
   MAIL = "your_email@gmail.com"
   PASSWORD = "your_email_password"
   \`\`\`

3. **Add birthday entries to `birthdays.csv` in this format:**
   \`\`\`
   name,email,year,month,day
   Alice,alice@example.com,1998,4,13
   Bob,bob@example.com,1995,6,24
   \`\`\`

4. **Customize the templates in `letter_templates/letter_1.txt`, etc.**

5. **Schedule the script to run daily** using **Task Scheduler** (Windows) or **cron job** (Linux/Mac).

## 🔒 Security Tip

> Use environment variables or a `.env` file instead of hardcoding your email credentials.

## 📬 Email Output Example

Each recipient receives a beautiful, personalized birthday email like this:

\`\`\`
Subject: HAPPY BIRTHDAY

Dear [NAME],

Wishing you a day filled with happiness and a year filled with joy. Happy Birthday!

Best,  
Your Name 🎈
\`\`\`

## 🧠 Inspiration

This project was built as a fun way to automate real-world tasks using Python, showcasing the power of scripting and email automation.

## 🤝 Connect with Me

- 🌐 [LinkedIn](https://www.linkedin.com/in/manoj-s-corex7)  
- 📸 [Instagram](https://www.instagram.com/white._.hatx7)  
- 📧 Email: mnaojcs6317@gmail.com

---

⭐ *Star this repo if you like automation projects!*
