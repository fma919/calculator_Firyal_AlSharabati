# build.py - PyBuilder build descriptor
# Author: Firyal Al Sharabati
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")

name = "calculator_Firyal_AlSharabati"
version = "0.1"
default_task = "publish"


@init
def initialize(project):
    project.set_property("name", "calculator_Firyal_AlSharabati")
    project.set_property("version", "0.1")
    project.set_property("default_task", "publish")

    # Tell PyBuilder where the source code and the unit tests live
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property("dir_source_unittest_python", "tests/unittest/calculator_Firyal_AlSharabati")
    project.set_property("unittest_module_glob", "test_*")
    project.set_property("unittest_module", "tests.unittest")
