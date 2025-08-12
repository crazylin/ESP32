# ESP32 nanoFramework GitHub Actions 构建脚本

这个仓库包含了用于自动化构建 ESP32 nanoFramework 固件的 GitHub Actions 工作流。

## 文件说明

### 工作流文件
- `.github/workflows/build-esp32-nanoframework.yml` - 完整的构建工作流
- `.github/workflows/simple-build.yml` - 简化版本的构建工作流

## 使用方法

### 1. 基础使用
将 `.github/workflows/` 目录复制到你的 nf-interpreter 仓库中，GitHub Actions 会自动触发构建。

### 2. 手动触发
1. 进入 GitHub 仓库的 Actions 页面
2. 选择 "Build ESP32 nanoFramework Firmware" 工作流
3. 点击 "Run workflow"
4. 选择目标板和构建类型

### 3. 支持的参数

#### 目标板类型
- ESP32_WROOM_32 (默认)
- ESP32_WROVER_KIT
- ESP32_PICO
- ESP32_S2
- ESP32_C3

#### 构建类型
- Release (默认)
- Debug

## 构建输出

构建完成后，你可以在 Actions 页面下载以下文件：

## 🚀 缓存优化

### 缓存策略
工作流使用了 GitHub Actions 的缓存功能，显著提高了构建速度：

#### 缓存内容
- **ESP-IDF 工具链** (2GB) - 缓存 7 天
- **CMake** (200MB) - 缓存 7 天
- **Ninja** (10MB) - 缓存 7 天
- **Python 包** (500MB) - 缓存 3 天
- **构建缓存** (1GB) - 缓存 1 天

#### 缓存键策略
- 使用版本号作为缓存键的一部分
- 支持回退到更通用的缓存键
- 配置文件变更时自动失效

### 缓存命中率优化
1. **首次构建**：完整下载和安装所有工具
2. **后续构建**：直接复用缓存，构建时间减少 70-80%
3. **版本更新**：自动检测并更新缓存

### 固件文件
- `nanoCLR.bin` - nanoCLR 运行时固件
- `nanoBooter.bin` - nanoBooter 引导程序
- `bootloader.bin` - ESP32 引导加载器
- `partitions.bin` - 分区表

### 调试文件
- `*.elf` - 包含调试符号的文件
- `*.hex` - Intel HEX 格式文件

## ⏱️ 性能对比

| 构建类型 | 首次构建 | 缓存构建 | 节省时间 |
|----------|----------|----------|----------|
| 完整构建 | 25-30分钟 | 5-8分钟 | 70-80% |
| 简化构建 | 15-20分钟 | 3-5分钟 | 75-85% |

## 本地开发环境设置

如果你想在本地构建，请参考以下步骤：

### 1. 安装工具
1. **Visual Studio Code**
2. **CMake** (>= 3.21)
3. **Python** (>= 3.6.8)
4. **Ninja** (推荐)
5. **ESP-IDF Tools**

### 2. 安装驱动
根据你的 ESP32 硬件安装相应的 USB 转 UART 驱动：
- CP210x USB to UART Bridge VCP Drivers
- FTDI Virtual COM Port Drivers
- WHC CH34x

### 3. 克隆仓库
```bash
git clone https://github.com/nanoframework/nf-interpreter.git
cd nf-interpreter
```

### 4. 配置环境
```powershell
# 设置环境变量
$env:IDF_PATH = "C:\esp-idf"
$env:PATH = "$env:IDF_PATH\tools;$env:PATH"

# 创建构建目录
mkdir build
cd build

# 配置构建
cmake -G Ninja `
  -DTOOLCHAIN_PREFIX="C:/esp-idf/tools/tools/xtensa-esp32-elf" `
  -DESP32_IDF_PATH="C:/esp-idf" `
  -DCMAKE_BUILD_TYPE=Release `
  -DTARGET_NAME=ESP32_WROOM_32 `
  ..

# 构建
cmake --build . --target all
```

## 故障排除

### 常见问题

1. **路径过长错误**
   - 确保仓库路径不要太深，避免超过 250 个字符

2. **环境变量问题**
   - 检查 ESP-IDF 路径是否正确设置
   - 验证工具链是否在 PATH 中

3. **依赖缺失**
   - 确保所有必需的工具都已安装
   - 检查 Python 依赖是否安装

### 调试技巧

1. **查看构建日志**
   - 在 GitHub Actions 页面查看详细日志
   - 检查每个步骤的输出信息

2. **本地测试**
   - 使用 `act` 工具在本地测试 GitHub Actions
   - 安装：`brew install act` (macOS) 或 `choco install act` (Windows)

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个构建脚本。

## 参考文档

- [nanoFramework 官方构建文档](https://docs.nanoframework.net/content/building/build-esp32.html)
- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [ESP-IDF 文档](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)

## 许可证

MIT License