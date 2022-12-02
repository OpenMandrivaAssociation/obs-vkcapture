Summary:	Free and open source plugin to allow recording/streaming in OBS as Vulkan or OpenGL game capture.
Name:		obs-vkcapture
Version:	1.2.2
Release:	1
License:	GPLv2.0
Group:		Video
Url:		https://github.com/nowrep/obs-vkcapture
Source0:	https://github.com/nowrep/obs-vkcapture/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

# Issue:    https://github.com/nowrep/obs-vkcapture/issues/23
Patch0:     fix-compilation-on-arm.patch

BuildRequires:	cmake ninja
BuildRequires:  pkgconfig(libobs)
BuildRequires:  vulkan-headers
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(opengl)
BuildRequires: glibc-static-devel

Requires: obs-studio
Requires: vulkan-loader

%description
Free and open source software for game capture in Vulkan and OpenGL in OBS-Studio.
This package is in the Restricted repository because it depend on OBS-Studio and OBS require x264 codec.
To use on X11 session you need to enable EGL. Like here: "OBS_USE_EGL=1 obs"
1. Add Game Capture to your OBS scene.
2. Start the game with capture enabled
-Vulkan
obs-vkcapture game
-OpenGL
obs-glcapture game

%prep
%autosetup -n %{name}-%{version} -p1
%cmake  \
    -DCMAKE_INSTALL_LIBDIR=%_lib \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/obs-gamecapture
%{_bindir}/obs-glcapture
%{_bindir}/obs-vkcapture
%{_libdir}/libVkLayer_obs_vkcapture.so
%{_libdir}/libobs_glcapture.so
%{_libdir}/obs-plugins/linux-vkcapture.so
%{_datadir}/vulkan/implicit_layer.d/obs_vkcapture_64.json
%{_datadir}/obs/obs-plugins/linux-vkcapture/locale/*-*.ini
