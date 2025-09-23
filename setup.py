import os
import re
import subprocess
import pybind11
import sys
from pathlib import Path

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext
#from wheel.bdist_wheel import bdist_wheel
from setuptools.command.build_py import build_py as _build_py    

class build_ext_first(_build_py):
    def run(self):
        self.run_command("build_ext")
        return super().run()

# A custom build extension for CMake.
class CMakeBuild(build_ext):
    def build_extension(self, ext):
        extdir = Path(self.get_ext_fullpath(ext.name)).parent.resolve()
            #f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}{os.sep}",
        cmake_args = [
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-Dpybind11_DIR={pybind11.get_cmake_dir()}",
            "-DCMAKE_BUILD_TYPE=Release", # or Debug
        ]
        build_args = []

        if sys.platform == "win32":
            cmake_args += ["-T", "ClangCl"] # Or "MSVC"
            build_args += ["--config", "Release"]

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        subprocess.check_call(
            ["cmake", str(Path().resolve())] + cmake_args, cwd=self.build_temp
        )
        subprocess.check_call(
            ["cmake", "--build", "."] + build_args, cwd=self.build_temp
        )

setup(
    name='opencl_tag',
    version='0.1',
    description='add custom event in opencl-intercept-layer',
    author='Your Name',
    author_email='your.email@example.com',
    ext_modules=[Extension('cl_tag', sources=[])],
    cmdclass={'build_ext': CMakeBuild, "build_py": build_ext_first},
    packages=['opencl_tag'],
    package_dir={"opencl_tag": "cl_tag"},
    package_data={'opencl_tag': ['*.pyd', '*.so']},
    include_package_data=True,
    zip_safe=False,
)

