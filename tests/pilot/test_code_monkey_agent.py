import json
import os
import time
import unittest

from core.config.config_loader import ConfigLoader
from core.llms import LLMFactory
from core.pilot.developer import DeveloperAgent
from core.pilot.harmony.resource import load_harmony_resource

os.chdir("../")
config = ConfigLoader.from_file("./config.yaml")
llm_client = LLMFactory.create_llm_from_config(llm_client_type="openai",
                                               llm_config=config.llm_config["openai"].model_dump(),
                                               generate_config={
                                                   "temperature": 0.01
                                               })

from core.pilot.code_monkey import CodeMonkeyAgent
from core.pilot.schema import BreakdownAndroidLayout
from core.tools.file_tools import create_file, read_file, list_files
from core.state.global_state import global_state
from core.translator import init_harmony_from_android

from core.tools.search_tools import search_component_document


class TestCodeMonkeyAgent(unittest.TestCase):

    def test_init_project(self):
        init_harmony_from_android(
            global_state.android.get("project_dir"),
            global_state.harmony.get("project_dir")
        )
        resources = load_harmony_resource(global_state.harmony.get("project_dir") + "/entry/src/main/resources")
        global_state.harmony.set("resources", resources)

    def test_translate_component(self):
        start_time = time.time()
        resources = load_harmony_resource(global_state.harmony.get("project_dir") + "/entry/src/main/resources")
        global_state.harmony.set("resources", resources)
        breakdown_android_layout = BreakdownAndroidLayout.common_parse_raw(r"""
{
    "tasks": [
        {
            "description": "实现安卓协同布局的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["androidx.coordinatorlayout.widget.CoordinatorLayout"],
                "content": "<androidx.coordinatorlayout.widget.CoordinatorLayout\n    xmlns:android=\"http://schemas.android.com/apk/res/android\"\n    xmlns:app=\"http://schemas.android.com/apk/res-auto\"\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"match_parent\"\n    android:fitsSystemWindows=\"true\">\n</androidx.coordinatorlayout.widget.CoordinatorLayout>",
                "description": "创建一个协调布局，作为整个页面的容器。其宽度和高度均占满父容器，并适应系统窗口，以避免被状态栏遮挡。"
            }
        },
        {
            "description": "实现安卓应用栏的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["com.google.android.material.appbar.AppBarLayout", "androidx.appcompat.widget.Toolbar"],
                "content": "<com.google.android.material.appbar.AppBarLayout\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"?attr/actionBarSize\"\n    android:fitsSystemWindows=\"true\">\n\n    <androidx.appcompat.widget.Toolbar\n        android:id=\"@+id/toolbar\"\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"wrap_content\"\n        android:background=\"?attr/colorPrimary\"\n        android:fitsSystemWindows=\"true\"\n        android:minHeight=\"?attr/actionBarSize\"\n        app:layout_scrollFlags=\"scroll|enterAlways\"\n        app:popupTheme=\"@style/ThemeOverlay.AppCompat.Light\"\n        app:theme=\"@style/ThemeOverlay.AppCompat.Dark.ActionBar\" />\n\n</com.google.android.material.appbar.AppBarLayout>",
                "description": "在应用中创建一个顶部应用栏，作为页面导航或标题显示的容器。该应用栏布局的宽度填满其父容器，高度自适应内容。应用栏的背景颜色根据应用主题颜色属性，支持滚动与进入行为，确保良好的用户体验。"
            }
        },
        {
            "description": "实现安卓滚动视图的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["ScrollView"],
                "content": "<ScrollView\n    android:id=\"@+id/nestedScrollView\"\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"match_parent\"\n    android:layout_marginTop=\"?attr/actionBarSize\"\n    android:fitsSystemWindows=\"true\">\n</ScrollView>",
                "description": "创建一个滚动视图，用于承载可以滚动的内容。该视图的宽度填满父容器，高度也填满父容器，并在顶部留有与应用栏相同的高度，以避免UI元素重叠。"
            }
        },
        {
            "description": "实现关于文本的卡片视图的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["androidx.cardview.widget.CardView", "LinearLayout", "TextView"],
                "content": "<androidx.cardview.widget.CardView\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"wrap_content\"\n    android:layout_marginBottom=\"4dp\"\n    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n    android:layout_marginTop=\"4dp\"\n    android:padding=\"16dp\"\n    app:cardCornerRadius=\"8dp\">\n\n    <LinearLayout\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"wrap_content\"\n        android:orientation=\"vertical\">\n\n        <TextView\n            android:id=\"@+id/text_view_about\"\n            android:layout_width=\"wrap_content\"\n            android:layout_height=\"wrap_content\"\n            android:layout_marginBottom=\"24dp\"\n            android:layout_marginLeft=\"16dp\"\n            android:layout_marginRight=\"16dp\"\n            android:layout_marginTop=\"16dp\"\n            android:breakStrategy=\"high_quality\"\n            android:hyphenationFrequency=\"full\"\n            android:text=\"@string/heading_about\"\n            android:textAppearance=\"?android:attr/textAppearanceMedium\"\n            android:textIsSelectable=\"true\"\n            android:textSize=\"16sp\" />\n\n    </LinearLayout>\n</androidx.cardview.widget.CardView>",
                "description": "创建一个用于显示关于信息的卡片。卡片宽度占满父布局，高度根据内容自适应。其内容内边距为 16dp，边角圆度为 8dp。内部包含一个线性布局，内部使用文本视图来显示关于标题。"
            }
        },
        {
            "description": "实现包含Logo的卡片视图的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["androidx.cardview.widget.CardView", "LinearLayout", "ImageView"],
                "content": "<androidx.cardview.widget.CardView\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"wrap_content\"\n    android:layout_marginBottom=\"4dp\"\n    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n    android:layout_marginTop=\"4dp\"\n    android:padding=\"16dp\"\n    app:cardCornerRadius=\"8dp\">\n\n    <LinearLayout\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"wrap_content\"\n        android:orientation=\"vertical\" android:padding=\"8dp\">\n\n        <ImageView\n            android:id=\"@+id/imageViewLogo\"\n            android:layout_width=\"wrap_content\"\n            android:layout_height=\"200dp\"\n            android:layout_gravity=\"center\"\n            android:layout_marginBottom=\"8dp\"\n            android:layout_marginLeft=\"8dp\"\n            android:layout_marginRight=\"8dp\"\n            android:layout_marginTop=\"8dp\"\n            app:srcCompat=\"@drawable/bookdash_logo\" />\n\n    </LinearLayout>\n</androidx.cardview.widget.CardView>",
                "description": "创建一张展示Logo的卡片。卡片的宽度占满父布局，高度根据内容自适应，内边距为 16dp，边角圆度为 8dp。卡片内部包含一个线性布局，其中有一个充满图像的视图用于展示Logo，且其横向和纵向均居中。"
            }
        },
        {
            "description": "实现关于Bookdash的介绍的卡片视图的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["androidx.cardview.widget.CardView", "LinearLayout", "TextView", "Button"],
                "content": "<androidx.cardview.widget.CardView\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"wrap_content\"\n    android:layout_marginBottom=\"4dp\"\n    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n    android:layout_marginTop=\"4dp\"\n    android:padding=\"16dp\"\n    app:cardCornerRadius=\"8dp\">\n\n    <LinearLayout\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"wrap_content\"\n        android:orientation=\"vertical\">\n\n        <TextView\n            android:id=\"@+id/textViewHeading\"\n            android:layout_width=\"wrap_content\"\n            android:layout_height=\"wrap_content\"\n            android:layout_marginBottom=\"8dp\"\n            android:layout_marginLeft=\"16dp\"\n            android:layout_marginRight=\"16dp\"\n            android:layout_marginTop=\"16dp\"\n            android:text=\"@string/why_bookdash_heading\"\n            android:textAppearance=\"?android:attr/textAppearanceLarge\"\n            android:textIsSelectable=\"true\"\n            android:textSize=\"24sp\" />\n\n        <TextView\n            android:id=\"@+id/text_why_bookdash\"\n            style=\"@style/TextAppearance.AppCompat.Medium\"\n            android:layout_width=\"wrap_content\"\n            android:layout_height=\"wrap_content\"\n            android:layout_marginBottom=\"16dp\"\n            android:layout_marginLeft=\"16dp\"\n            android:layout_marginRight=\"16dp\"\n            android:breakStrategy=\"high_quality\"\n            android:fontFamily=\"sans-serif\"\n            android:hyphenationFrequency=\"normal\"\n            android:text=\"@string/why_bookdash\"\n            android:textIsSelectable=\"true\"\n            android:textSize=\"16sp\" />\n\n        <Button\n            android:id=\"@+id/button_learn_more\"\n            style=\"@style/Widget.AppCompat.Button.Borderless\"\n            android:layout_width=\"wrap_content\"\n            android:layout_height=\"wrap_content\"\n            android:layout_marginBottom=\"8dp\"\n            android:layout_marginLeft=\"8dp\"\n            android:layout_marginRight=\"8dp\"\n            android:fontFamily=\"sans-serif\"\n            android:text=\"@string/learn_more\"\n            android:textColor=\"@color/colorAccent\" />\n    </LinearLayout>\n</androidx.cardview.widget.CardView>",
                "description": "创建一个用于介绍Bookdash的卡片。卡片宽度占满父布局，高度根据内容自适应，内边距为 16dp，边角圆度为 8dp。卡片内部包含一个垂直排列的线性布局，其中包含一个用于标题的文本视图和两个显示描述性文本的文本视图。布局还包含一个按钮供用户进一步的交互。"
            }
        }
    ]
}
        """)
        print(breakdown_android_layout.tasks)
        code_monkey_agent = CodeMonkeyAgent(llm_client=llm_client)
        # breakdown_android_layout.tasks = [breakdown_android_layout.tasks[4]]
        all_translations, translation_agent_task = code_monkey_agent.translate_component(breakdown_android_layout)
        developer_agent = DeveloperAgent(llm_client=llm_client)
        android_layout = {
            "name": "app/res/layout/activity_about.xml",
            "content": "<androidx.coordinatorlayout.widget.CoordinatorLayout\n    xmlns:android=\"http://schemas.android.com/apk/res/android\"\n    xmlns:app=\"http://schemas.android.com/apk/res-auto\"\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"match_parent\"\n    android:fitsSystemWindows=\"true\">\n\n    <ImageView\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"match_parent\"\n        android:scaleType=\"centerCrop\"\n        android:src=\"@drawable/appbackground\"/>\n\n    <com.google.android.material.appbar.AppBarLayout\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"?attr/actionBarSize\"\n        android:fitsSystemWindows=\"true\">\n\n        <androidx.appcompat.widget.Toolbar\n            android:id=\"@+id/toolbar\"\n            android:layout_width=\"match_parent\"\n            android:layout_height=\"wrap_content\"\n            android:background=\"?attr/colorPrimary\"\n            android:fitsSystemWindows=\"true\"\n            android:minHeight=\"?attr/actionBarSize\"\n            android:title=\"@string/action_about\"\n            app:layout_scrollFlags=\"scroll|enterAlways\"\n            app:popupTheme=\"@style/ThemeOverlay.AppCompat.Light\"\n            app:theme=\"@style/ThemeOverlay.AppCompat.Dark.ActionBar\"\n            />\n\n\n    </com.google.android.material.appbar.AppBarLayout>\n\n    <ScrollView\n        android:id=\"@+id/nestedScrollView\"\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"match_parent\"\n        android:layout_marginTop=\"?attr/actionBarSize\"\n        android:fitsSystemWindows=\"true\"\n        >\n\n        <LinearLayout\n            android:layout_width=\"match_parent\"\n            android:layout_height=\"wrap_content\"\n            android:orientation=\"vertical\"\n            android:paddingBottom=\"@dimen/activity_vertical_margin\"\n            android:paddingTop=\"@dimen/activity_vertical_margin\">\n\n            <androidx.cardview.widget.CardView\n                    android:layout_width=\"match_parent\"\n                    android:layout_height=\"wrap_content\"\n                    android:layout_marginBottom=\"4dp\"\n                    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n                    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n\n                    android:layout_marginTop=\"4dp\"\n                    android:padding=\"16dp\"\n                    app:cardCornerRadius=\"8dp\">\n\n                <LinearLayout\n                        android:layout_width=\"match_parent\"\n                        android:layout_height=\"wrap_content\"\n                        android:orientation=\"vertical\">\n\n                    <TextView\n                            android:id=\"@+id/text_view_about\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"wrap_content\"\n                            android:layout_marginBottom=\"24dp\"\n                            android:layout_marginLeft=\"16dp\"\n                            android:layout_marginRight=\"16dp\"\n                            android:layout_marginTop=\"16dp\"\n                            android:breakStrategy=\"high_quality\"\n                            android:hyphenationFrequency=\"full\"\n                            android:text=\"@string/heading_about\"\n                            android:textAppearance=\"?android:attr/textAppearanceMedium\"\n                            android:textIsSelectable=\"true\"\n                            android:textSize=\"16sp\">\n\n                        <requestFocus/>\n                    </TextView>\n                </LinearLayout>\n            </androidx.cardview.widget.CardView>\n\n            <androidx.cardview.widget.CardView\n                    android:layout_width=\"match_parent\"\n                    android:layout_height=\"wrap_content\"\n                    android:layout_marginBottom=\"4dp\"\n                    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n                    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n\n                    android:layout_marginTop=\"4dp\"\n                    android:padding=\"16dp\"\n                    app:cardCornerRadius=\"8dp\">\n\n                <LinearLayout\n                        android:layout_width=\"match_parent\"\n                        android:layout_height=\"wrap_content\"\n                        android:orientation=\"vertical\"\n                        android:padding=\"8dp\">\n\n                    <ImageView\n                            android:id=\"@+id/imageViewLogo\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"200dp\"\n                            android:layout_gravity=\"center\"\n                            android:layout_marginBottom=\"8dp\"\n                            android:layout_marginLeft=\"8dp\"\n                            android:layout_marginRight=\"8dp\"\n                            android:layout_marginTop=\"8dp\"\n                            app:srcCompat=\"@drawable/bookdash_logo\"/>\n\n\n                </LinearLayout>\n\n            </androidx.cardview.widget.CardView>\n\n            <androidx.cardview.widget.CardView\n                    android:layout_width=\"match_parent\"\n                    android:layout_height=\"wrap_content\"\n                    android:layout_marginBottom=\"4dp\"\n                    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n                    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n\n                    android:layout_marginTop=\"4dp\"\n                    android:padding=\"16dp\"\n                    app:cardCornerRadius=\"8dp\">\n\n                <LinearLayout\n                        android:layout_width=\"match_parent\"\n                        android:layout_height=\"wrap_content\"\n                        android:orientation=\"vertical\">\n\n                    <TextView\n                            android:id=\"@+id/textViewHeading\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"wrap_content\"\n                            android:layout_marginBottom=\"8dp\"\n                            android:layout_marginLeft=\"16dp\"\n                            android:layout_marginRight=\"16dp\"\n                            android:layout_marginTop=\"16dp\"\n                            android:text=\"@string/why_bookdash_heading\"\n                            android:textAppearance=\"?android:attr/textAppearanceLarge\"\n                            android:textIsSelectable=\"true\"\n                            android:textSize=\"24sp\"/>\n\n                    <TextView\n                            android:id=\"@+id/text_why_bookdash\"\n                            style=\"@style/TextAppearance.AppCompat.Medium\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"wrap_content\"\n                            android:layout_marginBottom=\"16dp\"\n\n                            android:layout_marginLeft=\"16dp\"\n                            android:layout_marginRight=\"16dp\"\n                            android:breakStrategy=\"high_quality\"\n                            android:fontFamily=\"sans-serif\"\n                            android:hyphenationFrequency=\"normal\"\n                            android:text=\"@string/why_bookdash\"\n                            android:textIsSelectable=\"true\"\n                            android:textSize=\"16sp\"/>\n\n                    <Button\n                            android:id=\"@+id/button_learn_more\"\n                            style=\"@style/Widget.AppCompat.Button.Borderless\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"wrap_content\"\n                            android:layout_marginBottom=\"8dp\"\n                            android:layout_marginLeft=\"8dp\"\n                            android:layout_marginRight=\"8dp\"\n                            android:fontFamily=\"sans-serif\"\n                            android:text=\"@string/learn_more\"\n                            android:textColor=\"@color/colorAccent\"/>\n                </LinearLayout>\n\n            </androidx.cardview.widget.CardView>\n\n\n        </LinearLayout>\n\n\n    </ScrollView>\n\n</androidx.coordinatorlayout.widget.CoordinatorLayout>\n\n\n",
            "java": "package org.bookdash.android.presentation.about;\n\nimport android.content.Context;\nimport android.content.Intent;\nimport android.net.Uri;\nimport android.os.Bundle;\nimport android.text.Html;\nimport android.text.util.Linkify;\nimport android.view.LayoutInflater;\nimport android.view.View;\nimport android.view.ViewGroup;\nimport android.widget.Button;\nimport android.widget.TextView;\n\nimport androidx.annotation.Nullable;\nimport androidx.appcompat.app.ActionBar;\nimport androidx.appcompat.app.AppCompatActivity;\nimport androidx.appcompat.widget.Toolbar;\nimport androidx.fragment.app.Fragment;\n\nimport org.bookdash.android.R;\nimport org.bookdash.android.presentation.main.NavDrawerInterface;\n\npublic class AboutFragment extends Fragment implements AboutContract.View {\n\n    private AboutPresenter aboutPresenter;\n    private NavDrawerInterface navDrawerInterface;\n\n    public static AboutFragment newInstance() {\n\n        Bundle args = new Bundle();\n\n        AboutFragment fragment = new AboutFragment();\n        fragment.setArguments(args);\n        return fragment;\n    }\n\n    @Nullable\n    @Override\n    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {\n        super.onCreateView(inflater, container, savedInstanceState);\n        return inflater.inflate(R.layout.activity_about, container, false);\n    }\n\n    @Override\n    public void onViewCreated(View view, @Nullable Bundle savedInstanceState) {\n        super.onViewCreated(view, savedInstanceState);\n        aboutPresenter = new AboutPresenter(this);\n\n        Toolbar toolbar = (Toolbar) view.findViewById(R.id.toolbar);\n        navDrawerInterface.setToolbar(toolbar);\n        ActionBar actionBar = ((AppCompatActivity) getActivity()).getSupportActionBar();\n\n        if (actionBar != null) {\n            actionBar.setDisplayHomeAsUpEnabled(true);\n            actionBar.setHomeAsUpIndicator(R.drawable.ic_menu_24dp);\n            actionBar.setTitle(R.string.about_heading);\n        }\n\n        TextView textViewWhyBookDash = (TextView) view.findViewById(R.id.text_why_bookdash);\n        textViewWhyBookDash.setText(Html.fromHtml(getString(R.string.why_bookdash)));\n        Linkify.addLinks(textViewWhyBookDash, Linkify.ALL);\n\n        TextView textViewHeading = (TextView) view.findViewById(R.id.text_view_about);\n        textViewHeading.setText(Html.fromHtml(getString(R.string.heading_about)));\n        Linkify.addLinks(textViewHeading, Linkify.ALL);\n\n        Button learnMoreBookDash = (Button) view.findViewById(R.id.button_learn_more);\n        learnMoreBookDash.setOnClickListener(new View.OnClickListener() {\n            @Override\n            public void onClick(View v) {\n                aboutPresenter.clickLearnMore();\n            }\n        });\n\n\n        textViewHeading.findFocus();\n    }\n\n    @Override\n    public void onAttach(Context context) {\n        super.onAttach(context);\n        if (context instanceof NavDrawerInterface) {\n            navDrawerInterface = (NavDrawerInterface) context;\n\n        }\n    }\n\n    @Override\n    public void onDetach() {\n        super.onDetach();\n        navDrawerInterface = null;\n    }\n\n\n    @Override\n    public void showLearnMorePage(String url) {\n        Intent intent = new Intent(Intent.ACTION_VIEW);\n        intent.setData(Uri.parse(url));\n        startActivity(intent);\n    }\n}\n",
            "contains": [],
            "resources": {
                "@drawable/appbackground": "resources/drawable/appbackground.xml",
                "@string/action_about": "resources/values/strings.xml",
                "@style/ThemeOverlay.AppCompat.Light": "resources/values/styles.xml",
                "@style/ThemeOverlay.AppCompat.Dark.ActionBar": "resources/values/styles.xml",
                "@dimen/activity_vertical_margin": "resources/values/dimens.xml",
                "@dimen/activity_horizontal_margin": "resources/values/dimens.xml",
                "@string/heading_about": "resources/values/strings.xml",
                "@drawable/bookdash_logo": "resources/drawable/bookdash_logo.xml",
                "@string/why_bookdash_heading": "resources/values/strings.xml",
                "@style/TextAppearance.AppCompat.Medium": "resources/values/styles.xml",
                "@string/why_bookdash": "resources/values/strings.xml",
                "@style/Widget.AppCompat.Button.Borderless": "resources/values/styles.xml",
                "@string/learn_more": "resources/values/strings.xml",
                "@color/colorAccent": "resources/values/colors.xml"
            }
        }
        developer_agent.assemble_harmony_layout(breakdown_android_layout, android_layout, all_translations)
        end_time = time.time()
        print(end_time - start_time)
        with open("temp_agent_task.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(translation_agent_task.model_dump(), ensure_ascii=False))
        print(all_translations)

    def test_translate_component_v1(self):
        resources = load_harmony_resource(global_state.harmony.get("project_dir") + "/entry/src/main/resources")
        global_state.harmony.set("resources", resources)
        code_monkey_agent = CodeMonkeyAgent(llm_client=llm_client)
        breakdown_android_layout = BreakdownAndroidLayout.common_parse_raw(r"""
{
    "tasks": [
        {
            "description": "实现安卓协同布局的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["androidx.coordinatorlayout.widget.CoordinatorLayout"],
                "content": "<androidx.coordinatorlayout.widget.CoordinatorLayout\n    xmlns:android=\"http://schemas.android.com/apk/res/android\"\n    xmlns:app=\"http://schemas.android.com/apk/res-auto\"\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"match_parent\"\n    android:fitsSystemWindows=\"true\">\n</androidx.coordinatorlayout.widget.CoordinatorLayout>",
                "description": "创建一个协调布局，作为整个页面的容器。其宽度和高度均占满父容器，并适应系统窗口，以避免被状态栏遮挡。"
            }
        },
        {
            "description": "实现安卓应用栏的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["com.google.android.material.appbar.AppBarLayout", "androidx.appcompat.widget.Toolbar"],
                "content": "<com.google.android.material.appbar.AppBarLayout\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"?attr/actionBarSize\"\n    android:fitsSystemWindows=\"true\">\n\n    <androidx.appcompat.widget.Toolbar\n        android:id=\"@+id/toolbar\"\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"wrap_content\"\n        android:background=\"?attr/colorPrimary\"\n        android:fitsSystemWindows=\"true\"\n        android:minHeight=\"?attr/actionBarSize\"\n        app:layout_scrollFlags=\"scroll|enterAlways\"\n        app:popupTheme=\"@style/ThemeOverlay.AppCompat.Light\"\n        app:theme=\"@style/ThemeOverlay.AppCompat.Dark.ActionBar\" />\n\n</com.google.android.material.appbar.AppBarLayout>",
                "description": "在应用中创建一个顶部应用栏，作为页面导航或标题显示的容器。该应用栏布局的宽度填满其父容器，高度自适应内容。应用栏的背景颜色根据应用主题颜色属性，支持滚动与进入行为，确保良好的用户体验。"
            }
        },
        {
            "description": "实现安卓滚动视图的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["ScrollView"],
                "content": "<ScrollView\n    android:id=\"@+id/nestedScrollView\"\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"match_parent\"\n    android:layout_marginTop=\"?attr/actionBarSize\"\n    android:fitsSystemWindows=\"true\">\n</ScrollView>",
                "description": "创建一个滚动视图，用于承载可以滚动的内容。该视图的宽度填满父容器，高度也填满父容器，并在顶部留有与应用栏相同的高度，以避免UI元素重叠。"
            }
        },
        {
            "description": "实现关于文本的卡片视图的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["androidx.cardview.widget.CardView", "LinearLayout", "TextView"],
                "content": "<androidx.cardview.widget.CardView\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"wrap_content\"\n    android:layout_marginBottom=\"4dp\"\n    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n    android:layout_marginTop=\"4dp\"\n    android:padding=\"16dp\"\n    app:cardCornerRadius=\"8dp\">\n\n    <LinearLayout\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"wrap_content\"\n        android:orientation=\"vertical\">\n\n        <TextView\n            android:id=\"@+id/text_view_about\"\n            android:layout_width=\"wrap_content\"\n            android:layout_height=\"wrap_content\"\n            android:layout_marginBottom=\"24dp\"\n            android:layout_marginLeft=\"16dp\"\n            android:layout_marginRight=\"16dp\"\n            android:layout_marginTop=\"16dp\"\n            android:breakStrategy=\"high_quality\"\n            android:hyphenationFrequency=\"full\"\n            android:text=\"@string/heading_about\"\n            android:textAppearance=\"?android:attr/textAppearanceMedium\"\n            android:textIsSelectable=\"true\"\n            android:textSize=\"16sp\" />\n\n    </LinearLayout>\n</androidx.cardview.widget.CardView>",
                "description": "创建一个用于显示关于信息的卡片。卡片宽度占满父布局，高度根据内容自适应。其内容内边距为 16dp，边角圆度为 8dp。内部包含一个线性布局，内部使用文本视图来显示关于标题。"
            }
        },
        {
            "description": "实现包含Logo的卡片视图的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["androidx.cardview.widget.CardView", "LinearLayout", "ImageView"],
                "content": "<androidx.cardview.widget.CardView\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"wrap_content\"\n    android:layout_marginBottom=\"4dp\"\n    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n    android:layout_marginTop=\"4dp\"\n    android:padding=\"16dp\"\n    app:cardCornerRadius=\"8dp\">\n\n    <LinearLayout\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"wrap_content\"\n        android:orientation=\"vertical\" android:padding=\"8dp\">\n\n        <ImageView\n            android:id=\"@+id/imageViewLogo\"\n            android:layout_width=\"wrap_content\"\n            android:layout_height=\"200dp\"\n            android:layout_gravity=\"center\"\n            android:layout_marginBottom=\"8dp\"\n            android:layout_marginLeft=\"8dp\"\n            android:layout_marginRight=\"8dp\"\n            android:layout_marginTop=\"8dp\"\n            app:srcCompat=\"@drawable/bookdash_logo\" />\n\n    </LinearLayout>\n</androidx.cardview.widget.CardView>",
                "description": "创建一张展示Logo的卡片。卡片的宽度占满父布局，高度根据内容自适应，内边距为 16dp，边角圆度为 8dp。卡片内部包含一个线性布局，其中有一个充满图像的视图用于展示Logo，且其横向和纵向均居中。"
            }
        },
        {
            "description": "实现关于Bookdash的介绍的卡片视图的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["androidx.cardview.widget.CardView", "LinearLayout", "TextView", "Button"],
                "content": "<androidx.cardview.widget.CardView\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"wrap_content\"\n    android:layout_marginBottom=\"4dp\"\n    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n    android:layout_marginTop=\"4dp\"\n    android:padding=\"16dp\"\n    app:cardCornerRadius=\"8dp\">\n\n    <LinearLayout\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"wrap_content\"\n        android:orientation=\"vertical\">\n\n        <TextView\n            android:id=\"@+id/textViewHeading\"\n            android:layout_width=\"wrap_content\"\n            android:layout_height=\"wrap_content\"\n            android:layout_marginBottom=\"8dp\"\n            android:layout_marginLeft=\"16dp\"\n            android:layout_marginRight=\"16dp\"\n            android:layout_marginTop=\"16dp\"\n            android:text=\"@string/why_bookdash_heading\"\n            android:textAppearance=\"?android:attr/textAppearanceLarge\"\n            android:textIsSelectable=\"true\"\n            android:textSize=\"24sp\" />\n\n        <TextView\n            android:id=\"@+id/text_why_bookdash\"\n            style=\"@style/TextAppearance.AppCompat.Medium\"\n            android:layout_width=\"wrap_content\"\n            android:layout_height=\"wrap_content\"\n            android:layout_marginBottom=\"16dp\"\n            android:layout_marginLeft=\"16dp\"\n            android:layout_marginRight=\"16dp\"\n            android:breakStrategy=\"high_quality\"\n            android:fontFamily=\"sans-serif\"\n            android:hyphenationFrequency=\"normal\"\n            android:text=\"@string/why_bookdash\"\n            android:textIsSelectable=\"true\"\n            android:textSize=\"16sp\" />\n\n        <Button\n            android:id=\"@+id/button_learn_more\"\n            style=\"@style/Widget.AppCompat.Button.Borderless\"\n            android:layout_width=\"wrap_content\"\n            android:layout_height=\"wrap_content\"\n            android:layout_marginBottom=\"8dp\"\n            android:layout_marginLeft=\"8dp\"\n            android:layout_marginRight=\"8dp\"\n            android:fontFamily=\"sans-serif\"\n            android:text=\"@string/learn_more\"\n            android:textColor=\"@color/colorAccent\" />\n    </LinearLayout>\n</androidx.cardview.widget.CardView>",
                "description": "创建一个用于介绍Bookdash的卡片。卡片宽度占满父布局，高度根据内容自适应，内边距为 16dp，边角圆度为 8dp。卡片内部包含一个垂直排列的线性布局，其中包含一个用于标题的文本视图和两个显示描述性文本的文本视图。布局还包含一个按钮供用户进一步的交互。"
            }
        }
        
        
    ]
}
""")
        start_time = time.time()
        all_translations, agent_task = code_monkey_agent.translate_component_v1(breakdown_android_layout)
        end_time = time.time()
        print(end_time - start_time)
        for translation, task in zip(all_translations, agent_task.subtasks):
            print(translation.target_component_code)
            print(translation.explanation)
            # print(task)
