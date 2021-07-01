# DIVE Deep student site

This is the repo for the student version of the DIVE Deep workshop notebooks.

- To preview the notebooks, click 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ccha23/divedeep/HEAD?urlpath=lab/tree/divedeep.ipynb)
- To run locally on your computer: 
  - Install [docker](
https://docs.docker.com/get-started/#download-and-install-docker).
  - Build the docker image, e.g., by the command
  ```docker built -t divedeep:latest https://github.com/ccha23/divedeep.git```
  - Run the docker image by the command, e.g., by the command
  ```docker run -p 10000:8888 -e JUPYTER_ENABLE_LAB=yes divedeep:latest
  - Access the notebooks at http://localhost:10000/
