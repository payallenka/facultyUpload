# CASE 2: Faculty Upload

> One of many case of the VendOPrint project

## Setting up a virtual environment

1. Install `virtualenv`

```bash
pip install virtualenv
```

2. Create and move into the project directory

```bash
mkdir projectA
cd projectA
```

3. Activate the virtual environment (for linux)

```bash
source env/bin/activate
```

4. Verify whether the virtual environment is created successfully

```bash
pip list
```

This will list all the dependencies of the virtual environment

Congratulations you have isolated application dependencies from the system dependencies!

## Creating a requirements file

```bash
pip freeze > requirements.txt
```

This will list all the dependencies of the application, which can be used to replicate across different systems

## Creating an environment file to store secrets or configuration information

1. Install python-dotenv to interact with environment variables.

```bash
pip install python-dotenv
```

2. create an .env file to store secrets or configuration information

```bash
touch .env
```

3. Open the environment file(linux)

```bash
nano .env
```

4. open the environment file and past the following lines

```bash
AWS_ACCESS_KEY_ID = 'your_aws_access_key'
AWS_SECRET_ACCESS_KEY = 'your_secret_access keys'
AWS_S3_BUCKET_NAME = 'your_bucket_name'

DB_HOST = 'your_db_host'
DB_USERNAME = 'your_db_username'
DB_PASSWORD = 'your_db_password'
DB_NAME = 'you_db_name'
```

5. Exit the nano editor

```shortcuts
ctrl + s and ctrl + x
```

6. Add a .gitignore file

```bash
touch .gitignore
```

7. Add .env to .gitignore file to prevent it from being committed to codebase
