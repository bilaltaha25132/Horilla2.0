"""
employee/accessibility.py

Employee accessibility related methods and functionalites
"""

from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse, JsonResponse
from horilla.decorators import login_required, permission_required
from accessibility.filters import AccessibilityFilter
from accessibility.models import DefaultAccessibility
from accessibility.accessibility import ACCESSBILITY_FEATURE


@login_required
@permission_required("auth.change_permission")
def user_accessibility(request):
    """
    User accessibility method
    """
    if request.POST:
        feature = request.POST["feature"]
        accessibility = DefaultAccessibility.objects.filter(feature=feature).first()
        accessibility = accessibility if accessibility else DefaultAccessibility()
        accessibility.feature = feature
        accessibility.filter = dict(request.POST)
        accessibility.save()
        if len(request.POST.keys()) > 1:
            messages.success(request, _("Accessibility filter saved"))
        else:
            messages.info(request, _("All filter cleared"))

        return HttpResponse("<script>$('#reloadMessagesButton').click()</script>")

    accessibility_filter = AccessibilityFilter()
    return render(
        request,
        "accessibility/accessibility.html",
        {
            "accessibility": ACCESSBILITY_FEATURE,
            "accessibility_filter": accessibility_filter,
        },
    )


@login_required
@permission_required("auth.change_permission")
def get_accessibility_data(request):
    """
    Save accessibility filter method
    """
    feature = request.GET["feature"]
    accessibility = DefaultAccessibility.objects.filter(feature=feature).first()
    if not accessibility:
        return JsonResponse("", safe=False)
    return JsonResponse(accessibility.filter)