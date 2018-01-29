import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "argoid-client",
    version = "1.2.0",
    author = "Wim Muskee",
    author_email = "wimmuskee@gmail.com",
    url = "https://github.com/wimmuskee/argoid",
    description = ("Scheduler for sensor driven interactions on single board computers like the Beaglebone."),
    license = "MIT",
    keywords = "scheduling daemon",
    packages=find_packages(),
    scripts=["argoid-client"],
    data_files=[("/etc/argoid", ["client/argoid-client.conf.example"]),
        ("/usr/share/argoid", ["client/argoid-client-conf.schema"])]
)
