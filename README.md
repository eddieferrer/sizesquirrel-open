# SizeSquirrel

[![Dependabot badge](https://flat.badgen.net/dependabot/wbkd/webpack-starter?icon=dependabot)](https://dependabot.com/)

Your climbing shoe resource. Climbing shoe sales, find your size for any climbing shoe, recommendations based on foot shape, and more.

[SizeSquirrel - Climbing shoe sizing, recommendations, and deals](https://sizesquirrel.com)

## Project Status

One day I wanted to buy climbing shoes online, and the idea for SizeSquirrel sprung up.

I am thankful for everyone that has used and continues to use the site and support it in some way.

SizeSquirrel was never as financially successful as I had hoped and the many hours I spent on it were a labor of love. These days it barely manages to pay for the costs of running it, and I find my free time to be too valuable to continue working on it.

Going forward, I will do my best to:

* Keep the site active and operational.
* Add new climbing shoes to the site as they are released.

**There will probably not be any work done on new features for the time being.**

## Contributing Guidelines

Actively looking for contributors.

If you would like to contribute to SizeSquirrel, please open a GitHub issue for discussion or a pull request directly.

No contribution is too small.

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
        npm run dev
        ```

4. Visit localhost:3000
