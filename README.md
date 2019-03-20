# Welcome to Budgie

This API will give you access to resources related to Budgie. It is powered by Django Rest Framework.

## Getting Started
- Create an empty directory to house your new project
- Run `virtualenv env` to create a virtual environment within that directory
- Run `source env/bin/activate` to initialize a virtual environment (`deactivate` to exit environment)
- Run `git clone git@github.com:jasehackman/Capstone-Budgie-DjangoREST.git`
- Run `cd capstone`
- Run `python manage.py makemigrations budgy`
- Run `python manage.py migrate`
- Initialize the project using the command line by typing `python manage.py runserver` in the main directory.
- Access the application in a browser at `http://localhost:8000/`.

## Using the API
All calls to the API will be made from `http://localhost:8000/`

## Resources

### Authentication
* This API uses token authentication.
  * Register: Post to `http://127.0.0.1:8000/register` with username, password, first_name, last_name and email. A token will be returned. Use it in all other requests
  * Login: Post to `http://127.0.0.1:8000/authenticate/` with username and password. A token will be returned. Use it in all other requests

### Budgets
* GET
    * GET All: You can access a list of all budgets by submitting a GET request to `http://localhost:8000/budgets`
    * GET One: You can get the information of a single budget by submitting a GET request to `http://localhost:8000/budgets/{budgetID}`
    * GET Archived Budgets: You can get all archived budgets by including the query `?archived=true`. Example: `http://localhost:8000/budgets/?archived=true`.
      * Replace `true` with `false` to get all non archived budgets
* PUT
    * PUT Update Single Budget: You can update a single budgets's information by submitting a PUT request to `http://localhost:8000/budgets/{budgetId}`
        * You must submit the entire changed object which will include: `name`, `amount`, `archived` and `user`

* POST
    * POST New Budgets: You can post a new budget by submitting a POST request to `http://localhost:8000/budgets`
        * The following fields must be included: `name`, `amount`, `archived` and `user`

### Categories
* GET
    * GET All: You can access a list of all categories by submitting a GET request to `http://localhost:8000/categories`
    * GET One: You can get the information of a single category by submitting a GET request to `http://localhost:8000/categories/{categoryID}`
    * GET Filter Categories: You can get categories filtered on `budget_id` and `name`. Example: `http://localhost:8000/categories/?budget_id=1`
* PUT
    * PUT Update Single Category: You can update a single category's information by submitting a PUT request to `http://localhost:8000/categories/{categoryId}`
        * You must submit the entire changed object which will include: `name`, `amount` and `budget`

* POST
    * POST New Categories: You can post a new category by submitting a POST request to `http://localhost:8000/categories`
        * The following fields must be included: `name`, `amount` and `budget`

### Expenses
* GET
    * GET All: You can access a list of all expenses by submitting a GET request to `http://localhost:8000/expenses`
    * GET One: You can get the information of a single expense by submitting a GET request to `http://localhost:8000/expenses/{expensesID}`

* PUT
    * PUT Update Single Expense: You can update a single expense's information by submitting a PUT request to `http://localhost:8000/expenses/{expenseId}`
        * You must submit the entire changed object which will include: `name`, `amount`, `date`, `notes` and `category_id`

* POST
    * POST New Expense: You can post a new expense by submitting a POST request to `http://localhost:8000/expenses`
        * The following fields must be included: `name`, `amount`, `date`, `notes` and `category_id`