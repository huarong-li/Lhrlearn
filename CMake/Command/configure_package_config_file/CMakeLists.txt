cmake_minimum_required(VERSION 2.8)

set(INCLUDE_INSTALL_DIR include/ CACHE PATH INSTALL_DIR)
set(LIB_INSTALL_DIR lib/ CACHE PATH LIB_INSTALL_DIR )
set(SYSCONFIG_INSTALL_DIR etc/foo/ CACHE PATH SYSCONFIG_INSTALL_DIR)

include(CMakePackageConfigHelpers)
configure_package_config_file(FooConfig.cmake.in
  ${CMAKE_CURRENT_BINARY_DIR}/FooConfig.cmake
  INSTALL_DESTINATION ${LIB_INSTALL_DIR}/Foo/cmake
  PATH_VARS INCLUDE_INSTALL_DIR SYSCONFIG_INSTALL_DIR LIB_INSTALL_DIR)
write_basic_package_version_file(
  ${CMAKE_CURRENT_BINARY_DIR}/FooConfigVersion.cmake
  VERSION 1.2.3
  COMPATIBILITY SameMajorVersion )
