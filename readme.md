## Jacques' Guide for Installation:

1. Install required packages:

    ```
    sudo apt install libopenmpi-dev libosmesa6-dev libgl1-mesa-glx libglfw3 libglew-dev patchelf
    ```
2. Clone this repository, create a conda environment and install the Spinning Up package:
    ```
    git clone https://github.com/JacquesCloete/spinningup.git
    cd spinningup
    conda env create -f conda-spinningup.yml
    conda activate spinningup
    pip install -e .
    ```
3. Install the [MuJoCo v2.1 binaries for Linux](https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz), extract the tar file, and move the extracted `mujoco210` directory into `~/.mujoco/` (note you have to create this hidden folder yourself).
4. Run `sudo nano ~/.bashrc` and append the following lines to the bashrc file:
    ```
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.mujoco/mujoco210/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia
    export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so
    ```
    (note: remember to source the bashrc file after editing; you'll also need to re-activate the conda environment)

If you want to remove the conda environment, run `conda remove -n spinningup --all`

If you can't get the MuJoCo stuff working, here is an [alternative guide](https://gist.github.com/saratrajput/60b1310fe9d9df664f9983b38b50d5da) that might help.

I've been seeing `Invalid MIT-MAGIC-COOKIE-1 key` appear in the terminal output when running any of the Spinning Up python scripts on my Ubuntu 20.04 local machine. Doing things like running `xhost +local:` do not help. Apparently this bug can happen when setting your NVIDIA driver to use OpenCL and CUDA before installing MPI on your local computer; simply switching to the X.Org driver before switching back again to the NVIDIA driver fixes it (see [here](https://askubuntu.com/questions/1265055/invalid-mit-magic-cookie-1-key-message-mpi-on-ubuntu-20-04)). Since the bug seems harmless I don't bother.

## Original Text:

**Status:** Maintenance (expect bug fixes and minor updates)

Welcome to Spinning Up in Deep RL! 
==================================

This is an educational resource produced by OpenAI that makes it easier to learn about deep reinforcement learning (deep RL).

For the unfamiliar: [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) (RL) is a machine learning approach for teaching agents how to solve tasks by trial and error. Deep RL refers to the combination of RL with [deep learning](http://ufldl.stanford.edu/tutorial/).

This module contains a variety of helpful resources, including:

- a short [introduction](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) to RL terminology, kinds of algorithms, and basic theory,
- an [essay](https://spinningup.openai.com/en/latest/spinningup/spinningup.html) about how to grow into an RL research role,
- a [curated list](https://spinningup.openai.com/en/latest/spinningup/keypapers.html) of important papers organized by topic,
- a well-documented [code repo](https://github.com/openai/spinningup) of short, standalone implementations of key algorithms,
- and a few [exercises](https://spinningup.openai.com/en/latest/spinningup/exercises.html) to serve as warm-ups.

Get started at [spinningup.openai.com](https://spinningup.openai.com)!


Citing Spinning Up
------------------

If you reference or use Spinning Up in your research, please cite:

```
@article{SpinningUp2018,
    author = {Achiam, Joshua},
    title = {{Spinning Up in Deep Reinforcement Learning}},
    year = {2018}
}
```