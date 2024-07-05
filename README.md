# DJANGO BLOG PROJECT
In this project, I utilized the Django Framework to develop a blog with an integrated Django Admin interface for creating posts.

![image](https://github.com/goncalvesfrederico/django-blog-project/assets/110829207/87799791-fe92-407a-8ea2-250e35a07ce3)
![image](https://github.com/goncalvesfrederico/django-blog-project/assets/110829207/6a55585f-c5af-423e-9d6c-4e868f282f15)
![image](https://github.com/goncalvesfrederico/django-blog-project/assets/110829207/269032dd-c311-450b-a54d-326278bf618c)
![image](https://github.com/goncalvesfrederico/django-blog-project/assets/110829207/76dc3e51-11d5-4b5c-a6ec-89626249297d)

## Features
- Create, edit, and delete blog posts through the Django Admin interface.
- Organize posts using categories and tags.
- Search functionality to find posts by title, excerpt, or content.
- Display post covers within the posts.
- Custom views and URLs for tags and categories.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/goncalvesfrederico/django-blog-project.git
    ```
2. Navigate to the project directory:
    ```bash
    cd django-blog-project
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the migrations:
    ```bash
    python manage.py migrate
    ```
5. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Docker Setup

1. Build the Docker image:
    ```bash
    docker build -t django-blog .
    ```
2. Run the Docker container:
    ```bash
    docker run -d -p 8000:8000 django-blog
    ```
3. Access the application at `http://127.0.0.1:8000/`.

## Usage
- Access the Django Admin interface at `http://127.0.0.1:8000/admin/` to create and manage posts.
- Visit the blog at `http://127.0.0.1:8000/` to see the posts.

## Contributing
- Fork the repository.
- Create a new branch for your feature or bugfix.
- Submit a pull request with a detailed explanation of your changes.

## License
This project is licensed under the MIT License.

For more information, visit the [GitHub repository](https://github.com/goncalvesfrederico/django-blog-project).
