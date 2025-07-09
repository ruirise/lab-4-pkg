import statistics
def area_stats(lists):
    if len(lists) == 0:
        raise ValueError("At least one shape is required")
    areas = [i.area() for i in lists]
    return {
        "n": len(areas),
        "mean": sum(areas)/len(areas),
        "total": sum(areas),
        "min": min(areas),
        "max": max(areas)
    }