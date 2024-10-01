import os
import unittest

from core.config.config_loader import ConfigLoader

from core.llms import LLMFactory
from core.pilot.code_monkey import CodeMonkeyAgent
from core.pilot.developer import DeveloperAgent
from core.pilot.harmony.resource import load_harmony_resource
from core.pilot.schema import BreakdownAndroidLayout
from core.tools.file_tools import create_file, read_file, list_files

os.chdir("../")
config = ConfigLoader.from_file("./config.yaml")
llm_client = LLMFactory.create_llm_from_config(llm_client_type="openai",
                                               llm_config=config.llm_config["deepseek"].dict())


class TestCodeMonkeyAgent(unittest.TestCase):

    def test_solve(self):
        problem = """将安卓布局组件 android.support.constraint.ConstraintLayout 转译为鸿蒙ArkUI组件，并保持布局和样式尽可能一致。
# android.support.constraint.ConstraintLayout
一个ConstraintLayout作为根布局，支持设置背景色和主题。
<android.support.constraint.ConstraintLayout\n    xmlns:android=\"http://schemas.android.com/apk/res/android\"\n    xmlns:app=\"http://schemas.android.com/apk/res-auto\"\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"match_parent\"\n    android:background=\"#d5efebe9\"\n    android:theme=\"@style/MyTheme\">\n    <!-- 子组件将嵌套在这里 -->\n</android.support.constraint.ConstraintLayout>
        """
        code_monkey_agent = CodeMonkeyAgent(llm_client=llm_client)
        code_monkey_agent.register_tool(create_file)
        code_monkey_agent.register_tool(read_file)
        code_monkey_agent.register_tool(list_files)
        code_monkey_agent.make_plan(problem)

    def test_translate_component(self):
        breakdown_android_layout = BreakdownAndroidLayout.common_parse_raw(r"""
        {
    "tasks": [
        {
            "description": "实现安卓布局组件 android.support.constraint.ConstraintLayout 的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["android.support.constraint.ConstraintLayout"],
                "content": "<android.support.constraint.ConstraintLayout\n    xmlns:android=\"http://schemas.android.com/apk/res/android\"\n    xmlns:app=\"http://schemas.android.com/apk/res-auto\"\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"match_parent\"\n    android:background=\"#d5efebe9\"\n    android:theme=\"@style/MyTheme\">\n    <!-- 子组件将嵌套在这里 -->\n</android.support.constraint.ConstraintLayout>",
                "description": "一个ConstraintLayout作为根布局，支持设置背景色和主题。"
            }
        },
        {
            "description": "实现安卓组件 android.support.v7.widget.CardView 的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["android.support.v7.widget.CardView", "LinearLayout"],
                "content": "<android.support.v7.widget.CardView\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"249dp\"\n    android:layout_margin=\"20dp\"\n    android:layout_marginBottom=\"8dp\"\n    app:cardBackgroundColor=\"#FF000000\"\n    app:cardElevation=\"8dp\">\n\n    <LinearLayout\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"match_parent\"\n        android:background=\"#fafafa\"\n        android:orientation=\"vertical\">\n        <!-- 子组件将嵌套在这里 -->\n    </LinearLayout>\n</android.support.v7.widget.CardView>",
                "description": "一个CardView组件，带有8dp的阴影，为内部LinearLayout提供了一个背景与边距。"
            }
        },
        {
            "description": "实现TextInputLayout及其包含的EditText组件的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["android.support.design.widget.TextInputLayout", "EditText"],
                "content": "<android.support.design.widget.TextInputLayout\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"wrap_content\"\n    android:layout_marginEnd=\"40dp\"\n    android:layout_marginStart=\"40dp\"\n    android:layout_marginTop=\"28dp\">\n\n    <EditText\n        android:id=\"@+id/loginid\"\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"wrap_content\"\n        android:drawablePadding=\"5sp\"\n        android:drawableStart=\"@drawable/ic_email_black\"\n        android:hint=\"Email\"\n        android:maxLines=\"1\"\n        android:singleLine=\"true\"\n        android:textColor=\"@color/blue_grey\" />\n</android.support.design.widget.TextInputLayout>",
                "description": "一个TextInputLayout包装了一个EditText，用于输入电子邮件，带有图标和提示。"
            }
        },
        {
            "description": "实现用于密码输入的TextInputLayout及其包含的EditText组件的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["android.support.design.widget.TextInputLayout", "EditText"],
                "content": "<android.support.design.widget.TextInputLayout\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"wrap_content\"\n    android:layout_marginEnd=\"40dp\"\n    android:layout_marginStart=\"40dp\"\n    android:layout_marginTop=\"0dp\">\n\n    <EditText\n        android:id=\"@+id/password\"\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"wrap_content\"\n        android:drawablePadding=\"5sp\"\n        android:drawableStart=\"@drawable/ic_person_black\"\n        android:hint=\"Password\"\n        android:inputType=\"textPassword\"\n        android:maxLines=\"1\"\n        android:singleLine=\"true\"\n        android:textColor=\"@color/blue_grey\" />\n</android.support.design.widget.TextInputLayout>",
                "description": "一个TextInputLayout包装了一个EditText，用于输入密码，带有图标和提示。"
            }
        },
        {
            "description": "实现用于登录的Button组件的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["Button"],
                "content": "<Button\n    android:id=\"@+id/login\"\n    android:layout_width=\"wrap_content\"\n    android:layout_height=\"wrap_content\"\n    android:layout_gravity=\"end\"\n    android:layout_margin=\"25sp\"\n    android:background=\"@drawable/btn_background\"\n    android:text=\"Sign In\"\n    android:textColor=\"@color/color_black_light\"\n    android:textStyle=\"bold\" />",
                "description": "一个用于登录的Button，样式自定义，背景为btn_background，文本颜色和样式设置明显。"
            }
        },
        {
            "description": "实现文本组件TextView用于密码找回功能的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["TextView"],
                "content": "<TextView\n    android:id=\"@+id/forget\"\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"wrap_content\"\n    android:layout_marginEnd=\"24dp\"\n    android:layout_marginStart=\"8dp\"\n    android:text=\"Forget Password? Click Here\"\n    android:textAlignment=\"textEnd\"\n    android:textColor=\"@color/blue_grey\"\n    android:textSize=\"15sp\" />",
                "description": "用于显示找回密码的TextView，文本居右对齐，样式简单明了。"
            }
        },
        {
            "description": "实现水平线性布局LinearLayout用于底部注册提示的转译，并保持布局和样式尽可能一致。",
            "done": false,
            "component": {
                "name": ["LinearLayout", "TextView"],
                "content": "<LinearLayout\n    android:id=\"@+id/linearLayout4\"\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"wrap_content\"\n    android:background=\"@color/black_trans80\"\n    android:gravity=\"bottom|center\"\n    android:orientation=\"horizontal\"\n    android:padding=\"20sp\">\n\n    <TextView\n        android:layout_width=\"wrap_content\"\n        android:layout_height=\"match_parent\"\n        android:gravity=\"bottom\"\n        android:text=\"Don't have an Account?\"\n        android:textColor=\"@color/blue_grey\"\n        android:textSize=\"15sp\" />\n\n    <TextView\n        android:id=\"@+id/signup\"\n        android:layout_width=\"wrap_content\"\n        android:layout_height=\"match_parent\"\n        android:clickable=\"true\"\n        android:focusable=\"true\"\n        android:gravity=\"bottom\"\n        android:text=\"SignUp\"\n        android:textColor=\"@color/blue_grey\"\n        android:textSize=\"15sp\"\n        android:textStyle=\"bold\" />\n</LinearLayout>",
                "description": "一个水平线性布局，包含提示账户注册的文本和一个可点击的注册链接。"
            }
        }
    ]
}
        """)
        code_monkey_agent = CodeMonkeyAgent(llm_client=llm_client)
        all_translations = code_monkey_agent.translate_component(breakdown_android_layout)
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
        print(all_translations)
