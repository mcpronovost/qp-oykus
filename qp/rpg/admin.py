from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from ordered_model.admin import OrderedInlineModelAdminMixin, OrderedTabularInline
from qp.rpg.models import qpRpg, qpRpgRace, qpRpgSkill, qpRpgCurrency, qpRpgStyle, qpSettingsRpg

@admin.register(qpSettingsRpg)
class qpSettingsRpgAdmin(admin.ModelAdmin):
    list_display = ["__str__", "rpg", "modifier_resistance_physical"]
    fieldsets = [
        (_("Settings"), {
            "fields": [
                "rpg"
            ]
        }),
        (_("Limits"), {
            "fields": [
                "limit_characters",
                "limit_races",
                "limit_skills"
            ]
        }),
        (_("Modifiers"), {
            "fields": [
                "modifier_resistance_physical",
                "modifier_resistance_mental",
                "modifier_resistance_spiritual"
            ]
        })
    ]


class qpRpgCurrencyInline(OrderedTabularInline):
    model = qpRpgCurrency
    extra = 0
    fields = ["name", "icon", "move_up_down_links"]
    readonly_fields = ["move_up_down_links"]
    ordering = ["order"]


class qpRpgStyleInline(admin.StackedInline):
    model = qpRpgStyle
    extra = 0


@admin.register(qpRpg)
class qpRpgAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    list_display = ["name", "owner"]
    fieldsets = [
        (_("RPG"), {
            "fields": [
                "name",
                "slug"
            ]
        }),
        (_("Staff"), {
            "fields": [
                "creator",
                "owner"
            ]
        }),
        (_("Identity"), {
            "fields": [
                "caption",
                "description",
                "primary_color",
                "icon"
            ]
        }),
        (_("Permissions"), {
            "fields": [
                "is_public",
                "is_active"
            ]
        }),
        (_("Dates"), {
            "fields": [
                "created_at",
                "updated_at"
            ]
        })
    ]
    readonly_fields = ["created_at", "updated_at"]
    inlines = [qpRpgCurrencyInline, qpRpgStyleInline]


@admin.register(qpRpgRace)
class qpRpgRaceAdmin(admin.ModelAdmin):
    list_display = ["name", "rpg"]


@admin.register(qpRpgSkill)
class qpRpgSkillAdmin(admin.ModelAdmin):
    list_display = ["name", "attribute", "rpg"]
