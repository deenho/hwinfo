# The upstream CMake test directory is intentionally empty. The actual test
# registered by CMake is the system_info example, so reproduce that behavior.
if get_option('build_testing')
  if get_option('build_examples')
    test('system_info', system_info)
  else
    system_info_test = executable(
      'system_info',
      '../examples/system_infoMain.cpp',
      dependencies: [hwinfo_dep],
    )
    test('system_info', system_info_test)
  endif
endif
