
# Octopus-in-spack

Support repository for getting the [OCTOPUS code](http://octopus-code.org) package into [Spack](http://spack.readthedocs.io).

## Status

Compile Octopus with Spack [on (Debian) Linux]:

[![debian-spack-develop](https://github.com/fangohr/octopus-in-spack/actions/workflows/debian-spack-develop.yml/badge.svg)](https://github.com/fangohr/octopus-in-spack/actions/workflows/debian-spack-develop.yml)
[![debian-spack-v0.16.2](https://github.com/fangohr/octopus-in-spack/actions/workflows/debian-spack-v0.16.2.yml/badge.svg)](https://github.com/fangohr/octopus-in-spack/actions/workflows/debian-spack-v0.16.2.yml)

Compile Octopus on Debian Linux:

[![debian-native](https://github.com/fangohr/octopus-in-spack/actions/workflows/debian-native.yml/badge.svg)](https://github.com/fangohr/octopus-in-spack/actions/workflows/debian-native.yml)


# Required commands

## Compilation of Octopus using Spack

At the moment, this is under development, and we need two lines:

- get spack: `git clone https://github.com/fangohr/spack`
- check out the right branch: `git checkout octopus-review-2021-08`

Then activate spack:

- `source spack/share/spack/setup-env.sh`

Then compile octopus (this could take some time). For this example, we want to include netcdf support:

- `spack install octopus +netcdf`

Ideally, there are no errors.

This should install Octopus 11.1 

## To use Octopus after installation

1. Activate spack:

- `source spack/share/spack/setup-env.sh`

2. Load octopus

- `spack load octopus`

3. Use octopus (it should be in the `$PATH`)
