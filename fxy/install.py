import os
import json
from jupyter_client.kernelspec import KernelSpecManager
from IPython.utils.tempdir import TemporaryDirectory

from IPython.paths import get_ipython_dir
from IPython.paths import get_ipython_dir
from IPython.core.profiledir import ProfileDir

from appdirs import user_config_dir
from setuptools.command.install import install
from pathlib import Path

# Create the configuration directory
config_dir = user_config_dir("fxy")


def save_variable_to_json(variable_name, variable_value, filename):
    """Saves a variable to a specified JSON file in the config directory."""
    config_dir = user_config_dir("fxy")

    config_file = os.path.join(config_dir, filename)

    # Load existing variables if the file exists
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            variables = json.load(f)
    else:
        variables = {}

    variables[variable_name] = variable_value

    with open(config_file, 'w') as f:
        json.dump(variables, f)

def save_kernel_info(kernel_name):
    save_variable_to_json(kernel_name, {"status": "created"}, 'state.json')

def ensure_ipython_profile_exists(profile_name, exec_lines=[]):
    Path(config_dir).mkdir(parents=True, exist_ok=True)

    ipython_dir = get_ipython_dir()
    profile_dir = os.path.join(ipython_dir, f"profile_{profile_name}")

    if not os.path.exists(profile_dir):
        ProfileDir.create_profile_dir_by_name(ipython_dir, profile_name)

    # Path to the startup directory and 00-init.py
    startup_dir = os.path.join(profile_dir, "startup")
    os.makedirs(startup_dir, exist_ok=True)
    init_file = os.path.join(startup_dir, "00-init.py")

    # Write provided lines into the 00-init.py file
    with open(init_file, 'w') as f:
        for line in exec_lines:
            f.write(f"{line}\n")

    return profile_dir

def install_my_kernel_spec(kernel_name, exec_lines=[]):
    profile_path = ensure_ipython_profile_exists(kernel_name, exec_lines) #"/home/mindey/.ipython/profile_cas"

    kernel_json = {
     "argv": [
      "/home/mindey/.venv/bin/python3",
      "-Xfrozen_modules=off",
      "-m",
      "ipykernel_launcher",
      "-f",
      "{connection_file}",
      f"--profile-dir={profile_path}"
     ],
     "display_name": f"Python ({kernel_name})",
     "language": "python",
     "metadata": {
      "debugger": True
     }
    }

    with TemporaryDirectory() as td:
        os.chmod(td, 0o755)

        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)

        KernelSpecManager().install_kernel_spec(td, kernel_name, user=True)
        save_kernel_info(kernel_name)

if __name__ == '__main__':
    install_my_kernel_spec('fxy_calc', ['from fxy.calc import *', 'from fxy.plot import *'])
    install_my_kernel_spec('fxy_cas', ['from fxy.cas import *', 'from fxy.plot import *'])
    install_my_kernel_spec('fxy_lab', ['from fxy.lab import *', 'from fxy.plot import *'])
