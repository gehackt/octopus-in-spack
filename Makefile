
# Install octopus via spack. Using most recent spack version
spack-develop:
	docker build -f Dockerfile -t octopus-spack --build-arg SPACK_VERSION=develop  .

run-spack:
	docker run --rm -ti -v $PWD:/io octopus-spack 

# use particular versions of spack
spack-v0.17.0:
	docker build -f Dockerfile --build-arg SPACK_VERSION=v0.17.0 \
   -t octopus-spack-v0.17.0 .

spack-v0.17.2:
	docker build -f Dockerfile --build-arg SPACK_VERSION=v0.17.2 \
   -t octopus-spack-v0.17.2 .

debian-octopusstable:
	docker build -f Dockerfile-debian -t octopus .

debian-octopusdevelop:
	docker build -f Dockerfile-debian-develop -t octopus-develop .

.PHONY: octopus-spack-v0.17.0 octopus-spack run-spack debian-octopusstable debian-octopusdevelop debian-develop spack-v0.17.2



dockerhub-update-11.3:
	@echo "Run 'docker login'"
	docker build -f Dockerfile-debian -t fangohr/octopus:11.3 .
  @echo "Run 'docker push fangohr/octopus:11.3' "
