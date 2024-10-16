# Live Full Cycle Django

This project was created by following a live stream about development using Django. The goal is to build a web application using best practices with Django.

You can check the live stream that inspired this project [here](https://www.youtube.com/watch?v=bupRIZrXySk&t=1s&ab_channel=FullCycle).

## Features

- [x] Django admin interface for managing data
- [x] User authentication
- [x] CRUD functionality (Create, Read, Update, Delete)
- [x] Integration with a relational database
- [x] Form handling

## Technologies Used

- **Django**: The main framework for backend development.
- **Python**: The programming language used in the project.
- **HTML/CSS**: For the front-end visuals of the application.
- **PostgreSQL**: The relational database for storing data.
- **pgAdmin**: For managing the PostgreSQL database.
- **Docker Compose**: To manage and set up PostgreSQL and pgAdmin.
- **Pipenv**: For managing the Python environment and dependencies.

## Environment Variables

There are two `.env` files for this project:

- One in the root directory for Docker Compose settings.
- One inside the `videos` folder for Django settings.

Both `.env` files have corresponding `.env.example` files that you can use as a template.

## How to Run the Project

1. Clone the repository:
```bash
  git clone https://github.com/your-username/live-django.git
```

2. Copy the .env.example files to create your own .env files:
```bash
  cp .env.example .env
  cp videos/.env.example videos/.env
```

3. Create and activate a virtual environment using Pipenv:
```bash
  pipenv install
  pipenv shell
```

3. Run database migrations:
```bash
  python manage.py migrate
```

4. Start the PostgreSQL and pgAdmin services using Docker Compose:
```bash
  docker-compose up -d
```

5. Run the development server:
```bash
  python manage.py runserver
```

6. Access the Django Admin in your browser:
```
  http://127.0.0.1:8000/admin
```

## How to Contribute
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.