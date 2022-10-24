import re
from django.core.files.storage import get_storage_class
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.templatetags.static import static
from qp import settings

def toStaticHref(match):
    string = match.group(1).strip("/")
    string_path = static(string)
    return 'href="%s"' % (str(string_path))

def toStaticSrc(match):
    string = match.group(1).strip("/")
    string_path = static(string)
    return 'src="%s"' % (str(string_path))

def app(request):
    template = get_template("app.html")
    try:
        storage_class = get_storage_class(settings.STATICFILES_STORAGE)
        template_name = static("index.html").replace("/static/", "")
        with storage_class().open(template_name) as f:
            template = str(f.read(), "utf-8")
        #    template = re.sub(r'href="(.+)"', toStaticHref, template)
        #    template = re.sub(r'src="(.+)"', toStaticSrc, template)
    except Exception as e:
        print(e)
    return HttpResponse(template)

def api_v1(request):
    return render(request, "api-v1.html")
