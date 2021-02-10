from TikTokApi import TikTokApi
from django.http import HttpResponse
from django.shortcuts import render
import json
from django_json_error_response.http import (
    Http400Response,
    Http403Response,
    Http404Response,
    Http500Response,
    SuccessResponse,
    ErrorResponse
)

verifyFp = ""


def trend(request):
    api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
    result = api.trending(
        count=int(request.GET.get('count') or 30), referrer=request.GET.get('referrer'), proxy=request.GET.get('proxy') or '')
    return SuccessResponse(message=result)


def getTikTok(request):
    api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
    id = request.GET.get('id')
    url = request.GET.get('url')
    if id is not None:
        result = api.getTikTokById(id=id)
        return SuccessResponse(message=result)
    if url is not None:
        result = api.getTikTokByUrl(url=url)
        return SuccessResponse(message=result)


def getVideoById(request):
    api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
    id = request.GET.get('id')
    if id is not None:
        result = api.getTikTokById(request.GET.get('id'))
        return SuccessResponse(message=result)
    else:
        return ErrorResponse(message='id should not be ignored', status=402)
# get video by url, id
# params : url(string), id(string), waterMark(bool), return_bytes(1,0), proxy(string)


def downloadVideos(request):
    api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
    if request.method == 'GET':
        if 'url' in request.GET:
            url = request.GET.get('url')
            waterMark = request.GET.get('waterMark')
            try:
                if waterMark is None:
                    result = api.get_Video_By_Url(
                        url, return_bytes=request.GET.get('return_bytes') or 0)
                    return SuccessResponse(message=result)
                else:
                    result = api.get_Video_No_Watermark(
                        url, return_bytes=request.GET.get('return_bytes') or 0, proxy=request.GET.get('proxy'))
                    return SuccessResponse(message=result)
            except Exception as error:
                return ErrorResponse(str(error), status=403)
        elif 'id' in request.GET:
            id = request.GET.get('id')
            try:
                result = api.get_Video_No_Watermark_ID(
                    id, return_bytes=request.GET.get('return_bytes') or 0)
                return SuccessResponse(message=result)
            except Exception as error:
                return ErrorResponse(str(error), status=403)
        else:
            return ErrorResponse('Please specify url or id')


def getSound(request):
    api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
    result = api.bySound(id=request.GET.get(
        'id'), count=request.GET.get('count'), proxy=request.GET.get('proxy'))
    return SuccessResponse(messge=result)


def getUserByName(request):
    api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
    result = api.byUsername(username=request.GET.get(
        'username'), count=request.GET.get('count') or 30, proxy=request.GET.get('proxy') or None)
    return SuccessResponse(messge=result)


def getHashTag(request):
    api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
    result = api.byHashtag(hashtag=request.GET.get(
        'hashtag'), count=request.GET.get('count') or 30)
    return SuccessResponse(message=result)


def discoverMusic(request):
    api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
    result = api.discoverMusic(proxy=request.GET.get('proxy') or None)
    return SuccessResponse(message=result)


def discoverHashtags(request):
    api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
    result = api.discoverHashtags(proxy=request.GET.get('proxy') or None)
    return SuccessResponse(message=result)
