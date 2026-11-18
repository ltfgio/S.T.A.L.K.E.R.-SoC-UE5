using UnrealBuildTool;

public class STALKERSoCUE5 : ModuleRules
{
    public STALKERSoCUE5(ReadOnlyTargetRules Target) : base(Target)
    {
        PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
        PublicDependencyModuleNames.AddRange(new string[]
        {
            "Core",
            "CoreUObject",
            "Engine",
            "InputCore",
            "EnhancedInput"
        });
    }
}
