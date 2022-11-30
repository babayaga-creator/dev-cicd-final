# devops21 cicd final

# Brief Description
A project that has been automated according to the CI/CD priciples.
That uses a Flask application that gets deployed via a k8 kluster.
Where you will be able to connect to via your local k8 tool.

# Setup
1. Start by creating a virtual enviroment by typing this command "python3 -m venv .venv" and activate it by typing "source .venv/bin/activate"

2. Install dependices to the enviroment by typing this command "pip install -r requirments.txt".

3. And also type in this command "pre-commit install --hook-type pre-commit --hook-type pre-push" to activate you hooks before commit anything new in the project.

4. Create a branch named dev and add, commit your changes. it will trigger a workflow named deploy-stage.

5. in order to activate the second workflow named deploy-production. simply create a pull request into main from dev branch.
