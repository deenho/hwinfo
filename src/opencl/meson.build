message('Using OpenCL for GPU information...')

opencl_dep = dependency('OpenCL', required: true)

opencl_sources = files('device.cpp')
opencl_args = []
if host_machine.system() == 'windows'
  opencl_args += ['-DHWINFO_EXPORTS'] if build_shared else ['-DHWINFO_STATIC']
endif

opencl_device = static_library('opencl_device', opencl_sources,
  cpp_args: opencl_args,
  include_directories: include_directories('../../include'),
  dependencies: [opencl_dep],
  install: false,
)

opencl_device_dep = declare_dependency(
  link_with: opencl_device,
  dependencies: [opencl_dep],
)
