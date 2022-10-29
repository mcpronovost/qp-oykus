from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from django.utils.translation import gettext_lazy as _
from qp.quests.models import qpQuest, qpQuestLog

@admin.register(qpQuest)
class qpQuestAdmin(OrderedModelAdmin):
    list_display = ["title", "level", "section", "rpg", "order", "move_up_down_links"]
    list_filter = ["rpg", "section", "level"]
    filter_horizontal = ["skills"]
    readonly_fields = ["created_at", "updated_at"]


@admin.register(qpQuestLog)
class qpQuestLogAdmin(admin.ModelAdmin):
    list_display = ["quest", "character", "start", "end", "is_completed", "is_success"]