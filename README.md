# Car Search Aggregator

Car Search Aggregator is a Python Django Rest Framework (DRF) project that collects information from two websites: [Kufar Auto](https://auto.kufar.by/l/cars) and [Onliner Auto](https://ab.onliner.by/skoda/octavia/2-pokolenie-restayling). It allows users to search for cars and retrieve aggregated data from both websites in a unified format.

## Features

- Search for cars based on various criteria such as make, model, price range, etc.
- Retrieve aggregated car listings from Kufar Auto and Onliner Auto.
- Display detailed information about each car, including its specifications and pricing.
- Provide a user-friendly interface for easy navigation and interaction.

## Installation

1. Clone the repository from GitHub:
   ```shell
   git clone https://github.com/your-username/Car-Search-Aggregator.git
2. Change into the project directory:
    ```shell
   cd Car-Search-Aggregator
3. Create and activate a virtual environment:
    ```shell
    python3 -m venv venv
    source venv/bin/activate
4. Install the project dependencies:
    ```shell
    pip install -r requirements.txt
5. Run database migrations:
    ```shell
    python manage.py migrate
6. Start the development server:
    ```shell
    python manage.py runserver
6. Start the development server:
    ```shell
    python manage.py runserver
6. Access the application at http://localhost:8000 in your web browser.

## Usage

1. Open your web browser and visit `http://localhost:8000` to access the Car Search Aggregator.
2. Use the search functionality to specify your desired car criteria.
3. The application will retrieve aggregated car listings from both Kufar Auto and Onliner Auto based on your search criteria.
4. View the search results and click on individual car listings to see detailed information.

## Contributing

Contributions to the Car Search Aggregator project are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name for your feature or bug fix.
3. Make your changes and commit them with clear and concise commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository explaining your changes.
