import os
import os.path as osp
import sys
import shutil

from markdown_utils import extract_title
from markdown_to_html import markdown_to_html_node

basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

current_dir = osp.dirname(os.path.abspath(__file__))
STATIC_DIR = osp.join(current_dir, "../static/")
DOCS_DIR = osp.join(current_dir, "../docs/")
CONTENT_DIR = osp.join(current_dir, "../content/")
TEMPLATE_PATH = osp.join(current_dir, "../template.html")

def copy_static(src, dst):
    if not os.listdir(src):
        return
    
    for content in os.listdir(src):
        full_path = osp.join(src, content)

        if osp.isfile(full_path):
            print(f"++ Copying {content} to {dst}")
            shutil.copy(full_path, dst)
        else:
            target_dir = osp.join(DOCS_DIR, content)
            os.makedirs(target_dir, exist_ok=True)
            copy_static(full_path, target_dir)


def generate_pages_recursive(content_path, template_path, dest_dir_path, basepath):
    if not os.listdir(content_path):
        return
    
    for content in os.listdir(content_path):
        full_path = osp.join(content_path, content)

        if osp.isfile(full_path) and full_path.endswith(".md"):
            generate_page(full_path, dest_dir_path, template_path, basepath)
        
        elif osp.isdir(full_path):
            new_dest_dir_path = osp.join(dest_dir_path, content)
            os.makedirs(new_dest_dir_path, exist_ok=True)
            generate_pages_recursive(full_path, template_path, new_dest_dir_path)
    

def generate_page(full_path, dest_dir_path, template_path, basepath):
    print(f"Generating page from {full_path} to {dest_dir_path} using {template_path}")
    with open(full_path, "r") as f:
        md = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    title = extract_title(md)
    html = markdown_to_html_node(md).to_html()
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    template = template.replace("href=/", f'href="{basepath}').replace("src=/", f'src="{basepath}')

    os.makedirs(dest_dir_path, exist_ok=True)

    output_path = osp.join(dest_dir_path, "index.html")
    with open(output_path, "w") as f:
        f.write(template)

if __name__=="__main__":
    print(f"++ Creating new public directory at {DOCS_DIR}")
    if os.path.exists(DOCS_DIR):
        shutil.rmtree(DOCS_DIR)
    os.makedirs(DOCS_DIR)

    copy_static(STATIC_DIR, DOCS_DIR)
    generate_pages_recursive(CONTENT_DIR, TEMPLATE_PATH, DOCS_DIR, basepath)