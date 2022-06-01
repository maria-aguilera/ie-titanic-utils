# Bash script (commands to type in command line)
# To run it, do:
#
# $ source setup_script.sh

echo "Installing miniforge3..."
pyenv install miniforge3

export PYENV_VERSION=miniforge3

conda create -n titanic310 python=3.10 --yes


echo "Now you can run 'conda activate titanic310' on the terminal"
