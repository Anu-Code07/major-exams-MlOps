#!/usr/bin/env python3
"""
Script to force push changes to fix GitHub Actions.
"""
import subprocess
import sys
import os

def run_command(cmd):
    """Run a command and return the result."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        print(f"Command: {cmd}")
        print(f"Return code: {result.returncode}")
        if result.stdout:
            print(f"Output: {result.stdout}")
        if result.stderr:
            print(f"Error: {result.stderr}")
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print(f"Command timed out: {cmd}")
        return False
    except Exception as e:
        print(f"Error running command: {e}")
        return False

def main():
    print("🚀 Force pushing changes to fix GitHub Actions...")
    
    # Check current status
    print("\n1. Checking git status...")
    if not run_command("git status"):
        print("❌ Git status failed")
        return False
    
    # Add all changes
    print("\n2. Adding all changes...")
    if not run_command("git add ."):
        print("❌ Git add failed")
        return False
    
    # Commit changes
    print("\n3. Committing changes...")
    if not run_command('git commit -m "Fix test file for GitHub Actions - Ridge regression with polynomial features"'):
        print("❌ Git commit failed")
        return False
    
    # Force push to main
    print("\n4. Force pushing to main...")
    if not run_command("git push --force origin main"):
        print("❌ Git push failed")
        return False
    
    print("\n✅ Changes pushed successfully!")
    print("GitHub Actions should now run with the correct test file.")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 