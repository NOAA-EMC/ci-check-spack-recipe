# GitHub CI Action: check-spack-recipe

![Test action](https://github.com/NOAA-EMC/ci-check-spack-recipe/actions/workflows/test-action.yml/badge.svg)

This repository provides a GitHub Action for checking a Spack recipe for a 
CMake-based package to confirm that it contains variants reflecting the
options available in a given CMakeLists.txt.

This repository supports [NCEPLIBS](https://github.com/NOAA-EMC/NCEPLIBS) CI
workflows.

To submit bug reports, feature requests, or other code-related issues including
usage questions, please create a [GitHub
issue](https://github.com/NOAA-EMC/ci-check-spack-recipe/issues). For general
NCEPLIBS inquiries, contact [Alex Richert](mailto:alexander.richert@noaa.gov)
(secondary point of contact [Hang Lei](mailto:hang.lei@noaa.gov)).

### Authors

[Alex Richert](mailto:alexander.richert@noaa.gov)

### Usage

To use this Action, include the following step in your GitHub Actions workflow:
```
      - name: "Check Spack recipe"
        uses: NOAA-EMC/ci-check-spack-recipe@develop
        with:
          cmakelists-txt: my-sorc/CMakeLists.txt
          recipe-file: spack/package.py
          ignore-list: ENABLE_DOCS
```
The `cmakelists-txt` and `recipe-file` inputs must be specified, while
`ignore-list` provides an optional means of ignoring specific CMake option
names, such as `ENABLE_DOCS`, which are not intended for inclusion in the Spack
recipe.

## Disclaimer

The United States Department of Commerce (DOC) GitHub project code is provided
on an "as is" basis and the user assumes responsibility for its use. DOC has
relinquished control of the information and no longer has responsibility to
protect the integrity, confidentiality, or availability of the information. Any
claims against the Department of Commerce stemming from the use of its GitHub
project will be governed by all applicable Federal law. Any reference to
specific commercial products, processes, or services by service mark, trademark,
manufacturer, or otherwise, does not constitute or imply their endorsement,
recommendation or favoring by the Department of Commerce. The Department of
Commerce seal and logo, or the seal and logo of a DOC bureau, shall not be used
in any manner to imply endorsement of any commercial product or activity by DOC
or the United States Government.
