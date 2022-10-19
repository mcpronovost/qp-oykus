from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class AdminMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def get_app_list(self, app_list):
        qplist_order = ["auth", "projects", "forums", "notifications"]
        qplist = []
        qpauth_app = None
        qpauth_mod = []
        for a in app_list:
            try:
                a["ordering"] = qplist_order.index(a["app_label"])
            except Exception:
                a["ordering"] = 100
            # ===---
            if a["app_label"] == "auth":
                qpauth_app = a
                for m in a["models"]:
                    if m["object_name"] == "User":
                        qpauth_mod.append(m)
                continue
            elif a["app_label"] == "knox":
                for m in a["models"]:
                    if m["object_name"] == "AuthToken":
                        m["name"] = _("Tokens")
                        qpauth_mod.append(m)
                continue
            elif a["app_label"] == "forums":
                x = ["qpForum", "qpForumCategory", "qpForumSection", "qpForumTopic", "qpForumMessage"]
                for m in a["models"]:
                    m["ordering"] = x.index(m["object_name"])
                a["models"] = sorted(a["models"], key=lambda q: q["ordering"])
            # ===---
            qplist.append(a)
            # ===---
        if qpauth_app is not None:
            qpauth_app["models"] = qpauth_mod
        qplist.insert(0, qpauth_app)
        try:
            app_list = sorted(qplist, key=lambda q: q["ordering"])
        except Exception:
            pass
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