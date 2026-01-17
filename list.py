from pathlib import Path

current_dir = Path(".")

for file_path in current_dir.glob("*.blend"):
    
    file_name_only = file_path.stem
    
    print(f"{file_name_only}")
