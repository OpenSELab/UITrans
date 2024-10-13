import json


class AndroidProjConfig:
    PROJ_NAME: str
    PROJECT_ROOT: str
    PROJ_STRUCTURE: dict
    LLM_DEEPSEEK_BASEURL: str
    LLM_DEEPSEEK_API_KEY: str

    def __init__(self):
        self.PROJ_NAME = ""
        self.PROJECT_ROOT = ""
        self.PROJ_STRUCTURE = {}
        self.LLM_DEEPSEEK_BASEURL = "https://api.deepseek.com/v1"
        self.LLM_DEEPSEEK_API_KEY = "sk-ffc130d906ac4de391b4720b8be8c034"


android_config = AndroidProjConfig()


class PageItem:
    name: str
    content: str
    java: str
    contains: []
    resources: dict
    is_main_page: bool
    # 用于存储某个XML需要的模拟数据
    mock_data: dict
    # 项目所属模块
    module: str
    # 页面统计信息
    data_analysis: dict
    # 页面复杂度
    complexity: str
    # 所属项目
    proj_name: str

    def __init__(self, name: str, content: str, java: str, contains: list, resources: dict, is_main_page: bool, module):
        self.name = name
        self.content = content
        self.java = java
        self.contains = contains
        self.resources = resources
        self.is_main_page = is_main_page
        self.mock_data = {}
        self.module = module
        self.data_analysis = {}
        self.proj_name = android_config.PROJ_NAME

    def to_dict(self):
        return {
            'name': self.name,
            'content': self.content,
            'java': self.java,
            'contains': self.contains,
            # 'resources': self.resources,
            'is_main_page': self.is_main_page,
            'mock_data': self.mock_data,
            # 'data_analysis': self.data_analysis,
            # 'proj_name': self.proj_name
        }


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, PageItem):
            return obj.to_dict()
        return super().default(obj)


simple_components = {
    "View",
    "CheckBox",
    "EditText",
    "ProgressBar",
    "RadioGroup",
    "Spinner",
    "NumberPicker",
    "DatePicker",
    "TimePicker",
    "SearchView",
    "ImageButton",
    "CalendarView",
    "CheckedTextView",
    "Chronometer",
    "RatingBar",
    "SeekBar",
    "TableLayout",
    "ZoomButton",
    "DigitalClock",
    "Switch",
    "Space",
    "LinearLayout",
    "RelativeLayout",
    "TableLayout",
    "AbsoluteLayout",
    "FrameLayout",
    "ListView",
    "GridView",
    "androidx.constraintlayout.widget.ConstraintLayout",
    "ScrollView",
    "com.google.android.material.card.MaterialCardView",
    "com.google.android.material.slider.Slider",
    "com.google.android.material.divider.MaterialDivider",
    "com.google.android.material.floatingactionbutton.FloatingActionButton",
    "com.google.android.material.tabs.TabLayout",
    "com.google.android.material.chip.Chip",
    "com.google.android.material.progressindicator.LinearProgressIndicator",
    "com.google.android.material.progressindicator.CircularProgressIndicator",
    "com.google.android.material.button.MaterialButtonToggleGroup",
    "com.google.android.material.switchmaterial.SwitchMaterial",
    "androidx.appcompat.widget.AppCompatButton",
    "androidx.appcompat.widget.Toolbar",
    "androidx.appcompat.widget.AppCompatRatingBar",
    "androidx.appcompat.widget.AppCompatToggleButton",
    "androidx.appcompat.widget.SwitchCompat",
    "androidx.appcompat.widget.AppCompatCheckBox",
    "androidx.appcompat.widget.AppCompatEditText",
    "androidx.appcompat.widget.AppCompatRadioButton",
    "androidx.appcompat.widget.AppCompatSeekBar",
    "TextView",
    "ImageView",
    "Button"
}
