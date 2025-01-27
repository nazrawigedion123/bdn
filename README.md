README.md

Welcome to the BDN Django Project

This repository contains the code for the BDN company portfolio website, a Django-based application showcasing our services and expertise.

About BDN

We are a team of dedicated professionals committed to delivering top-notch solutions tailored to your needs. We bring a wealth of experience and a passion for innovation to every project we undertake.

Getting Started

To clone this repository and run the Django application locally, follow these steps:

1. Prerequisites

    Make sure you have Git installed on your system. You can download it from https://git-scm.com/.
    You'll also need Python (version 3.6 or later) and pip (the Python package installer) installed. You can download Python from https://www.python.org/downloads/.

2. Clone the Repository

Open a terminal or command prompt and navigate to the directory where you want to clone the repository. Then, use the following command to clone the BDN project from GitHub (or your preferred hosting platform):
Bash

git clone https://nazrawigedion123/bdn.git


3. Create a Virtual Environment (Recommended)

It's highly recommended to create a virtual environment to isolate the project's dependencies from your system-wide Python installations. Here's how to create one using venv:
Bash
    

python -m venv venv

This creates a virtual environment directory named venv. Activate it using the following command (depending on your operating system):
bash

    Windows: venv\Scripts\activate.bat

bash



    macOS/Linux: source venv/bin/activate





4. Install Dependencies

Navigate to the project directory (usually bdn) and install the required Python packages listed in the requirements.txt file using pip:
Bash

pip install -r requirements.txt

5. Run the Development Server

With the virtual environment activated and dependencies installed, you can start the Django development server:
Bash

python manage.py runserver

This will typically start the server at [invalid URL removed] (or http://localhost:8000/) in your web browser. You can then access the BDN portfolio website and explore its features.

Additional Notes

    The Django project files are located inside the bdnpage directory.
    The README.md, requirements.txt, and other configuration files are located at the root of the repository.
    You might need to configure additional settings (database connection, etc.) depending on your specific deployment environment. Refer to the Django documentation for more details: https://docs.djangoproject.com/en/5.1/

Feel free to explore the code and customize the website to your company's needs. If you have any questions, don't hesitate to reach out to the development team.