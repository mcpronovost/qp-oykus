from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from qp.characters.models import qpCharacter

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
    readonly_fields = ["user", "rpg", "created_at", "updated_at"]