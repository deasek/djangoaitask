# Aionix Test Assignment

## Local development setup
- Make sure to have docker and docker compose installed
- Clone the repository
- Copy `.env.example` to `.env`, add `OPENAI_API_KEY`
- Run `docker compose up -d --build`
- Run migrations: `docker compose exec app python3 manage.py migrate`
- Create super user: `docker compose exec app python3 manage.py createsuperuser`

## Test user input

Test user input on http://localhost:8001

Example input test has been added to this repo as `example_text.txt`. Only plain text files are supported.
Each paragraph is separated by a blank line.
Admin interface (http://localhost:8001/admin) may be used (after login as super user) to browse generated summaries:
http://localhost:8001/admin/core/summary/



## Code quality, formatting and linters
To run linter and code formatter (`ruff`) run: `docker compose exec app python3 ruff .`