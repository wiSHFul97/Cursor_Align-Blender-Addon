import bpy

class View3D_OT_align_view_to_cursor_op(bpy.types.Operator):
    """Align view to 3D cursor"""
    bl_idname = "view3d.align_to_3d_cursor"
    bl_label = "Align to 3d_cursor"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        bpy.ops.mesh.primitive_plane_add(align='CURSOR')
        bpy.ops.view3d.view_axis(type='TOP', align_active=True, relative=False)

        if bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT':
            bpy.ops.object.delete()
        else:
            bpy.ops.mesh.delete(type='VERT')

        return {'FINISHED'}


def register():
    bpy.utils.register_class(View3D_OT_align_view_to_cursor_op)


def unregister():
    bpy.utils.unregister_class(View3D_OT_align_view_to_cursor_op)


if __name__ == "__main__":
    register()


