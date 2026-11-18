#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "SocArtifactPickup.generated.h"

class USphereComponent;
class UStaticMeshComponent;
class UPrimitiveComponent;

UCLASS()
class STALKERSOCUE5_API ASocArtifactPickup : public AActor
{
    GENERATED_BODY()

public:
    ASocArtifactPickup();
    virtual void Tick(float DeltaTime) override;

protected:
    virtual void BeginPlay() override;

private:
    UPROPERTY(VisibleAnywhere, Category="Pickup")
    TObjectPtr<USphereComponent> Trigger;

    UPROPERTY(VisibleAnywhere, Category="Pickup")
    TObjectPtr<UStaticMeshComponent> ArtifactMesh;

    UFUNCTION()
    void HandleOverlap(
        UPrimitiveComponent* OverlappedComponent,
        AActor* OtherActor,
        UPrimitiveComponent* OtherComponent,
        int32 OtherBodyIndex,
        bool bFromSweep,
        const FHitResult& SweepResult);
};
