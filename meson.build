project(
  'hwinfo',
  'cpp',
  version: '1.0.0',
  default_options: [
    'cpp_std=c++17',
    'warning_level=3',
    'werror=true',
  ],
)

cpp = meson.get_compiler('cpp')

# The original CMake project builds either shared or static libraries.
# If both options are enabled, static takes precedence, matching the CMake logic.
build_shared = get_option('hwinfo_shared') and not get_option('hwinfo_static')

project_inc = include_directories('include')
generated_inc = include_directories('data')

common_args = ['-Wno-unknown-pragmas', '-Wno-overflow']
if host_machine.system() == 'windows'
  common_args += ['-DWIN32']
endif

if cpp.get_id() != 'msvc'
  add_project_arguments(common_args, language: 'cpp')
endif

if host_machine.system() == 'windows'
  if cpp.get_id() == 'msvc'
    add_project_arguments('/W4', '/WX', language: 'cpp')
  endif
endif

subdir('data')
subdir('src')

# Keep the convenient aggregate target from the CMake build as a Meson dependency.
# There is no physical "hwinfo" library: the original target is INTERFACE-only.
hwinfo_dep = declare_dependency(
  include_directories: project_inc,
  dependencies: component_deps,
)

if get_option('build_examples') or get_option('build_testing')
  subdir('examples')
endif

if get_option('build_testing')
  subdir('test')
endif

pkg = import('pkgconfig')
pkg.generate(
  name: 'hwinfo',
  description: 'Modern C++ API for retrieving hardware information',
  version: meson.project_version(),
  libraries: component_libs,
)
