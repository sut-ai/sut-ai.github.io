# SUT-AI

## For Course Organizers

### Adding a New Page
To add a new page, you can create a directory in `src/`. Let's say you create `src/example/`. Then you should create `src/example/index.html`. A general html is written and you can use it by putting the following in your `index.html`.
```
{% extends 'common_index.html' %}
```
Then you can create `src/example/context.yml` to define your page.

### Using `common_index.html`
The `common_index.html` implements a general webpage. It includes a navbar and uses the `parts` key from the related `context.yml` to generate each part. There are different types of "part", defined by `type` key of each item in `parts`.

| Type | Functionality |
|---|---|
| section | This is the go-to "part", which just renders markdown from `text` key (which can be empty). You can also include `subsections` which takes the same key `text` and renders the value of it as markdown.  |
| table | This "part" is to generate responsive tables. These are different from markdown tables in case of how they are displayed in small screens of phones.<br><br>It takes two keys `columns` and `rows`. `columns` is a mapping from column names to column metadata, accepting keys `display_name`, `size` (an integer weight, relative to total size), and `cell_class` which should be a css class that gets added to each cell.<br>`rows` is a list, each having the same keys as the column names (not the `display_name`) having the value of that column in the row. The values are rendered as markdown. |
| people | This "part" is to generate a responsive grid of instructors and teaching assistants. It takes a `people_data` key with a list value, that defines roles (instructors, head assistants, assistants, etc), each item accepting keys `role`, `display_name` and `people`. The `people` value should be a list of people data, each taking the keys `name`, `pic`, and `website` (optional). The `pic` can either be a link, or a path to a picture file in the repo (relative to `assets`). |

### Archiving The Website
After each semester, to archive the website, create a new directory in `src/archive`.
As an example it could be `src/archive/fall2023`.
Then move every file and directory (excluding `src/archive`) from the `src` directory into `src/archive/fall2023`.

Then you should add a link to this archived website. Depending on the state of the website, there is a section for archives. Remember to add the new link there, using other links as an example.


### Adding Internal Links
All internal links should be relative, except for links to archives and to assets (e.g. slides). This is to make archiving easy. 

## Development
The code uses:
- `jinja2` for template rendering
  - Check the code in `main.py`. It looks for all `index.html` files in `src/` and generates a page relative to that. It passes the `context.yml` next to it to the template. It also checks `globals.py` and passes every function/data that `Globals.get()` returns to the template.
  - Current `globals.py` implements a functionality to render header (navbar), by finding the first `header_context.yml` in the parent directories of the current `index.html` and passing its value to the template, which is used by the default `base/header.html`.
- `tailwindcss` for styling
  - You should avoid adding new css classes. But if you 1. can't find any other way, 2. have searched [tailwind docs](https://tailwindcss.com/docs/) and have not found the style you want, 3. have asked every chat gpt version for a solution, then you can add your own classes in `assets/css/main.css`.
- jekyll to host github pages (this is redundant and can be removed in production at least).
  - For development, you should run the docker container defined in `docker-compose.yml`, and run `python main.py` after every change you make anywhere.
    - The website can be accessed from your [http://localhost:4000](http://localhost:4000)
    - You can fix this by adding a watcher for files in your IDE, or adding a feature to code to run it with watch on files.