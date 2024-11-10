# Excel Automation with Django and RabbitMQ

This project demonstrates automated Excel file generation using Django and RabbitMQ. 

## Project Overview

- **Django**: Manages the web interface and user requests.
- **RabbitMQ**: Message broker to communicate between producer and consumer.
- **Pandas**: Converts JSON data to an Excel file.
- **Faker**: Generates random data for demo purposes.

## Setup

### Requirements

- **Python 3.x**
- `django`, `pika`, `pandas`, `openpyxl`, `faker`
- RabbitMQ instance (CloudAMQP or local)

### Installation

1. Clone the repo and navigate into it:
   ```bash
   git clone <repository-url>
   cd <repository-name>

2. Install dependencies:
    ```bash
    pip install django pika pandas openpyxl faker

3. Start Django and run consumer.py:
    ```bash
    python manage.py runserver
    python consumer.py
