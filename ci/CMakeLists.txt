# Minimal CMakeLists.txt for testing ci-check-spack-recipe action
cmake_minimum_required(VERSION 3.15)
project(test-package VERSION 1.0.0 LANGUAGES C)

# Test options
option(PRESENT_OPTION "Option that is present in package.py" ON)
option(MISSING_OPTION "Option that is missing in package.py" OFF)
option(OPTION_TO_IGNORE "Option that should be ignored" OFF)

# Dummy target
add_library(test-lib INTERFACE)
