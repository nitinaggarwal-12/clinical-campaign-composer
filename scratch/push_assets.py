import os
import subprocess
import glob
import shutil

# Working directory
cwd = "/Users/nitinagga/Documents/Maestro-Automated-Claims-Harvesting-&-Trigger-Pipeline"

def run_git(args):
    result = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running git {' '.join(args)}:")
        print(result.stderr)
        return False
    return True

def main():
    git_dir = os.path.join(cwd, ".git")
    if os.path.exists(git_dir):
        print("🗑️ Removing existing .git directory to start 100% fresh...")
        shutil.rmtree(git_dir)
        
    print("🆕 Initializing fresh Git repository...")
    if not run_git(["init"]):
        return
        
    print("🔗 Configuring remote origin...")
    if not run_git(["remote", "add", "origin", "https://github.com/nitinaggarwal-12/clinical-campaign-composer.git"]):
        return
        
    print("🌿 Setting default branch to main...")
    if not run_git(["branch", "-M", "main"]):
        return
        
    print("📦 Stage 1: Adding and committing all core source code files first (excluding large assets)...")
    # Add everything except pdf, pptx, png
    if not run_git(["add", ".", ":!*.pdf", ":!*.pptx", ":!*.png"]):
        return
    if not run_git(["commit", "-m", "initial commit: clinical campaign composer - core source code"]):
        return
        
    print("📤 Pushing core source code to GitHub...")
    # Force push in case there is any remote history conflict
    if run_git(["push", "-f", "-u", "origin", "main"]):
        print("✅ Core source code pushed successfully!")
    else:
        print("❌ Failed to push core source code. Aborting.")
        return
    
    # Find all PDF, PPTX, and PNG files in the working directory
    patterns = ["**/*.pdf", "**/*.pptx", "**/*.png"]
    large_files = []
    for pattern in patterns:
        for filepath in glob.glob(os.path.join(cwd, pattern), recursive=True):
            # Exclude virtual environments, node_modules, or git folders
            if ".venv" not in filepath and ".git" not in filepath and "node_modules" not in filepath:
                # Store relative path for git
                rel_path = os.path.relpath(filepath, cwd)
                large_files.append(rel_path)
                
    print(f"\n🔍 Stage 2: Found {len(large_files)} binary/asset files to push individually.")
    
    # Sort files by size so we push smaller ones first, and larger ones later
    large_files.sort(key=lambda f: os.path.getsize(os.path.join(cwd, f)))
    
    for i, filepath in enumerate(large_files, 1):
        full_path = os.path.join(cwd, filepath)
        size_mb = os.path.getsize(full_path) / (1024 * 1024)
        filename = os.path.basename(filepath)
        print(f"\n🚀 [{i}/{len(large_files)}] Pushing {filepath} ({size_mb:.2f} MB)...")
        
        # Add the single file
        if not run_git(["add", filepath]):
            print(f"⚠️ Failed to stage {filepath}, skipping...")
            continue
            
        # Commit the single file
        if not run_git(["commit", "-m", f"add asset: {filename}"]):
            print(f"⚠️ Failed to commit {filepath}, skipping...")
            run_git(["reset", "HEAD"]) # Unstage
            continue
            
        # Push the single file
        if not run_git(["push", "origin", "main"]):
            print(f"❌ Failed to push {filepath} due to network/SSL limits. Skipping for now...")
            # Undo the commit and unstage the file to keep working tree clean
            run_git(["reset", "--soft", "HEAD~1"])
            run_git(["reset", "HEAD", filepath])
            continue
            
        print(f"✅ Successfully pushed {filename}!")
        
    print("\n🎉 WORKSPACE SYNC PROCESS COMPLETE!")

if __name__ == "__main__":
    main()
