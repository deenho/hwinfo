# ----- hwinfo ---------------------------------------------------------------------------------------------------------
hwinfo_lib = library('hwinfo', 'INTERFACE')
# target_include_directories(['hwinfo', 'INTERFACE', '$<BUILD_INTERFACE:${HWINFO_INCLUDE_DIR}>', '$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>'])
lfreist-hwinfo::hwinfo_lib = library('lfreist-hwinfo::hwinfo', 'ALIAS', 'hwinfo')
# set_target_properties(['hwinfo', 'PROPERTIES', 'OUTPUT_NAME', 'hwinfo'])
# function(['hwinfo_configure_api', 'target_name'])
if 'WIN32'
  if 'HWINFO_SHARED'
    # target_compile_definitions([target_name, 'PRIVATE', 'HWINFO_EXPORTS'])
  else
    # target_compile_definitions([target_name, 'PUBLIC', 'HWINFO_STATIC'])
  endif
endif
# endfunction()
# === Components =======================================================================================================
# ----- BATTERY --------------------------------------------------------------------------------------------------------
if 'HWINFO_BATTERY'
  battery_src_files = ['battery.cpp', 'apple/battery.cpp', 'linux/battery.cpp', 'windows/battery.cpp', 'windows/utils/wmi_wrapper.cpp']
  hwinfo_battery_lib = library('hwinfo_battery', battery_src_files)
  # hwinfo_configure_api('hwinfo_battery')
  # target_include_directories(['hwinfo_battery', 'PUBLIC', '$<BUILD_INTERFACE:${HWINFO_INCLUDE_DIR}>', '$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>'])
  if 'APPLE'
    # target_link_libraries(['hwinfo_battery', 'PRIVATE', '-framework IOKit', '-framework CoreFoundation'])
  endif
  # target_link_libraries(['hwinfo', 'INTERFACE', 'hwinfo_battery'])
  # set_target_properties(['hwinfo_battery', 'PROPERTIES', 'OUTPUT_NAME', 'hwinfo_battery'])
  # install(['TARGETS', 'hwinfo_battery', 'EXPORT', 'lfreist-hwinfoTargets', 'LIBRARY', 'DESTINATION', cmake_install_libdir, 'ARCHIVE', 'DESTINATION', 'lib', 'RUNTIME', 'DESTINATION', 'bin'])
  # install(['FILES', hwinfo_include_dir, '/hwinfo/battery.h', 'DESTINATION', cmake_install_includedir, '/hwinfo'])
endif
# ______________________________________________________________________________________________________________________
# ----- CPU ------------------------------------------------------------------------------------------------------------
if 'HWINFO_CPU'
  cpu_src_files = ['cpu.cpp', 'apple/cpu.cpp', 'linux/cpu.cpp', 'windows/cpu.cpp', 'windows/utils/wmi_wrapper.cpp', 'apple/monitoring/cpu.cpp', 'linux/monitoring/cpu.cpp', 'windows/monitoring/cpu.cpp']
  hwinfo_cpu_lib = library('hwinfo_cpu', hwinfo_build, cpu_src_files)
  # hwinfo_configure_api('hwinfo_cpu')
  # target_include_directories(['hwinfo_cpu', 'PUBLIC', '$<BUILD_INTERFACE:${HWINFO_INCLUDE_DIR}>', '$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>'])
  if 'WIN32'
    # target_link_libraries(['hwinfo_cpu', 'PRIVATE', 'ntdll', 'powrprof'])
  endif
  if 'MINGW'
    # target_link_libraries(['hwinfo_cpu', 'PUBLIC', 'PowrProf', 'ntdll'])
  endif
  # target_link_libraries(['hwinfo', 'INTERFACE', 'hwinfo_cpu'])
  # set_target_properties(['hwinfo_cpu', 'PROPERTIES', 'OUTPUT_NAME', 'hwinfo_cpu'])
  # install(['TARGETS', 'hwinfo_cpu', 'EXPORT', 'lfreist-hwinfoTargets', 'LIBRARY', 'DESTINATION', cmake_install_libdir, 'ARCHIVE', 'DESTINATION', 'lib', 'RUNTIME', 'DESTINATION', 'bin'])
  # install(['FILES', hwinfo_include_dir, '/hwinfo/cpu.h', 'DESTINATION', cmake_install_includedir, '/hwinfo'])
  # install(['FILES', hwinfo_include_dir, '/hwinfo/monitoring/monitor.h', hwinfo_include_dir, '/hwinfo/monitoring/cpu.h', 'DESTINATION', cmake_install_includedir, '/hwinfo/monitoring'])
endif
# ______________________________________________________________________________________________________________________
# ----- DISK -----------------------------------------------------------------------------------------------------------
if 'HWINFO_DISK'
  disk_src_files = ['disk.cpp', 'apple/disk.cpp', 'linux/disk.cpp', 'windows/disk.cpp', 'windows/utils/wmi_wrapper.cpp', 'apple/monitoring/disk.cpp', 'linux/monitoring/disk.cpp', 'windows/monitoring/disk.cpp']
  hwinfo_disk_lib = library('hwinfo_disk', hwinfo_build, disk_src_files)
  # hwinfo_configure_api('hwinfo_disk')
  # target_include_directories(['hwinfo_disk', 'PUBLIC', '$<BUILD_INTERFACE:${HWINFO_INCLUDE_DIR}>', '$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>'])
  if 'APPLE'
    # target_link_libraries(['hwinfo_disk', 'PRIVATE', '-framework IOKit', '-framework CoreFoundation'])
  endif
  # target_link_libraries(['hwinfo', 'INTERFACE', 'hwinfo_disk'])
  # set_target_properties(['hwinfo_disk', 'PROPERTIES', 'OUTPUT_NAME', 'hwinfo_disk'])
  # install(['TARGETS', 'hwinfo_disk', 'EXPORT', 'lfreist-hwinfoTargets', 'LIBRARY', 'DESTINATION', cmake_install_libdir, 'ARCHIVE', 'DESTINATION', 'lib', 'RUNTIME', 'DESTINATION', 'bin'])
  # install(['FILES', hwinfo_include_dir, '/hwinfo/disk.h', 'DESTINATION', cmake_install_includedir, '/hwinfo'])
  # install(['FILES', hwinfo_include_dir, '/hwinfo/monitoring/disk.h', 'DESTINATION', cmake_install_includedir, '/hwinfo/monitoring'])
endif
# ______________________________________________________________________________________________________________________
# ----- GPU ------------------------------------------------------------------------------------------------------------
if 'HWINFO_GPU'
  gpu_src_files = ['gpu.cpp', 'apple/gpu.cpp', 'linux/gpu.cpp', 'windows/gpu.cpp', 'windows/utils/wmi_wrapper.cpp', 'PCIMapper.cpp']
  if 'HWINFO_GPU_OPENCL'
    subdir('opencl')
  endif
  hwinfo_gpu_lib = library('hwinfo_gpu', hwinfo_build, gpu_src_files)
  # hwinfo_configure_api('hwinfo_gpu')
  if 'HWINFO_GPU_OPENCL'
    # target_compile_definitions(['hwinfo_gpu', 'PUBLIC', 'USE_OCL'])
    # target_link_libraries(['hwinfo_gpu', 'PRIVATE', 'opencl_device'])
  endif
  # target_include_directories(['hwinfo_gpu', 'PUBLIC', '$<BUILD_INTERFACE:${HWINFO_INCLUDE_DIR}>', '$<BUILD_INTERFACE:${HWINFO_CMAKE_BINARY_DIR}/generated>', '$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>'])
  # add_dependencies(['hwinfo_gpu', 'generate_pci_ids_header'])
  if 'WIN32'
    # target_link_libraries(['hwinfo_gpu', 'PRIVATE', 'dxgi', 'setupapi'])
  endif
  if 'MINGW'
    # target_link_libraries(['hwinfo_gpu', 'PUBLIC', 'dxgi', 'setupapi'])
  endif
  # target_link_libraries(['hwinfo', 'INTERFACE', 'hwinfo_gpu'])
  # set_target_properties(['hwinfo_gpu', 'PROPERTIES', 'OUTPUT_NAME', 'hwinfo_gpu'])
  # install(['TARGETS', 'hwinfo_gpu', 'EXPORT', 'lfreist-hwinfoTargets', 'LIBRARY', 'DESTINATION', cmake_install_libdir, 'ARCHIVE', 'DESTINATION', 'lib', 'RUNTIME', 'DESTINATION', 'bin'])
  # install(['FILES', hwinfo_include_dir, '/hwinfo/gpu.h', 'DESTINATION', cmake_install_includedir, '/hwinfo'])
  if 'HWINFO_GPU_OPENCL'
    # install(['DIRECTORY', hwinfo_include_dir, '/hwinfo/opencl', 'DESTINATION', cmake_install_includedir, '/hwinfo'])
  endif
endif
# ______________________________________________________________________________________________________________________
# ----- Mainboard ------------------------------------------------------------------------------------------------------
if 'HWINFO_MAINBOARD'
  mainboard_src_files = ['mainboard.cpp', 'apple/mainboard.cpp', 'linux/mainboard.cpp', 'windows/mainboard.cpp', 'windows/utils/wmi_wrapper.cpp']
  hwinfo_mainboard_lib = library('hwinfo_mainboard', hwinfo_build, mainboard_src_files)
  # hwinfo_configure_api('hwinfo_mainboard')
  # target_include_directories(['hwinfo_mainboard', 'PUBLIC', '$<BUILD_INTERFACE:${HWINFO_INCLUDE_DIR}>', '$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>'])
  if 'APPLE'
    # target_link_libraries(['hwinfo_mainboard', 'PRIVATE', '-framework IOKit', '-framework CoreFoundation'])
  endif
  if 'MINGW'
    # target_link_libraries(['hwinfo_mainboard', 'PUBLIC', 'wbemuuid'])
  endif
  # target_link_libraries(['hwinfo', 'INTERFACE', 'hwinfo_mainboard'])
  # set_target_properties(['hwinfo_mainboard', 'PROPERTIES', 'OUTPUT_NAME', 'hwinfo_mainboard'])
  # install(['TARGETS', 'hwinfo_mainboard', 'EXPORT', 'lfreist-hwinfoTargets', 'LIBRARY', 'DESTINATION', cmake_install_libdir, 'ARCHIVE', 'DESTINATION', 'lib', 'RUNTIME', 'DESTINATION', 'bin'])
  # install(['FILES', hwinfo_include_dir, '/hwinfo/mainboard.h', 'DESTINATION', cmake_install_includedir, '/hwinfo'])
endif
# ______________________________________________________________________________________________________________________
# ----- OS -------------------------------------------------------------------------------------------------------------
if 'HWINFO_OS'
  os_src_files = ['os.cpp', 'apple/os.cpp', 'linux/os.cpp', 'windows/os.cpp', 'windows/utils/wmi_wrapper.cpp']
  hwinfo_os_lib = library('hwinfo_os', hwinfo_build, os_src_files)
  # hwinfo_configure_api('hwinfo_os')
  # target_include_directories(['hwinfo_os', 'PUBLIC', '$<BUILD_INTERFACE:${HWINFO_INCLUDE_DIR}>', '$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>'])
  # target_link_libraries(['hwinfo', 'INTERFACE', 'hwinfo_os'])
  # set_target_properties(['hwinfo_os', 'PROPERTIES', 'OUTPUT_NAME', 'hwinfo_os'])
  # install(['TARGETS', 'hwinfo_os', 'EXPORT', 'lfreist-hwinfoTargets', 'LIBRARY', 'DESTINATION', cmake_install_libdir, 'ARCHIVE', 'DESTINATION', 'lib', 'RUNTIME', 'DESTINATION', 'bin'])
  # install(['FILES', hwinfo_include_dir, '/hwinfo/os.h', 'DESTINATION', cmake_install_includedir, '/hwinfo'])
endif
# ______________________________________________________________________________________________________________________
# ----- RAM ------------------------------------------------------------------------------------------------------------
if 'HWINFO_RAM'
  ram_src_files = ['ram.cpp', 'apple/ram.cpp', 'linux/ram.cpp', 'windows/ram.cpp', 'windows/utils/wmi_wrapper.cpp', 'apple/monitoring/ram.cpp', 'linux/monitoring/ram.cpp', 'windows/monitoring/ram.cpp']
  hwinfo_ram_lib = library('hwinfo_ram', hwinfo_build, ram_src_files)
  # hwinfo_configure_api('hwinfo_ram')
  # target_include_directories(['hwinfo_ram', 'PUBLIC', '$<BUILD_INTERFACE:${HWINFO_INCLUDE_DIR}>', '$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>'])
  # target_link_libraries(['hwinfo', 'INTERFACE', 'hwinfo_ram'])
  # set_target_properties(['hwinfo_ram', 'PROPERTIES', 'OUTPUT_NAME', 'hwinfo_ram'])
  # install(['TARGETS', 'hwinfo_ram', 'EXPORT', 'lfreist-hwinfoTargets', 'LIBRARY', 'DESTINATION', cmake_install_libdir, 'ARCHIVE', 'DESTINATION', 'lib', 'RUNTIME', 'DESTINATION', 'bin'])
  # install(['FILES', hwinfo_include_dir, '/hwinfo/ram.h', 'DESTINATION', cmake_install_includedir, '/hwinfo'])
  # install(['FILES', hwinfo_include_dir, '/hwinfo/monitoring/ram.h', 'DESTINATION', cmake_install_includedir, '/hwinfo/monitoring'])
endif
# ______________________________________________________________________________________________________________________
# ----- NETWORK --------------------------------------------------------------------------------------------------------
if 'HWINFO_NETWORK'
  network_src_files = ['network.cpp', 'apple/network.cpp', 'linux/network.cpp', 'windows/network.cpp', 'windows/utils/wmi_wrapper.cpp']
  hwinfo_network_lib = library('hwinfo_network', hwinfo_build, network_src_files)
  # hwinfo_configure_api('hwinfo_network')
  # target_include_directories(['hwinfo_network', 'PUBLIC', '$<BUILD_INTERFACE:${HWINFO_INCLUDE_DIR}>', '$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>'])
  # target_link_libraries(['hwinfo', 'INTERFACE', 'hwinfo_network'])
  # set_target_properties(['hwinfo_network', 'PROPERTIES', 'OUTPUT_NAME', 'hwinfo_network'])
  # install(['TARGETS', 'hwinfo_network', 'EXPORT', 'lfreist-hwinfoTargets', 'LIBRARY', 'DESTINATION', cmake_install_libdir, 'ARCHIVE', 'DESTINATION', 'lib', 'RUNTIME', 'DESTINATION', 'bin'])
  # install(['FILES', hwinfo_include_dir, '/hwinfo/network.h', 'DESTINATION', cmake_install_includedir, '/hwinfo'])
endif
# ______________________________________________________________________________________________________________________
# install(['FILES', hwinfo_include_dir, '/hwinfo/platform.h', hwinfo_include_dir, '/hwinfo/hwinfo.h', 'DESTINATION', cmake_install_includedir, '/hwinfo'])
# install(['DIRECTORY', hwinfo_include_dir, '/hwinfo/utils', 'DESTINATION', cmake_install_includedir, '/hwinfo'])
# install(['TARGETS', 'hwinfo', 'EXPORT', 'lfreist-hwinfoTargets', 'LIBRARY', 'DESTINATION', cmake_install_libdir, 'ARCHIVE', 'DESTINATION', 'lib', 'RUNTIME', 'DESTINATION', 'bin'])
