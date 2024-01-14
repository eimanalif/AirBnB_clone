AirBnB CLONE_ The console


This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine



Using the Console
The HBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.


commands

create
Usage: create <class>

show
Usage: show <class> <id> or <class>.show(<id>)

destroy
Usage: destroy <class> <id> or <class>.destroy(<id>)

all
Usage: all or all <class> or <class>.all()


count
Usage: count <class> or <class>.count()

update
Usage: update <class> <id> <attribute name> "<attribute value>" or <class>.update(<id>, <attribute name>, <attribute value>) or <class>.update( <id>, <attribute dictionary>).


