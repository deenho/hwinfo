    # message('Using OpenCL for GPU information...')
    OpenCLHeaders_dep = dependency('OpenCLHeaders')
    if 'OpenCLHeaders_FOUND'
      OpenCLHeadersCpp_dep = dependency('OpenCLHeadersCpp')
      OpenCLICDLoader_dep = dependency('OpenCLICDLoader')
    else
      opencl_sdk_build_samples = ['OFF', 'CACHE', 'BOOL', '', 'FORCE']
      # fetchcontent_declare(['opencl', 'GIT_REPOSITORY', 'https://github.com/KhronosGroup/OpenCL-SDK.git', 'GIT_TAG', 'v2023.04.17'])
      # fetchcontent_makeavailable('opencl')
    endif
    opencl_device_lib = static_library('opencl_device', 'device.cpp')
    # hwinfo_configure_api('opencl_device')
    # target_include_directories(['opencl_device', 'PUBLIC', project_source_dir, '/include'])
    # target_link_libraries(['opencl_device', 'PUBLIC', 'OpenCL::HeadersCpp', 'OpenCL::OpenCL'])
