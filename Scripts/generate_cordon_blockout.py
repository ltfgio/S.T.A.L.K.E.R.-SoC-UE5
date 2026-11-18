import unreal

# Original, asset-free greybox blockout. All geometry uses Unreal primitive meshes.
level_path = "/Game/Cordon/L_Cordon_Blockout_Bright"
subsystem = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
if not subsystem.new_level(level_path, False):
    raise RuntimeError("Could not create level: " + level_path)

cube = unreal.load_asset("/Engine/BasicShapes/Cube")
sphere = unreal.load_asset("/Engine/BasicShapes/Sphere")
if not cube or not sphere:
    raise RuntimeError("Required Engine primitive meshes are missing")

materials = {
    "ground": unreal.load_asset("/Game/LevelPrototyping/Materials/MI_PrototypeGrid_Gray.MI_PrototypeGrid_Gray"),
    "concrete": unreal.load_asset("/Game/LevelPrototyping/Materials/MI_PrototypeGrid_Gray_02.MI_PrototypeGrid_Gray_02"),
    "accent": unreal.load_asset("/Game/LevelPrototyping/Materials/MI_DefaultColorway.MI_DefaultColorway"),
    "dark": unreal.load_asset("/Game/LevelPrototyping/Materials/MI_PrototypeGrid_TopDark.MI_PrototypeGrid_TopDark"),
}


def spawn_box(label, x, y, z, sx, sy, sz, material="concrete", mesh=cube):
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.StaticMeshActor,
        unreal.Vector(x, y, z),
        unreal.Rotator(0, 0, 0),
        False,
    )
    if not actor:
        raise RuntimeError("Could not spawn actor: " + label)
    actor.set_actor_label(label)
    component = actor.static_mesh_component
    component.set_static_mesh(mesh)
    component.set_mobility(unreal.ComponentMobility.STATIC)
    component.set_collision_profile_name("BlockAll")
    actor.set_actor_scale3d(unreal.Vector(sx / 100.0, sy / 100.0, sz / 100.0))
    mat = materials.get(material)
    if mat:
        component.set_material(0, mat)
    return actor


def house(label, x, y, width=700, depth=600, height=280):
    # Simple readable rural-house silhouettes, intentionally untextured.
    spawn_box(label + " / walls", x, y, height / 2, width, depth, height, "accent")
    spawn_box(label + " / roof", x, y, height + 85, width + 100, depth + 100, 170, "dark")
    spawn_box(label + " / door", x + width * .26, y - depth / 2 - 2, 95, 100, 12, 190, "dark")
    spawn_box(label + " / window left", x - width * .22, y - depth / 2 - 4, 165, 120, 12, 90, "ground")
    spawn_box(label + " / window right", x + width * .08, y - depth / 2 - 4, 165, 120, 12, 90, "ground")


# Ground, road and simple verge. The cross-axis is X; the player starts toward the south.
spawn_box("Blockout / ground", 0, 0, -160, 30000, 18000, 300, "ground")
spawn_box("Road / main", 2500, 0, 5, 18000, 760, 24, "dark")
for x in range(-5500, 10501, 1200):
    spawn_box("Road / centre marker", x, 0, 19, 500, 22, 3, "accent")
spawn_box("Roadside / left shoulder", 2500, -490, 4, 18000, 200, 18, "concrete")
spawn_box("Roadside / right shoulder", 2500, 490, 4, 18000, 200, 18, "concrete")

# Entry checkpoint: booth, barrier, gate posts and roof frame.
spawn_box("Checkpoint / booth", 950, -930, 135, 360, 330, 270, "accent")
spawn_box("Checkpoint / booth roof", 950, -930, 290, 420, 390, 45, "dark")
spawn_box("Checkpoint / gate post L", 820, -390, 220, 80, 80, 440, "concrete")
spawn_box("Checkpoint / gate post R", 820, 390, 220, 80, 80, 440, "concrete")
spawn_box("Checkpoint / overhead beam", 820, 0, 440, 80, 860, 70, "accent")
spawn_box("Checkpoint / road barrier", 1430, 0, 85, 45, 790, 22, "accent")
for y in (-1050, -820, 820, 1050):
    spawn_box("Checkpoint / fence post", 820, y, 115, 35, 35, 230, "dark")
for y in range(-1000, 1001, 260):
    spawn_box("Checkpoint / fence rail", 820, y, 90, 28, 260, 22, "dark")
    spawn_box("Checkpoint / fence rail", 820, y, 175, 28, 260, 18, "dark")

# Cordon settlement blockout.
house("Cordon / farmhouse A", 3300, -1250, 760, 620, 300)
house("Cordon / farmhouse B", 4100, 1300, 620, 700, 260)
house("Cordon / roadside shed", 5200, -1250, 520, 420, 220)
spawn_box("Cordon / bus stop shelter", 5700, 760, 125, 420, 300, 25, "dark")
for x in (5520, 5880):
    spawn_box("Cordon / bus stop support", x, 760, 115, 24, 24, 230, "accent")

# Fence lines and a small farm yard, kept clear of the road.
for y in (-1850, 1850):
    for x in range(-1000, 7601, 500):
        spawn_box("Cordon / fence post", x, y, 85, 24, 24, 170, "dark")
    for x in range(-750, 7401, 1000):
        spawn_box("Cordon / fence rail", x, y, 55, 1000, 20, 16, "dark")
        spawn_box("Cordon / fence rail", x, y, 115, 1000, 20, 16, "dark")

# Low-poly tree silhouettes around the playable route; no external foliage assets.
for x, y, scale in [
    (-3500,-2300,1.1),(-2400,-2700,.9),(-900,-2500,1.0),(700,-2500,1.2),
    (2400,-2400,.9),(3900,-2500,1.1),(5600,-2400,.9),(7600,-2500,1.1),
    (-3000,2450,1.1),(-1600,2700,.9),(300,2500,1.0),(2200,2600,1.1),
    (4400,2500,.9),(6500,2500,1.2),(8200,2200,.9),(9000,-1900,1.1),
]:
    spawn_box("Cordon / tree trunk", x, y, 180 * scale, 75 * scale, 75 * scale, 360 * scale, "dark")
    spawn_box("Cordon / tree crown", x, y, 490 * scale, 430 * scale, 430 * scale, 480 * scale, "accent", sphere)

# Distant stepped silhouettes frame the playable area without consuming landscape memory.
for x, y, sx, sy, sz in [
    (-7800,-6500,4200,5200,650),(-1800,-7200,5000,4000,900),
    (4300,-7000,5200,4300,750),(9000,6500,4800,4400,850),
    (1000,7200,6000,4200,700),(-7600,5000,4200,5000,800),
]:
    spawn_box("Distant ridge / blockout", x, y, sz / 2 - 100, sx, sy, sz, "ground")

# Player start faces down the approach toward the checkpoint.
start = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.PlayerStart, unreal.Vector(-4200, 0, 115), unreal.Rotator(0, 0, 0), False
)
start.set_actor_label("Player Start / Cordon approach")

# Basic outdoor lighting and atmospheric depth.
sun = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.DirectionalLight, unreal.Vector(0, 0, 5000), unreal.Rotator(-32, 0, -28), False
)
sun.set_actor_label("Lighting / sun")
atmosphere = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.SkyAtmosphere, unreal.Vector(0, 0, 0), unreal.Rotator(0, 0, 0), False
)
atmosphere.set_actor_label("Atmosphere / sky")
sun.light_component.set_editor_property("intensity", 100000.0)
sun.light_component.set_editor_property("atmosphere_sun_light", True)
sky = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.SkyLight, unreal.Vector(0, 0, 500), unreal.Rotator(0, 0, 0), False
)
sky.set_actor_label("Lighting / sky fill")
sky.light_component.set_editor_property("intensity", 2.0)
sky.light_component.set_editor_property("real_time_capture", True)
fog = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.ExponentialHeightFog, unreal.Vector(0, 0, 0), unreal.Rotator(0, 0, 0), False
)
fog.set_actor_label("Atmosphere / distance fog")
fog.component.set_editor_property("fog_density", 0.001)
fog.component.set_editor_property("fog_height_falloff", 0.22)

if not subsystem.save_current_level():
    raise RuntimeError("Could not save generated Cordon level")

print("CORDON_BLOCKOUT_CREATED actors=" + str(len(unreal.EditorLevelLibrary.get_all_level_actors())))
