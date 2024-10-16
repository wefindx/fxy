import os
import json
from jupyter_client.kernelspec import KernelSpecManager
from IPython.utils.tempdir import TemporaryDirectory

from IPython.paths import get_ipython_dir
from IPython.paths import get_ipython_dir
from IPython.core.profiledir import ProfileDir

def ensure_ipython_profile_exists(profile_name, exec_lines=[]):
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

if __name__ == '__main__':
    install_my_kernel_spec('calc_qt', ['from fxy.calc import *'])
    install_my_kernel_spec('cas_qt', ['from fxy.cas import *'])
    install_my_kernel_spec('lab_qt', ['from fxy.lab import *', 'from fxy.plot import *'])
