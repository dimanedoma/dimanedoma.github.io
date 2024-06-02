import os
import sys

def rename_files_and_update_html(directory):
    # Traverse the directory recursively
    for root, dirs, files in os.walk(directory):
        # Rename files that start with an underscore
        for filename in files:
            if filename.startswith('_'):
                old_path = os.path.join(root, filename)
                new_filename = filename[1:]
                new_path = os.path.join(root, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")
                # Update HTML files with the new filename
                update_html_references(directory, filename, new_filename)

def update_html_references(directory, old_filename, new_filename):
    # Traverse the directory recursively to find .html files
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.html'):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                # Replace old filename with new filename in the content
                updated_content = content.replace(old_filename, new_filename)
                if content != updated_content:
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(updated_content)
                    print(f"Updated HTML file: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <folder>")
        sys.exit(1)

    target_directory = sys.argv[1]
    rename_files_and_update_html(target_directory)