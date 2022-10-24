from django.contrib import admin
from qp.rpg.models import *

@admin.register(qpSettingsRpg)
class qpSettingsRpgAdmin(admin.ModelAdmin):
    list_display = ["__str__", "rpg", "modifier_resistance_physical"]

@admin.register(qpRpg)
class qpRpgAdmin(admin.ModelAdmin):
    list_display = ["name", "owner"]
    readonly_fields = ["created_at", "updated_at"]

@admin.register(qpRpgRace)
class qpRpgRaceAdmin(admin.ModelAdmin):
    list_display = ["name", "rpg"]

@admin.register(qpRpgSkill)
class qpRpgSkillAdmin(admin.ModelAdmin):
    list_display = ["name", "attribute", "rpg"]