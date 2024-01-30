import uuid

def show_task(file_path):

    with open(file_path,'r') as file:
        first_character = file.read(1)
        # check is first character is empty or not
        if not first_character:
            print("Empty List\n")
        else:
            print(file.read(),'\n')

def add_task(file_path,the_task,the_deadline):

    with open(file_path,'a') as file:
        file.write(f'{uuid.uuid4()} | {the_task} | {the_deadline}\n')
        # \n fo new line each time text appends

def complete_task(file_path, task_id):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            # Check if the line contains the task_id
            if task_id not in line:
                file.write(line)
    print(f"Task with ID '{task_id}' completed.\n")

while True:
    print('== TODO LIST ==')
    print("[1] show tasks")
    print('[2] add task')
    print("[3] complete task")
    print("[4] exit")

    # create a file, does not overwrite, each time it runs
    file_path = 'todo_list.txt'
    with open(file_path,'a+') as file:
        pass

    my_choice = input('Your choice: ')

    if my_choice == '1':
        print('\n[YOUR TASKS]')
        show_task(file_path)

    elif my_choice == '2':
        print('\n[ADD TASK]')
        the_task = input('What is the task? ')
        the_deadline = input('What is the deadline? ')
        print()
        add_task(file_path,the_task,the_deadline)
    
    elif my_choice == '3':
        print('\n[COMPLETE TASK]')
        print('\n[YOUR TASKS]')
        show_task(file_path)
        
        task_id = input('Enter id to complete: ')
        complete_task(file_path,task_id)

    elif my_choice == '4':
        break
    
    else:
        print('Enter a correct number\n')
