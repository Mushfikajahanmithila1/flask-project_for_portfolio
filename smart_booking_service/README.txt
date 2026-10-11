SMART BOOKING SERVICE - FLASK DEMO

1. Open this folder in VS Code.
2. Activate your virtual environment.
3. Install: pip install -r requirements.txt
4. Run: python run.py
5. Open: http://127.0.0.1:5000

This is a learning demo, not production-ready authentication. Demo accounts are stored in the signed browser session and only work in that browser session. Do not use real passwords.

The Service model expects title, description, price, and status. If an old database has a different schema, back it up first. To start fresh, stop Flask and rename/delete the old database file only if you do not need its data. Then restart python run.py.
