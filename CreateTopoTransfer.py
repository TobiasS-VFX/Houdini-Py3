# import houdini python enviro

import hou

# get mesh file path from user *** this will only work when run inside Houdini

filePath = hou.ui.selectFile(title = 'Select Import Mesh...')

# get the obj context and create geo

obj= hou.node('/obj')
geo_node = obj.createNode('geo', 'Topo_Transfer_Setup')

# create nodes

file_node = geo_node.createNode('file', 'Import_Mesh')
test_geo = geo_node.createNode('testgeometry_templatehead')
match_size = geo_node.createNode('matchsize', 'Match_Import_To_Template_Size')
topo_xfr = geo_node.createNode('topotransfer')

# set filepath field for import mesh

file_node.parm("file").set(filePath)

# set inputs

match_size.setInput(0, file_node, 0)
match_size.setInput(1, test_geo, 0)
topo_xfr.setInput(1, match_size, 0)
topo_xfr.setInput(0, test_geo, 0)

# set parms

match_size.parm('doscale').set(1)
match_size.parm('scale_axis').set(5)

# set flags

topo_xfr.setDisplayFlag(True)
file_node.setRenderFlag(False)

# organize layout

geo_node.layoutChildren()