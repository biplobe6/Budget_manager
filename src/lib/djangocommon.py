def get_object_or_none(model_reference, *args, **kwargs):
    try:
        return model_reference.objects.get(*args, **kwargs)
    except model_reference.DoesNotExist:
        return None
