# === Components =======================================================================================================
# ----- BATTERY --------------------------------------------------------------------------------------------------------
  battery_src_files = ['battery.cpp', 'apple/battery.cpp', 'linux/battery.cpp', 'windows/battery.cpp', 'windows/utils/wmi_wrapper.cpp']
  hwinfo_battery_lib = library('hwinfo_battery', battery_src_files)
# ______________________________________________________________________________________________________________________
# ----- CPU ------------------------------------------------------------------------------------------------------------
  cpu_src_files = ['cpu.cpp', 'apple/cpu.cpp', 'linux/cpu.cpp', 'windows/cpu.cpp', 'windows/utils/wmi_wrapper.cpp', 'apple/monitoring/cpu.cpp', 'linux/monitoring/cpu.cpp', 'windows/monitoring/cpu.cpp']
  hwinfo_cpu_lib = library('hwinfo_cpu', cpu_src_files)
# ______________________________________________________________________________________________________________________
# ----- DISK -----------------------------------------------------------------------------------------------------------
  disk_src_files = ['disk.cpp', 'apple/disk.cpp', 'linux/disk.cpp', 'windows/disk.cpp', 'windows/utils/wmi_wrapper.cpp', 'apple/monitoring/disk.cpp', 'linux/monitoring/disk.cpp', 'windows/monitoring/disk.cpp']
  hwinfo_disk_lib = library('hwinfo_disk', disk_src_files)
# ______________________________________________________________________________________________________________________
# ----- GPU ------------------------------------------------------------------------------------------------------------
  gpu_src_files = ['gpu.cpp', 'apple/gpu.cpp', 'linux/gpu.cpp', 'windows/gpu.cpp', 'windows/utils/wmi_wrapper.cpp', 'PCIMapper.cpp']
  hwinfo_gpu_lib = library('hwinfo_gpu', gpu_src_files)
# ______________________________________________________________________________________________________________________
# ----- Mainboard ------------------------------------------------------------------------------------------------------
  mainboard_src_files = ['mainboard.cpp', 'apple/mainboard.cpp', 'linux/mainboard.cpp', 'windows/mainboard.cpp', 'windows/utils/wmi_wrapper.cpp']
  hwinfo_mainboard_lib = library('hwinfo_mainboard', mainboard_src_files)
# ______________________________________________________________________________________________________________________
# ----- OS -------------------------------------------------------------------------------------------------------------
  os_src_files = ['os.cpp', 'apple/os.cpp', 'linux/os.cpp', 'windows/os.cpp', 'windows/utils/wmi_wrapper.cpp']
  hwinfo_os_lib = library('hwinfo_os', os_src_files)
# ______________________________________________________________________________________________________________________
# ----- RAM ------------------------------------------------------------------------------------------------------------
  ram_src_files = ['ram.cpp', 'apple/ram.cpp', 'linux/ram.cpp', 'windows/ram.cpp', 'windows/utils/wmi_wrapper.cpp', 'apple/monitoring/ram.cpp', 'linux/monitoring/ram.cpp', 'windows/monitoring/ram.cpp']
  hwinfo_ram_lib = library('hwinfo_ram', ram_src_files)
# ______________________________________________________________________________________________________________________
# ----- NETWORK --------------------------------------------------------------------------------------------------------
  network_src_files = ['network.cpp', 'apple/network.cpp', 'linux/network.cpp', 'windows/network.cpp', 'windows/utils/wmi_wrapper.cpp']
  hwinfo_network_lib = library('hwinfo_network', network_src_files)
# ______________________________________________________________________________________________________________________

hwinfo_src = ([
  battery_src_files,
  cpu_src_files,
  disk_src_files,
  gpu_src_files,
  mainboard_src_files,
  os_src_files,
  ram_src_files,
  network_src_files
])