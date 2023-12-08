class ToDoList:

    def __init__(self):
        self.tasks = {}

    def add_task(self, task_description):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {'description': task_description, 'completed': False}
        print(f'Task "{task_description}" added with ID {task_id}')

    def view_tasks(self):
        print('\nTo-Do List:')
        for task_id, task_details in self.tasks.items():
            status = 'Completed' if task_details['completed'] else 'Not Completed'
            print(f'{task_id}. {task_details["description"]} - {status}')
        print()

    def update_task(self, task_id, new_description):
        if task_id in self.tasks:
            self.tasks[task_id]['description'] = new_description
            print(f'Task {task_id} updated: {new_description}')
        else:
            print(f'Task {task_id} not found')

    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True
            print(f'Task {task_id} marked as completed')
        else:
            print(f'Task {task_id} not found')

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f'Task {task_id} deleted')
        else:
            print(f'Task {task_id} not found')

def main():
    todo_list = ToDoList()

    while True:
        print('\nTo-Do List Application:')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Update Task')
        print('4. Mark Task as Completed')
        print('5. Delete Task')
        print('6. Exit')

        choice = input('Enter your choice (1-6): ')

        if choice == '1':
            task_description = input('Enter task description: ')
            todo_list.add_task(task_description)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            task_id = int(input('Enter task ID to update: '))
            new_description = input('Enter new task description: ')
            todo_list.update_task(task_id, new_description)

        elif choice == '4':
            task_id = int(input('Enter task ID to mark as completed: '))
            todo_list.complete_task(task_id)

        elif choice == '5':
            task_id = int(input('Enter task ID to delete: '))
            todo_list.delete_task(task_id)

        elif choice == '6':
            print('Exiting To-Do List Application. Goodbye!')
            break

        else:
            print('Invalid choice. Please enter a number between 1 and 6.')

if __name__ == '__main__':
    main()
