from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

@api_view(['GET'])
def home(request):
    return Response(json.dumps({ "slack_name": "example_name",
            "current_day": "Monday",
            "utc_time": "2023-08-21T15:04:05Z",
            "track": "backend",
            "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
            "github_repo_url": "https://github.com/username/repo",
            "status_code": "200"
        }))

# Create your views here.
