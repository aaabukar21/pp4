# pp4
Restaurant Booking System

This project is a simple Django-based restaurant reservation system that allows users to book a table at a restaurant. It includes a booking form where users can select their preferred reservation details such as date, time, and number of people. Once a reservation is made, the user is redirected to a confirmation page. Admins can manage the bookings via the Django Admin panel.

Features

The system allows users to make bookings by filling in a form with details like the reservation date, time, and number of people. After submitting the form, users are redirected to a confirmation page displaying their booking details. Admin users can manage these bookings via the Django Admin panel.

Technologies Used

The backend of the system is built using Django, a Python framework, and it uses PostgreSQL as the database. However, the system is compatible with MySQL as well. The frontend is built using basic HTML and CSS.

Installation

To get started with this project, first clone the repository to your local machine. You can use Git to clone the repository from your chosen platform.

Once you have the project files, create a virtual environment to isolate the project’s dependencies. On Windows, you can run the command python -m venv venv, while on macOS or Linux, use python3 -m venv venv.

After creating the virtual environment, activate it. On Windows, activate it by running the command .\venv\Scripts\Activate.ps1. On macOS or Linux, use source venv/bin/activate.

Next, install the required dependencies by running pip install -r requirements.txt. This will install all the necessary packages for the project.

Before running the server, you need to configure the database settings. In the settings.py file, set up your PostgreSQL database (or MySQL if you prefer). Ensure PostgreSQL is installed and create a database for this project.

Once the database is set up, run python manage.py migrate to apply all migrations and set up the database tables.

To access the Django admin panel, create a superuser account by running python manage.py createsuperuser. Follow the prompts to set up a superuser with your preferred email and password.

Now you can start the development server by running python manage.py runserver 127.0.0.1:5050. The application will be available at http://127.0.0.1:5050.

Usage

To make a reservation, open your browser and go to http://127.0.0.1:5050/reservations/book/. You will see a booking form where you can select the reservation date, time, and number of people. After submitting the form, you will be redirected to a confirmation page that shows your booking details.

If you're an admin, you can manage the reservations through the Django admin interface. Simply navigate to http://127.0.0.1:5050/admin/ and log in using the superuser credentials you created earlier. From the admin dashboard, you can view, add, and delete reservations.

Folder Structure

The project is organised with the following structure:

The main project directory contains the manage.py file, which is used to interact with your Django project. Inside this directory, there is a folder named django_project/ which holds all the configuration files like settings.py and urls.py.

There is also the reservations/ app, which handles the reservation functionality. This app contains files like models.py for defining the data models, views.py for the view logic, and forms.py for creating reservation forms. The app also contains the urls.py for defining routes specific to the reservation functionality.

Inside the app's templates/ folder, you'll find HTML files for rendering the booking form (book_table.html) and a success page (booking_success.html) upon booking.

Troubleshooting

If you encounter any issues with migrations, you can run python manage.py makemigrations to create new migration files, if necessary, and then apply them by running python manage.py migrate.

If the server is not running or you receive errors, ensure that your virtual environment is activated and that all dependencies are installed. Use the command pip install -r requirements.txt to check if any dependencies are missing.

Contributing

If you'd like to contribute to this project, you are welcome to fork the repository and submit a pull request with your changes. Please ensure that your code adheres to the project's coding standards and includes appropriate tests.

License

This project is open-source and available under the MIT License.

