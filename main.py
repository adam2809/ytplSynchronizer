from os import system as run_command

def put_file_on_connected_device(source, dest):
    print(run_command(f"adb push {source} {dest}"))
