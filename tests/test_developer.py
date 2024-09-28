import json
import os
from core.config.config_loader import ConfigLoader
from core.pilot.harmony.component.components import get_harmony_component
from core.pilot.harmony.resource import load_harmony_resource
from core.pilot.harmony.utils import get_component_related_types
from core.pilot.schema import BreakdownLayoutTranslation, ChooseComponent, BreakdownLayout
from core.prompt.prompt_loader import PromptLoader
from template import HarmonyEmptyAbilityV5ProjectTemplate
from core.llms.oai_client import OpenAIClient

os.chdir("../")

ConfigLoader.from_file("./config.yaml")
harmony_template = HarmonyEmptyAbilityV5ProjectTemplate()
openai_default_config = ConfigLoader.get_config().llm_config.get("deepseek").model_dump()
resource = load_harmony_resource(r"D:\Codes\Python\harmony-pilot\demos\haromny_demos\hmdemo\entry\src\main\resources")

"""# FirstFragment
## 导航栏功能
这个功能点涉及将一个导航栏（默认显示在屏幕顶部），用于提供标准的导航和操作功能。导航栏的样式为宽度匹配父布局，高度为默认的56vp，导航栏的功能包括显示标题，没有回退按钮。
## 滚动布局功能
这个功能点涉及一个滚动布局组件，用于在页面上实现内容滚动显示。滚动布局包含下列按钮组件和文本显示组件。滚动视图的宽度和高度都设置为与父容器匹配。
## 按钮导航功能
这个功能点涉及将一个按钮组件放置在屏幕顶部中央，按钮的文本内容为“Next”（引用自资源文件@string/next）。当用户点击该按钮时，应用会从当前的FirstFragment导航到SecondFragment。
## 文本显示功能
这个功能点涉及将一个文本视图组件放置在按钮组件下方，文本视图的文本内容为“Lorem Ipsum”（引用自资源文件@string/lorem_ipsum）。文本视图位于屏幕中央，并且与按钮组件之间有16vp的垂直间距。文本左对齐。
## 浮动操作按钮功能
这个功能点涉及将一个浮动操作按钮（默认显示在屏幕底部右侧。浮动操作按钮的样式为宽度自适应内容，高度自适应内容，位于底部和右侧，右侧外边距为`@dimen/fab_margin`，底部外边距为16vp，图标为`ic_dialog_email`（邮件图标）。浮动操作按钮的功能包括在点击时显示一个默认显示在屏幕底部的快捷消息提示，提示内容为"Replace with your own action"。
"""


layout_files = {
    "res/layout/activity_main.xml": {
        "name": "res/layout/activity_main.xml",
        "content": """<?xml version="1.0" encoding="utf-8"?>
<androidx.coordinatorlayout.widget.CoordinatorLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:fitsSystemWindows="true"
    tools:context=".MainActivity">

    <com.google.android.material.appbar.AppBarLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:fitsSystemWindows="true">

        <com.google.android.material.appbar.MaterialToolbar
            android:id="@+id/toolbar"
            android:layout_width="match_parent"
            android:layout_height="?attr/actionBarSize" />

    </com.google.android.material.appbar.AppBarLayout>

    <include layout="@layout/content_main" />

    <com.google.android.material.floatingactionbutton.FloatingActionButton
        android:id="@+id/fab"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="bottom|end"
        android:layout_marginEnd="@dimen/fab_margin"
        android:layout_marginBottom="16dp"
        app:srcCompat="@android:drawable/ic_dialog_email" />

</androidx.coordinatorlayout.widget.CoordinatorLayout>
        """,
        "contains": ["res/layout/content_main.xml"],
        "java": ""  # java code
    },
    "res/layout/content_main.xml": {
        "name": "res/layout/content_main.xml",
        "content": """<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    app:layout_behavior="@string/appbar_scrolling_view_behavior">

    <fragment
        android:id="@+id/nav_host_fragment_content_main"
        android:name="androidx.navigation.fragment.NavHostFragment"
        android:layout_width="0dp"
        android:layout_height="0dp"
        app:defaultNavHost="true"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:navGraph="@navigation/nav_graph" />
</androidx.constraintlayout.widget.ConstraintLayout>
        """,
        "contains": ["res/layout/fragment_first.xml"],
        "java": ""  # java code
    },
    "res/layout/fragment_first.xml": {
        "name": "res/layout/fragment_first.xml",
        "content": """<?xml version="1.0" encoding="utf-8"?>
<androidx.core.widget.NestedScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".FirstFragment">

    <androidx.constraintlayout.widget.ConstraintLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:padding="16dp">

        <Button
            android:id="@+id/button_first"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/next"
            app:layout_constraintBottom_toTopOf="@id/textview_first"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent" />

        <TextView
            android:id="@+id/textview_first"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginTop="16dp"
            android:text="@string/lorem_ipsum"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toBottomOf="@id/button_first" />
    </androidx.constraintlayout.widget.ConstraintLayout>
</androidx.core.widget.NestedScrollView>    
        """,
        "contains": [],
        "java": ""  # java code
    }
}


def test_choose_component():
    layout_translation = BreakdownLayoutTranslation.model_validate(json.loads("""
{
  "tasks": [
    {
      "description": "创建ets/pages/FragmentFirst.ets页面，实现安卓布局文件res/layout/fragment_first.xml的转译。",
      "done": false,
      "harmony": "ets/pages/FragmentFirst.ets",
      "android": "res/layout/fragment_first.xml"
    },
    {
      "description": "创建ets/pages/ContentMain.ets页面，实现安卓布局文件res/layout/content_main.xml的转译。",
      "done": false,
      "harmony": "ets/pages/ContentMain.ets",
      "android": "res/layout/content_main.xml"
    },
    {
      "description": "创建ets/pages/Index.ets页面，实现安卓布局文件res/layout/activity_main.xml的转译。",
      "done": false,
      "harmony": "ets/pages/Index.ets",
      "android": "res/layout/activity_main.xml"
    }
  ]
}
        """))
    client = OpenAIClient(openai_default_config)
    current_task_index = 0
    current_task = layout_translation.tasks[current_task_index]
    android_layout = layout_files[current_task.android]
    current_task_description = f"""{current_task.description}
# {android_layout['name']}
{android_layout['content']}
"""
    system_prompt = PromptLoader.get_prompt("developer/system.prompt")
    choose_component_prompt = PromptLoader.get_prompt(
        "developer/choose_component.prompt",
        tasks=layout_translation.tasks,
        current_task_description=current_task_description,
        harmony_components=get_harmony_component()
    )
    print(choose_component_prompt)
    response = client.create(messages=[
        {"content": system_prompt, "role": "system"},
        {"content": choose_component_prompt, "role": "user"}
    ], model_schema=ChooseComponent)
    print(response.choices[0].message.content)
    choose_component = ChooseComponent.common_parse_raw(response.choices[0].message.content)
    related_component = {}
    for component in choose_component.components:
        related_component.update(get_harmony_component(component))
    print(related_component)


def test_breakdown_layout():
    client = OpenAIClient(openai_default_config)

    layout_files = {
        "materialhelptutorial/res/layout/activity_help_tutorial.xml": {
            "name": "materialhelptutorial/res/layout/activity_help_tutorial.xml",
            "content": "<RelativeLayout xmlns:android=\"http://schemas.android.com/apk/res/android\"\nxmlns:app=\"http://schemas.android.com/apk/res-auto\"\nandroid:layout_width=\"match_parent\"\nandroid:id=\"@+id/activity_help_root\"\nandroid:layout_height=\"match_parent\"\nandroid:orientation=\"vertical\">\n\n<androidx.viewpager.widget.ViewPager\nandroid:id=\"@+id/activity_help_view_pager\"\nandroid:clipToPadding=\"false\"\nandroid:clipChildren=\"false\"\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"match_parent\"\nandroid:layout_above=\"@+id/linear_layout_indicator\">\n\n</androidx.viewpager.widget.ViewPager>\n\n<View android:layout_width=\"match_parent\"\n\nandroid:layout_above=\"@+id/linear_layout_indicator\"\nandroid:layout_height=\"1dp\"\nandroid:background=\"#E0E0E0\"\n/>\n<LinearLayout\nandroid:id=\"@+id/linear_layout_indicator\"\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"56dp\"\nandroid:weightSum=\"1\"\nandroid:layout_alignParentBottom=\"true\"\nandroid:orientation=\"horizontal\">\n\n<Button\nandroid:id=\"@+id/activity_help_skip_textview\"\nandroid:layout_width=\"0dp\"\nandroid:layout_height=\"match_parent\"\nandroid:layout_alignParentBottom=\"true\"\nandroid:layout_centerInParent=\"true\"\nstyle=\"@android:style/Widget.Holo.Button.Borderless\"\nandroid:fontFamily=\"sans-serif\"\nandroid:gravity=\"center\"\nandroid:text=\"@string/tutorial_skip\"\nandroid:textColor=\"@color/tutorial_buttonTextColor\"\nandroid:textSize=\"18sp\"\nandroid:layout_weight=\"0.25\" />\n\n<za.co.riggaroo.materialhelptutorial.view.CirclePageIndicator\nandroid:id=\"@+id/activity_help_view_page_indicator\"\nandroid:layout_width=\"0dp\"\nandroid:layout_height=\"wrap_content\"\nandroid:layout_above=\"@id/activity_help_skip_textview\"\napp:fillColor=\"#41FFFFFF\"\napp:pageColor=\"#14FFFFFF\"\napp:radius=\"6dp\"\nandroid:layout_weight=\"0.5\"\napp:strokeColor=\"#E0E0E0\"\napp:strokeWidth=\"0dp\"\nandroid:layout_gravity=\"center_vertical\"\nandroid:minHeight=\"24dp\" />\n\n<LinearLayout\nandroid:layout_width=\"0dp\"\nandroid:layout_weight=\"0.25\"\nandroid:orientation=\"vertical\"\nandroid:layout_height=\"match_parent\">\n<ImageButton\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"match_parent\"\nandroid:src=\"@drawable/ic_navigate_next\"\nstyle=\"@android:style/Widget.Holo.Button.Borderless\"\nandroid:id=\"@+id/activity_next_button\"\nandroid:layout_margin=\"8dp\"\nandroid:visibility=\"visible\"\nandroid:padding=\"16dp\" />\n<Button\nandroid:id=\"@+id/activity_tutorial_done\"\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"match_parent\"\nstyle=\"@android:style/Widget.Holo.Button.Borderless\"\nandroid:fontFamily=\"sans-serif\"\nandroid:gravity=\"center\"\nandroid:text=\"@string/tutorial_done\"\nandroid:textColor=\"@color/tutorial_buttonTextColor\"\nandroid:textSize=\"18sp\"\nandroid:visibility=\"gone\" />\n</LinearLayout>\n\n</LinearLayout>\n\n\n</RelativeLayout>",
            "java": " package za.co.riggaroo.materialhelptutorial.tutorial;\n\n\nimport android.app.ActionBar;\nimport android.os.Build;\nimport android.os.Bundle;\nimport android.view.View;\nimport android.view.Window;\nimport android.view.WindowManager;\nimport android.widget.Button;\nimport android.widget.ImageButton;\nimport android.widget.TextView;\n\nimport androidx.appcompat.app.AppCompatActivity;\nimport androidx.viewpager.widget.ViewPager;\n\nimport java.util.List;\n\nimport za.co.riggaroo.materialhelptutorial.MaterialTutorialFragment;\nimport za.co.riggaroo.materialhelptutorial.R;\nimport za.co.riggaroo.materialhelptutorial.TutorialItem;\nimport za.co.riggaroo.materialhelptutorial.adapter.MaterialTutorialAdapter;\nimport za.co.riggaroo.materialhelptutorial.view.CirclePageIndicator;\n\npublic class MaterialTutorialActivity extends AppCompatActivity implements MaterialTutorialContract.View {\n\npublic static final String MATERIAL_TUTORIAL_ARG_TUTORIAL_ITEMS = \"tutorial_items\";\nprivate static final String TAG = \"MaterialTutActivity\";\nprivate ViewPager mHelpTutorialViewPager;\nprivate View mRootView;\nprivate TextView mTextViewSkip;\nprivate ImageButton mNextButton;\nprivate Button mDoneButton;\nprivate MaterialTutorialPresenter materialTutorialPresenter;\n\nprivate View.OnClickListener finishTutorialClickListener = new View.OnClickListener() {\n@Override\npublic void onClick(View v) {\nmaterialTutorialPresenter.doneOrSkipClick();\n\n}\n};\n\n\n@Override\nprotected void onCreate(Bundle savedInstanceState) {\nsuper.onCreate(savedInstanceState);\nsetContentView(R.layout.activity_help_tutorial);\n\nmaterialTutorialPresenter = new MaterialTutorialPresenter(this, this);\nsetStatusBarColor();\nActionBar actionBar = getActionBar();\n\nif (actionBar != null) {\ngetActionBar().hide();\n}\nmRootView = findViewById(R.id.activity_help_root);\nmHelpTutorialViewPager = (ViewPager) findViewById(R.id.activity_help_view_pager);\nmTextViewSkip = (TextView) findViewById(R.id.activity_help_skip_textview);\nmNextButton = (ImageButton) findViewById(R.id.activity_next_button);\nmDoneButton = (Button) findViewById(R.id.activity_tutorial_done);\n\nmTextViewSkip.setOnClickListener(finishTutorialClickListener);\nmDoneButton.setOnClickListener(finishTutorialClickListener);\n\n\nmNextButton.setOnClickListener(new View.OnClickListener() {\n@Override\npublic void onClick(View v) {\nmaterialTutorialPresenter.nextClick();\n\n\n}\n});\nList<TutorialItem> tutorialItems = getIntent().getParcelableArrayListExtra(MATERIAL_TUTORIAL_ARG_TUTORIAL_ITEMS);\nif (tutorialItems == null) {\nshowEndTutorial();\n} else {\nmaterialTutorialPresenter.loadViewPagerFragments(tutorialItems);\n}\n}\n\nprivate void setStatusBarColor() {\nif (isFinishing()) {\nreturn;\n}\nif (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {\nWindow window = getWindow();\nwindow.addFlags(WindowManager.LayoutParams.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS);\nwindow.addFlags(WindowManager.LayoutParams.FLAG_TRANSLUCENT_STATUS);\n}\n}\n\n@Override\npublic void showNextTutorial() {\nint currentItem = mHelpTutorialViewPager.getCurrentItem();\nif (currentItem < materialTutorialPresenter.getNumberOfTutorials()) {\nmHelpTutorialViewPager.setCurrentItem(mHelpTutorialViewPager.getCurrentItem() + 1);\n}\n}\n\n@Override\npublic void showEndTutorial() {\nsetResult(RESULT_OK);\nfinish();\n}\n\n@Override\npublic void setBackgroundColor(int color) {\nmRootView.setBackgroundColor(color);\n}\n\n@Override\npublic void showDoneButton() {\nmTextViewSkip.setVisibility(View.INVISIBLE);\nmNextButton.setVisibility(View.GONE);\nmDoneButton.setVisibility(View.VISIBLE);\n}\n\n@Override\npublic void showSkipButton() {\nmTextViewSkip.setVisibility(View.VISIBLE);\nmNextButton.setVisibility(View.VISIBLE);\nmDoneButton.setVisibility(View.GONE);\n}\n\n@Override\npublic void setViewPagerFragments(List<MaterialTutorialFragment> materialTutorialFragments) {\nmHelpTutorialViewPager.setAdapter(new MaterialTutorialAdapter(getSupportFragmentManager(), materialTutorialFragments));\nCirclePageIndicator mCirclePageIndicator = (CirclePageIndicator) findViewById(R.id.activity_help_view_page_indicator);\n\nmCirclePageIndicator.setViewPager(mHelpTutorialViewPager);\nmCirclePageIndicator.setOnPageChangeListener(new ViewPager.OnPageChangeListener() {\n@Override\npublic void onPageScrolled(int i, float v, int i2) {\n\n}\n\n@Override\npublic void onPageSelected(int i) {\nmaterialTutorialPresenter.onPageSelected(mHelpTutorialViewPager.getCurrentItem());\n\n}\n\n@Override\npublic void onPageScrollStateChanged(int i) {\n\n}\n});\nmHelpTutorialViewPager.setPageTransformer(true, new ViewPager.PageTransformer() {\n@Override\npublic void transformPage(View page, float position) {\nmaterialTutorialPresenter.transformPage(page, position);\n}\n}\n\n);\n}\n} ",
            "contains": [],
            "resources": {
                "@color/tutorial_buttonTextColor": "resources/values/colors.xml",
                "@drawable/ic_navigate_next": "resources/drawable/ic_navigate_next.png",
                "@android:style/Widget.Holo.Button.Borderless": "resources/values/styles.xml",
                "@string/tutorial_skip": "resources/values/strings.xml",
                "@string/tutorial_done": "resources/values/strings.xml"
            }
        }
    }
    current_task_index = 0
    android_layout_xml_name = list(layout_files.keys())[current_task_index]
    layout_translation = BreakdownLayoutTranslation(
        tasks=[{
            "description": f"将{android_layout_xml_name}转译为对应的Harmony页面",
            "done": False,
            "android": android_layout_xml_name,
            "harmony": "ets/pages/Index.ets"
        }]
    )
    # layout_translation = BreakdownLayoutTranslation.model_validate(json.loads())
    system_prompt = PromptLoader.get_prompt("developer/system.prompt")
    translate_layout_plan_prompt = PromptLoader.get_prompt(
        "developer/breakdown_android_layout.prompt",
        tasks=layout_translation.tasks,
        current_task=layout_translation.tasks[current_task_index],
        android_layout=layout_files[layout_translation.tasks[current_task_index].android],
        harmony_components=get_harmony_component(),
        is_component_content=False,
        is_type_content=True,
        project_resources=resource
    )
    print(translate_layout_plan_prompt)
    response = client.create(messages=[
        {"content": system_prompt, "role": "system"},
        {"content": translate_layout_plan_prompt, "role": "user"}
    ], model_schema=BreakdownLayout, temperature=0.2)
    print(response.choices[0].message.content)
    print(response.usage)
