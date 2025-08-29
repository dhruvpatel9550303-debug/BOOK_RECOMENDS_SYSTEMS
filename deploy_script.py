import os
import subprocess
import sys

def check_git():
    """Check if git is installed and initialized"""
    try:
        subprocess.run(['git', '--version'], check=True, capture_output=True)
        print("✅ Git is installed")
        return True
    except:
        print("❌ Git not found. Please install Git first.")
        return False

def init_git_repo():
    """Initialize git repository and make first commit"""
    try:
        # Check if git is already initialized
        if os.path.exists('.git'):
            print("✅ Git repository already exists")
            return True
            
        # Initialize git
        subprocess.run(['git', 'init'], check=True)
        print("✅ Git repository initialized")
        
        # Add all files
        subprocess.run(['git', 'add', '.'], check=True)
        print("✅ Files added to git")
        
        # Make first commit
        subprocess.run(['git', 'commit', '-m', 'Initial commit for deployment'], check=True)
        print("✅ Initial commit made")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🚀 Book Recommender System - Deployment Helper")
    print("=" * 50)
    
    if not check_git():
        return
    
    print("\n📋 Next steps:")
    print("1. Create a GitHub repository at github.com")
    print("2. Run these commands:")
    print("   git remote add origin YOUR_GITHUB_REPO_URL")
    print("   git push -u origin main")
    print("3. Go to render.com and deploy from GitHub")
    
    if init_git_repo():
        print("\n✅ Your local repository is ready!")
        print("🔗 Now create a GitHub repo and push your code")

if __name__ == "__main__":
    main()
