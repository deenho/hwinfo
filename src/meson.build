component_libs = []
component_deps = []

hwinfo_inc = include_directories('..', '../include')

# Platform libraries used by the original CMake targets.
apple_frameworks = []
if host_machine.system() == 'darwin'
  apple_frameworks = [
    cpp.find_library('IOKit', required: true),
    cpp.find_library('CoreFoundation', required: true),
  ]
endif

win_ntdll = []
win_powrprof = []
win_dxgi = []
win_setupapi = []
win_wbem = []

if host_machine.system() == 'windows'
  win_ntdll = [cpp.find_library('ntdll', required: true)]
  win_powrprof = [cpp.find_library('powrprof', required: true)]
  win_dxgi = [cpp.find_library('dxgi', required: true)]
  win_setupapi = [cpp.find_library('setupapi', required: true)]
endif

# Helper: create a shared library when requested, otherwise a static library.
# Static mode intentionally wins if both hwinfo_shared and hwinfo_static are enabled.
# ----- BATTERY ---------------------------------------------------------------
if get_option('hwinfo_battery')
  battery_sources = files(
    'battery.cpp',
    'apple/battery.cpp',
    'linux/battery.cpp',
    'windows/battery.cpp',
    'windows/utils/wmi_wrapper.cpp',
  )

  battery_args = []
  if host_machine.system() == 'windows'
    if build_shared
      battery_args += ['-DHWINFO_EXPORTS']  
    else 
      battery_args += ['-DHWINFO_STATIC']
    endif
  endif

  if build_shared
    hwinfo_battery = shared_library('hwinfo_battery', battery_sources,
      cpp_args: battery_args,
      include_directories: hwinfo_inc,
      dependencies: apple_frameworks,
      install: true,
    )
  else
    hwinfo_battery = static_library('hwinfo_battery', battery_sources,
      cpp_args: battery_args,
      include_directories: hwinfo_inc,
      dependencies: apple_frameworks,
      install: true,
    )
  endif

  component_libs += [hwinfo_battery]
  component_deps += [declare_dependency(link_with: hwinfo_battery)]
  install_headers('../include/hwinfo/battery.h', subdir: 'hwinfo')
endif

# ----- CPU -------------------------------------------------------------------
if get_option('hwinfo_cpu')
  cpu_sources = files(
    'cpu.cpp',
    'apple/cpu.cpp',
    'linux/cpu.cpp',
    'windows/cpu.cpp',
    'windows/utils/wmi_wrapper.cpp',
    'apple/monitoring/cpu.cpp',
    'linux/monitoring/cpu.cpp',
    'windows/monitoring/cpu.cpp',
  )

  cpu_args = []
  if host_machine.system() == 'windows'
    if build_shared
      cpu_args += ['-DHWINFO_EXPORTS']
    else
      cpu_args += ['-DHWINFO_STATIC']
    endif
  endif

  cpu_deps = []
  if host_machine.system() == 'windows'
    cpu_deps += win_ntdll + win_powrprof
  endif

  if build_shared
    hwinfo_cpu = shared_library('hwinfo_cpu', cpu_sources,
      cpp_args: cpu_args,
      include_directories: hwinfo_inc,
      dependencies: cpu_deps,
      install: true,
    )
  else
    hwinfo_cpu = static_library('hwinfo_cpu', cpu_sources,
      cpp_args: cpu_args,
      include_directories: hwinfo_inc,
      dependencies: cpu_deps,
      install: true,
    )
  endif

  component_libs += [hwinfo_cpu]
  component_deps += [declare_dependency(link_with: hwinfo_cpu, dependencies: cpu_deps)]
  install_headers('../include/hwinfo/cpu.h', subdir: 'hwinfo')
  install_headers('../include/hwinfo/monitoring/monitor.h', '../include/hwinfo/monitoring/cpu.h', subdir: 'hwinfo/monitoring')
endif

# ----- DISK ------------------------------------------------------------------
if get_option('hwinfo_disk')
  disk_sources = files(
    'disk.cpp',
    'apple/disk.cpp',
    'linux/disk.cpp',
    'windows/disk.cpp',
    'windows/utils/wmi_wrapper.cpp',
    'apple/monitoring/disk.cpp',
    'linux/monitoring/disk.cpp',
    'windows/monitoring/disk.cpp',
  )

  disk_args = []
  if host_machine.system() == 'windows'
    if build_shared
      disk_args += ['-DHWINFO_EXPORTS']
    else
      disk_args += ['-DHWINFO_STATIC']
    endif
  endif

  if build_shared
    hwinfo_disk = shared_library('hwinfo_disk', disk_sources,
      cpp_args: disk_args,
      include_directories: hwinfo_inc,
      dependencies: apple_frameworks,
      install: true,
    )
  else
    hwinfo_disk = static_library('hwinfo_disk', disk_sources,
      cpp_args: disk_args,
      include_directories: hwinfo_inc,
      dependencies: apple_frameworks,
      install: true,
    )
  endif

  component_libs += [hwinfo_disk]
  component_deps += [declare_dependency(link_with: hwinfo_disk)]
  install_headers('../include/hwinfo/disk.h', subdir: 'hwinfo')
  install_headers('../include/hwinfo/monitoring/disk.h', subdir: 'hwinfo/monitoring')
endif

# ----- GPU -------------------------------------------------------------------
if get_option('hwinfo_gpu')
  gpu_sources = files(
    'gpu.cpp',
    'apple/gpu.cpp',
    'linux/gpu.cpp',
    'windows/gpu.cpp',
    'windows/utils/wmi_wrapper.cpp',
    'PCIMapper.cpp',
  )


  gpu_args = []
  gpu_deps = [generated_pci_dep]
  if host_machine.system() == 'windows'
    if build_shared
      gpu_args += ['-DHWINFO_EXPORTS']
    else
      gpu_args += ['-DHWINFO_STATIC']
    endif
    gpu_deps += win_dxgi + win_setupapi
  endif

  if get_option('hwinfo_gpu_opencl')
    subdir('opencl')
    gpu_args += ['-DUSE_OCL']
    gpu_deps += [opencl_device_dep]
  endif

  if build_shared
    hwinfo_gpu = shared_library('hwinfo_gpu', gpu_sources,
      cpp_args: gpu_args,
      include_directories: [hwinfo_inc, generated_inc],
      dependencies: gpu_deps,
      install: true,
    )
  else
    hwinfo_gpu = static_library('hwinfo_gpu', gpu_sources,
      cpp_args: gpu_args,
      include_directories: [hwinfo_inc, generated_inc],
      dependencies: gpu_deps,
      install: true,
    )
  endif

  component_libs += [hwinfo_gpu]
  gpu_public_args = []
  if get_option('hwinfo_gpu_opencl')
    gpu_public_args = ['-DUSE_OCL']
  endif
  component_deps += [declare_dependency(
    link_with: hwinfo_gpu,
    dependencies: gpu_deps,
    compile_args: gpu_public_args,
  )]
  install_headers('../include/hwinfo/gpu.h', subdir: 'hwinfo')
  if get_option('hwinfo_gpu_opencl')
    install_subdir('../include/hwinfo/opencl', install_dir: get_option('includedir') / 'hwinfo')
  endif
endif

# ----- MAINBOARD -------------------------------------------------------------
if get_option('hwinfo_mainboard')
  mainboard_sources = files(
    'mainboard.cpp',
    'apple/mainboard.cpp',
    'linux/mainboard.cpp',
    'windows/mainboard.cpp',
    'windows/utils/wmi_wrapper.cpp',
  )

  mainboard_args = []
  mainboard_deps = []
  if host_machine.system() == 'windows'
    if build_shared
      mainboard_args += ['-DHWINFO_EXPORTS'] 
    else 
      mainboard_args += ['-DHWINFO_STATIC']
    endif
    if host_machine.cpu_family() == 'x86'
      mainboard_deps += [cpp.find_library('wbemuuid', required: true)]
    endif
  endif

  if build_shared
    hwinfo_mainboard = shared_library('hwinfo_mainboard', mainboard_sources,
      cpp_args: mainboard_args,
      include_directories: hwinfo_inc,
      dependencies: mainboard_deps,
      install: true,
    )
  else
    hwinfo_mainboard = static_library('hwinfo_mainboard', mainboard_sources,
      cpp_args: mainboard_args,
      include_directories: hwinfo_inc,
      dependencies: mainboard_deps,
      install: true,
    )
  endif

  component_libs += [hwinfo_mainboard]
  component_deps += [declare_dependency(link_with: hwinfo_mainboard, dependencies: mainboard_deps)]
  install_headers('../include/hwinfo/mainboard.h', subdir: 'hwinfo')
endif

# ----- OS --------------------------------------------------------------------
if get_option('hwinfo_os')
  os_sources = files(
    'os.cpp',
    'apple/os.cpp',
    'linux/os.cpp',
    'windows/os.cpp',
    'windows/utils/wmi_wrapper.cpp',
  )

  os_args = []
  if host_machine.system() == 'windows'
    if build_shared
      os_args += ['-DHWINFO_EXPORTS'] 
    else 
      os_args += ['-DHWINFO_STATIC']
    endif
  endif

  if build_shared
    hwinfo_os = shared_library('hwinfo_os', os_sources,
      cpp_args: os_args,
      include_directories: hwinfo_inc,
      install: true,
    )
  else
    hwinfo_os = static_library('hwinfo_os', os_sources,
      cpp_args: os_args,
      include_directories: hwinfo_inc,
      install: true,
    )
  endif

  component_libs += [hwinfo_os]
  component_deps += [declare_dependency(link_with: hwinfo_os)]
  install_headers('../include/hwinfo/os.h', subdir: 'hwinfo')
endif

# ----- RAM -------------------------------------------------------------------
if get_option('hwinfo_ram')
  ram_sources = files(
    'ram.cpp',
    'apple/ram.cpp',
    'linux/ram.cpp',
    'windows/ram.cpp',
    'windows/utils/wmi_wrapper.cpp',
    'apple/monitoring/ram.cpp',
    'linux/monitoring/ram.cpp',
    'windows/monitoring/ram.cpp',
  )

  ram_args = []
  if host_machine.system() == 'windows'
    if build_shared
      ram_args += ['-DHWINFO_EXPORTS'] 
    else 
      ram_args += ['-DHWINFO_STATIC']
    endif
  endif

  if build_shared
    hwinfo_ram = shared_library('hwinfo_ram', ram_sources,
      cpp_args: ram_args,
      include_directories: hwinfo_inc,
      install: true,
    )
  else
    hwinfo_ram = static_library('hwinfo_ram', ram_sources,
      cpp_args: ram_args,
      include_directories: hwinfo_inc,
      install: true,
    )
  endif

  component_libs += [hwinfo_ram]
  component_deps += [declare_dependency(link_with: hwinfo_ram)]
  install_headers('../include/hwinfo/ram.h', subdir: 'hwinfo')
  install_headers('../include/hwinfo/monitoring/ram.h', subdir: 'hwinfo/monitoring')
endif

# ----- NETWORK ----------------------------------------------------------------
if get_option('hwinfo_network')
  network_sources = files(
    'network.cpp',
    'apple/network.cpp',
    'linux/network.cpp',
    'windows/network.cpp',
    'windows/utils/wmi_wrapper.cpp',
  )

  network_args = []
  if host_machine.system() == 'windows'
    if build_shared
      network_args += ['-DHWINFO_EXPORTS']
    else 
      network_args += ['-DHWINFO_STATIC']
    endif
  endif

  if build_shared
    hwinfo_network = shared_library('hwinfo_network', network_sources,
      cpp_args: network_args,
      include_directories: hwinfo_inc,
      install: true,
    )
  else
    hwinfo_network = static_library('hwinfo_network', network_sources,
      cpp_args: network_args,
      include_directories: hwinfo_inc,
      install: true,
    )
  endif

  component_libs += [hwinfo_network]
  component_deps += [declare_dependency(link_with: hwinfo_network)]
  install_headers('../include/hwinfo/network.h', subdir: 'hwinfo')
endif

install_headers(
  '../include/hwinfo/platform.h',
  '../include/hwinfo/hwinfo.h',
  subdir: 'hwinfo',
)
install_subdir('../include/hwinfo/utils', install_dir: get_option('includedir') / 'hwinfo')
