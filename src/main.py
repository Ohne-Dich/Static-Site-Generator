import os
import shutil

from copystatic import copy_files_recursive
from htmlnode import HTMLNode
from markdown_blocks import markdown_to_html_node


dir_path_static = "./static"
dir_path_public = "./public"

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("#").strip()
    raise Exception("No header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as file:
        markdown = file.read()

    with open(template_path, 'r') as file2:
        template = file2.read()

    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()
    title = extract_title(markdown)
    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as output_file:
        output_file.write(full_html) 

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    pathes = os.listdir(dir_path_content)
    for path in pathes:
        full_source_path = os.path.join(dir_path_content, path)
        if os.path.isfile(full_source_path):
            dest_path = os.path.join(dest_dir_path, path.replace('.md', '.html'))
            generate_page(full_source_path, template_path, dest_path)
        else:          
            next_dir_path_content = os.path.join(dir_path_content, path)
            next_dest_dir_path = os.path.join(dest_dir_path, path)
            generate_pages_recursive(next_dir_path_content, template_path, next_dest_dir_path)

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Recreating public directory...")
    os.makedirs(dir_path_public, exist_ok=True)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating index.html...")
    generate_pages_recursive(
        dir_path_content="./content", 
        template_path="./template.html", 
        dest_dir_path="./public"
    )

main()
