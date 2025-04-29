Study Quest
Study Quest is a gamified check-in and rewards system designed for students at King Mongkut's University of Technology Thonburi (KMUTT). Built with Streamlit, this web application encourages students to engage in study activities by earning points for checking in at various campus study locations, participating in campaigns, and redeeming rewards.
Features

User Authentication: Secure login and registration with email, password, name, and student ID.
Check-in System: Earn points by checking in at study locations via QR code or geolocation (simulated in the current version).
Rewards System: Redeem points for rewards like coffee discounts, bookstore coupons, and more.
Leaderboard: View top students based on points and levels.
Campaigns: Participate in special events for bonus points.
Profile Management: Update personal details and change passwords.
Responsive UI: Orange-themed interface with tabs for Home, Locations, Campaigns, and Settings.
Mock Data: Uses mock user data and study locations for demonstration purposes.

Tech Stack

Frontend & Backend: Streamlit
Programming Language: Python 3.8+
Libraries:
streamlit for the web interface
pandas for data handling
pytz for timezone support
hashlib for password hashing


Deployment: Streamlit Cloud
Version Control: Git/GitHub

Project Structure
study-quest/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

Prerequisites

Python 3.8 or higher
Git
A GitHub account for deployment
A Streamlit Cloud account for hosting

Local Setup

Clone the Repository:
git clone https://github.com/your-username/study-quest.git
cd study-quest


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Run the App:
streamlit run app.py

Open http://localhost:8501 in your browser to view the app.

Test Credentials:Use the following mock user to log in:

Email: example.student@kmutt.ac.th
Password: SecurePass@2025



Deployment to Streamlit Cloud

Push Code to GitHub:

Create a new repository on GitHub (e.g., study-quest).
Initialize a local Git repository:git init
git add app.py requirements.txt
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/study-quest.git
git branch -M main
git push -u origin main




Deploy on Streamlit Cloud:

Log in to share.streamlit.io with your GitHub account.
Click "New app" and select your study-quest repository.
Set the branch to main and the main file to app.py.
(Optional) In Advanced settings, specify Python 3.9 or higher.
Click "Deploy" and wait for the app to build.
Access the app at the provided URL (e.g., https://your-username-study-quest.streamlit.app).


Troubleshooting:

Check deployment logs for errors.
Ensure requirements.txt includes all dependencies.
Verify internet access for external resources (e.g., QR code API).



Usage

Login/Register: Use an email and password to log in or create an account.
Check-in: Simulate checking in at study locations (e.g., Library, Co-working Space) to earn points.
View Rewards: Redeem points for rewards and track claimed rewards.
Leaderboard: See your rank among top students.
Campaigns: Participate in special events for bonus points.
Settings: Update your profile, change your password, or view registered users.

Notes

Mock Data: The app uses st.session_state for mock user data, check-ins, rewards, and leaderboards. For production, integrate a database (e.g., SQLite, PostgreSQL).
QR Code & Geolocation: Check-ins are simulated. Implement real QR code scanning and geolocation APIs for production.
Security: Passwords are hashed with hashlib.sha256. Consider using bcrypt for stronger security in production.
JavaScript Limitation: Login/registration toggling uses buttons due to Streamlit’s JavaScript constraints.

Future Improvements

Integrate a real database for user and check-in data.
Add real QR code scanning functionality.
Implement geolocation-based check-ins with privacy compliance.
Enhance security with stronger password hashing and rate-limiting.
Add notifications for campaigns and rewards.
Support custom themes and multilingual interfaces.

Contributing

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions or feedback, contact:

Developer: Phurinat P
Email: example.student@kmutt.ac.th


© 2025 King Mongkut's University of Technology Thonburi | Study Quest System
