from django.shortcuts import render, redirect
from .forms import PropertyForm
from .models import InternalProperty, PropertyImage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q, Case, When, IntegerField

@login_required
def add_property(request):

    if request.method == "POST":

        form = PropertyForm(
            request.POST
        )

        if form.is_valid():

            property_obj = form.save(
                commit=False
            )

            property_obj = form.save(commit=False)
            property_obj.owner = request.user
            property_obj.agent_name = request.user.username
            property_obj.save()

            images = request.FILES.getlist(
                "images"
            )

            for image in images:

                PropertyImage.objects.create(
                    property=property_obj,
                    image=image
                )

            return redirect(
                "property_list"
            )

    else:

        form = PropertyForm()

    return render(
        request,
        "properties/add_property.html",
        {
            "form": form
        }
    )
@login_required
def property_list(request):

    properties = InternalProperty.objects.filter(
        status='active'
    ).order_by('-created_at')

    return render(
        request,
        'properties/property_list.html',
        {
            'properties': properties
        }
    )

@login_required
def my_properties(request):

    properties = InternalProperty.objects.filter(
        owner=request.user
    )

    query = request.GET.get("q")

    if query:
        properties = properties.filter(
            Q(title__icontains=query) |
            Q(location__icontains=query) |
            Q(property_category__icontains=query)
        )

    properties = properties.annotate(
        sort_order=Case(
            When(status='active', then=0),
            When(status='sold', then=1),
            output_field=IntegerField()
        )
    ).order_by(
        'sort_order',
        '-created_at'
    )

    return render(
        request,
        "properties/my_properties.html",
        {
            "properties": properties,
            "query": query
        }
    )

@login_required
def property_detail(request, slug):

    property = get_object_or_404(
        InternalProperty,
        slug=slug
    )

    return render(
        request,
        "properties/property_detail.html",
        {
            "property": property
        }
    )

@login_required
def toggle_sold(request, pk):

    property = get_object_or_404(
        InternalProperty,
        pk=pk,
        owner=request.user
    )

    if property.status == 'active':
        property.status = 'sold'
    else:
        property.status = 'active'

    property.save()

    return redirect('my_properties')

@login_required
def delete_property(request, pk):

    property = get_object_or_404(
        InternalProperty,
        pk=pk,
        owner=request.user
    )

    property.delete()

    return redirect('my_properties')

@login_required
def edit_property(request, pk):

    property = get_object_or_404(
        InternalProperty,
        pk=pk,
        owner=request.user
    )

    if request.method == 'POST':

        form = PropertyForm(
            request.POST,
            instance=property
        )

        if form.is_valid():

            form.save()

            return redirect(
                'property_detail',
                slug=property.slug
            )

    else:

        form = PropertyForm(
            instance=property
        )

    return render(
        request,
        'properties/edit_property.html',
        {
            'form': form,
            'property': property
        }
    )

@login_required
def edit_property(request, pk):

    property = get_object_or_404(
        InternalProperty,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":

        form = PropertyForm(
            request.POST,
            instance=property
        )

        if form.is_valid():

            form.save()

            images = request.FILES.getlist("images")

            for image in images:

                PropertyImage.objects.create(
                    property=property,
                    image=image
                )

            return redirect(
                "property_detail",
                slug=property.slug
            )

    else:

        form = PropertyForm(
            instance=property
        )

    return render(
        request,
        "properties/edit_property.html",
        {
            "form": form,
            "property": property
        }
    )

@login_required
def delete_image(request, pk):

    image = get_object_or_404(
        PropertyImage,
        pk=pk
    )

    if image.property.owner != request.user:
        return redirect("my_properties")

    property_id = image.property.id

    image.delete()

    return redirect(
        "edit_property",
        pk=property_id
    )