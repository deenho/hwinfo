# Generate the same C/C++ byte-array header that data/embed.cmake produced.
py = import('python').find_installation('python3', required: true)

pci_ids_header = custom_target(
  'pci_ids_header',
  input: 'pci.ids',
  output: 'pci.ids.h',
  command: [py, files('embed.py'), '@INPUT@', '@OUTPUT@', 'pci_ids'],
  depend_files: files('embed.py'),
  build_by_default: true,
)

# The generated header is consumed by src/PCIMapper.cpp.
generated_pci_dep = declare_dependency(
  include_directories: include_directories('.'),
  sources: pci_ids_header,
)
