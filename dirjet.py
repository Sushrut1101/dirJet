import os
import pickle
from pathlib import Path
import argparse

DB_PATH = Path.home() / ".dirjet_db"

def load_db():
    if DB_PATH.exists():
        with open(DB_PATH, 'rb') as db_file:
            return pickle.load(db_file)
    else:
        return {}

def save_db(db):
    with open(DB_PATH, 'wb') as db_file:
        pickle.dump(db, db_file)

def add_path(path, db):
    path = os.path.abspath(path)
    if path in db:
        db[path] += 1
    else:
        db[path] = 1
    save_db(db)

def jump_to_directory(query, db):
    query = query.lower()
    for path in sorted(db, key=db.get, reverse=True):
        if query in path.lower():
            print(f"Jumping to {path}")
            os.chdir(path)
            break

def parse_args():
    parser = argparse.ArgumentParser(description="Navigate directories efficiently.")
    parser.add_argument("query", help="Directory query or bookmark alias")
    parser.add_argument("-b", "--bookmark", action="store_true", help="Bookmark the current directory")
    parser.add_argument("-l", "--list", action="store_true", help="List all bookmarked directories")
    return parser.parse_args()

def main():
    args = parse_args()
    db = load_db()
    
    if args.bookmark:
        add_path(os.getcwd(), db)
    elif args.list:
        for path in db:
            print(path)
    else:
        jump_to_directory(args.query, db)

if __name__ == "__main__":
    main()
