from app import create_app
from tests.fixtures import load_test_data

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        load_test_data()
    app.run(debug=True)