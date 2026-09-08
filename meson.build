project('hwinfo', 
    'cpp',
    version: '1.0.0', 
    license: 'MIT',
    default_options: ['cpp_std=c++17']
)

subdir('data')
subdir('src')

hwinfo_dep = declare_dependency(
  include_directories: include_directories('include') 
)
