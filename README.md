# Personal Finance Tracker 
A Flask-based web application for tracking and managing personal expenses.

##  Features (In Progress)
-  Log and categorize expenses with a user-friendly interface.
-  View spending insights through interactive Chart.js visualizations.
-  Bootstrap-powered responsive design.
-  **Upcoming Features:** User authentication, data export, and deployment.

##  Technologies Used
- **Backend:** Flask, SQLite, SQLAlchemy  
- **Frontend:** HTML, Bootstrap, Chart.js  
- **Deployment (Planned):** Render / PythonAnywhere  

##  How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_GITHUB_USERNAME/personal-finance-tracker.git
cd personal-finance-tracker

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize the database
python
>>> from app import db, app
>>> with app.app_context():
>>>     db.create_all()
>>> exit()

# 5. Run the Flask app
python run.py

# 6. Open in browser
http://127.0.0.1:5000/
