#####################################################
# APS106 Winter 2021 - Lab 7 - Chemical Eqn Checker #
#####################################################

######################################################
# PART 1 - Complete the function below to deocompose
#          a compound formula written as a string
#          in a dictionary
######################################################

def mol_form(compound_formula):
    """(str) -> dictionary
    When passed a string of the compound formula, returns a dictionary 
    with the elements as keys and the number of atoms of that element as values.
    
    >>> mol_form("C2H6O1")
    {'C': 2, 'H': 6, 'O': 1}
    >>> mol_form("C1H4")
    {'C': 1, 'H': 4}
    """
    poison = {}
    i = 0
    j = 0
    for char in compound_formula:
        if char.isalpha():
            j += 1
        elif char.isdigit():
            element = compound_formula[i:j]
            poison[element] = char
            i = j + 1
            j = i
    return poison
    
print(mol_form("C2H6O1"))
print(mol_form("C1H4"))
print(mol_form("K1Fe4"))
    
    
######################################################
# PART 2 - Complete the function below that takes two 
#          tuples representing one side of a
#          chemical equation and returns a dictionary
#          with the elements as keys and the total
#          number of atoms in the entire expression
#          as values.
######################################################
    
def expr_form(expr_coeffs,expr_molecs):
    """
    (tuple (of ints), tuple (of dictionaries)) -> dictionary
    
    This function accepts two input tuples that represent a chemical expression,
    or one side of a chemical equation. The first tuple contains integers that
    represent the coefficients for molecules within the expression. The second
    tuple contains dictionaries that define these molecules. The molecule
    dictionaries have the form {'atomic symbol' : number of atoms}. The order
    of the coefficients correspond to the order of molecule dictionaries.
    The function creates and returns a dictionary containing all elements within
    the expression as keys and the corresponding number of atoms for each element
    within the expression as values.
    
    For example, consider the expression 2NaCl + H2 + 5NaF
    
    >>> expr_form((2,1,5), ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1}))
    {'Na': 7, 'Cl': 2, 'H': 2, 'F': 5}
    
    """
    from collections import Counter
    i = 0
    empty = []
    
    for item in expr_molecs:
        nay = [item *expr_coeffs[i] for item in expr_molecs[i].values()]
        product = sum([[a]*b for a,b in zip(list(expr_molecs[i].keys()),nay)],[])
        empty.extend(product)
        
        i += 1
    
    return dict(Counter(empty)) 

########################################################
# PART 3 - Check if two dictionaries representing
#          the type and number of atoms on two sides of
#          a chemical equation contain different
#          key-value pairs
########################################################

def find_unbalanced_atoms(reactant_atoms, product_atoms):
    """
    (Dict,Dict) -> Set
    
    Determine if reactant_atoms and product_atoms contain equal key-value
    pairs. The keys of both dictionaries are strings representing the 
    chemical abbreviation, the value is an integer representing the number
    of atoms of that element on one side of a chemical equation.
    
    Return a set containing all the elements that are not balanced between
    the two dictionaries.
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 1, "Cl" : 2})
    {'Na'}
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 2, "Cl" : 2})
    set()
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "F" : 2, "Cl" : 2})
    {'F', 'Na'}
    """
    if reactant_atoms == product_atoms:
        return set()
    else:
        empty = set()
        diff1 = set(reactant_atoms) - set(product_atoms)
        diff2 = set(product_atoms) - set(reactant_atoms)
        empty.update(diff1)
        empty.update(diff2)        
        for key in reactant_atoms:
            if (key in product_atoms and reactant_atoms[key] != product_atoms[key]):
                empty.add(key)
                if ((key in reactant_atoms) and (key not in product_atoms)):
                    empty.add(key)
        return (empty)


########################################################
# PART 4 - Check if a chemical equation represented by
#          two nested tuples is balanced
########################################################

def check_eqn_balance(reactants,products):
    """
    (tuple,tuple) -> Set
    
    Check if a chemical equation is balanced. Return any unbalanced
    elements in a set.
    
    Both inputs are nested tuples. The first element of each tuple is a tuple
    containing the coefficients for molecules in the reactant or product expression.
    The second element is a tuple containing strings of the molecules within
    the reactant or product expression. The order of the coefficients corresponds
    to the order of the molecules. The function returns a set containing any
    elements that are unbalanced in the equation.
    
    For example, the following balanced equation
    C3H8 + 5O2 <-> 4H2O + 3CO2
    
    would be input as the following two tuples:
    reactants: ((1,5), ("C3H8","O2"))
    products: ((4,3), ("H2O1","C1O2"))
    
    >>> check_eqn_balance(((1,5), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))
    set()
    
    Similarly for the unbalanced equation
    
    C3H8 + 2O2 <-> 4H2O + 3CO2
    
    would be input as the following two tuples:
    reactants: ((1,2), ("C3H8","O2"))
    products: ((4,3), ("H2O1","C1O2"))
    
    >>> check_eqn_balance(((1,2), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))
    {'O'}
    
    """
    
    pass #TODO your code here