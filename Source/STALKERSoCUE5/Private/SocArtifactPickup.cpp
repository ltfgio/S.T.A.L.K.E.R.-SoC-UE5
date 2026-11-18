#include "SocArtifactPickup.h"

#include "Components/SphereComponent.h"
#include "Components/StaticMeshComponent.h"
#include "Engine/Engine.h"
#include "GameFramework/Character.h"
#include "UObject/ConstructorHelpers.h"

ASocArtifactPickup::ASocArtifactPickup()
{
    PrimaryActorTick.bCanEverTick = true;

    Trigger = CreateDefaultSubobject<USphereComponent>(TEXT("Trigger"));
    SetRootComponent(Trigger);
    Trigger->SetSphereRadius(115.0f);
    Trigger->SetCollisionEnabled(ECollisionEnabled::QueryOnly);
    Trigger->SetCollisionObjectType(ECC_WorldDynamic);
    Trigger->SetCollisionResponseToAllChannels(ECR_Ignore);
    Trigger->SetCollisionResponseToChannel(ECC_Pawn, ECR_Overlap);
    Trigger->SetGenerateOverlapEvents(true);

    ArtifactMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("ArtifactMesh"));
    ArtifactMesh->SetupAttachment(Trigger);
    ArtifactMesh->SetCollisionEnabled(ECollisionEnabled::NoCollision);
    ArtifactMesh->SetRelativeScale3D(FVector(0.4f));

    static ConstructorHelpers::FObjectFinder<UStaticMesh> SphereMesh(
        TEXT("/Engine/BasicShapes/Sphere.Sphere"));
    if (SphereMesh.Succeeded())
    {
        ArtifactMesh->SetStaticMesh(SphereMesh.Object);
    }
}

void ASocArtifactPickup::BeginPlay()
{
    Super::BeginPlay();
    Trigger->OnComponentBeginOverlap.AddDynamic(this, &ASocArtifactPickup::HandleOverlap);
}

void ASocArtifactPickup::HandleOverlap(
    UPrimitiveComponent* OverlappedComponent,
    AActor* OtherActor,
    UPrimitiveComponent* OtherComponent,
    int32 OtherBodyIndex,
    bool bFromSweep,
    const FHitResult& SweepResult)
{
    if (!Cast<ACharacter>(OtherActor))
    {
        return;
    }

    if (GEngine)
    {
        GEngine->AddOnScreenDebugMessage(
            INDEX_NONE,
            3.0f,
            FColor::Cyan,
            TEXT("Prototype artifact collected"));
    }

    Destroy();
}

void ASocArtifactPickup::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);
    AddActorLocalRotation(FRotator(0.0f, 50.0f * DeltaTime, 0.0f));
}
