flask docker pwd
================

This is a small example to show how a flask app in a docker container can interact with the host filesystem in a *very* unsafe way.

build
-----
To build the docker image, clone this repository then in the same dir as the Dockerfile run the following:

`docker build -t odf/flask-docker-pwd .`

The "odf/flask-docker-pwd" part is just a name and can be anyting you want.
Also note the "." at the end of the command.

running
-------
Once the image is built run it with the following:

`docker run -it --rm -v $(pwd):/context -p 5000:5000 odf/flask-docker-pwd`

The `-it` part is "interactive tty", this is so you can <kbd>control c</kbd> to kill the server.
The `--rm` flag is so docker cleans up the stateless container after you end the process.
The `-v $(pwd):/context` maps the current working directory to the `/context` mount point *inside* the container. The `$(pwd)` could also be some other path on the host system as long as docker has access to it.
The `-p 5000:5000` part maps port 5000 on the host to 5000 in the container.
This is so you can access the flask server in the container by going to http://localhost:5000.
The syntax is `-p host_port:container_port`.
Finally, the `odf/flask-docker-pwd` is whatever you named the image in the build step above.

using
-----
Once the container is running, you should be able to go to http://localhost:5000 and see a list of files in the directory that was mapped into the container.
Clicking on any of the file names will bring you to a new page which runs an `os.stat` on the file and tells you how large it is in bytes (just to prove it is doing something).


.devcontainer
-------------
This repo also has a [VS Code devcontainer definition](https://code.visualstudio.com/docs/remote/containers) if you open this repository in VS Code and you have the remote containers extension installed, it might ask if you want to reopen this repository in a container. 
This is fine if you want to see how that works, but the dev container does not have any [docker in docker](https://github.com/microsoft/vscode-dev-containers/tree/master/containers/docker-in-docker) configured, so avoid opening in a container if you just want to build and run.