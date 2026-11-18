import unreal

map_path = "/Game/Cordon/L_Cordon_Blockout_Balanced"
if not unreal.EditorLevelLibrary.load_level(map_path):
    raise RuntimeError("Could not load Cordon blockout: " + map_path)

pickup_class = unreal.load_class(None, "/Script/STALKERSoCUE5.SocArtifactPickup")
if not pickup_class:
    raise RuntimeError("SocArtifactPickup class is not available; build the C++ module first")

pickup = unreal.EditorLevelLibrary.spawn_actor_from_class(
    pickup_class,
    unreal.Vector(-3500, 0, 110),
    unreal.Rotator(0, 0, 0),
    False,
)
if not pickup:
    raise RuntimeError("Could not place prototype artifact")

pickup.set_actor_label("Gameplay / prototype artifact pickup")
if not unreal.get_editor_subsystem(unreal.LevelEditorSubsystem).save_current_level():
    raise RuntimeError("Could not save the Cordon map")

print("PROTOTYPE_ARTIFACT_PLACED at=(-3500,0,110)")
