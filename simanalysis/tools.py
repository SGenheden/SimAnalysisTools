"""
Tools to analysis molecular simulations
"""
from __future__ import division, print_function, absolute_import

def simanal() :
    """
    Entry point for performing actions on trajectories by wrapping around
    the MDAnalysis. The available tools are listed from actions.py and the
    trajectory processing is taken from traj.py
    """

    import inspect
    import sys
    import simanalysis.actions as actions
    from simanalysis.traj import TrajectoryProcessor

    def __pred(c) :
        return inspect.isclass(c) and c.__module__ == "simanalysis.actions" and \
                issubclass(c,actions.TrajectoryAction) and \
                c.__name__ != "TrajectoryAction"

    actionclasses = {name.lower():c
        for name,c in inspect.getmembers(sys.modules["simanalysis.actions"],__pred)}

    commands = {}
    helplines = []
    for actionclass in sorted(actionclasses) :
        actionstr = actionclasses[actionclass].command_name()
        commands[actionstr] = actionclass
        helplines.append("%-25s - %s"%(actionstr,
                            actionclasses[actionclass].descr()))

    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1].lower() == "-h") :
        help = """
-------------------------------------------------------
simanalysis - a tool to analyze simulation trajectories
-------------------------------------------------------

Available commands:
%s
"""
        print(help%"\n".join(helplines))

    elif len(sys.argv) > 1 and sys.argv[1] in commands :

            clsname = commands[sys.argv[1]]
            processor = TrajectoryProcessor()
            analysis = actionclasses[clsname](processor)
            processor.setup(printargs=True)
            processor.process()

    else :
        print ("Unrecognizable command: use -h for help.")
