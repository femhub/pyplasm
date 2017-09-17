from .utils import flatten
from .fenvs import NCLabTurtleImage, NCLabTurtleTrace, NCLabTurtle, \
                   NCLabTurtleTrace3D, NCLabTurtleImage3D, NCLabTurtle3D, \
                   NCLAB_TURTLE_IMAGE_H, PRISM

class StepAccumulator:
    pending_actions = dict()
    model_triples = []
    geom_base = set()

    @staticmethod
    def add_object(ob):
        """Add internal PLaSM object to the current step"""
        StepAccumulator.pending_actions[id(ob)] = {'action': 'add', 'geom': ob}

    @staticmethod
    def add_shapes(obj):
        """
        Add objects to state of the current step. Argument can
        either be a single BASEOBJ or list of BASEOBJs.

        Added objects are in "pending" state which means you
        have to call .forward_one_step function with step id (number)
        to assign all pending objects to particular step identifier.
        """
        def safe_add(base):
            if hasattr(base, 'geom'):
                StepAccumulator.add_object(base.geom)

        if isinstance(obj, list):
            f = flatten(obj)
            for o in f:
                safe_add(o)
        else:
            safe_add(obj)


    @staticmethod
    def remove_object(ob):
        """
        Remove object from set of existing steps. This does not mean
        that object will not be included in the result. This means that
        object is scheduled to be removed in the next step. This can be used
        to remove previous turtle position or hide intermediate states of
        some operation ex. union or subtraction.
        """
        if not isinstance(ob, list):
            lob = [ob]
        else:
            lob = ob

        for el in lob:
            if hasattr(el, 'geom'):
                geom = el.geom
            else:
                geom = el

            if id(geom) in StepAccumulator.pending_actions:
                del StepAccumulator.pending_actions[id(geom)]
            else:
                StepAccumulator.pending_actions[id(geom)] = {'action': 'remove', 'geom': geom}

    @staticmethod
    def modeling_history():
        return StepAccumulator.model_triples

    @staticmethod
    def reset_history():
        StepAccumulator.geom_base.clear()
        StepAccumulator.pending_actions.clear()
        del StepAccumulator.model_triples[:]

    @staticmethod
    def forward_one_step(step_id):
        """
        Add all pending shapes to database of unique shapes
        and create a history of the current steps by creating list
        of tripels (stepId, action, geometryId). This will allow to
        reproduce all user actions in UI.
        """
        for geom_id, action in StepAccumulator.pending_actions.items():
            StepAccumulator.model_triples.append((step_id, action['action'], geom_id))
            StepAccumulator.geom_base.add(action['geom'])
        StepAccumulator.pending_actions.clear()

    @staticmethod
    def historical_objects():
        """
        Return all objects that appeared during stepping session.
        It allows us to restore the modeling history.
        """
        return StepAccumulator.geom_base

    @staticmethod
    def generate_trace(turtle, trace_gen, img_gen, turtle_thickness=None):
        """
        Generate trace that was accumulated by turtle since
        previous call of this function. It also creates a turtle
        image at its current location.
        """
        if len(turtle.lines) > 0:
            if not hasattr(turtle, 'nclab_path_length'):
                turtle.nclab_path_length = 0

            new_path_segments = turtle.lines[turtle.nclab_path_length:]

            orig_lines = turtle.lines
            turtle.lines = new_path_segments
            if isinstance(turtle, NCLabTurtle):
                layer = 0
                dots = True
                elev = 0
                trace = NCLabTurtleTrace(turtle.lines, layer, dots, elev)
            elif isinstance(turtle, NCLabTurtle3D):
                trace = NCLabTurtleTrace3D(turtle)

            StepAccumulator.add_shapes(trace)
            turtle.lines = orig_lines

            turtle.nclab_path_length = len(turtle.lines)-1

        StepAccumulator.remove_turtle_image(turtle)
        if isinstance(turtle, NCLabTurtle):
            image = NCLabTurtleImage(turtle)
            if turtle_thickness:
                turtle.nclab_step_image = PRISM(image, turtle_thickness)
            else:
                turtle.nclab_step_image = PRISM(image, NCLAB_TURTLE_IMAGE_H)
        elif isinstance(turtle, NCLabTurtle3D):
            turtle.nclab_step_image = NCLabTurtleImage3D(turtle)
        StepAccumulator.add_shapes(turtle.nclab_step_image)

    @staticmethod
    def remove_turtle_image(turtle):
        """
        Remove representation of a turtle if it was there.
        By "removing" we mean saving "remove" action of a turtle
        so UI will handle removal in the current step.
        """
        if hasattr(turtle, 'nclab_step_image'):
            for image_el in turtle.nclab_step_image:
                StepAccumulator.remove_object(image_el.geom)
            turtle.nclab_step_image = []
