using UnrealBuildTool;
using System.Collections.Generic;

public class STALKERSoCUE5Target : TargetRules
{
    public STALKERSoCUE5Target(TargetInfo Target) : base(Target)
    {
        Type = TargetType.Game;
        DefaultBuildSettings = BuildSettingsVersion.V7;
        IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_8;
        ExtraModuleNames.Add("STALKERSoCUE5");
    }
}
