import os
import os.path as osp
import shutil

from markdown_utils import extract_title
from markdown_to_html import markdown_to_html_node

CURRENT_DIR = osp.dirname(os.path.abspath(__file__))
STATIC_DIR = osp.join(CURRENT_DIR, "../static/")
PUBLIC_DIR = osp.join(CURRENT_DIR, "../public/")
CONTENT_DIR = osp.join(CURRENT_DIR, "../content/")
TEMPLATE_PATH = osp.join(CURRENT_DIR, "../template.html")

def copy_static(src, dst):
    if not os.listdir(src):
        return
    
    for content in os.listdir(src):
        full_path = osp.join(src, content)

        if osp.isfile(full_path):
            print(f"++ Copying {content} to {dst}")
            shutil.copy(full_path, dst)
        else:
            target_dir = osp.join(PUBLIC_DIR, content)
            os.makedirs(target_dir, exist_ok=True)
            copy_static(full_path, target_dir)


def generate_pages_recursive(content_path, template_path, dest_dir_path):
    if not os.listdir(content_path):
        return
    
    for content in os.listdir(content_path):
        full_path = osp.join(content_path, content)

        if osp.isfile(full_path) and full_path.endswith(".md"):
            print(f"Generating page from {full_path} to {dest_dir_path} using {template_path}")
            with open(full_path, "r") as f:
                md = f.read()

            with open(template_path, "r") as f:
                template = f.read()

            title = extract_title(md)
            html = markdown_to_html_node(md).to_html()
            template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

            os.makedirs(dest_dir_path, exist_ok=True)

            output_path = osp.join(dest_dir_path, "index.html")
            with open(output_path, "w") as f:
                f.write(template)
        
        elif osp.isdir(full_path):
            new_dest_dir_path = osp.join(dest_dir_path, content)
            os.makedirs(new_dest_dir_path, exist_ok=True)
            generate_pages_recursive(full_path, template_path, new_dest_dir_path)

    
if __name__=="__main__":
    print(f"++ Creating new public directory at {PUBLIC_DIR}")
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)
    os.makedirs(PUBLIC_DIR)

    copy_static(STATIC_DIR, PUBLIC_DIR)
    generate_pages_recursive(CONTENT_DIR, TEMPLATE_PATH, PUBLIC_DIR)