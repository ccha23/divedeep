# DIVE Deep student site

This is the repo for the student version of notebooks in  
<https://www.cs.cityu.edu.hk/~ccha23/deepbook>


- To preview the notebooks with temporary storage, click 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ccha23/divedeep/HEAD?urlpath=lab/tree/divedeep.ipynb)

- To run locally on your computer with permanent storage:
  - Install [docker](
https://docs.docker.com/get-started/#download-and-install-docker).
  - Run the docker in a terminal from a working directory of your choice:
  ```docker run --rm -p 10000:8888 -v "${PWD}":/home/jovyan chungc/nobf:divedeep start-notebook.sh --NotebookApp.token=''```
  - Open the notebooks in a web browser:  
  <http://localhost:10000/git-pull?repo=https%3A%2F%2Fgithub.com%2Fccha23%2Fdivedeep&urlpath=lab%2Ftree%2Fdivedeep%2Fdivedeep.ipynb&branch=master>
  - You can work on the notebooks under the `deepdive` subfolder. After you are done, stop the notebook server by `Ctrl+c` in the terminal running docker.
