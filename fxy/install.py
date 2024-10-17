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
    profile_path = ensure_ipython_profile_exists(kernel_name, exec_lines)

    import os, sys, platform
    if platform.system() == 'Windows':
        python_executable = os.path.join(Path(sys.prefix), 'Scripts', 'python.exe')
    else:
        python_executable = os.path.join(Path(sys.prefix), 'bin', 'python')

    kernel_json = {
     "argv": [
      python_executable,
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
        # Removed save_kernel_info call

def kernel_exists(kernel_name):
    """Check if the kernel exists using KernelSpecManager."""
    ksm = KernelSpecManager()
    kernels = ksm.get_all_specs()
    return kernel_name in kernels

if __name__ == '__main__':
    install_my_kernel_spec('fxy_calc', ['from fxy.calc import *', 'from fxy.plot import *'])
    install_my_kernel_spec('fxy_cas', ['from fxy.cas import *', 'from fxy.plot import *'])
    install_my_kernel_spec('fxy_lab', ['from fxy.lab import *', 'from fxy.plot import *'])
