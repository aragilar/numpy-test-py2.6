from setuptools import setup
from disutils.command.build import build

class BuildTest(build):
    def run(self):
        import numpy

setup(
    name="test",
    setup_requires=["numpy==1.11.1"],
    cmdclass = {"build": BuildTest}
)
