from conans import ConanFile, CMake, tools


class FreeImage(ConanFile):
    name = "freeimage"
    version = "3.17.0"
    license = "https://github.com/fanxiaochen/freeimage-cmake/blob/master/license-fi.txt"
    url = "https://github.com/fanxiaochen/freeimage-cmake.git"
    homepage = "https://github.com/fanxiaochen/freeimage-cmake"
    description = "FreeImage is an Open Source library project for developers who would like to support popular graphics image formats like PNG, BMP, JPEG, TIFF and others as needed by today's multimedia applications."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=False"
    generators = "cmake"

    def configure(self):
        if self.settings.os == "Windows":
            self.options.remove("fPIC")

    def source(self):
        git = tools.Git()
        git.clone("{}.git".format(self.homepage))

    def build(self):
        cmake = CMake(self)
        cmake.configure( source_folder=".")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.h", dst="include", src="FreeImage.h")
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.libs = ["freeimage"]
