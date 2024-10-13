import re

code = """
@Entry
@Component
struct ProfilePage {
  build() {
    RelativeContainer() {
      // // 顶部照片区域
      // Image($r('app.media.foreground'))
      //   .id('photoHeader')
      //   .width('auto')
      //   .height('auto')
      //   .alignRules({
      //     top: { anchor: '__container__', align: VerticalAlign.Top },
      //     center: { anchor: '__container__', align: VerticalAlign.Center }  // change
      //   })

      // 用户信息展示区域
      RelativeContainer() {
        Text('Nearest Kirana Store')
          .id('tvName')
          .width('auto')
          .height('auto')
          .margin({ top: '68vp' })
          .fontFamily('HarmonyOS Sans')
          .fontSize('24fp')
          .fontColor(Color.Black)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center }  // change
          })

        Text('profile@grocery.com')
          .id('tvEmail')
          .width('250vp')
          .height('auto')
          .margin({ top: '68vp' })
          .fontFamily('HarmonyOS Sans')
          .fontSize('14fp')
          .fontColor(Color.Black)
          .textAlign(TextAlign.Center)
          .alignRules({
            top: { anchor: 'tvName', align: VerticalAlign.Bottom },
            center: { anchor: '__container__', align: VerticalAlign.Center }  // change
          })

        Text('9090909090')
          .id('tvMob')
          .width('auto')
          .height('auto')
          .margin({ top: '68vp' })
          .fontFamily('HarmonyOS Sans')
          .fontSize('16fp')
          .fontColor(Color.Black)
          .alignRules({
            top: { anchor: 'tvEmail', align: VerticalAlign.Bottom },
            center: { anchor: '__container__', align: VerticalAlign.Center }  // change
          })

        Text('GoGrocery Store, Bilaspur, Chhattisgarh')
          .id('tvAddress')
          .width('auto')
          .height('auto')
          .margin({ top: '68vp' })
          .fontFamily('HarmonyOS Sans')
          .fontSize('16fp')
          .fontColor(Color.Black)
          .textAlign(TextAlign.Center)
          .maxLines(3)
          .alignRules({
            top: { anchor: 'tvMob', align: VerticalAlign.Bottom },
            center: { anchor: '__container__', align: VerticalAlign.Center }  // change
          })
      }
      .width('100%')
      .height('100%')
      .margin({ top: '100vp', bottom: '16vp', left: '10vp', right: '10vp' })
      // .backgroundColor($r('app.media.profile_background'))
      .shadow({ radius: 2 })
      .padding({ bottom: '16vp' })

      // 按钮区域
      RelativeContainer() {
        // Blank()
        //   .id('spaceHolder')
        //   .width('10vp')
        //   .height('0vp')
        //   .alignRules({
        //     top: { anchor: 'tvMob', align: VerticalAlign.Bottom },
        //     center: { anchor: '__container__', align: HorizontalAlign.Center }
        //   })

        Button('change password')
          .id('btnChangePSW')
          .width('130vp')
          .height('40vp')
          .margin({ bottom: '16vp' })
          .alignRules({
            top: { anchor: 'tvAddress', align: VerticalAlign.Bottom },
            left: { anchor: 'spaceHolder', align: HorizontalAlign.Start }
          })
          // .backgroundColor($r('app.media.message_button'))
          .fontFamily('HarmonyOS Sans')
          .fontColor($r('app.color.colorButton'))
          .fontSize('14fp')

        Button('Change Details')
          .id('btnChangeDetails')
          .width('130vp')
          .height('40vp')
          .margin({ bottom: '16vp' })
          .alignRules({
            top: { anchor: 'tvAddress', align: VerticalAlign.Bottom },
            right: { anchor: 'spaceHolder', align: HorizontalAlign.End }
          })
          // .backgroundColor($r('app.media.connect_button'))
          .fontFamily('HarmonyOS Sans')
          .fontColor(Color.White)
          .fontSize('14fp')
      }
    }
    .width('100%')
    .height('wrap_content')
  }
}
"""

wrap_content_pattern = r"\.(width|height)\('wrap_content'\)"
cleaned_code = re.sub(wrap_content_pattern, lambda mat: f".{mat.group(1)}('auto')", code)
print(cleaned_code)