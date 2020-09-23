# SizeSquirrel

[![Dependabot badge](https://flat.badgen.net/dependabot/wbkd/webpack-starter?icon=dependabot)](https://dependabot.com/)

Your climbing shoe resource. Climbing shoe sales, find your size for any climbing shoe, recommendations based on foot shape, and more.

## Instructions for running in development

1. Clone Repository

    ```bash
    git clone git@github.com/eddieferrer/sizesquirrel-open.git
    ```

    Use one terminal window to run the backend server. Use a separate window to run the frontend server

2. Run the backend server. In directory `sizesquirrel-open/`

    1. Make virtual environment with python3

        ```bash
        mkvirtualenv --python=/usr/bin/python3 sizesquirrel
        ```

    2. Activate virtual environment

        ```bash
        workon sizesquirrel
        ```

    3. Install python dependencies

        ```bash
        pip install -r requirements.txt
        ```

    4. Copy sample database

        ```bash
        cp sample_dev-database.db dev-database.db
        ```

    5. Run prerequisite scripts

        ```bash
        python batch_process_feeds dev
        python manage.py set_stats
        ```

    6. Run backend server

        ````bash
        python manage.py runserver
        ````

3. Run the frontend server. In directory `sizesquirrel-open/frontend`

    1. Install npm packages

        ```bash
        npm install
        ```

    2. Run development server

        ```bash
        npm run serve
        ```

4. Visit localhost:5000

## Contributing Guidelines 

Coming soon...
