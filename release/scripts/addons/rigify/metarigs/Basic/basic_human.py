import bpy


from mathutils import Color


def create(obj):
    # generated by rigify.utils.write_metarig
    bpy.ops.object.mode_set(mode='EDIT')
    arm = obj.data

    for i in range(6):
        arm.rigify_colors.add()

    arm.rigify_colors[0].name = "Root"
    arm.rigify_colors[0].active = Color((0.5490000247955322, 1.0, 1.0))
    arm.rigify_colors[0].normal = Color((0.43529415130615234, 0.18431372940540314, 0.41568630933761597))
    arm.rigify_colors[0].select = Color((0.3140000104904175, 0.7839999794960022, 1.0))
    arm.rigify_colors[0].standard_colors_lock = True
    arm.rigify_colors[1].name = "IK"
    arm.rigify_colors[1].active = Color((0.5490000247955322, 1.0, 1.0))
    arm.rigify_colors[1].normal = Color((0.6039215922355652, 0.0, 0.0))
    arm.rigify_colors[1].select = Color((0.3140000104904175, 0.7839999794960022, 1.0))
    arm.rigify_colors[1].standard_colors_lock = True
    arm.rigify_colors[2].name = "Special"
    arm.rigify_colors[2].active = Color((0.5490000247955322, 1.0, 1.0))
    arm.rigify_colors[2].normal = Color((0.9568628072738647, 0.7882353663444519, 0.0470588281750679))
    arm.rigify_colors[2].select = Color((0.3140000104904175, 0.7839999794960022, 1.0))
    arm.rigify_colors[2].standard_colors_lock = True
    arm.rigify_colors[3].name = "Tweak"
    arm.rigify_colors[3].active = Color((0.5490000247955322, 1.0, 1.0))
    arm.rigify_colors[3].normal = Color((0.03921568766236305, 0.21176472306251526, 0.5803921818733215))
    arm.rigify_colors[3].select = Color((0.3140000104904175, 0.7839999794960022, 1.0))
    arm.rigify_colors[3].standard_colors_lock = True
    arm.rigify_colors[4].name = "FK"
    arm.rigify_colors[4].active = Color((0.5490000247955322, 1.0, 1.0))
    arm.rigify_colors[4].normal = Color((0.11764706671237946, 0.5686274766921997, 0.03529411926865578))
    arm.rigify_colors[4].select = Color((0.3140000104904175, 0.7839999794960022, 1.0))
    arm.rigify_colors[4].standard_colors_lock = True
    arm.rigify_colors[5].name = "Extra"
    arm.rigify_colors[5].active = Color((0.5490000247955322, 1.0, 1.0))
    arm.rigify_colors[5].normal = Color((0.9686275124549866, 0.250980406999588, 0.0941176563501358))
    arm.rigify_colors[5].select = Color((0.3140000104904175, 0.7839999794960022, 1.0))
    arm.rigify_colors[5].standard_colors_lock = True

    for i in range(29):
        arm.rigify_layers.add()

    arm.rigify_layers[0].name = " "
    arm.rigify_layers[0].row = 1
    arm.rigify_layers[0].set = False
    arm.rigify_layers[0].group = 0
    arm.rigify_layers[1].name = " "
    arm.rigify_layers[1].row = 1
    arm.rigify_layers[1].set = False
    arm.rigify_layers[1].group = 0
    arm.rigify_layers[2].name = " "
    arm.rigify_layers[2].row = 1
    arm.rigify_layers[2].set = False
    arm.rigify_layers[2].group = 0
    arm.rigify_layers[3].name = "Torso"
    arm.rigify_layers[3].row = 3
    arm.rigify_layers[3].set = False
    arm.rigify_layers[3].group = 3
    arm.rigify_layers[4].name = "Torso (Tweak)"
    arm.rigify_layers[4].row = 4
    arm.rigify_layers[4].set = False
    arm.rigify_layers[4].group = 4
    arm.rigify_layers[5].name = " "
    arm.rigify_layers[5].row = 1
    arm.rigify_layers[5].set = False
    arm.rigify_layers[5].group = 0
    arm.rigify_layers[6].name = " "
    arm.rigify_layers[6].row = 1
    arm.rigify_layers[6].set = False
    arm.rigify_layers[6].group = 0
    arm.rigify_layers[7].name = "Arm.L (IK)"
    arm.rigify_layers[7].row = 7
    arm.rigify_layers[7].set = False
    arm.rigify_layers[7].group = 2
    arm.rigify_layers[8].name = "Arm.L (FK)"
    arm.rigify_layers[8].row = 8
    arm.rigify_layers[8].set = False
    arm.rigify_layers[8].group = 5
    arm.rigify_layers[9].name = "Arm.L (Tweak)"
    arm.rigify_layers[9].row = 9
    arm.rigify_layers[9].set = False
    arm.rigify_layers[9].group = 4
    arm.rigify_layers[10].name = "Arm.R (IK)"
    arm.rigify_layers[10].row = 7
    arm.rigify_layers[10].set = False
    arm.rigify_layers[10].group = 2
    arm.rigify_layers[11].name = "Arm.R (FK)"
    arm.rigify_layers[11].row = 8
    arm.rigify_layers[11].set = False
    arm.rigify_layers[11].group = 5
    arm.rigify_layers[12].name = "Arm.R (Tweak)"
    arm.rigify_layers[12].row = 9
    arm.rigify_layers[12].set = False
    arm.rigify_layers[12].group = 4
    arm.rigify_layers[13].name = "Leg.L (IK)"
    arm.rigify_layers[13].row = 10
    arm.rigify_layers[13].set = False
    arm.rigify_layers[13].group = 2
    arm.rigify_layers[14].name = "Leg.L (FK)"
    arm.rigify_layers[14].row = 11
    arm.rigify_layers[14].set = False
    arm.rigify_layers[14].group = 5
    arm.rigify_layers[15].name = "Leg.L (Tweak)"
    arm.rigify_layers[15].row = 12
    arm.rigify_layers[15].set = False
    arm.rigify_layers[15].group = 4
    arm.rigify_layers[16].name = "Leg.R (IK)"
    arm.rigify_layers[16].row = 10
    arm.rigify_layers[16].set = False
    arm.rigify_layers[16].group = 2
    arm.rigify_layers[17].name = "Leg.R (FK)"
    arm.rigify_layers[17].row = 11
    arm.rigify_layers[17].set = False
    arm.rigify_layers[17].group = 5
    arm.rigify_layers[18].name = "Leg.R (Tweak)"
    arm.rigify_layers[18].row = 12
    arm.rigify_layers[18].set = False
    arm.rigify_layers[18].group = 4
    arm.rigify_layers[19].name = ""
    arm.rigify_layers[19].row = 1
    arm.rigify_layers[19].set = False
    arm.rigify_layers[19].group = 0
    arm.rigify_layers[20].name = ""
    arm.rigify_layers[20].row = 1
    arm.rigify_layers[20].set = False
    arm.rigify_layers[20].group = 0
    arm.rigify_layers[21].name = ""
    arm.rigify_layers[21].row = 1
    arm.rigify_layers[21].set = False
    arm.rigify_layers[21].group = 0
    arm.rigify_layers[22].name = ""
    arm.rigify_layers[22].row = 1
    arm.rigify_layers[22].set = False
    arm.rigify_layers[22].group = 0
    arm.rigify_layers[23].name = ""
    arm.rigify_layers[23].row = 1
    arm.rigify_layers[23].set = False
    arm.rigify_layers[23].group = 0
    arm.rigify_layers[24].name = ""
    arm.rigify_layers[24].row = 1
    arm.rigify_layers[24].set = False
    arm.rigify_layers[24].group = 0
    arm.rigify_layers[25].name = ""
    arm.rigify_layers[25].row = 1
    arm.rigify_layers[25].set = False
    arm.rigify_layers[25].group = 0
    arm.rigify_layers[26].name = ""
    arm.rigify_layers[26].row = 1
    arm.rigify_layers[26].set = False
    arm.rigify_layers[26].group = 0
    arm.rigify_layers[27].name = ""
    arm.rigify_layers[27].row = 1
    arm.rigify_layers[27].set = False
    arm.rigify_layers[27].group = 0
    arm.rigify_layers[28].name = "Root"
    arm.rigify_layers[28].row = 14
    arm.rigify_layers[28].set = False
    arm.rigify_layers[28].group = 1

    bones = {}

    bone = arm.edit_bones.new('spine')
    bone.head[:] = 0.0000, 0.0552, 1.0099
    bone.tail[:] = 0.0000, 0.0172, 1.1573
    bone.roll = 0.0000
    bone.use_connect = False
    bones['spine'] = bone.name
    bone = arm.edit_bones.new('spine.001')
    bone.head[:] = 0.0000, 0.0172, 1.1573
    bone.tail[:] = 0.0000, 0.0004, 1.2929
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine']]
    bones['spine.001'] = bone.name
    bone = arm.edit_bones.new('pelvis.L')
    bone.head[:] = 0.0000, 0.0552, 1.0099
    bone.tail[:] = 0.1112, -0.0451, 1.1533
    bone.roll = -1.0756
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine']]
    bones['pelvis.L'] = bone.name
    bone = arm.edit_bones.new('pelvis.R')
    bone.head[:] = -0.0000, 0.0552, 1.0099
    bone.tail[:] = -0.1112, -0.0451, 1.1533
    bone.roll = 1.0756
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine']]
    bones['pelvis.R'] = bone.name
    bone = arm.edit_bones.new('thigh.L')
    bone.head[:] = 0.0980, 0.0124, 1.0720
    bone.tail[:] = 0.0980, -0.0286, 0.5372
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine']]
    bones['thigh.L'] = bone.name
    bone = arm.edit_bones.new('thigh.R')
    bone.head[:] = -0.0980, 0.0124, 1.0720
    bone.tail[:] = -0.0980, -0.0286, 0.5372
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine']]
    bones['thigh.R'] = bone.name
    bone = arm.edit_bones.new('spine.002')
    bone.head[:] = 0.0000, 0.0004, 1.2929
    bone.tail[:] = 0.0000, 0.0059, 1.4657
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.001']]
    bones['spine.002'] = bone.name
    bone = arm.edit_bones.new('shin.L')
    bone.head[:] = 0.0980, -0.0286, 0.5372
    bone.tail[:] = 0.0980, 0.0162, 0.0852
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['thigh.L']]
    bones['shin.L'] = bone.name
    bone = arm.edit_bones.new('shin.R')
    bone.head[:] = -0.0980, -0.0286, 0.5372
    bone.tail[:] = -0.0980, 0.0162, 0.0852
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['thigh.R']]
    bones['shin.R'] = bone.name
    bone = arm.edit_bones.new('spine.003')
    bone.head[:] = 0.0000, 0.0059, 1.4657
    bone.tail[:] = 0.0000, 0.0114, 1.6582
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.002']]
    bones['spine.003'] = bone.name
    bone = arm.edit_bones.new('foot.L')
    bone.head[:] = 0.0980, 0.0162, 0.0852
    bone.tail[:] = 0.0980, -0.0934, 0.0167
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['shin.L']]
    bones['foot.L'] = bone.name
    bone = arm.edit_bones.new('foot.R')
    bone.head[:] = -0.0980, 0.0162, 0.0852
    bone.tail[:] = -0.0980, -0.0934, 0.0167
    bone.roll = -0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['shin.R']]
    bones['foot.R'] = bone.name
    bone = arm.edit_bones.new('spine.004')
    bone.head[:] = 0.0000, 0.0114, 1.6582
    bone.tail[:] = 0.0000, -0.0130, 1.7197
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['spine.004'] = bone.name
    bone = arm.edit_bones.new('shoulder.L')
    bone.head[:] = 0.0183, -0.0684, 1.6051
    bone.tail[:] = 0.1694, 0.0205, 1.6050
    bone.roll = 0.0004
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['shoulder.L'] = bone.name
    bone = arm.edit_bones.new('shoulder.R')
    bone.head[:] = -0.0183, -0.0684, 1.6051
    bone.tail[:] = -0.1694, 0.0205, 1.6050
    bone.roll = -0.0004
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['shoulder.R'] = bone.name
    bone = arm.edit_bones.new('breast.L')
    bone.head[:] = 0.1184, 0.0485, 1.4596
    bone.tail[:] = 0.1184, -0.0907, 1.4596
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['breast.L'] = bone.name
    bone = arm.edit_bones.new('breast.R')
    bone.head[:] = -0.1184, 0.0485, 1.4596
    bone.tail[:] = -0.1184, -0.0907, 1.4596
    bone.roll = -0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['breast.R'] = bone.name
    bone = arm.edit_bones.new('toe.L')
    bone.head[:] = 0.0980, -0.0934, 0.0167
    bone.tail[:] = 0.0980, -0.1606, 0.0167
    bone.roll = -0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['foot.L']]
    bones['toe.L'] = bone.name
    bone = arm.edit_bones.new('heel.02.L')
    bone.head[:] = 0.0600, 0.0459, 0.0000
    bone.tail[:] = 0.1400, 0.0459, 0.0000
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['foot.L']]
    bones['heel.02.L'] = bone.name
    bone = arm.edit_bones.new('toe.R')
    bone.head[:] = -0.0980, -0.0934, 0.0167
    bone.tail[:] = -0.0980, -0.1606, 0.0167
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['foot.R']]
    bones['toe.R'] = bone.name
    bone = arm.edit_bones.new('heel.02.R')
    bone.head[:] = -0.0600, 0.0459, 0.0000
    bone.tail[:] = -0.1400, 0.0459, 0.0000
    bone.roll = -0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['foot.R']]
    bones['heel.02.R'] = bone.name
    bone = arm.edit_bones.new('spine.005')
    bone.head[:] = 0.0000, -0.0130, 1.7197
    bone.tail[:] = 0.0000, -0.0247, 1.7813
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.004']]
    bones['spine.005'] = bone.name
    bone = arm.edit_bones.new('upper_arm.L')
    bone.head[:] = 0.1953, 0.0267, 1.5846
    bone.tail[:] = 0.4424, 0.0885, 1.4491
    bone.roll = 2.0724
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['shoulder.L']]
    bones['upper_arm.L'] = bone.name
    bone = arm.edit_bones.new('upper_arm.R')
    bone.head[:] = -0.1953, 0.0267, 1.5846
    bone.tail[:] = -0.4424, 0.0885, 1.4491
    bone.roll = -2.0724
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['shoulder.R']]
    bones['upper_arm.R'] = bone.name
    bone = arm.edit_bones.new('spine.006')
    bone.head[:] = 0.0000, -0.0247, 1.7813
    bone.tail[:] = 0.0000, -0.0247, 1.9796
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.005']]
    bones['spine.006'] = bone.name
    bone = arm.edit_bones.new('forearm.L')
    bone.head[:] = 0.4424, 0.0885, 1.4491
    bone.tail[:] = 0.6594, 0.0492, 1.3061
    bone.roll = 2.1535
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['upper_arm.L']]
    bones['forearm.L'] = bone.name
    bone = arm.edit_bones.new('forearm.R')
    bone.head[:] = -0.4424, 0.0885, 1.4491
    bone.tail[:] = -0.6594, 0.0492, 1.3061
    bone.roll = -2.1535
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['upper_arm.R']]
    bones['forearm.R'] = bone.name
    bone = arm.edit_bones.new('hand.L')
    bone.head[:] = 0.6594, 0.0492, 1.3061
    bone.tail[:] = 0.7234, 0.0412, 1.2585
    bone.roll = 2.2103
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['forearm.L']]
    bones['hand.L'] = bone.name
    bone = arm.edit_bones.new('hand.R')
    bone.head[:] = -0.6594, 0.0492, 1.3061
    bone.tail[:] = -0.7234, 0.0412, 1.2585
    bone.roll = -2.2103
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['forearm.R']]
    bones['hand.R'] = bone.name

    bpy.ops.object.mode_set(mode='OBJECT')
    pbone = obj.pose.bones[bones['spine']]
    pbone.rigify_type = 'spines.super_spine'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.neck_pos = 5
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.tweak_layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['spine.001']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['pelvis.L']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'YXZ'
    pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.make_control = False
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['pelvis.R']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'YXZ'
    pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.make_control = False
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['thigh.L']]
    pbone.rigify_type = 'limbs.super_limb'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.limb_type = "leg"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['thigh.R']]
    pbone.rigify_type = 'limbs.super_limb'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.limb_type = "leg"
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['spine.002']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['shin.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['shin.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['spine.003']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['foot.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['foot.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['spine.004']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['shoulder.L']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'YXZ'
    pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.make_widget = False
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['shoulder.R']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'YXZ'
    pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.make_widget = False
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['breast.L']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'YXZ'
    pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['breast.R']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'YXZ'
    pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['toe.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['heel.02.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['toe.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['heel.02.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['spine.005']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['upper_arm.L']]
    pbone.rigify_type = 'limbs.super_limb'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['upper_arm.R']]
    pbone.rigify_type = 'limbs.super_limb'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['spine.006']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['forearm.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['forearm.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['hand.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['hand.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

    bpy.ops.object.mode_set(mode='EDIT')
    for bone in arm.edit_bones:
        bone.select = False
        bone.select_head = False
        bone.select_tail = False
    for b in bones:
        bone = arm.edit_bones[bones[b]]
        bone.select = True
        bone.select_head = True
        bone.select_tail = True
        arm.edit_bones.active = bone

    arm.layers = [(x in [3, 7, 10, 13, 16]) for x in range(32)]

if __name__ == "__main__":
    create(bpy.context.active_object)