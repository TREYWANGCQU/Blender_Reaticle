import bpy

from .arm import Rig as armRig
from .leg import Rig as legRig
from .paw import Rig as pawRig


class Rig:

    def __init__(self, obj, bone_name, params):
        """ Initialize super_limb rig wrapper class """
        self.obj = obj
        self.params = params

        if params.limb_type == 'arm':
            self.limb = armRig(obj, bone_name, params)
        elif params.limb_type == 'leg':
            self.limb = legRig(obj, bone_name, params)
        elif params.limb_type == 'paw':
            self.limb = pawRig(obj, bone_name, params)

    def generate(self):

        return self.limb.generate()

    @staticmethod
    def get_future_names(bones):
        if bones[0].rigify_parameters.limb_type == 'arm':
            return armRig.get_future_names(bones)
        elif bones[0].rigify_parameters.limb_type == 'leg':
            return legRig.get_future_names(bones)
        elif bones[0].rigify_parameters.limb_type == 'paw':
            return pawRig.get_future_names(bones)


def add_parameters(params):
    """ Add the parameters of this rig type to the
        RigifyParameters PropertyGroup
    """

    items = [
        ('arm', 'Arm', ''),
        ('leg', 'Leg', ''),
        ('paw', 'Paw', '')
    ]

    params.limb_type = bpy.props.EnumProperty(
        items   = items,
        name    = "Limb Type",
        default = 'arm'
    )

    items = [
        ('x', 'X manual', ''),
        ('z', 'Z manual', ''),
        ('automatic', 'Automatic', '')
    ]

    params.rotation_axis = bpy.props.EnumProperty(
        items   = items,
        name    = "Rotation Axis",
        default = 'automatic'
    )

    params.auto_align_extremity = bpy.props.BoolProperty(
        name='auto_align_extremity',
        default=False,
        description="Auto Align Extremity Bone"
    )

    params.segments = bpy.props.IntProperty(
        name        = 'limb segments',
        default     = 2,
        min         = 1,
        description = 'Number of segments'
    )

    params.bbones = bpy.props.IntProperty(
        name        = 'bbone segments',
        default     = 10,
        min         = 1,
        description = 'Number of segments'
    )

    # Setting up extra layers for the FK and tweak
    params.tweak_extra_layers = bpy.props.BoolProperty(
        name        = "tweak_extra_layers",
        default     = True,
        description = ""
        )

    params.tweak_layers = bpy.props.BoolVectorProperty(
        size        = 32,
        description = "Layers for the tweak controls to be on",
        default     = tuple( [ i == 1 for i in range(0, 32) ] )
        )

    # Setting up extra layers for the FK and tweak
    params.fk_extra_layers = bpy.props.BoolProperty(
        name        = "fk_extra_layers",
        default     = True,
        description = ""
        )

    params.fk_layers = bpy.props.BoolVectorProperty(
        size        = 32,
        description = "Layers for the FK controls to be on",
        default     = tuple( [ i == 1 for i in range(0, 32) ] )
        )


def parameters_ui(layout, params):
    """ Create the ui for the rig parameters."""

    r = layout.row()
    r.prop(params, "limb_type")

    r = layout.row()
    r.prop(params, "rotation_axis")

    if 'auto' not in params.rotation_axis.lower():
        r = layout.row()
        etremities = {'arm': 'Hand', 'leg': 'Foot', 'paw': 'Claw'}
        text = "Auto align " + etremities[params.limb_type]
        r.prop(params, "auto_align_extremity", text=text)

    r = layout.row()
    r.prop(params, "segments")

    r = layout.row()
    r.prop(params, "bbones")

    bone_layers = bpy.context.active_pose_bone.bone.layers[:]

    for layer in ['fk', 'tweak']:
        r = layout.row()
        r.prop(params, layer + "_extra_layers")
        r.active = params.tweak_extra_layers

        col = r.column(align=True)
        row = col.row(align=True)

        for i in range(8):
            icon = "NONE"
            if bone_layers[i]:
                icon = "LAYER_ACTIVE"
            row.prop(params, layer + "_layers", index=i, toggle=True, text="", icon=icon)

        row = col.row(align=True)

        for i in range(16,24):
            icon = "NONE"
            if bone_layers[i]:
                icon = "LAYER_ACTIVE"
            row.prop(params, layer + "_layers", index=i, toggle=True, text="", icon=icon)

        col = r.column(align=True)
        row = col.row(align=True)

        for i in range(8,16):
            icon = "NONE"
            if bone_layers[i]:
                icon = "LAYER_ACTIVE"
            row.prop(params, layer + "_layers", index=i, toggle=True, text="", icon=icon)

        row = col.row(align=True)

        for i in range(24,32):
            icon = "NONE"
            if bone_layers[i]:
                icon = "LAYER_ACTIVE"
            row.prop(params, layer + "_layers", index=i, toggle=True, text="", icon=icon)


def create_sample(obj):
    # generated by rigify.utils.write_metarig
    bpy.ops.object.mode_set(mode='EDIT')
    arm = obj.data

    bones = {}

    bone = arm.edit_bones.new('upper_arm.L')
    bone.head[:] = -0.0016, 0.0060, -0.0012
    bone.tail[:] = 0.2455, 0.0678, -0.1367
    bone.roll = 2.0724
    bone.use_connect = False
    bones['upper_arm.L'] = bone.name
    bone = arm.edit_bones.new('forearm.L')
    bone.head[:] = 0.2455, 0.0678, -0.1367
    bone.tail[:] = 0.4625, 0.0285, -0.2797
    bone.roll = 2.1535
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['upper_arm.L']]
    bones['forearm.L'] = bone.name
    bone = arm.edit_bones.new('hand.L')
    bone.head[:] = 0.4625, 0.0285, -0.2797
    bone.tail[:] = 0.5265, 0.0205, -0.3273
    bone.roll = 2.2103
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['forearm.L']]
    bones['hand.L'] = bone.name

    bpy.ops.object.mode_set(mode='OBJECT')
    pbone = obj.pose.bones[bones['upper_arm.L']]
    pbone.rigify_type = 'limbs.super_limb'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    try:
        pbone.rigify_parameters.separate_ik_layers = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.ik_layers = [
            False, False, False, False, False, False, False, False, True, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False
        ]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.separate_hose_layers = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.hose_layers = [
            False, False, False, False, False, False, False, False, False, True,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False
        ]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.tweak_layers = [
            False, False, False, False, False, False, False, False, False, True,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False
        ]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.fk_layers = [
            False, False, False, False, False, False, False, False, True, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False
        ]
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['forearm.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone = obj.pose.bones[bones['hand.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'

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
