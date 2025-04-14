# static-site-generator

Welcome to my personal website repo! This website was generated using a custom-built [static site generator](https://www.boot.dev/courses/build-static-site-generator-python) from the course on [Boot.dev](https://www.boot.dev).

## Features

- **Custom Static Site Generator**: A Python-based script that takes Markdown files and converts them into static HTML pages.
- **Customizable Layout**: Simple and easy-to-modify HTML and CSS templates.

## Installation

### Prerequisites

- Python 3.7+ installed on your machine.

### Steps

1. Clone this repo:
  
  ```
  git clone https://github.com/marlyr/static-site-generator.git
  ```

2. Navigate into the project directory:

  ```
  cd static-site-generator
  ```

4. To add your first page, create an `index.md` file inside the `content/` directory. You can also create multiple pages by using subdirectories (e.g., `content/blog/post-one/index.md`).

5. Place your images inside the `static/images/` directory.

6. Build your site:
  ```
  sh main.sh
  ```
## Customization
Edit `template.html` to change the layout.
Edit `static/index.css` to update the styling.
