# Circle-Scheduler

## 開発の流れ

[x] 簡易的アルゴリズム作成
[x] 簡易的スケジュール取得 API
[x] スケジュール全体を取得、表示
[x] スケジュールのコンフリクトを表示
[x] 全員の日程調整の回答内容を表示
[x] 演目ごとのメンバー、練習時間を表示
[] supabase セットアップ
[] prisma orm セットアップ
[] テーブル作成
[] テストデータ保存
[] テストデータ編集
[] types 作成
[] イベント作成機能
[] 日程調整回答機能
[] アルゴリズム改良
[] バックエンドデプロイ
[] (認証機能)

## できたら追加したい

メンバーごとのスケジュールを取得する機能
演目ごとのスケジュールを取得する機能
1 練習、1 セクション、1 日、1 週間、1 か月ごとの詳細ページ
メンバーの練習間の空き時間が短くなるようにスケジュールを組むアルゴリズム
aws 用いる

# データベース設計

## サークルテーブル

- サークル id
- イベント
- 全メンバー数

## イベントテーブル

- イベント id
- イベント名
- 出演メンバー数
- 日程調整の範囲
- 演目

## メンバーテーブル

- メンバー id
- 名前
- イベント
- 出演する演目
- 日程調整の回答
- 練習日

## 演目テーブル

- 演目 id
- 演目名
- 出演メンバー
- 練習日

## スケジュールテーブル

- 日付 id
- 日付
- 演目名
- メンバー
- 被り

## 被りテーブル

- 被り id
- 被った日時
- 被ったジャンル
- 被ったメンバー

# フェーズ 1: 基盤構築

## プロジェクトのセットアップ

Supabase セットアップ
Prisma ORM セットアップ
プロジェクト構造の整理
GitHub リポジトリ設定

## データベース設計と実装

テーブル作成
マイグレーション設定
テストデータ投入
型定義（Types）作成

# フェーズ 2: コア機能開発

## 認証基盤実装

Supabase Auth 設定
ログイン/ログアウトフロー
認可制御

## イベント管理機能

イベント作成
演目登録
メンバー割り当て

## スケジュール管理の基本機能

日程調整回答機能
基本的なスケジュール表示
スケジュールコンフリクト検出

# フェーズ 3: アルゴリズム開発

## スケジューリングアルゴリズム実装

基本的なスケジュール生成
コンフリクト解決ロジック
アルゴリズムの最適化

# フェーズ 4: 拡張機能開発

## 詳細表示機能

メンバーごとのスケジュール表示
演目ごとのスケジュール表示
期間別（日/週/月）表示

# スケジュール最適化

メンバーの空き時間最適化
練習効率の向上
パフォーマンスチューニング

# フェーズ 5: インフラ構築とデプロイ

## AWS インフラ設計と構築

アーキテクチャ設計
インフラのコード化（IaC）
監視・ロギング設定

# デプロイメント

CI/CD パイプライン構築
ステージング環境構築
本番環境デプロイ

# 主な改善点：

## 認証機能を早期に実装

データセキュリティの確保
ユーザー関連機能の早期テスト可能

## フェーズを明確に分割

各フェーズでの成果物を明確化
デバッグとテストを効率化

## インフラ構築を独立したフェーズに

AWS リソースの効率的な利用
スケーラビリティの確保

## 段階的な機能拡張

コア機能を優先
フィードバックを基に拡張機能を実装
