# Eshop project

This project is an eshop, it was developed with django 5.1.7, includes the eshop basic features like, shopping cart, payment methods and confirmation email

## Useful command:
Command to execute stripe local webhook listener:
> `stripe listen --forward-to localhost:8000/payment/webhook/`

Command to run celery container:
> `docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13.1-management`

Command to run celery workers:
> `celery -A django_project worker -l info`

Command to run redis container:
> `docker run -it --rm --name redis -p 6379:6379 redis:7.2.4`
