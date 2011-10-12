""" This toy circuit included a sensory neuron (S1), interneurons (I1, I2, I3,
and I4) and a motor neuron (M1) that are coupled with chemical synapses
(between I1 and I2) and gap junctions (between I1-I3, I3-I2, I1-I4, I4-I3).

It is modeled after the C.elegans network and serves as a test circuit
for analysis method implementation. It also shows the distinction made
between a circuit which includes detailed skeletonized neuronal morphologies
and the extracted wiring diagram with nodes representing neurons and
edges representing chemical synapses and/or gap junctions.

Varshney LR, Chen BL, Paniagua E, Hall DH, Chklovskii DB (2011) Structural
Properties of the Caenorhabditis elegans Neuronal Network. PLoS Comput Biol
7(2): e1001066. doi:10.1371/journal.pcbi.1001066

"""
import numpy as np

from .. import Circuit

metadata = {'name' : 'testcircuit002',
            'neuronmap': {
                111: {'name':'S1'},
                222: {'name':'I1'},
                333: {'name':'I2'},
                444: {'name':'M1'},
                555: {'name':'I3'},
                666: {'name':'I4'}
            }}

vert = np.array([[0, 0, 0],    # S1: skeleton node (root)
                 [0, -5, 0],   # S1: skeleton node
                 [0, -10, 0],  # S1-I1: connector
                 [0, -15, 0],  # I1: skeleton node
                 [0, -20, 0],  # I1: skeleton node (root)
                 [0, -25, 0],  # I1-I2: connector
                 [0, -30, 0],  # I2: skeleton node
                 [0, -35, 0],  # I2: skeleton node (root)
                 [0, -40, 0],  # I2-M1: connector
                 [0, -45, 0],  # M1: skeleton node
                 [0, -50, 0],  # M1: skeleton node (root)
                 [10, -25, 0],  # I3: skeleton node
                 [15, -25, 0],  # I3: skeleton node (root)
                 [-10, -25, 0],  # I4: skeleton node
                 [-15, -25, 0],  # I4: skeleton node (root)
                 [5, -22.5, 0],  # I1-I3: connector
                 [5, -27.5, 0],  # I3-I2: connector
                 [-5, -22.5, 0],  # I1-I4: connector
                 [-5, -27.5, 0],  # I4-I2: connector
                 ],
                 dtype=np.float32)


conn = np.array([[0, 1], # neurite 111
                [1,2], # presynaptic
                [2,3], # postsynaptic
                [3,4], # neurite 222
                [4,5], # presynaptic
                [5,6], # postsynaptic
                [6,7], # neurite 333
                [7,8], # presynaptic
                [8,9], # postsynaptic
                [9,10], # neurite 444
                [11,12], # neurite 555
                [13,14], # neurite 666

                [4,15], # gap junction
                [12,15], # gap junction
                [12,16], # gap junction
                [6,16], # gap junction
                [4,17], # gap junction
                [13,17], # gap junction
                [13,18], # gap junction
                [6,18], # gap junction
                ],
                dtype=np.uint32)

vertices_properties = {
    "id": {"data": np.array(range(19), dtype=np.uint32)+100,
           "metadata": {}
    },
    "label": {"data": np.array([2,1,3,1,2,3,1,2,3,1,2,1,2,1,2,4,4,4,4], dtype=np.uint32),
              "metadata": {
                    "type": "categorial",
                    "semantics": {
                        1: {"name": "skeleton node", "ref": "XXX"},
                        2: {"name": "skeleton root node", "ref": "XXX"},
                        3: {"name": "chemical synapse", "ref": "XXX"},
                        4: {"name": "gap junction", "ref": "XXX"},
                    }
              }
    }
}

connectivity_properties = {
    "id": {"data": np.array([111, 111, 222, 222, 222, 333, 333, 333, 444, 444, 555, 666,
                             222, 555, 555, 333, 222, 666, 666, 333], dtype=np.uint32),
            "metadata": {}
    },
    "type": {"data": np.array([1,2,3,1,2,3,1,2,3,1,1,1,4,4,4,4,4,4,4,4], dtype=np.uint32),
             "metadata": {
                    "type": "categorial",
                    "value": {
                        0: {"name": "unknown"},
                        1: {"name": "neurite", "ref": "XXX"},
                        2: {"name": "presynaptic", "ref": "XXX"},
                        3: {"name": "postsynaptic", "ref": "XXX"},
                        4: {"name": "gap junction", "ref": "XXX"}
                    }
                }
    }
}

testcircuit = Circuit(
        vertices=vert, connectivity=conn,
        vertices_properties=vertices_properties,
        connectivity_properties=connectivity_properties,
        metadata=metadata
    )