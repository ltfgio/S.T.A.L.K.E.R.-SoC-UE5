# S.T.A.L.K.E.R. Shadow of Chernobyl — UE5 Prototype

This repository currently contains a first-person Unreal Engine template, an original asset-free Cordon greybox, and a small C++ gameplay scaffold for the first Windows test build. It is an early blockout, not a finished remake and does not contain original S.T.A.L.K.E.R. game assets.

## Environment

- Unreal Engine 5.8.4
- Windows 11 x64
- Visual Studio Community with the C++ desktop/game toolchain and Windows SDK

## Open and play

Open `STALKERSoCUE5.uproject` in Unreal Editor. The default map is `Content/Cordon/L_Cordon_Blockout_Balanced.umap`. The current map uses engine primitive meshes and prototype materials to mark the road, checkpoint, settlement buildings, fences, and tree silhouettes. The first-person template controls are WASD, mouse look, and Space to jump.

## Generate the greybox

The reproducible Unreal Python script is `Scripts/generate_cordon_blockout.py`. Run it through the UE 5.8.4 Python Script Commandlet with the project open path set to this `.uproject`. It creates the balanced blockout map using assets already included with the project or engine. `Scripts/tune_blockout_exposure.py` applies the current manual exposure setup. `Scripts/place_prototype_artifact.py` places the C++ artifact pickup in the map.

The `Source/STALKERSoCUE5` module builds for Editor and Game targets. It currently contains `ASocArtifactPickup`, a spinning prototype pickup that displays a message and removes itself when touched by the first-person character.

## Package a Windows development build

From a Windows PowerShell prompt, run the Unreal Automation Tool `BuildCookRun` task for `Win64`, `Development`, with build, cook, stage, pak, and archive enabled. Keep archives outside the Git working tree. The latest successful C++ package is `D:\STALKERSoCUE5-Cordon-ManualExposureBuild\Windows`. Earlier successful archives are `D:\STALKERSoCUE5-Cordon-Blockout-BalancedBuild\Windows` and `D:\STALKERSoCUE5-Cordon-Blockout-CppBuild\Windows`.

## Current limits

- No original game source code, levels, textures, sounds, models, or licensed assets are included.
- The greybox is for layout and basic packaging checks. Terrain, player character, weapons, UI, quests, AI, audio, and gameplay systems still need implementation.
- The first-person pawn and input behavior come from the UE template and are temporary.
- The artifact pickup compiles and is included in the packaged map, but its in-game overlap/message has not yet been visually verified.
- The prototype does not need inbound network access for local single-player testing.
