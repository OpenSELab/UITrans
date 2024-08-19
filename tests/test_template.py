import os

os.environ["HARMONY_PILOT_LOGGER_LEVEL"] = "DEBUG"


def test_template_files():
    from template.harmony_empty_ability import HarmonyEmptyAbilityV5ProjectTemplate
    os.chdir("../")
    template = HarmonyEmptyAbilityV5ProjectTemplate()
    print(len(template.files))
