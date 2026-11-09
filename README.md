
# Task Manager
I chose the Task Manager project because of my extensive experience and familiarity with building similar projects in previous semesters, and because it is significantly more dynamic and interactive than the other options.

## Project Overview

Task Manager is a simple application built with Python.
It allows users to add, view, complete, and delete tasks.
Tasks are stored in a JSON file.

## Tech Stack

- Python 3.12
- Docker
- JSON
- Git and GitHub

## Project Structure

TaskManager/
├── src/
│   └── main.py
├── README.md
├── Dockerfile
├── .dockerignore
├── .gitignore
└── docs/
    ├── screenshots/
    └── notes.md

## Build and Run Using Docker

### 1. Build the Docker Image

```bash
docker build -t task-manager .
```

### 2. Run the Container

```bash
docker run --name task-manager -it -v task_data:/app/data task-manager
```

### 3. Start the Existing Container Again

```bash
docker start -ai task-manager
```

## Stop and Clean Up

Exit the application by choosing option 5.

To stop the container:

```bash
docker stop task-manager
```

To remove the container:

```bash
docker rm task-manager
```

To remove the Docker volume:

```bash
docker volume rm task_data
```

## Configuration Notes

- Application language: Python 3.12
- Docker working directory: /app
- Data directory: /app/data
- Docker volume: task_data
- No environment variables are required

## How to Test

Run the application and try the following:

1. Add a new task
2. View all tasks
3. Complete a task
4. Delete a task
5. Exit the application

The application stores tasks in a JSON file

## Attribution

This project was created independently for the OS Lab Assignment 2
