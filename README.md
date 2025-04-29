# 🎓 Study Quest  
*A gamified check-in and rewards system for KMUTT students*

**Study Quest** is a web-based application built with **Streamlit** to motivate students at **King Mongkut's University of Technology Thonburi (KMUTT)** to engage in study activities. Through check-ins, campaigns, and a point-based rewards system, students are rewarded for productive behavior across campus.

---

## 🚀 Key Features

- **🔐 User Authentication**  
  Register and log in securely using email, password, full name, and student ID.

- **📍 Check-in System**  
  Earn points by checking in at designated study spots using QR codes or simulated geolocation.

- **🎁 Rewards System**  
  Redeem earned points for perks such as:
  - Coffee discounts  
  - Bookstore coupons  
  - Event access and more

- **🏆 Leaderboard**  
  Track your progress and see how you rank against fellow students.

- **📣 Campaigns**  
  Join time-limited campaigns to earn bonus points.

- **👤 Profile Management**  
  Update your personal information or reset your password anytime.

- **📱 Responsive UI**  
  Streamlit-based orange-themed layout with tabs for:
  - Home  
  - Locations  
  - Campaigns  
  - Settings

- **🧪 Mock Data**  
  Pre-loaded users and study locations for demo/testing purposes.

---

## ⚙️ Tech Stack

- **Frontend & Backend:** Streamlit  
- **Programming Language:** Python 3.8+  
- **Libraries Used:**
  - `streamlit` – UI & interactivity  
  - `pandas` – Data handling  
  - `pytz` – Timezone management  
  - `hashlib` – Password hashing  

- **Hosting:** Streamlit Cloud  
- **Version Control:** Git + GitHub

---

## 📁 Project Structure

```
study-quest/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 💻 Getting Started

### ✅ Prerequisites

- Python 3.8 or newer  
- Git  
- GitHub account  
- Streamlit Cloud account  

### 🧪 Local Setup

```bash
# Clone the repo
git clone https://github.com/your-username/study-quest.git
cd study-quest

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch app
streamlit run app.py
```

Open your browser at [http://localhost:8501](http://localhost:8501)

### 🔐 Test Login

```text
Email:    example.student@kmutt.ac.th  
Password: SecurePass@2025  
```

---

## ☁️ Deploying to Streamlit Cloud

### 1. Push Code to GitHub

```bash
git init
git add app.py requirements.txt
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/study-quest.git
git branch -M main
git push -u origin main
```

### 2. Deploy

- Log in at [share.streamlit.io](https://share.streamlit.io)  
- Click **“New app”**, select your repository  
- Set branch to `main`, main file to `app.py`  
- (Optional) Use Python 3.9+  
- Click **Deploy**  
- Access the app at `https://your-username-study-quest.streamlit.app`

---

## 🧩 Troubleshooting

- Check deployment logs  
- Ensure all libraries are in `requirements.txt`  
- Ensure external services (e.g., QR code API) are reachable

---

## 📌 App Usage Overview

| Section      | Description |
|--------------|-------------|
| 🔑 Login/Register | Register or log in using your KMUTT email |
| 📍 Check-in      | Simulated check-in at Library, Co-working Space, etc. |
| 🎁 Rewards       | Browse and redeem available rewards |
| 🏆 Leaderboard   | View ranking of top students |
| 📣 Campaigns     | Join special time-based events for extra points |
| ⚙️ Settings      | Edit profile, change password, view registered users |

---

## ⚠️ Notes for Developers

- **Mock Data:** Stored in `st.session_state`; switch to a real DB (e.g., SQLite/PostgreSQL) for production  
- **QR & Geolocation:** Currently simulated; integrate actual QR scanner/geolocation APIs for production  
- **Security:** Uses `hashlib.sha256` — replace with `bcrypt` in production  
- **JS Limitation:** Login/register logic uses buttons due to Streamlit’s JavaScript limitations

---

## 🔮 Future Enhancements

- Real database integration  
- QR code and GPS-based check-ins  
- Stronger password hashing & rate limiting  
- In-app notifications  
- Custom themes & language support  

---

## 🤝 Contributing

1. Fork this repo  
2. Create your feature branch: `git checkout -b feature/your-feature`  
3. Commit changes: `git commit -m "Add your feature"`  
4. Push to GitHub: `git push origin feature/your-feature`  
5. Open a pull request  

---

## 📜 License

Licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 📬 Contact

**Developer:** Phurinat P  
**Email:** example.student@kmutt.ac.th

---

© 2025 King Mongkut's University of Technology Thonburi | Study Quest System

---
