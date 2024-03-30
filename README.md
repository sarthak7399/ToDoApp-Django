# Simple ToDo App with Django

This repository contains a basic ToDo application built using Django. The app allows users to manage tasks with basic CRUD operations.

## Installation

### 1. Install Python

If Python is not already installed on your system, you can download and install it from the official website: [Python Downloads](https://www.python.org/downloads/)

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies for Python projects. Open a terminal and run the following commands to create and activate a virtual environment:

```bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
# For Windows
myenv\Scripts\activate
# For macOS/Linux
source myenv/bin/activate
```

### 3. Install Django

With the virtual environment activated, install Django using pip:

```bash
pip install django
```

## Basic Commands

### Initializing a Django Project

To initialize a new Django project, run the following command:

```bash
django-admin startproject mytodoapp
```

## Creating Django App

Navigate into the project directory and create a new Django app:

```bash
cd mytodoapp
django-admin startapp todo
```

## Running Migrations

Django uses migrations to manage database schema changes. Run the following commands to apply migrations:

### Navigate to the project directory

```bash
cd mytodoapp
```

### Run migrations

```bash
python manage.py migrate
```

## Running the Application

To run the Django development server and access the ToDo app, execute the following command:

```bash
python manage.py runserver
```

### File Structure and Roles

## manage.py

```text
This is a command-line utility that lets you interact with Django project. It's used for various tasks such as running the development server, creating migrations, and more
```

## mytodoapp/

```text
This is the project directory created by the startproject command. It contains settings for the project, including database configuration, URL configurations, and other project-specific settings
```

## todo/

```text
This is the app directory created by the startapp command. It contains models, views, templates, and other components related to the ToDo app
```

## models.py

```text
Defines the data models for the ToDo app. Models represent database tables and their relationships
```

## views.py

```text
Contains view functions or classes that handle requests and generate responses. Views interact with models to fetch or modify data and render templates
```

## urls.py

```text
Defines URL patterns for the ToDo app. It maps URLs to view functions or classes
```

## templates/

```text
This directory contains HTML templates for the ToDo app. Templates are rendered with dynamic content using Django's template language
```

## migrations/

```text
This directory stores database migrations created by Django. Migrations track changes to the database schema over time
```
