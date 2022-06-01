# ie-titanic-utils
Sample project for Python Workshop (IE MBD)

(Full description to be completed)

(With extra information)

## Solutions
1. VERY BAD:" *Just" go to `/workspace/ie-titanic-utils`"
    - Con: Users will start polluting everything.
2. QUITE BAD: I send the file (`str_utils.py`) and the user puts it in their working directory
    - If they're working on several directories, they will end up with several copies
    - You don't control the code anymore
3. BAD: Change `sys.path`which contains the list of predefined locations of python predefined modules.
    - Users use the development version i.e. whenever you make any change; you make a mistake, users will start using that and will need to separate into production environment and development environment.
4. EXCELLENT: Attending the rest of the course


# Installing Python

pyenv
|
|-miniforge3 (once per machine)
    |
    |-conda
        |
        | - create environment (once per project)
            |
            | Isolated environment with both conda and pip  (everyday)


Anaconda Inc. != Anaconda Distribution != conda
|
|- Anaconda Distribution (product)
    |
    | - conda (software)
    | -pandas
    | -scikit-learn
     - ...


