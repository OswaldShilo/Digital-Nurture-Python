# Exercise 50: Backup Utility
# Objective: Copy files to backup folder, skip duplicates, log operations

import shutil, os, hashlib, logging

logging.basicConfig(filename="backup.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s")

def file_hash(filepath):
    h = hashlib.md5()
    with open(filepath, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def backup_files(source_dir, backup_dir):
    os.makedirs(backup_dir, exist_ok=True)
    seen, copied, skipped = set(), 0, 0
    try:
        files = os.listdir(source_dir)
    except FileNotFoundError:
        print(f"Error: Source '{source_dir}' not found.")
        return
    for filename in files:
        src = os.path.join(source_dir, filename)
        dst = os.path.join(backup_dir, filename)
        try:
            fhash = file_hash(src)
            if fhash in seen:
                logging.info(f"Skipped duplicate: {filename}")
                skipped += 1
            else:
                seen.add(fhash)
                shutil.copy2(src, dst)
                logging.info(f"Copied: {filename}")
                copied += 1
        except PermissionError:
            logging.warning(f"Permission denied: {filename}")
    print(f"Done -> Copied: {copied}, Duplicates skipped: {skipped}")
    print("Log written to backup.log")

# Demo: create small source folder
os.makedirs("source_files", exist_ok=True)
for name, content in [("a.txt", "Hello"), ("b.txt", "World"), ("c.txt", "Hello")]:
    with open(os.path.join("source_files", name), "w") as f:
        f.write(content)

backup_files("source_files", "backup_files")
