'''
 si potrebbe definire una classe AbelianGroup per rappresentare un gruppo abeliano finito e implementare metodi per eseguire operazioni di gruppo come la somma e la moltiplicazione.
'''
class AbelianGroup:
  def __init__(self, elements, operation):
    self.elements = elements
    self.operation = operation

  def __add__(self, other):
    if not isinstance(other, AbelianGroup):
      raise TypeError("Can only add AbelianGroup objects")
    if self.elements != other.elements:
      raise ValueError("Groups must have the same elements")
    new_elements = [self.operation(a, b) for a in self.elements for b in other.elements]
    return AbelianGroup(new_elements, self.operation)
    
