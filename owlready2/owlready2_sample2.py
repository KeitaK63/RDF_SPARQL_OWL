'For learning OWL and owlready2'
'From "https://qiita.com/sci-koke/items/a650c09bf77331f5537f"'
'From "https://owlready2.readthedocs.io/en/latest/class.html"'

'* Owlready2 * Warning: optimized Cython parser module "owlready2_optimized" is not available, defaulting to slower Python implementation'
'↑ This wartning mean is You can either install Cython (and a C compiler) and re-install Owlready to benefit from the optimized module, or continue using the non-optimized version'

'pip install Owlready2'


from owlready2 import *
onto_path.append("./RDF_SPARQL_OWL/owlready2/")
onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
onto.load()

class NonVegetarianPizza(onto.Pizza):
    equivalent_to = [onto.Pizza & ( onto.has_topping.some(onto.MeatTopping) | onto.has_topping.some(onto.FishTopping)) ]

    def eat(self):
        print("Beurk! I'm vegetarian!")

print(onto.Pizza)

test_pizza = onto.Pizza("test_pizza_owl_identifier")
test_pizza.has_topping = [ onto.CheeseTopping(),onto.TomatoTopping() ]
test_pizza.has_topping.append(onto.MeatTopping())

print(test_pizza.__class__)
onto.save()
