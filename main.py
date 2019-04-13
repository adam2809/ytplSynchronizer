import subsystem

def run_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    # Returns a (output, error) pair
    return process.communicate()

def put_file_on_connected_device(source, dest):
    output, error = run_command(f"adb push {source} {dest}")
    print(output)
