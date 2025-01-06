@Entry
@Component
struct ListRow {
  build() {
    Column() {
      // 分割线
      Divider()
        .width('100%')
        .height('1vp')
        .backgroundColor($r('app.color.listDivider'))

      RelativeContainer() {
        Column() {
          Text('16:00')
            .fontColor($r('app.color.textColorPrimary'))
            .fontSize(16)
            .fontWeight(FontWeight.Bold)
            .width('auto')
            .height('auto')
          Text('No data')
            .fontSize(16)
            .width('auto')
            .height('auto')

          Text('Wind: 0 m/s')
            .id('itemWind')
            .width('auto')
            .height('auto')
            .margin({ top: '8vp' })
            .fontSize('16fp')
          Text('Pressure: 0 hpa')
            .id('itemPressure')
            .width('auto')
            .height('auto')
            .fontSize('16fp')
          Text('Humidity: 0 %')
            .id('itemHumidity')
            .width('auto')
            .height('auto')
            .fontSize('16fp')
        }
        .width('auto')
        .height('auto')
        .margin({ left: 16, top: 16 })

        Text('o')
          .id('itemIcon')
          .width('auto')
          .height('auto')
          .alignRules({
            right: {anchor: '__container__', align: HorizontalAlign.End},
            top: {anchor: '__container__', align: VerticalAlign.Top}
          })
          .margin({
            right: 16,
            top: 16
          })
          .layoutWeight(1)
          .fontSize('48fp')

        Text('θ °c')
          .id('itemTemperature')
          .width('auto')
          .height('auto')
          .fontSize('22fp')
          .margin({top: 8})
          .alignRules({
            top: {anchor: 'itemIcon', align: VerticalAlign.Bottom},
            right: {anchor: 'itemIcon', align: HorizontalAlign.End}
          })
      }
      .width('100%')
      .height('auto')
    }
    .width('100%')
    .height('auto')
    .padding({ bottom: '16vp' })
    // .orientation(FlexDirection.Column)  // modify example: comment out incorrectly used attributes
  }
}
