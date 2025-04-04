def custom_processor(request):
    return {
        'user': request.user if request.user.is_authenticated else None,
        'is_superuser': request.user.is_superuser if request.user.is_authenticated else False,
    }