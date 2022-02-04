import os
import argparse

parser = argparse.ArgumentParser(
    description="manage commands",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

# creating app folder structure
parser.add_argument("create_app", type=str, help="create_app command")
parser.add_argument("app_name", type=str, help="name of the app")

args = parser.parse_args()

# if create_app given with the app name
if args.create_app == 'create_app' and args.app_name:
    current_path = os.getcwd()  # getting current path
    app = args.app_name
    new_path = os.path.join(current_path, app)
    os.mkdir(new_path)  # creating app folder
    for f in ['__init__.py', 'models.py', 'routes.py']:
        with open(os.path.join(new_path, f), 'w') as fp:
            pass
    pages_dir = os.path.join(new_path, 'pages')
    os.mkdir(pages_dir)  # creating pages directory
    for f in ['__init__.py', 'filters.py']:
        with open(os.path.join(pages_dir, f), 'w') as fp:
            pass
    page1_dir = os.path.join(pages_dir, 'page1')
    os.mkdir(page1_dir)
    for f in ['__init__.py', 'view.py']:
        with open(os.path.join(page1_dir, f), 'w') as fp:
            pass

print(f'{args.app_name} is succussfully create')
