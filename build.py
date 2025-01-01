import os
import json
import shutil

def build():
    # Create output directories
    os.makedirs('.vercel/output/static', exist_ok=True)
    
    # Copy static files
    if os.path.exists('static'):
        shutil.copytree('static', '.vercel/output/static', dirs_exist_ok=True)
    
    # Generate config.json
    config = {
        "version": 3,
        "routes": [
            {
                "src": "/static/(.*)",
                "dest": "/static/$1"
            },
            {
                "src": "/(.*)",
                "dest": "/api/index.py"
            }
        ]
    }
    
    with open('.vercel/output/config.json', 'w') as f:
        json.dump(config, f)

if __name__ == '__main__':
    build()