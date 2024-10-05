from template.harmony_empty_ability import HarmonyEmptyAbilityV5ProjectTemplate


class TemplateManager:

    @classmethod
    def get_template(cls, name):
        if name == HarmonyEmptyAbilityV5ProjectTemplate.name:
            return HarmonyEmptyAbilityV5ProjectTemplate()
        else:
            raise ValueError(f'Unknown template name {name}')


template_manager = TemplateManager()
