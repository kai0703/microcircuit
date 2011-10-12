"""
The ``modularization`` module provides functionality to compartmentalize
circuitry based on various criteria

"""

import numpy as np


def subcircuit_fromindex(circuit, indices):
    """ Extract subcircuit from vertices indices
    """
    G = circuit.asgraph(add_attributes=True)
    return G.subgraph(indices)


def unique_values(circuit, property, type='vertices'):
    """Return array with unique values for a given property
    """
    if type == 'vertices':
        prop = circuit.vertices_properties
    elif type == 'connectivity':
        prop = circuit.connectivity_properties
    else:
        raise Exception("Invalid `type` parameter")
    if property in prop:
        return np.unique(prop[property]["data"])
    else:
        return None

def subcircuit(circuit, property, value, type='vertices'):
    """ Return subcircuit to extract a particular skeleton or subcircuit

    Parameters
    ----------
    property : str
        Property value used for extraction
    value : number
        The value that select the subcircuit, such as an identifier
    type : {'vertices', 'connectivity'}
        Selection based on vertices or connectivity properties
    """

    if type == 'vertices':
        prop = circuit.vertices_properties
    elif type == 'connectivity':
        prop = circuit.connectivity_properties
    else:
        raise Exception("Invalid `type` parameter")
    if property in prop:
        if type == 'vertices':
            idx = np.where(prop[property]["data"] == value)[0]
        else:
            # extract the connections and retrieve the node indices
            idx = np.where(prop[property]["data"] == value)[0]
            idx = circuit.connectivity[idx].ravel()
        return subcircuit_fromindex(circuit, idx)
    else:
        raise Exception("Property {0} does not exist".format(property))


def wiring_diagram(circuit, neuronmap='neuronmap'):
    """ Extract the wiring diagram from a circuit
    """
    if circuit.metadata.has_key(neuronmap):
        neuronmap = circuit.metadata[neuronmap]
    
    for id, value in neuronmap.items():
        print id, value

    