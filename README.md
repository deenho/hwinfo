> **Warning**
> hwinfo.io is not affiliated with this repository.
> Any claim that this is the official product repository of hwinfo.io is false.

[![Linux (clang)](https://github.com/lfreist/hwinfo/actions/workflows/build-linux-clang.yml/badge.svg)](https://github.com/lfreist/hwinfo/actions/workflows/build-linux-clang.yml)
[![Linux (gcc)](https://github.com/lfreist/hwinfo/actions/workflows/build-linux-gcc.yml/badge.svg)](https://github.com/lfreist/hwinfo/actions/workflows/build-linux-gcc.yml)

[![MacOS](https://github.com/lfreist/hwinfo/actions/workflows/build-macos.yml/badge.svg)](https://github.com/lfreist/hwinfo/actions/workflows/build-macos.yml)

[![Windows (Visual Studio)](https://github.com/lfreist/hwinfo/actions/workflows/build-windows-vs.yml/badge.svg)](https://github.com/lfreist/hwinfo/actions/workflows/build-windows-vs.yml)
[![Windows (MinGW)](https://github.com/lfreist/hwinfo/actions/workflows/build-windows-mingw.yml/badge.svg)](https://github.com/lfreist/hwinfo/actions/workflows/build-windows-mingw.yml)

[![clang format](https://github.com/lfreist/hwinfo/actions/workflows/format-check.yml/badge.svg)](https://github.com/lfreist/hwinfo/actions/workflows/format-check.yml)

# hwinfo

hwinfo provides an easy-to-use and modern C++ API for retrieving hardware information of your systems components such as
CPU, RAM, GPU, Disks, Mainboard, ...

> **Note**
>
> If you face any issues, find bugs or if your platform is not supported yet, do not hesitate
> to [create an issue](https://github.com/lfreist/hwinfo/issues).

## Content

- [hwinfo](#hwinfo)
  - [Content](#content)
  - [Supported Components](#supported-components)
  - [Build `hwinfo`](#build-hwinfo)
  - [Example](#example)

## Supported Components

> **Note**
>
> The listed components that are not yet implemented (indicated with ❌) are in development and will be supported in
> future releases. **You are welcome to start contributing and help improving this library!**

| Component        | Info               | Linux | Apple | Windows |
|------------------|:-------------------|:-----:|:-----:|:-------:|
| CPU              | Vendor             |  ✔️   |  ✔️   |   ✔️    |
|                  | Model              |  ✔️   |  ✔️   |   ✔️    |
|                  | Frequency          |  ✔️   |  ❌️   |   ✔️    |
|                  | Physical Cores     |  ✔️   |  ✔️   |   ✔️    |
|                  | Logical Cores      |  ✔️   |  ✔️   |   ✔️    |
|                  | Cache Size         |  ✔️   |  ✔️️  |   ✔️    |
| GPU              | Vendor             |  ✔️   |  ❌️   |   ✔️    |
|                  | Model              |  ✔️   |  ❌️   |   ✔️    |
|                  | Memory Size        |   ❌   |   ❌   |   ✔️    |
| Memory (RAM)     | Vendor             |   ❌   |   ❌   |   ✔️    |
|                  | Model              |   ❌   |   ❌   |   ✔️    |
|                  | Name               |   ❌   |   ❌   |   ✔️    |
|                  | Serial Number      |   ❌   |   ❌   |   ✔️    |
|                  | Total Memory Size  |  ✔️   |  ✔️   |   ✔️    |
|                  | Free Memory Size   |  ✔️   |  ✔️   |   ✔️    |
| Mainboard        | Vendor             |  ✔️   |  ✔️   |   ✔️    |
|                  | Model              |  ✔️   |   ❌   |   ✔️    |
|                  | Version            |  ✔️   |   ❌   |   ✔️    |
|                  | Serial-Number      |   ❌   |  ✔️   |   ✔️    |
|                  | Bios               |   ❌   |   ❌   |    ❌    |
| Disk             | Vendor             |  ✔️   |  ✔️   |   ✔️    |
|                  | Model              |  ✔️   |  ✔️   |   ✔️    |
|                  | Serial-Number      |  ✔️   |  ✔️   |   ✔️    |
|                  | Size               |  ✔️   |  ✔️   |   ✔️    |
|                  | Free Size          |  ✔️   |  ✔️   |   ✔️    |
|                  | Volumes            |  ✔️   |  ✔️   |   ✔️    |
| Operating System | Name               |  ✔️   |  ✔️   |   ✔️    |
|                  | Short Name         |  ✔️   |  ✔️   |   ✔️    |
|                  | Version            |  ✔️   |  ✔️   |    ❌    |
|                  | Kernel             |  ✔️   |  ✔️   |    ❌    |
|                  | Architecture (Bit) |  ✔️   |  ✔️   |   ✔️    |
|                  | Endianess          |  ✔️   |  ✔️   |   ✔️    |
| Battery          | Vendor             |  ✔️   |  ❌️   |    ❌    |
|                  | Model              |  ✔️   |   ❌   |    ❌    |
|                  | Serial Number      |  ✔️   |  ✔️   |    ❌    |
|                  | Technology         |  ✔️   |   ❌   |    ❌    |
|                  | Capacity           |  ✔️   |  ✔️   |   ️❌    |
|                  | Charging           |  ✔️   |  ✔️   |    ❌    |

All components are available via the `hwinfo::hwinfo` target, or via individual CMake targets, which you can choose and
link against depending on your needs.

```cmake
target_link_libraries(your_target PRIVATE hwinfo::hwinfo)
```

or

```cmake
target_link_libraries(
  your_target
  PRIVATE hwinfo::cpu
          hwinfo::gpu
          hwinfo::ram
          hwinfo::mainboard
          hwinfo::disk
          hwinfo::os
          hwinfo::battery)
```

The CMake options control which components will be built and available in the library:

- `HWINFO_OS` "Enable OS detection" (default to `ON`)
- `HWINFO_MAINBOARD` "Enable mainboard detection" (default to `ON`)
- `HWINFO_CPU` "Enable CPU detection" (default to `ON`)
- `HWINFO_DISK` "Enable disk detection" (default to `ON`)
- `HWINFO_RAM` "Enable RAM detection" (default to `ON`)
- `HWINFO_GPU` "Enable GPU detection" (default to `ON`)
- `HWINFO_GPU_OPENCL` "Enable usage of OpenCL in GPU information" (default to `OFF`)
- `HWINFO_BATTERY` "Enable battery detection" (default to `ON`)

## Build `hwinfo`

> Requirements: git, meson, ninja, and a C++17 compiler (gcc, clang, or MSVC)

1. Download the repository:
   ```bash
   git clone https://github.com/lfreist/hwinfo
   cd hwinfo
   ```

2. Configure and build using Meson:
   ```bash
   meson setup build --buildtype=release
   meson compile -C build
   ```

3. Run the test suite:
   ```bash
   meson test -C build --verbose
   ```

The main build options are exposed as Meson boolean options, for example:
```bash
meson setup build -Dhwinfo_cpu=true -Dhwinfo_gpu=false
```

Use `-Dhwinfo_shared=true` for shared libraries (the default) or
`-Dhwinfo_static=true` for static libraries. If both are enabled, the static configuration takes precedence.

## Example

See [system_infoMain.cpp](examples/system_infoMain.cpp)

The output should look similar to this one:

```
Hardware Report:

----------------------------------- CPU -----------------------------------
Socket 0:
 vendor:            GenuineIntel
 model:             Intel(R) Core(TM) i7-10700K CPU @ 3.80GHz
 physical cores:    8
 logical cores:     16
 max frequency:     3792
 regular frequency: 3792
 min frequency:     -1
 current frequency: 3792
 cache size:        16777216
----------------------------------- OS ------------------------------------
Operating System:   Microsoft Windows 11 Professional (build 22621)
short name:         Windows
version:            <unknown>
kernel:             <unknown>
architecture:       64 bit
endianess:          little endian
----------------------------------- GPU -----------------------------------
GPU 0:
  vendor:           NVIDIA
  model:            NVIDIA GeForce RTX 3070 Ti
  driverVersion:    31.0.15.2698
  memory [MiB]:     8190
  min frequency:    0
  cur frequency:    0
  max frequency:    0
----------------------------------- RAM -----------------------------------
vendor:             Corsair
model:              CMK32GX4M2Z3600C18
name:               Physical Memory
serial-number:      ***
size [MiB]:         65437
free [MiB]:         54405
available [MiB]:    54405
------------------------------- Main Board --------------------------------
vendor:             ASUSTeK COMPUTER INC.
name:               PRIME Z490-A
version:            Rev 1.xx
serial-number:      ***
------------------------------- Batteries ---------------------------------
No Batteries installed or detected
--------------------------------- Disks -----------------------------------
Disk 0:
  vendor:           (Standard disk drives)
  model:            WD_BLACK SN850 Heatsink 1TB
  serial-number:    ***.
  size:             1000202273280
Disk 1:
  vendor:           (Standard disk drives)
  model:            Intenso SSD Sata III
  serial-number:    ***
  size:             120031511040
Disk 2:
  vendor:           (Standard disk drives)
  model:            KINGSTON SA400S37240G
  serial-number:    ***
  size:             240054796800
Disk 3:
  vendor:           (Standard disk drives)
  model:            WDS500G3X0C-00SJG0
  serial-number:    ***.
  size:             500105249280
Disk 4:
  vendor:           (Standard disk drives)
  model:            ST750LM022 HN-M750MBB
  serial-number:    ***
  size:             750153761280
---------------------------------------------------------------------------

```
