'For learning OWL and owlready2'
'From "https://qiita.com/sci-koke/items/a650c09bf77331f5537f"'
'From "https://owlready2.readthedocs.io/en/latest/class.html"'

'* Owlready2 * Warning: optimized Cython parser module "owlready2_optimized" is not available, defaulting to slower Python implementation'
'↑ This wartning mean is You can either install Cython (and a C compiler) and re-install Owlready to benefit from the optimized module, or continue using the non-optimized version'

'pip install Owlready2'

from owlready2 import *
onto = get_ontology("http://test1.org/onto.owl")

with onto:
    #エンティティクラス
    class Pizza(Thing):
        pass
    class MeatPizza(Pizza):
        pass

    class Topping(Thing):
        pass

    # プロパティクラス
    class has_Topping(Pizza >> Topping):
        pass


print(Pizza)

'The .subclasses() method returns the list of direct subclasses of a class.'
print(Pizza.subclasses())

'Owlready2 provides the .is_a attribute for getting the list of superclasses'
print(MeatPizza.is_a)

'The .descendants() and .ancestors() Class methods return a set of the descendant and ancestor Classes.'
print(MeatPizza.ancestors())

'The .iri attribute of the Class can be used to obtain the full IRI of the class.'
print(Pizza.iri)
