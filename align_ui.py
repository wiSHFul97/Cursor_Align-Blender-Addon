import bpy


class VIEW3D_PT_align_ui(bpy.types.Panel):
    """Panel of Align View to 3D Cursor"""
    bl_label = "Align to 3d cursor"
    bl_category = 'View'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        self.layout.operator("view3d.align_to_3d_cursor")


def register():
    bpy.utils.register_class(VIEW3D_PT_align_ui)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_align_ui)

