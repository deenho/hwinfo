project('hwinfo', 'version', '1.0.0', 'languages', 'cpp', default_options : ['default_library=static'])
cmake_cxx_standard = '17'
if 'WIN32'
  # add_definitions('-DWIN32')
  cmake_windows_export_all_symbols = 'ON'
endif
if 'MSVC'
  # add_compile_options(['/W4', '/WX'])
else
  # add_compile_options(['-Wall', '-Wextra', '-Wpedantic', '-Wno-unknown-pragmas', '-Wno-overflow'])
endif
if 'NOT', 'HWINFO_CMAKE_BINARY_DIR'
  hwinfo_cmake_binary_dir = cmake_binary_dir
endif
cmake_library_output_directory = hwinfo_cmake_binary_dir
cmake_runtime_output_directory = hwinfo_cmake_binary_dir
# string(['COMPARE', 'EQUAL', '${CMAKE_SOURCE_DIR}', '${CMAKE_CURRENT_SOURCE_DIR}', 'PROJECT_IS_TOP_LEVEL'])
# Components
if 'NOT', 'HWINFO_STATIC', 'AND', 'HWINFO_SHARED'
  build_shared_libs = 'ON'
else
  build_shared_libs = 'OFF'
endif
subdir('data')
hwinfo_include_dir = '${CMAKE_CURRENT_SOURCE_DIR}/include'
subdir('src')
# write_basic_package_version_file(['${CMAKE_CURRENT_BINARY_DIR}/lfreist-hwinfoConfigVersion.cmake', 'VERSION', project_version, 'COMPATIBILITY', 'AnyNewerVersion'])
# configure_file(['cmake/lfreist-hwinfoConfig.cmake.in', '${CMAKE_CURRENT_BINARY_DIR}/lfreist-hwinfoConfig.cmake', '@ONLY'])
# install(['FILES', '${CMAKE_CURRENT_BINARY_DIR}/lfreist-hwinfoConfig.cmake', '${CMAKE_CURRENT_BINARY_DIR}/lfreist-hwinfoConfigVersion.cmake', 'DESTINATION', cmake_install_libdir, '/cmake/hwinfo'])
# install(['EXPORT', 'lfreist-hwinfoTargets', 'FILE', 'lfreist-hwinfoTargets.cmake', 'NAMESPACE', 'lfreist-hwinfo::', 'DESTINATION', cmake_install_libdir, '/cmake/hwinfo'])
if 'BUILD_EXAMPLES', 'OR', 'BUILD_TESTING'
  subdir('examples')
endif
if 'BUILD_TESTING'
  subdir('test')
  test('system_info', 'system_info')
endif
