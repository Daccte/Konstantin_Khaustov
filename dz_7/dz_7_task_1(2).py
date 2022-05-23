import os

new_dir = ('settings', 'mainapp', 'adminapp', 'authapp')
for i in new_dir:
    dir_path = os.path.join('my_project', i)
    os.makedirs(dir_path, exist_ok=True)
