import subprocess, shlex, sys, os

command_error = "Command not recognised.\n"
setup_error = f"{command_error}Exiting setup."

home = os.path.expanduser('~')
base_path = os.path.dirname(__file__)
std_config_path = f"{home}/.zanz_notify_config"
dest_path = f"{home}/.notify"

bashrc_edit = """alias notify='python3 $HOME/.notify/notify_app.py'
export PYTHONPATH=$HOME/.notify/python_module
"""

credentials = "credentials = 0"
done = False
update = False

if len(sys.argv) == 2 and sys.argv[1] == "-update":
    update = True

if not update:
    print("\nThanks for installing notify!\n\nBase repo: https://github.com/Zanzibarr/Telegram_Python_Notifier\nScript made by @Zanzibarr and @RickSrick.")
print("\nBeginning setup...\n")

if os.path.exists(std_config_path):
    load_conf_in = input(f"Found config file inside {std_config_path}.\nLOAD THIS CONFIGURATION? [y/n /q to quit]: ")
    while load_conf_in not in ("y", "n", "q"):
        load_conf_in = input(f"{command_error}LOAD THIS CONFIGURATION? [y/n /q to quit]: ")
        
    if load_conf_in == "q":
        print("Exiting setup.")
        exit(0)
    elif load_conf_in == "y":
        print("Loading configuration...")
        credentials = "credentials = json.load(open('"+std_config_path+"', 'r'))"
        done = True

if not done:
    setup_mode = input(f"Wish to store the credentials?\nStoring the credentials writes them on plain text inside the config file ({std_config_path}).\nIf you choose not to store them you will be asked to insert the credentials each time.\nSTORE THE CREDENTIALS? [y/n /q to quit]: ")

    while setup_mode not in ("y", "n", "q"):
        setup_mode = input(f"{command_error}LOAD THIS CONFIGURATION? [y/n /q to quit]: ")
    
    if setup_mode == "q":
        print("Exiting setup.")
        exit(0)
    elif setup_mode == "y":
        token = input("Insert the token for the bot you want to use: ")
        chat_id = input("Insert the your chat id: ")
        print(f"Storing credentials inside {std_config_path}...")
        json_cred = '{"token":"'+token+'","chatid":"'+chat_id+'"}'
        conf_file = open(std_config_path, "w")
        conf_file.write(json_cred)
        conf_file.close()
        credentials = "credentials = json.load(open('"+std_config_path+"', 'r'))"

print("Writing notify_app.py")

with open(f"{base_path}/setup_files/notif_app.py", "r") as f:
    script = f.read()
    
START_IN = "'''>>__EDIT__>>"
END_IN = "<<__EDIT__<<'''"
        
p1, _, r= script.partition(START_IN)
r = r.partition(END_IN)[2]

script = p1+credentials+r

with open(f"{base_path}/notify_app.py", "w") as f:
    f.write(script)

if not os.path.isdir(f"{dest_path}"):
    os.mkdir(f"{dest_path}")
if not os.path.isdir(f"{dest_path}/python_module"):
    os.mkdir(f"{dest_path}/python_module")

print(f"Moving files to base path ({dest_path})")
subprocess.run(shlex.split(f"cp {base_path}/notify.py {dest_path}/python_module/notify.py"))
subprocess.run(shlex.split(f"cp {base_path}/notify_app.py {dest_path}/notify_app.py"))

done = False

with open(f"{home}/.bashrc", "r") as f:
    if bashrc_edit in f.read():
        done = True

if not done:
    print(f"Writing on {home}/.bashrc file (append)...")
    with open(f"{home}/.bashrc", "a") as f:
        f.write(bashrc_edit)
    reb = ""
    while reb not in ("y", "n"):
        reb = input(f"To use notify you will have to reboot.\nREBOOT NOW? [y/n]: ")
        if reb not in ("y", "n"):
            print("Command not recognised.")
    if reb == "y":
        subprocess.run(shlex.split("reboot"))

print("Setup completed.")
