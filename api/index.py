from app import create_app

app = create_app()

def handler(request):
    return app

if __name__ == '__main__':
    app.run()