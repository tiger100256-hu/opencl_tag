#install
pip install setuptools wheel
python setup.py sdist bdist_wheel

#usage
from opencl_tag import OPENCL_TAG
opencl_tag = OPENCL_TAG()
opencl_tag.tag()
