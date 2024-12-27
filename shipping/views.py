from django.shortcuts import render
from django.http import JsonResponse

def cbm_calculator(request):
    if request.method == "POST":
        # Get inputs
        length = float(request.POST.get("length", 0))
        breadth = float(request.POST.get("breadth", 0))
        height = float(request.POST.get("height", 0))
        quantity = int(request.POST.get("quantity", 1))
        unit = request.POST.get("unit")

        # Convert input dimensions to meters
        conversion_factors = {
            "mm": 0.001,
            "cm": 0.01,
            "m": 1,
            "inch": 0.0254,
            "feet": 0.3048,
            "yard": 0.9144,
        }
        factor = conversion_factors.get(unit, 1)

        length_m = length * factor
        breadth_m = breadth * factor
        height_m = height * factor

        # Calculate volumes
        volume_m3 = length_m * breadth_m * height_m * quantity
        volume_ft3 = volume_m3 * 35.3147

        # Prepare response data
        data = {
            "volume_m3": round(volume_m3, 3),
            "volume_ft3": round(volume_ft3, 3),
        }
        return JsonResponse(data)

    return render(request, "cbm_calculator.html")
