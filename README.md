# ESP32 nanoFramework 构建项目

## 简介
这个项目包含用于构建nanoFramework ESP32固件的GitHub Actions工作流。

## 工作流文件
- `.github/workflows/nanoframework-esp32-build.yml` - 主要构建工作流
- `.github/workflows/build.yml` - 简单测试工作流
- `.github/workflows/nanoframework-config.yml` - 构建配置

## 如何使用

### 前提条件
1. 确保这是一个GitHub仓库
2. 工作流文件已推送到主分支

### 触发构建
1. 访问GitHub仓库页面
2. 点击顶部的"Actions"选项卡
3. 选择可用的工作流
4. 点击"Run workflow"

## 支持的开发板
- ESP32_WROOM_32
- ESP32_WROVER_KIT
- ESP32_PICO
- ESP32_S2
- ESP32_C3

## 构建输出
- nanoCLR.bin
- nanoBooter.bin
- bootloader.bin
- partitions.bin