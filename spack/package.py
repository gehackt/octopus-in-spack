# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os 
import llnl.util.tty as tty
from spack.package import *


class Octopus(AutotoolsPackage, CudaPackage):
    """A real-space finite-difference (time-dependent) density-functional
    theory code."""

    homepage = "https://octopus-code.org/"
    url = "https://gitlab.com/octopus-code/octopus/-/archive/11.3/octopus-11.3.tar.gz"
    git      = "https://gitlab.com/octopus-code/octopus"
    

    maintainers = ['fangohr', 'RemiLacroix-IDRIS']

    #Versions and their hashes
    version('11.4', sha256='73bb872bff8165ddd8efc5b891f767cb3fe575b5a4b518416c834450a4492da7')
    version('11.3', sha256='0c98417071b5e38ba6cbdd409adf917837c387a010e321c0a7f94d9bd9478930')
    version('11.1',  sha256='d943cc2419ca409dda7459b7622987029f2af89984d0d5f39a6b464c3fc266da')
    version('10.5',  sha256='deb92e3491b0c6ac5736960d075b44cab466f528b69715ed44968ecfe2953ec4')
    version('10.4',  sha256='4de9dc6f5815a45e43320e4abc7ef3e501e34bc327441376ea20ca1a992bdb72')
    version('10.3',  sha256='4633490e21593b51b60a8391b8aa0ed17fa52a3a0030630de123b67a41f88b33')
    version('10.2',  sha256='393e2ba7b18af1b736ad6deb339ba0cef18c6417671da7a6f1fcc3a5d8f7586b')
    version('10.1',  sha256='b6a660a99ed593c1d491e2d11cfff9ce87f0d80d527d9ff47fd983533d45adc6')
    version('10.0',  sha256='ccf62200e3f37911bfff6d127ebe74220996e9c09383a10b1420c81d931dcf23')
    version('7.3',   sha256='ad843d49d4beeed63e8b9a2ca6bfb2f4c5a421f13a4f66dc7b02f6d6a5c4d742')
    version('6.0',   sha256='4a802ee86c1e06846aa7fa317bd2216c6170871632c9e03d020d7970a08a8198')
    version('5.0.1', sha256='3423049729e03f25512b1b315d9d62691cd0a6bd2722c7373a61d51bfbee14e0')

    #variants
    variant('mpi', default=True, description='Build with MPI support')

    #dependencies
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("mpi",when="+mpi")

    def autoreconf(self, spec, prefix):

        autoreconf("--install", "--verbose", "--force")

    def configure_args(self):
        lapack = self.spec['lapack'].libs
        blas = self.spec['blas'].libs
        args = []
        args.extend([
            '--prefix=%s' % prefix,
            '--with-blas=%s' % blas.ld_flags,
            '--with-lapack=%s' % lapack.ld_flags,
            '--with-gsl-prefix=%s' % spec['gsl'].prefix,
            '--with-libxc-prefix=%s' % spec['libxc'].prefix,
            '--enable-openmp',
        ])
        if '+mpi' in self.spec: # we build with MPI
            args.extend([
                '--enable-mpi',
                'CC=%s' % self.spec['mpi'].mpicc,
                'FC=%s' % self.spec['mpi'].mpifc,
                ])
        else:
            args.extend([
                '--disable-mpi', #check if this is needed
                'CC=%s' % self.compiler.cc,
                'FC=%s' % self.compiler.fc,
                ])

        return args
