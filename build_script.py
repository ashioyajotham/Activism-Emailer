import shutil
import os

def build():
    # Clear existing build
    if os.path.exists('.vercel/output'):
        shutil.rmtree('.vercel/output')
    
    # Create static directory
    os.makedirs('.vercel/output/static', exist_ok=True)
    
    # Copy static files
    shutil.copytree('static', '.vercel/output/static', dirs_exist_ok=True)

if __name__ == '__main__':
    build()