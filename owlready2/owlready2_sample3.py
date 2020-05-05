'For learning OWL and owlready2'
'From "https://qiita.com/sci-koke/items/a650c09bf77331f5537f"'
'From "https://owlready2.readthedocs.io/en/latest/class.html"'

'* Owlready2 * Warning: optimized Cython parser module "owlready2_optimized" is not available, defaulting to slower Python implementation'
'↑ This wartning mean is You can either install Cython (and a C compiler) and re-install Owlready to benefit from the optimized module, or continue using the non-optimized version'

'pip install Owlready2'

'Making a new Ontology about motor cycle'
from owlready2 import *
onto_path.append("./RDF_SPARQL_OWL/owlready2/")
onto = get_ontology("file://./RDF_SPARQL_OWL/owlready2/onto_MotorCycle.owl")

with onto:
    class Vehicle(Thing):
        pass

    class TowWheeledVehicle(Vehicle):
        pass

    class MotorCycle(TowWheeledVehicle):
        pass


onto.save()
