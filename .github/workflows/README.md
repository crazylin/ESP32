# nanoFramework ESP32 GitHub Actions Build

This repository contains GitHub Actions workflows for building nanoFramework firmware for ESP32 targets based on the official [nanoFramework documentation](https://docs.nanoframework.net/content/building/build-esp32.html).

## Available Workflows

### 1. Build nanoFramework ESP32 Firmware (`nanoframework-esp32-build.yml`)

A comprehensive workflow that builds nanoFramework firmware for various ESP32 targets using the official build process.

#### Features
- **Multiple ESP32 targets**: ESP32_WROOM_32, ESP32_WROVER_KIT, ESP32_PICO, ESP32_S2, ESP32_C3
- **Build types**: Release and Debug
- **Debug symbols**: Optional debug symbol generation
- **Caching**: Optimized caching for ESP-IDF, CMake, Ninja, and Python packages
- **Artifacts**: Automatic packaging and upload of firmware binaries
- **Cross-platform**: Windows-based build environment

#### Manual Triggers

This workflow must be triggered manually from the GitHub Actions page:

1. Go to **Actions** → **Build nanoFramework ESP32 Firmware**
2. Click **Run workflow**
3. Select parameters:
   - **Target ESP32 board**: Choose your target board
   - **Build type**: Release (optimized) or Debug (with symbols)
   - **Enable debug symbols**: Check to include debug information

#### Build Outputs

After successful build, the following artifacts are available:

- **nanoCLR.bin**: The main nanoCLR firmware
- **nanoBooter.bin**: Bootloader for nanoFramework
- **bootloader.bin**: ESP32 bootloader
- **partitions.bin**: Partition table
- ***.elf**: Debug symbol files
- ***.hex**: Intel HEX format files

#### Configuration Files

- `nanoframework-config.yml`: Contains build parameters and ESP32 target configurations
- `nanoframework-esp32-build.yml`: Main build workflow

#### Usage

1. **Manual Build**: Use the workflow_dispatch trigger to manually start builds
2. **Target Selection**: Choose from supported ESP32 boards
3. **Build Type**: Select Release for production or Debug for development
4. **Download Artifacts**: Firmware packages are available as downloadable artifacts

#### Technical Details

Based on the official nanoFramework ESP32 build process:

- **ESP-IDF**: v4.4.6 (as recommended by nanoFramework)
- **CMake**: 3.21.0+ (minimum required version)
- **Python**: 3.8 (for ESP-IDF tools)
- **Ninja**: 1.10.0 (build system)
- **Toolchain**: xtensa-esp32-elf (for ESP32 targets)

#### Environment Setup

The workflow automatically:
1. Installs ESP-IDF tools and toolchain
2. Configures CMake build system
3. Sets up Python environment
4. Builds nanoCLR and nanoBooter
5. Packages firmware for distribution

#### Troubleshooting

- **Build failures**: Check the build logs for specific error messages
- **Cache issues**: Clear cache by re-running the workflow
- **Target issues**: Verify target board selection matches your hardware
- **Tool versions**: Refer to `nanoframework-config.yml` for tool version requirements

#### Customization

To add new ESP32 targets:
1. Update the `target_board` choices in the workflow
2. Add target configuration in `nanoframework-config.yml`
3. Ensure ESP-IDF support for the new target

#### Notes

- This workflow is designed for Windows runners to match the official nanoFramework build environment
- All builds are manual to prevent unnecessary resource usage
- Artifacts are retained for 30 days
- Debug builds include full symbol information for debugging