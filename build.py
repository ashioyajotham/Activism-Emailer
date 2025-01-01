import os
import json
import shutil

def setup_vercel():
    # Create output directories
    os.makedirs('.vercel/output/static', exist_ok=True)
    
    # Copy static files
    if os.path.exists('static'):
        shutil.copytree('static', '.vercel/output/static', dirs_exist_ok=True)
    
    # Generate config.json
    config = {
        "version": 2,
        "routes": [
            {
                "src": "/static/(.*)",
                "dest": "/static/$1",
                "headers": {
                    "cache-control": "public, max-age=31536000, immutable"
                }
            },
            {
                "src": "/(.*)",
                "dest": "/api/index.py"
            }
        ],
        "outputDirectory": "output"
    }
    
    with open('.vercel/output/config.json', 'w') as f:
        json.dump(config, f)

if __name__ == '__main__':
    setup_vercel()