# NetPlanner

# Debugging instructions

In order to run a debug Flask web server and access the site for debugging, you will need to run 5 terminal commands commands
from the root directory of the project (that is to say, the outermost NetPlanner folder).

* `pip install flask`
If you do not have python and pip installed, you will need to install both first. (pip is typically included with python).
* `pip install -e .`
This will install the netplanner web app and allow it to be run on your local debug server
* `export FLASK_APP=netplanner` (use `set` instead of `export` on Windows systems)
* `export FLASK_DEBUG=1` (again, use `set` instead of `export` on Windows systems)
* `flask run` This will run the server on port 5000. The web app will now be accesable in any web browser at `http://localhost:5000`

*Note: Do NOT try to access the web server via `https`. It will not work as there is no valid certificate at this time.* 
