import os
import json

# Create .vercel/output directory
os.makedirs('.vercel/output', exist_ok=True)

# Create config.json
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

# Create static directory in output
os.makedirs('.vercel/output/static', exist_ok=True)