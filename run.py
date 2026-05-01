# run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Run without the reloader; the development reloader can pick up changes
    # in the virtualenv or system packages and cause unexpected restarts.
    app.run(debug=True, use_reloader=False, port=5002)