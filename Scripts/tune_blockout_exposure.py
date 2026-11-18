import unreal

map_path = "/Game/Cordon/L_Cordon_Blockout_Balanced"
if not unreal.EditorLevelLibrary.load_level(map_path):
    raise RuntimeError("Could not load Cordon blockout: " + map_path)

volume = None
for actor in unreal.EditorLevelLibrary.get_all_level_actors():
    if isinstance(actor, unreal.PostProcessVolume) and actor.get_actor_label() == "Lighting / manual exposure":
        volume = actor
        break

if not volume:
    volume = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.PostProcessVolume,
        unreal.Vector(0, 0, 0),
        unreal.Rotator(0, 0, 0),
        False,
    )
if not volume:
    raise RuntimeError("Could not create post-process volume")

volume.set_actor_label("Lighting / manual exposure")
volume.set_editor_property("unbound", True)
settings = volume.get_editor_property("settings")

def set_post_process_property(names, value):
    for name in names:
        try:
            settings.set_editor_property(name, value)
            print("EXPOSURE_PROPERTY_SET " + name)
            return
        except Exception:
            pass
    raise RuntimeError("Could not set any of these PostProcessSettings fields: " + str(names))

set_post_process_property(
    ("override_auto_exposure_method", "b_override_auto_exposure_method", "bOverride_AutoExposureMethod"),
    True,
)
set_post_process_property(("auto_exposure_method", "AutoExposureMethod"), unreal.AutoExposureMethod.AEM_MANUAL)
set_post_process_property(
    ("override_auto_exposure_bias", "b_override_auto_exposure_bias", "bOverride_AutoExposureBias"),
    True,
)
set_post_process_property(("auto_exposure_bias", "AutoExposureBias"), -1.0)
volume.set_editor_property("settings", settings)

if not unreal.get_editor_subsystem(unreal.LevelEditorSubsystem).save_current_level():
    raise RuntimeError("Could not save Cordon map")

print("CORDON_EXPOSURE_SET method=Manual bias=-1.0")
