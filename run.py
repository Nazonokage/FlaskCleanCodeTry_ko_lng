# run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    url = "http://localhost:7080/flaskdemo"
    print(f"Server is running at: {url}")
    app.run(host='0.0.0.0', port=7080, debug=True)