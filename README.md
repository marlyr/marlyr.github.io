# static-site-generator

Welcome to my personal website repo! This website was generated using a custom-built [static site generator](https://www.boot.dev/courses/build-static-site-generator-python) from the course on [Boot.dev](https://www.boot.dev).

## Features

- **Custom Static Site Generator**: A Python-based script that takes Markdown files and converts them into static HTML pages.
- **Customizable Layout**: Simple and easy-to-modify HTML and CSS templates.

## If you want to make your own personal website, here's how:

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/marlyr/marlyr.github.io.git
   cd marlyr.github.io
   ```
2. Rename the repository to match your GitHub username:

- Navigate to your GitHub repository page for this project.
- Click on the “Settings” tab.
- Under the “Repository Name” section, rename it to `YOUR_USERNAME.github.io`.

3. Edit index.md for your first page:

You can find the index.md file inside the content/ directory. Edit it to include your personal information and any content you'd like to appear on your homepage. You can also create multiple pages by creating subdirectories (e.g., content/blog/post-one/index.md for a blog post).

4. Place your images inside the `static/images/` directory.

5. Build your site:

```bash
python3 src/main.py
```
This will generate your static site in the `docs/` folder.

6. If you'd like to serve it locally, use a simple server (e.g., Python's built-in HTTP server) to preview the site:

```bash
sh main.sh
```
Then, visit http://localhost:8888 in your browser.

7. Deploy on GitHub Pages:

- Push your changes to forked repo.

- Go to your GitHub repository's settings and select the Pages section.

- Set the Source to the `main` branch and the `docs/` folder (which is where the generated HTML files are located).

- Your site will be live at https://YOUR_USERNAME.github.io/.


> [!NOTE]
> If you decided to name your repo something else other than `YOUR_USERNAME.github.io`, then build your site by running this instead:
> ```bash
> python3 src/main.py "/YOUR_REPO_NAME/"
> ```
> This will adjust the paths for your custom repository name.

## Further customization

- Edit template.html to change the layout.
- Edit static/index.css to update the styling.
