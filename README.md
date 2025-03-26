# Eshop project

This project is an eshop, it was developed with python 3.13 and django 5.1.7, includes the basic features for an eshop, like the shopping cart, payment methods and confirmation email.
The technologies used to build this project:
- Django: To build the web application.
- Celery with RabbitMQ and Flower: To build the asynchronous heavy tasks.
- Redis: To store some data that is taken frequently.
- Stripe: To manage the payment with credit cards.
- Django rosetta: To manage the site translation.

## To run this project:
1. Create the virtual enviroment (In my case with conda):
> `conda create -n "eshop_venv" python=3.13`

2. Activate the virtual enviroment:
> `conda activate eshop_venv`

3. Create your .env file from example.env:

4. Install the dependencies:
> `pip install -r requirements`

5. Make the migrations:
> `python manage.py makemigrations`

6. Apply the migrations:
> `python manage.py migrate`

7. Create the super user:
> `python manage.py createsuperuser`

8. Generate the static files:
> `django-admin collectstatic`

9. Run the celery container:
> `docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13.1-management`

10. Run celery workers:
> `celery -A django_project worker -l info`

11. Redis container:
> `docker run -it --rm --name redis -p 6379:6379 redis:7.2.4`

12. Run stripe local webhook listener:
> `stripe listen --forward-to localhost:8000/payment/webhook/`

13. Finally run the server:
> `python manage.py runserver`
