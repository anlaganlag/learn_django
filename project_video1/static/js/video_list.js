
@ajax_required
@require_http_methods(["POST"])
def video_delete(request): 
    video_id = request.POST['video_id']
    instance = Video.objects.get(id=video_id)
    instance.delete()
    return JsonResponse({"code": 0, "msg": "success"})