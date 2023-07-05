# DIVE Deep student site

Welcome to the DIVE Deep student site repository! Here, you can access the notebooks for the course at 

> <https://www.cs.cityu.edu.hk/~ccha23/deepbook>. 

To preview the notebooks with temporary storage, simply click the Binder badge below:

> [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ccha23/divedeep/HEAD?urlpath=lab/tree/divedeep.ipynb)

If you prefer to run the notebooks locally on your computer with persistent storage, follow these steps:

1. Install [docker](
https://docs.docker.com/get-started/#download-and-install-docker).

2. Run the docker in a terminal from any working directory of your choice:  
    ```markdown
    docker run --rm -p 10000:8888 \
              -v myhome:/home/jovyan \
              chungc/deepnb \
              start-notebook.sh --NotebookApp.token=''
    ```
    Please note that the first run may take a few minutes to download [the docker image](https://hub.docker.com/r/chungc/deepnb/tags), but subsequent runs should be faster. Also, ensure that port 10000 is free for use. If not, feel free to change it to a free port on your computer. You can also change the name "myhome" of the docker volume.

3. Pull the notebooks from this repo in a web browser:  
    > <http://localhost:10000/git-pull?repo=https%3A%2F%2Fgithub.com%2Fccha23%2Fdivedeep&urlpath=lab%2Ftree%2Fdivedeep%2Fdivedeep.ipynb&branch=master>

    You can work on the notebooks under the `divedeep` subfolder. If you visit the link again, it will automatically pull and merge changes from the repo without overwriting your changes.

4. To finish, stop the notebook server by pressing `Control-C` in the terminal that runs the docker. If you want to restart, simply run the docker command again. Your files should still be under the `divedeep` subfolder.