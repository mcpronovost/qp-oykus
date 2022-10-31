from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from qp.characters.models import qpCharacter, qpCharacterSkill, qpCharacterCurrency

class qpCharacterSkillInline(admin.StackedInline):
    model = qpCharacterSkill
    extra = 0


class qpCharacterCurrencyInline(admin.StackedInline):
    model = qpCharacterCurrency
    extra = 0


@admin.register(qpCharacter)
class qpCharacterAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "rpg"]
    fieldsets = [
        (_("Character"), {
            "fields": [
                "user",
                "rpg"
            ]
        }),
        (_("Identity"), {
            "fields": [
                "first_name",
                "middle_name",
                "last_name",
                "gender",
                "race",
                "avatar"
            ]
        }),
        (_("Identity"), {
            "fields": [
                "location"
            ]
        }),
        (_("Resistances"), {
            "fields": [
                "resistance_physical",
                "resistance_mental",
                "resistance_spiritual"
            ]
        }),
        (_("Attributes"), {
            "fields": [
                ("attribute_strength", "attribute_constitution"),
                ("attribute_dexterity", "attribute_perception"),
                ("attribute_intelligence", "attribute_willpower")
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
    inlines = [qpCharacterSkillInline, qpCharacterCurrencyInline]