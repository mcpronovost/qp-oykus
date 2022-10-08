from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class AdminMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def get_app_list(self, app_list):
        qplist = []
        qpauth_app = None
        qpauth_mod = []
        for a in app_list:
            if a["app_label"] == "auth":
                qpauth_app = a
                for m in a["models"]:
                    if m["object_name"] == "User":
                        qpauth_mod.append(m)
            elif a["app_label"] == "knox":
                for m in a["models"]:
                    if m["object_name"] == "AuthToken":
                        m["name"] = _("Tokens")
                        qpauth_mod.append(m)
            else:
                qplist.append(a)
            # ===---
        qpauth_app["models"] = qpauth_mod
        qplist.insert(0, qpauth_app)
        app_list = qplist
        return app_list

    def process_template_response(self, request, response):
        if not request.path.startswith(reverse("admin:index")):
            return response
        app_list = []
        if "app_list" in response.context_data:
            app_list = response.context_data["app_list"]
        elif "available_apps" in response.context_data:
            app_list = response.context_data['available_apps']
        # ===---
        app_list = self.get_app_list(app_list)
        response.context_data["app_list"] = app_list
        response.context_data["available_apps"] = app_list
        # ===---
        return response