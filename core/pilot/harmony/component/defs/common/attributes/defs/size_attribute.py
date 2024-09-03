SIZE_COMMON_ATTRIBUTES = {
  "width": {
    "description": "设置组件自身的宽度，缺省时使用元素自身内容需要的宽度。若子组件的宽大于父组件的宽，则会画出父组件的范围。从API version 10开始，该接口支持calc计算特性。",
    "params": {
      "value": {
        "type": "Length",
        "required": True,
        "description": "要设置的组件宽度。单位：vp"
      }
    }
  },
  "height": {
    "description": "设置组件自身的高度，缺省时使用元素自身内容需要的高度。若子组件的高大于父组件的高，则会画出父组件的范围。从API version 10开始，该接口支持calc计算特性。",
    "params": {
      "value": {
        "type": "Length",
        "required": True,
        "description": "要设置的组件高度。单位：vp"
      }
    }
  },
  "size": {
    "description": "设置高宽尺寸。从API version 10开始，该接口支持calc计算特性。",
    "params": {
      "value": {
        "type": "SizeOptions",
        "required": True,
        "description": "要设置的高宽尺寸。"
      }
    }
  },
  "padding": {
    "description": "设置内边距属性。从API version 10开始，该接口支持calc计算特性。",
    "params": {
      "value": {
        "type": ["Padding", "Length", "LocalizedPadding"],
        "required": True,
        "description": "设置组件的内边距。参数为Length类型时，四个方向内边距同时生效。默认值：0。单位：vp。padding设置百分比时，上下左右内边距均以父容器的width作为基础值。"
      }
    }
  },
  "margin": {
    "description": "设置外边距属性。从API version 10开始，该接口支持calc计算特性。",
    "params": {
      "value": {
        "type": ["Margin", "Length", "LocalizedMargin"],
        "required": True,
        "description": "设置组件的外边距。参数为Length类型时，四个方向外边距同时生效。默认值：0。单位：vp。margin设置百分比时，上下左右外边距均以父容器的width作为基础值。"
      }
    }
  },
  "layoutWeight": {
    "description": "对子组件进行重新布局。",
    "params": {
      "value": {
        "type": ["number", "string"],
        "required": True,
        "description": "父容器尺寸确定时，设置了layoutWeight属性的子元素与兄弟元素占主轴尺寸按照权重进行分配，忽略元素本身尺寸设置，表示自适应占满剩余空间。默认值：0。仅在Row/Column/Flex布局中生效。可选值为大于等于0的数字，或者可以转换为数字的字符串。"
      }
    }
  },
  "constraintSize": {
    "description": "设置约束尺寸，组件布局时，进行尺寸范围限制。从API version 10开始，该接口支持calc计算特性。",
    "params": {
      "value": {
        "type": "ConstraintSizeOptions",
        "required": True,
        "description": "设置约束尺寸。constraintSize的优先级高于Width和Height。取值结果参考constraintSize取值对width/height影响。默认值：{ minWidth: 0, maxWidth: Infinity, minHeight: 0, maxHeight: Infinity }。单位：vp"
      }
    }
  }
}