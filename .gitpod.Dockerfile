FROM gitpod/workspace-full
                    
USER gitpod

RUN sudo apt-get install -y scons libpython2-dev python-dev zlib1g-dev libc6-dev 
