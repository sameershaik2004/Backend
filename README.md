# Todo List App

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/sameershaik2004/Backend.git
    cd Backend
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv env
    ```

3. Activate the virtual environment:
    - For Windows:
      ```bash
      .\env\Scripts\activate
      ```
    - For Mac/Linux:
      ```bash
      source env/bin/activate
      ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:
    ```bash
    python manage.py migrate
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Running Tests

1. Install `coverage`:
    ```bash
    pip install coverage
    ```

2. Run tests with coverage:
    ```bash
    coverage run manage.py test
    ```

3. View the coverage report:
    ```bash
    coverage html
    ```

4. Open `htmlcov/index.html` in a browser.
