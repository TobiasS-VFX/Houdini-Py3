# import houdini python enviro

import hou

# get the stage context and create material library

stage= hou.node('/stage')

mLib_node = hou.node('/stage/Material_X_Library')

if not mLib_node:
    mLib_node = stage.createNode('materiallibrary', 'Material_X_Library')

# create material X nodes

mtlxSurf = mLib_node.createNode('mtlxsurfacematerial')
mtlxStdSurf = mLib_node.createNode('mtlxstandard_surface')
mtlxDisp = mLib_node.createNode('mtlxdisplacement')
albedo_img = mLib_node.createNode('mtlximage', 'Albedo')
rough_img = mLib_node.createNode('mtlximage', 'Roughness')
opacity_img = mLib_node.createNode('mtlximage', 'Opacity')
normal_img = mLib_node.createNode('mtlximage', 'Normal')
displace_img = mLib_node.createNode('mtlximage', 'Displacement')

# connect nodes

mtlxSurf.setInput(0, mtlxStdSurf, 0)
mtlxSurf.setInput(1, mtlxDisp, 0)
mtlxStdSurf.setInput(1, albedo_img,0)
mtlxStdSurf.setInput(6, rough_img,0)
mtlxStdSurf.setInput(38, opacity_img,0)
mtlxStdSurf.setInput(40, normal_img,0)
mtlxDisp.setInput(0, displace_img,0)

# organize layout

mLib_node.layoutChildren()