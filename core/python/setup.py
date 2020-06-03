
from setuptools import find_packages
from setuptools import setup
from kungfu.version import get_version

setup(
    name="kungfu",
    version= get_version(),
    author="taurus.ai",
    license="Apache-2.0",
    packages=find_packages(exclude=["hooks", "test", "extensions"]),
    include_package_data=True,
    install_requires=[
        "click>=5.1",
        "sqlalchemy==1.3.8",
        "psutil==5.6.6",
        "numpy",
        "pandas",
        "tabulate==0.8.3",
        "PyInquirer==1.0.3",
        "prompt_toolkit==1.0.14",
        "rx==3.0.1"
    ],
    entry_points={"console_scripts": ["kfc = kungfu.__main__:main"]},
)
