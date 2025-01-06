@Entry
@Component
struct NavHeaderMain {
  build() {
    RelativeContainer() {
      Column() {
        Image($r('app.media.ic_nav_header_logo'))
          .width($r('app.float.profile_width'))
          .height($r('app.float.profile_height'))
          .objectFit(ImageFit.Contain)
          .alt($r('app.string.app_name'))

        Text($r('app.string.app_name'))
          .width('100%')
          .height('auto')
          .fontColor(Color.Black)
          .margin({ top: $r('app.float.nav_header_vertical_spacing') })
      }
      .width('100%')
      .height('auto')
      .padding($r('app.float.nav_header_padding'))
      .alignRules({  // modified example: add missing attributes
        center: {anchor: '__container__', align: VerticalAlign.Center}  // modified example: add missing attributes
      })
    }
    .width('100%')
    .height($r('app.float.nav_header_height'))
    .alignSelf(ItemAlign.End)  // modified example: adjust attributes appropriately to modify component layout
  }
}
