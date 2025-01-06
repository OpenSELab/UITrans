@Entry
@Component
struct AppPreferences {
  @State isNotificationOn: boolean = true;

  build() {
    Column() {
      // 第一个偏好设置项
      Column() {
        Text($r('app.string.show_tutorial_settings_title'))
          .width('100%')
          .height('auto')
          .fontSize(20)
          .fontColor(Color.Black)
          .margin({ bottom: '8vp' })
        Text($r('app.string.show_tutorial_settings_summary'))
          .width('100%')
          .height('auto')
          .fontSize(16)
          .fontColor(Color.Gray)
          .margin({ bottom: '8vp' })
      }
      .width('100%')
      .height('auto')
      .margin({ bottom: '16vp' })

      // 第二个偏好设置项（开关偏好设置）
      Row() {
        Column() {
          Text($r('app.string.settings_new_book_notifications'))
            .fontSize(20)
            .fontColor(Color.Black)
            .margin({ top: '8vp', bottom: '4vp' })
          Text($r('app.string.settings_new_book_notifications_summary'))
            .fontSize(16)
            .fontColor(Color.Gray)
        }
        .height('auto')
        .alignItems(HorizontalAlign.Start)  // modify example: Add missing attributes

        Toggle({
          type: ToggleType.Switch,  // modify example: Add missing attributes
          isOn: this.isNotificationOn  // modify example: Add missing attributes
        })
          .width('auto')
          .height('auto')
          .selectedColor(Color.Blue)
          .switchPointColor(Color.White) 
          .onChange((isOn: boolean) => {
            this.isNotificationOn = isOn;
            console.info(`Switch is ${isOn ? 'ON' : 'OFF'}`);
          })
      }
      .width('100%')
    }
    .width('100%')
    .height('100%')
    .padding({ top: '16vp', bottom: '16vp', left: '16vp', right: '16vp' })
  }
}
