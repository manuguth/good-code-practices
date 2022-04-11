# Rodem Good Practices

## Installation

### Docker

The easiest way to run the code for the workshop is using a docker image via

```bash
docker run -it -p 8881:8881  gitlab-registry.cern.ch/rodem-workshops/rodem-good-practices/base-python:latest bash
```

if you want to make the current folder accessible within the image you need to mount it via `-v $(pwd):<path-to-folder>` and to change the working directory to your current directory you can specify it via `-w $(pwd)`.

To run a Jupyter Notebook within the Docker image, use the following command:

```bash
jupyter notebook --ip 0.0.0.0 --no-browser --port 8881
```

### Singularity

Using singularity you can simply run

```bash
singularity exec --pwd ${PWD} docker://gitlab-registry.cern.ch/rodem-workshops/rodem-good-practices/base-python:latest jupyter notebook --no-browser --port 8871
```

with the `-B` flag you can mount additional directories.

## Additional Material

<https://umami.docs.cern.ch/setup/development/good_practices_code/>
