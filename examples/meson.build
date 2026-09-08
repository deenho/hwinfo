if get_option('build_examples')
  system_info = executable(
    'system_info',
    'system_infoMain.cpp',
    dependencies: [hwinfo_dep],
    install: true,
  )

  live_monitor = executable(
    'live_monitor',
    'live_monitorMain.cpp',
    dependencies: [hwinfo_dep],
    install: true,
  )
endif
