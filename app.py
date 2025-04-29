import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime
import pytz
import hashlib

# Set page config with orange theme
st.set_page_config(
    page_title="Study Quest",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for orange theme
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF5E6;
    }
    .css-1d391kg, .st-b7, .st-b8, .st-b9 {
        background-color: #FFA500 !important;
        color: white !important;
    }
    .css-1d391kg:hover, .st-b7:hover, .st-b8:hover, .st-b9:hover {
        background-color: #FF8C00 !important;
    }
    .st-eb, .st-ec, .st-ed {
        border-color: #FFA500 !important;
    }
    .css-1aumxhk {
        color: #FF8C00;
    }
    .css-10trblm {
        color: #FF6B00;
    }
    .css-1q8dd3e {
        color: #FF6B00;
    }
    .sidebar .sidebar-content {
        background-color: #FFE4B2;
    }
    .stAlert {
        background-color: #FFE4B2;
        border-left: 5px solid #FF8C00;
    }

    .auth-header {
        text-align: center;
        margin-bottom: 25px;
    }
    
    .auth-switch {
        text-align: center;
        margin-top: 20px;
        font-size: 0.9em;
    }
    
    .auth-switch a {
        color: #FF8C00;
        text-decoration: none;
        cursor: pointer;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session states
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'auth_page' not in st.session_state:
    st.session_state.auth_page = 'login'

# Mock user database (in a real app, this would be in a real database)
if 'user_accounts' not in st.session_state:
    st.session_state.user_accounts = {
        'Phurinat.pola@kmutt.ac.th': {
            'password': hashlib.sha256('Nano@2527'.encode()).hexdigest(),
            'name': 'Phurinat P',
            'student_id': '66070501042'
        }
    }

# User data (in a real app, this would be from a database)
if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        'points': 250,
        'level': 3,
        'checkins': [
            {'location': 'Library', 'time': '2023-05-01 09:30', 'points': 20},
            {'location': 'Co-working Space B', 'time': '2023-05-02 14:15', 'points': 15},
            {'location': 'Reading Zone A', 'time': '2023-05-03 16:45', 'points': 10}
        ],
        'rewards': [
            {'name': 'Coffee Discount', 'cost': 50, 'claimed': True},
            {'name': 'Bookstore Coupon', 'cost': 100, 'claimed': False}
        ]
    }

# Helper functions for authentication
def login_user(email, password):
    if email in st.session_state.user_accounts:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if st.session_state.user_accounts[email]['password'] == hashed_password:
            st.session_state.logged_in = True
            st.session_state.current_user = email
            return True
    return False

def register_user(email, password, name, student_id):
    if email in st.session_state.user_accounts:
        return False
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    st.session_state.user_accounts[email] = {
        'password': hashed_password,
        'name': name,
        'student_id': student_id
    }
    st.session_state.logged_in = True
    st.session_state.current_user = email
    return True

def logout_user():
    st.session_state.logged_in = False
    if 'current_user' in st.session_state:
        del st.session_state.current_user

# Toggle between login and registration forms
def toggle_auth_page():
    if st.session_state.auth_page == 'login':
        st.session_state.auth_page = 'register'
    else:
        st.session_state.auth_page = 'login'

# Locations data
locations = [
    {'name': 'Library', 'image': '📚', 'points': 20, 'description': 'Quiet study space with extensive book collection', 'facilities': ['WiFi', 'Computers', 'Printers', 'Study Rooms']},
    {'name': 'Reading Zone A', 'image': '🪑', 'points': 15, 'description': 'Comfortable chairs for individual reading', 'facilities': ['WiFi', 'Power Outlets']},
    {'name': 'Co-working Space B', 'image': '👥', 'points': 25, 'description': 'Collaborative workspace for group projects', 'facilities': ['WiFi', 'Whiteboards', 'Projector']},
    {'name': 'Computer Lab 3', 'image': '💻', 'points': 15, 'description': 'High-performance computers for technical work', 'facilities': ['WiFi', 'Specialized Software']}
]

# Rewards data
rewards = [
    {'name': 'Coffee Discount (10%)', 'cost': 50, 'stock': 20},
    {'name': 'Bookstore Coupon (15%)', 'cost': 100, 'stock': 10},
    {'name': 'Extended Book Loan', 'cost': 150, 'stock': 5},
    {'name': 'Special Study Room Booking', 'cost': 200, 'stock': 3},
    {'name': 'University Merchandise', 'cost': 300, 'stock': 2}
]

# Leaderboard data
leaderboard = [
    {'rank': 1, 'name': 'Natthapong L.', 'points': 850, 'level': 8},
    {'rank': 2, 'name': 'Jirayu K.', 'points': 720, 'level': 7},
    {'rank': 3, 'name': 'Pimchanok W.', 'points': 680, 'level': 6},
    {'rank': 4, 'name': 'Somsak P.', 'points': 550, 'level': 5},
    {'rank': 5, 'name': 'You', 'points': st.session_state.user_data['points'], 'level': st.session_state.user_data['level']},
    {'rank': 6, 'name': 'Araya T.', 'points': 210, 'level': 2},
    {'rank': 7, 'name': 'Manop C.', 'points': 180, 'level': 2},
    {'rank': 8, 'name': 'Siriporn L.', 'points': 150, 'level': 1},
    {'rank': 9, 'name': 'Kittisak R.', 'points': 120, 'level': 1},
    {'rank': 10, 'name': 'Wanida M.', 'points': 90, 'level': 1}
]

# Campaigns data
campaigns = [
    {'title': 'Morning Study Challenge', 'description': 'Check-in at the library before 9 AM for double points!', 'end_date': '2023-06-15'},
    {'title': 'Workshop Bonus', 'description': 'Attend the research skills workshop for +50 points', 'end_date': '2023-05-20'},
    {'title': 'Feedback Rewards', 'description': 'Complete the library feedback survey for +30 points', 'end_date': '2023-05-30'}
]

# Login & Registration Forms
def show_login_form():
    st.markdown('<div class="auth-form">', unsafe_allow_html=True)
    st.markdown('<h2 class="auth-header">🏫 Study Quest</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="auth-header">Login</h3>', unsafe_allow_html=True)
    
    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Login", use_container_width=True):
            if login_user(email, password):
                st.success("Login successful!")
                time.sleep(1)
                st.experimental_rerun()
            else:
                st.error("Invalid email or password")
    
    st.markdown('<div class="auth-switch">Don\'t have an account? <a id="toggle-register">Register</a></div>', unsafe_allow_html=True)
    
    # JavaScript to handle the toggle link click
    st.markdown("""
    <script>
        document.getElementById('toggle-register').addEventListener('click', function() {
            window.parent.postMessage({type: 'streamlit:setComponentValue', value: 'toggle_auth'}, '*');
        });
    </script>
    """, unsafe_allow_html=True)
    
    # Using a button as a workaround for the JavaScript limitation
    if st.button("Switch to Registration", key="switch_to_register"):
        toggle_auth_page()
        st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_registration_form():
    st.markdown('<div class="auth-form">', unsafe_allow_html=True)
    st.markdown('<h2 class="auth-header">🏫 Study Quest</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="auth-header">Create Account</h3>', unsafe_allow_html=True)
    
    name = st.text_input("Full Name", key="reg_name")
    student_id = st.text_input("Student ID", key="reg_student_id")
    email = st.text_input("Email", key="reg_email")
    password = st.text_input("Password", type="password", key="reg_password")
    confirm_password = st.text_input("Confirm Password", type="password", key="reg_confirm_password")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Register", use_container_width=True):
            if not name or not student_id or not email or not password:
                st.error("Please fill in all fields")
            elif password != confirm_password:
                st.error("Passwords do not match")
            elif register_user(email, password, name, student_id):
                st.success("Registration successful! Logging you in...")
                time.sleep(1)
                st.experimental_rerun()
            else:
                st.error("Email already registered")
    
    st.markdown('<div class="auth-switch">Already have an account? <a id="toggle-login">Login</a></div>', unsafe_allow_html=True)
    
    # Using a button as a workaround for the JavaScript limitation
    if st.button("Switch to Login", key="switch_to_login"):
        toggle_auth_page()
        st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Main app
if not st.session_state.logged_in:
    # Show authentication forms
    if st.session_state.auth_page == 'login':
        show_login_form()
    else:
        show_registration_form()
else:
    # App layout
    st.title("🏫 Study Quest")
    st.markdown("Gamified Check-in & Rewards System")

    # Sidebar
    with st.sidebar:
        st.header("Your Profile")
        
        # Get user info
        user_email = st.session_state.current_user
        user_name = st.session_state.user_accounts[user_email]['name']
        st.markdown(f"**Welcome, {user_name}!**")
        
        st.markdown(f"### Level {st.session_state.user_data['level']}")
        
        # Progress bar for level
        progress = (st.session_state.user_data['points'] % 100) / 100
        st.progress(progress)
        st.markdown(f"**{st.session_state.user_data['points']} points** to next level")
        
        st.markdown("---")
        st.markdown("### Quick Actions")
        if st.button("🏆 Check-in Now"):
            st.session_state.show_checkin = True
        if st.button("🎁 View Rewards"):
            st.session_state.show_rewards = True
        if st.button("📊 View Leaderboard"):
            st.session_state.show_leaderboard = True
        
        st.markdown("---")
        if st.button("Log Out"):
            logout_user()
            st.experimental_rerun()

    # Main content - Enhanced tabs
    tabs = st.tabs([
        "🏠 Home", 
        "📍 Locations", 
        "📅 Campaigns", 
        "⚙️ Settings"
    ])

    # Custom CSS for enhanced tabs
    st.markdown("""
        <style>
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            border-radius: 12px;
            background-color: #FFE4B2;
            padding: 10px 10px 0 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 8px 8px 0 0;
            padding: 10px 24px;
            font-weight: 600;
            background-color: #FFD699;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: #FFA500 !important;
            color: white !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Section headers */
        .section-header {
            color: #FF6B00;
            border-bottom: 2px solid #FFA500;
            padding-bottom: 8px;
            margin-bottom: 16px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Home Tab
    with tabs[0]:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.markdown('<h2 class="section-header">Welcome to Study Quest!</h2>', unsafe_allow_html=True)
        st.markdown("Check-in at Study locations to earn points and redeem exciting rewards!")
        
        col1, col2 = st.columns([3, 4])
        
        with col1:
            st.markdown('<h3 class="section-header">Your Stats</h3>', unsafe_allow_html=True)
            
            # Enhanced metrics with emojis and color
            st.markdown(f"""
            <div style="background-color:#FFF0D9; padding:15px; border-radius:10px; margin-bottom:15px;">
                <h4 style="margin:0; color:#FF6B00;">🏆 Total Points</h4>
                <p style="font-size:28px; font-weight:bold; margin:5px 0;">{st.session_state.user_data['points']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="background-color:#FFF0D9; padding:15px; border-radius:10px; margin-bottom:15px;">
                <h4 style="margin:0; color:#FF6B00;">⭐ Current Level</h4>
                <p style="font-size:28px; font-weight:bold; margin:5px 0;">{st.session_state.user_data['level']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="background-color:#FFF0D9; padding:15px; border-radius:10px; margin-bottom:15px;">
                <h4 style="margin:0; color:#FF6B00;">📅 Check-ins This Week</h4>
                <p style="font-size:28px; font-weight:bold; margin:5px 0;">{len(st.session_state.user_data['checkins'])}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown('<h3 class="section-header">Recent Check-ins</h3>', unsafe_allow_html=True)
            for checkin in st.session_state.user_data['checkins'][-3:]:
                st.markdown(f"""
                <div style="background-color:#FFF0D9; padding:12px; border-radius:8px; margin-bottom:8px; border-left:4px solid #FFA500;">
                    <p style="margin:0;"><span style="font-weight:bold;">✅ {checkin['location']}</span></p>
                    <p style="margin:0; font-size:0.9em; color:#666;">⏱️ {checkin['time']}</p>
                    <p style="margin:0; color:#FF6B00; font-weight:bold;">+{checkin['points']} pts</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown('<h3 class="section-header">Featured Locations</h3>', unsafe_allow_html=True)
            featured = random.sample(locations, 2)
            for loc in featured:
                with st.expander(f"{loc['image']} {loc['name']} - {loc['points']} points"):
                    st.markdown(f"""
                    <div style="background-color:#FFF0D9; padding:15px; border-radius:8px;">
                        <p style="font-style:italic;">{loc['description']}</p>
                        <p><strong>Facilities:</strong> {", ".join(loc['facilities'])}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.button(f"Check-in at {loc['name']}", 
                              key=f"checkin_{loc['name']}",
                              use_container_width=True)

            # Daily challenge card
            st.markdown('<h3 class="section-header">Today\'s Challenge</h3>', unsafe_allow_html=True)
            st.markdown(f"""
            <div style="background-color:#FFF0D9; padding:15px; border-radius:10px; border-left:4px solid #FF8C00;">
                <h4 style="margin:0; color:#FF6B00;">Study Streak Challenge</h4>
                <p>Check in at 3 different locations today to earn 50 bonus points!</p>
                <div style="background-color:#FFE4B2; height:10px; border-radius:5px; margin:10px 0;">
                    <div style="background-color:#FF8C00; width:{min(len(st.session_state.user_data['checkins']), 3) * 33}%; height:10px; border-radius:5px;"></div>
                </div>
                <p style="text-align:right; font-size:0.9em;">{min(len(st.session_state.user_data['checkins']), 3)}/3 locations</p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Locations Tab
    with tabs[1]:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.markdown('<h2 class="section-header">Study Locations</h2>', unsafe_allow_html=True)
        st.markdown("Discover places to study and collaborate across Study")
        
        loc_cols = st.columns(2)
        
        for i, loc in enumerate(locations):
            with loc_cols[i % 2]:
                st.markdown(f"""
                <div style="background-color:#FFF0D9; padding:20px; border-radius:10px; margin-bottom:20px;">
                    <h3 style="color:#FF6B00; margin-top:0;">{loc['image']} {loc['name']}</h3>
                    <div style="display:flex; align-items:center; gap:5px; margin-bottom:10px;">
                        <span style="background-color:#FF8C00; color:white; padding:5px 10px; border-radius:20px; font-weight:bold;">
                            +{loc['points']} pts
                        </span>
                        <span style="background-color:#FFE4B2; color:#FF6B00; padding:5px 10px; border-radius:20px;">
                            {random.choice(['Low', 'Medium', 'High'])} Occupancy
                        </span>
                    </div>
                    <p><em>{loc['description']}</em></p>
                    <p><strong>Facilities:</strong> {', '.join(loc['facilities'])}</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.button(f"Check-in at {loc['name']}", 
                         key=f"loc_checkin_{loc['name']}",
                         use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Campaigns Tab
    with tabs[2]:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.markdown('<h2 class="section-header">Special Campaigns</h2>', unsafe_allow_html=True)
        st.markdown("Participate in these special events for bonus points!")
        
        for i, campaign in enumerate(campaigns):
            st.markdown(f"""
            <div style="background-color:#FFF0D9; padding:20px; border-radius:10px; margin-bottom:20px; 
                        border-left:5px solid {['#FF8C00', '#FF6B00', '#FFA500'][i % 3]};">
                <h3 style="color:#FF6B00; margin-top:0;">{campaign['title']}</h3>
                <p>{campaign['description']}</p>
                <p><strong>⏱️ Ends on:</strong> {campaign['end_date']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.button("Participate", 
                     key=f"campaign_{campaign['title']}",
                     use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Settings Tab
    with tabs[3]:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.markdown('<h2 class="section-header">Settings & Account</h2>', unsafe_allow_html=True)
        
        setting_tabs = st.tabs(["🎁 Rewards", "🏆 Leaderboard", "👤 Profile"])
        
        with setting_tabs[0]:
            st.markdown('<h3 class="section-header">Available Rewards</h3>', unsafe_allow_html=True)
            
            reward_cols = st.columns(2)
            for i, reward in enumerate(rewards):
                with reward_cols[i % 2]:
                    st.markdown(f"""
                    <div style="background-color:#FFF0D9; padding:15px; border-radius:10px; margin-bottom:15px;">
                        <h4 style="margin:0; color:#FF6B00;">{reward['name']}</h4>
                        <div style="display:flex; justify-content:space-between; align-items:center; margin:10px 0;">
                            <span style="font-weight:bold;">{reward['cost']} pts</span>
                            <span>Stock: {reward['stock']}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.button(f"Redeem {reward['name']}", 
                             key=f"redeem_{reward['name']}",
                             use_container_width=True,
                             disabled=st.session_state.user_data['points'] < reward['cost'])
            
            st.markdown('<h3 class="section-header">Your Claimed Rewards</h3>', unsafe_allow_html=True)
            for reward in st.session_state.user_data['rewards']:
                status = "✅ Claimed" if reward['claimed'] else "🔄 Pending pickup"
                st.markdown(f"""
                <div style="background-color:#FFF0D9; padding:12px; border-radius:8px; margin-bottom:8px; 
                            border-left:4px solid {'#4CAF50' if reward['claimed'] else '#FFA500'};">
                    <p style="margin:0;"><span style="font-weight:bold;">{reward['name']}</span> ({reward['cost']} pts)</p>
                    <p style="margin:0; font-size:0.9em; color:#666;">{status}</p>
                </div>
                """, unsafe_allow_html=True)
        
        with setting_tabs[1]:
            st.markdown('<h3 class="section-header">Top Students</h3>', unsafe_allow_html=True)
            
            # Enhanced leaderboard
            for user in leaderboard:
                # Highlight the current user
                is_you = user['name'] == 'You'
                bg_color = "#FFE4B2" if is_you else "#FFF0D9"
                border = "3px solid #FF8C00" if is_you else "none"
                
                st.markdown(f"""
                <div style="background-color:{bg_color}; padding:12px; border-radius:8px; margin-bottom:8px; border:{border};">
                    <div style="display:flex; align-items:center; justify-content:space-between;">
                        <div style="display:flex; align-items:center; gap:15px;">
                            <span style="font-size:20px; font-weight:bold; color:#FF6B00;">#{user['rank']}</span>
                            <div>
                                <p style="margin:0; font-weight:bold;">{user['name']}</p>
                                <p style="margin:0; font-size:0.9em;">Level {user['level']}</p>
                            </div>
                        </div>
                        <span style="font-size:18px; font-weight:bold;">{user['points']} pts</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with setting_tabs[2]:
            st.markdown('<h3 class="section-header">Account Settings</h3>', unsafe_allow_html=True)
            
            # Pre-fill user info
            user_info = st.session_state.user_accounts[st.session_state.current_user]
            
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Name", value=user_info['name'])
                student_id = st.text_input("Student ID", value=user_info['student_id'])
            with col2:
                email = st.text_input("Email", value=st.session_state.current_user, disabled=True)
                st.selectbox("Faculty", ["Engineering", "Science", "Arts", "Business", "Medicine"])
            
            if st.button("Save Changes", use_container_width=True):
                # Update user info in the mock database
                st.session_state.user_accounts[st.session_state.current_user]['name'] = name
                st.session_state.user_accounts[st.session_state.current_user]['student_id'] = student_id
                st.success("Profile updated successfully!")
                time.sleep(1)
                st.experimental_rerun()
                
            st.markdown("### Security")
            
            with st.expander("Change Password"):
                current_password = st.text_input("Current Password", type="password")
                new_password = st.text_input("New Password", type="password")
                confirm_password = st.text_input("Confirm New Password", type="password")
                
                if st.button("Update Password"):
                    if not current_password or not new_password or not confirm_password:
                        st.error("Please fill in all password fields")
                    elif new_password != confirm_password:
                        st.error("New passwords do not match")
                    elif hashlib.sha256(current_password.encode()).hexdigest() != user_info['password']:
                        st.error("Current password is incorrect")
                    else:
                        st.session_state.user_accounts[st.session_state.current_user]['password'] = hashlib.sha256(new_password.encode()).hexdigest()
                        st.success("Password updated successfully!")
                        time.sleep(1)
                        st.experimental_rerun()

            st.markdown("### Registered Users")
            users_df = pd.DataFrame([
                {
                    "Name": info["name"],
                    "Email": email,
                    "Student ID": info.get("student_id", "")
                }
                for email, info in st.session_state.user_accounts.items()
            ])
            st.dataframe(users_df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Check-in modal
    if st.session_state.get('show_checkin', False):
        with st.container():
            st.subheader("Check-in to a Location")
            
            method = st.radio("Check-in method:", ["QR Code", "Geolocation"])
            
            if method == "QR Code":
                st.markdown("Scan the QR code at your location:")
                # QR code scanner placeholder
                st.image("https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=StudyQuestCheckIn", width=150)
                if st.button("Simulate QR Scan"):
                    loc = random.choice(locations)
                    now = datetime.now(pytz.timezone('Asia/Bangkok')).strftime("%Y-%m-%d %H:%M")
                    points = loc['points'] + random.randint(0, 10)
                    st.session_state.user_data['points'] += points
                    st.session_state.user_data['checkins'].append({
                        'location': loc['name'],
                        'time': now,
                        'points': points
                    })
                    st.success(f"Checked in at {loc['name']}! +{points} points")
                    time.sleep(1)
                    st.session_state.show_checkin = False
                    st.experimental_rerun()
            
            elif method == "Geolocation":
                st.markdown("Ensure your location services are enabled")
                if st.button("Check my location"):
                    loc = random.choice(locations)
                    now = datetime.now(pytz.timezone('Asia/Bangkok')).strftime("%Y-%m-%d %H:%M")
                    points = loc['points'] + random.randint(0, 10)
                    st.session_state.user_data['points'] += points
                    st.session_state.user_data['checkins'].append({
                        'location': loc['name'],
                        'time': now,
                        'points': points
                    })
                    st.success(f"Checked in at {loc['name']}! +{points} points")
                    time.sleep(1)
                    st.session_state.show_checkin = False
                    st.experimental_rerun()
            
            if st.button("Cancel"):
                st.session_state.show_checkin = False
                st.experimental_rerun()

    # Rewards modal
    if st.session_state.get('show_rewards', False):
        with st.container():
            st.subheader("Your Rewards")
            for reward in st.session_state.user_data['rewards']:
                status = "✅ Claimed" if reward['claimed'] else "🔄 Pending pickup"
                st.markdown(f"- **{reward['name']}** ({reward['cost']} pts) — {status}")
            if st.button("Close Rewards"):
                st.session_state.show_rewards = False
                st.experimental_rerun()

    # Leaderboard modal
    if st.session_state.get('show_leaderboard', False):
        with st.container():
            st.subheader("Leaderboard")
            for user in leaderboard:
                st.markdown(f"**#{user['rank']} {user['name']}** — {user['points']} pts (Level {user['level']})")
            if st.button("Close Leaderboard"):
                st.session_state.show_leaderboard = False
                st.experimental_rerun()

    # Footer
    st.markdown("---")
    st.markdown("© 2025 King Mongkut's University of Technology Thonburi | Study Quest System")
