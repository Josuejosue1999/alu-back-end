#!/usr/bin/python3
import requests

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    # Fetch employee information
    response = requests.get(employee_url)
    if response.status_code != 200:
        print(f"Failed to retrieve employee information for ID: {employee_id}")
        return

    employee_data = response.json()
    employee_name = employee_data['name']

    # Fetch employee's TODO list
    response = requests.get(todos_url)
    if response.status_code != 200:
        print(f"Failed to retrieve TODO list for employee: {employee_name}")
        return

    todos_data = response.json()
    total_tasks = len(todos_data)
    done_tasks = [todo['title'] for todo in todos_data if todo['completed']]

    # Display TODO list progress
    print(f"Employee {employee_name} is done with tasks ({len(done_tasks)}/{total_tasks}):")
    print(f"{employee_name}: {len(done_tasks)}/{total_tasks}")
    for task in done_tasks:
        print("\t", task)

# Example usage: get_employee_todo_progress(1)