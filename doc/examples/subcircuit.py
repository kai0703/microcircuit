"""
# extract subcircuit
subcirc = mc.transforms.modularization.subcircuit(circuit, 'id',
                                                  500, 'connectivity')
print subcirc.edges()
print circuit.relabel_verticesid

"""