from django.contrib import admin
from qp.forums.models import (
  qpForum,
  qpForumCategory,
  qpForumSection,
  qpForumTopic,
  qpForumMessage
)

@admin.register(qpForum)
class qpForumAdmin(admin.ModelAdmin):
    list_display = ["name", "owner"]
    readonly_fields = ["created_at", "updated_at"]

@admin.register(qpForumCategory)
class qpForumCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "forum"]
    readonly_fields = ["created_at", "updated_at"]

@admin.register(qpForumSection)
class qpForumSectionAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "forum"]
    readonly_fields = ["created_at", "updated_at"]

@admin.register(qpForumTopic)
class qpForumTopicAdmin(admin.ModelAdmin):
    list_display = ["title", "section", "category", "forum"]
    readonly_fields = ["created_at", "updated_at"]

@admin.register(qpForumMessage)
class qpForumMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "topic", "section", "category", "forum"]
    readonly_fields = ["created_at", "updated_at"]
