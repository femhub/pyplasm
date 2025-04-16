from .common import flatten

from ..turtle.turtle_2d_utils import (
    NCLabTurtleImage,
    NCLabTurtleTrace,
    NCLAB_TURTLE_IMAGE_H,
    NCLAB_TURTLE_TRACE_H,
)
from ..turtle.turtle_2d import NCLabTurtle
from ..turtle.turtle_3d_utils import NCLabTurtleTrace3D, NCLabTurtleImage3D
from ..turtle.turtle_3d import NCLabTurtle3D
from ..geometry.prism import PRISM


class StepAccumulator:
    pending_actions = dict()
    model_triples = []
    geom_base = set()
    accumulated_trace = []

    @staticmethod
    def add_object(ob, action="add"):
        """Add internal PLaSM object to the current step"""
        StepAccumulator.pending_actions[id(ob)] = {"action": action, "geom": ob}

    @staticmethod
    def remove_unused_objects(objects):
        """
        Generate 'remove' action for every object that is not listed
        in argument. Used to implement SHOW command functionality in step mode.
        """
        if isinstance(objects, (list, tuple)):
            fgeoms = [o.geom for o in flatten(objects) if hasattr(o, "geom")]
            to_remove = StepAccumulator.geom_base.difference(fgeoms)
            StepAccumulator.remove_object(to_remove)

    @staticmethod
    def add_shapes(obj, copy=False):
        """
        Add objects to state of the current step. Argument can
        either be a single BASEOBJ or list of BASEOBJs.

        Added objects are in "pending" state which means you
        have to call .forward_one_step function with step id (number)
        to assign all pending objects to specific step identifier.
        """

        def safe_add(base):
            if hasattr(base, "geom"):
                if copy:
                    StepAccumulator.add_object(base.geom, action="copy")
                else:
                    StepAccumulator.add_object(base.geom)

        if isinstance(obj, (list, tuple)):
            f = flatten(obj)
            for o in f:
                safe_add(o)
        else:
            safe_add(obj)

    @staticmethod
    def remove_object(ob):
        """
        Remove object from the set of existing steps. This does not mean
        that object will not be included in the result. This means that
        object is scheduled to be removed in the next step. This can be used
        to remove previous turtle position or hide intermediate states of
        some operation ex. union or subtraction.
        """
        if not isinstance(ob, (list, tuple)):
            lob = [ob]
        else:
            lob = ob
        lob = flatten(lob)

        for el in lob:
            if hasattr(el, "geom"):
                geom = el.geom
            else:
                geom = el

            # If an object has already been added
            # in the current step (line), remove it from the list
            # of actions to store. Previously added object was probably
            # internal and intermediate stage and we won't waste
            # space and network bandwidth to send it to user because
            # he would not see it anyway.
            #
            # However, we need to store the 'remove' action regardless
            # of wheter it represents temporary object or something else
            # because we cannot tell the difference between those two situations.
            if id(geom) in StepAccumulator.pending_actions:
                del StepAccumulator.pending_actions[id(geom)]
            StepAccumulator.pending_actions[id(geom)] = {
                "action": "remove",
                "geom": geom,
            }

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
        of tripels (stepId, action, geometryId). This will allow us to
        reproduce all user actions in UI.

        Every object which was an object of 'remove' action should have
        also corresponding 'add' action in model history. If there is no 'add' action for a
        specific 'remove', the object was only an intermediate stage
        and we should not store any action involving it.
        """
        for geom_id, action in StepAccumulator.pending_actions.items():
            if (
                action["action"] == "remove"
                and action["geom"] not in StepAccumulator.geom_base
            ):
                continue
            StepAccumulator.model_triples.append((step_id, action["action"], geom_id))
            StepAccumulator.geom_base.add(action["geom"])
        StepAccumulator.pending_actions.clear()

    @staticmethod
    def historical_objects():
        """
        Return all objects that appeared during stepping session.
        It allows us to restore the modeling history.
        """
        return StepAccumulator.geom_base

    @staticmethod
    def remove_trace(turtle, trace_gen):
        StepAccumulator.remove_object(StepAccumulator.accumulated_trace)

    @staticmethod
    def generate_trace(turtle, trace_gen, img_gen, turtle_thickness=None):
        """
        Generate trace that was accumulated by turtle since
        previous call of this function. It also creates a turtle
        image at its current location.
        """
        if len(turtle.lines) > 0:
            if not hasattr(turtle, "nclab_path_length"):
                turtle.nclab_path_length = 0

            new_path_segments = turtle.lines[turtle.nclab_path_length :]

            orig_lines = turtle.lines
            turtle.lines = new_path_segments
            if isinstance(turtle, NCLabTurtle):
                layer = 0
                dots = True
                elev = NCLAB_TURTLE_TRACE_H
                trace = NCLabTurtleTrace(turtle.lines, layer, dots, elev)
            elif isinstance(turtle, NCLabTurtle3D):
                trace = NCLabTurtleTrace3D(turtle)

            StepAccumulator.add_shapes(trace)
            StepAccumulator.accumulated_trace.extend(trace)
            turtle.lines = orig_lines

            turtle.nclab_path_length = len(turtle.lines) - 1

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
        if hasattr(turtle, "nclab_step_image"):
            for image_el in turtle.nclab_step_image:
                StepAccumulator.remove_object(image_el.geom)
            turtle.nclab_step_image = []
