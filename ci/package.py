# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class TestPackage(CMakePackage):
    """Minimal test package for ci-check-spack-recipe action"""

    homepage = "https://github.com/NOAA-EMC/ci-check-spack-recipe"
    url = "https://github.com/NOAA-EMC/ci-check-spack-recipe/archive/v1.0.0.tar.gz"

    maintainers = ["AlexanderRichert-NOAA"]

    version("1.0.0", sha256="0000000000000000000000000000000000000000000000000000000000000000")

    # This variant is present and should be found
    variant(
        "present_option",
        default=True,
        description="Option that is present in CMakeLists.txt"
    )

    def cmake_args(self):
        args = [
            self.define_from_variant("PRESENT_OPTION", "present_option"),
        ]
        return args
