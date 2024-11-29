cmake_minimum_required(VERSION 3.5)
project(py_srvcli)

# Gerekli bağımlılıkları ekle
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Mesaj ve servis dosyalarını işaretle
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/Triangle.srv"
  "msg/Dimensions.msg"
)

# Python paketini yükle
ament_python_install_package(${PROJECT_NAME})

# Yürütülebilir Python betiklerini yükle
install(
  PROGRAMS
  py_srvcli/server.py
  py_srvcli/client.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
