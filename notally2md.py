import csv
import os
import json
import re

def safe_filename(title):
    # Replace non-ASCII characters with a placeholder
    return re.sub(r'[^\x00-\x7F]+', '_', title)

def convert_to_markdown(csv_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            note_id = row['id']
            note_type = row['type']
            title = row['title']
            body = row['body']
            items_json = row['items']
            
            if note_type == 'NOTE':
                filename = f"note_{note_id}.md"
            elif note_type == 'LIST':
                filename = f"list_{note_id}.md"
            else:
                continue
            
            if title:
                filename = f"{safe_filename(title)}.md"
            
            # Ensure the directory structure exists
            filepath = os.path.join(output_dir, filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            with open(filepath, 'w') as f:
                f.write(f"# {title}\n\n")
                
                if body:
                    f.write(body)
                
                if note_type == 'LIST':
                    items = json.loads(items_json)
                    for item in items:
                        checked = "[x]" if item.get('checked', False) else "[ ]"
                        text = item.get('text', '')
                        f.write(f"{checked} {text}\n")
            
            print(f"Converted {note_type} {note_id} to markdown: {filename}")

if __name__ == "__main__":
    csv_file = "notally_backup.csv"
    output_dir = "markdown_notes"
    
    convert_to_markdown(csv_file, output_dir)

# It will export the converted csv to md files to a folder named markdown_files
