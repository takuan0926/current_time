# current_time　- 現在時刻配信ノード
current_timeは指定したトピックで現在時刻を定期的に配信するROS2ノードです。
# 機能
- 現在時刻を定期的に配信。
- 実行時に現在時刻を表示します

# 動作環境
このノードはROS2（Foxyまたはそれ以降のバージョン）で動作します。
- ROS2 Foxy
- Python3.8以上
- Ubuntu20.04以上（推奨）

# 使用方法
## 1.リポジトリをクローンして依存関係をインストール
```
git clone https://github.com/takuan0926/current_time_publisher.git
cd current_time_publisher
colcon build
source install/setup.bash
```
## 2.ノードを起動
デフォルトでは、current_timeというトピックで現在時刻を知らせます。
```
ros2 run current_time_publisher time_publisher
```
実行中に現在時刻が以下の形式で出力されます。
出力
```
2024-11-30 12:13:40
```
## 3.他のノードがトピックを購読
他のノードがこのトピックを購読することで、現在時刻を利用することができます。
```
ros2 topic echo /current_time
```
出力
```
data: '2024-11-30 12:13:40'
data: '2024-11-30 12:13:41'
```
## エラーハンドリング
- 正常に時刻が配信されている場合、コンソールに現在時刻が表示されます。
- 何か問題が発生した場合は、適切なエラーメッセージが表示されます。
## 使用例
ノードの起動
```
ros2 run current_time_publisher current_time_publisher
```
出力例（毎秒更新される現在時刻）：
```
2024-11-30 12:13:40
2024-11-30 12:13:41
2024-11-30 12:13:42
```
## トピックの確認
/current_timeトピックが正しくパブリッシュされているか確認するには、別のターミナルで以下のコマンドを実行します。
```
ros2 topic echo /current_time
```
出力例
```
data: '2024-11-30 12:13:40'
data: '2024-11-30 12:13:41'
```
# ライセンス
-  このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- © 2024 Suzuki Takuma
