Summary:	Free and open source plugin to allow recording/streaming in OBS as Vulkan or OpenGL game capture.
Name:		obs-vkcapture
Version:	0.8.1
Release:	1
License:	GPLv2.0
Group:		Video
Url:		https://github.com/nowrep/obs-vkcapture
Source0:	https://github.com/nowrep/obs-vkcapture/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake ninja
BuildRequires:  pkgconfig(libobs)
BuildRequires:  vulkan-headers
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)

Requires: obs-studio
Requires: vulkan-loader

%description
Free and open source software for game capture in Vulkan and OpenGL in OBS-Studio.
This package is in the Restricted repository because it depend on OBS-Studio and OBS require x264 codec.

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
