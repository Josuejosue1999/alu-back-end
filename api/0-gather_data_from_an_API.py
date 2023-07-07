#!/usr/bin/python3

"""
Python script to retrieve and display an employee's TODO list progress.
Usage: ./gather_data_from_an_API.py employee_id
"""

import sys
import requests

API_BASE_URL = 'https://jsonplaceholder.typicode.com'
EMPLOYEE_ENDPOINT = '/users/{employee_id}'
TODO_ENDPOINT = '/todos?userId={employee_id}'


def get_employee_info(employee_id):
    """Retrieve employee information"""
    url = API_BASE_URL + EMPLOYEE_ENDPOINT.format(employee_id=employee_id)
    response = requests.get(url)
    employee_info = response.json()
    return employee_info['name']


def get_todo_list(employee_id):
    """Retrieve employee's TODO list"""
    url = API_BASE_URL + TODO_ENDPOINT.format(employee_id=employee_id)
    response = requests.get(url)
    todo_list = response.json()
    return todo_list


def display_todo_progress(employee_name, todo_list):
    """Display employee's TODO list progress"""
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task['completed'])
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todo_list:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./gather_data_from_an_API.py employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]
    employee_name = get_employee_info(employee_id)
    todo_list = get_todo_list(employee_id)
    display_todo_progress(employee_name, todo_list)
