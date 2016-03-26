%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Library for managing partitions
Name:		kpmcore
Version:	2.1.1
Release:	1
License:	GPLv3
Group:		System/Libraries
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/kpmcore/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(blkid)
BuildRequires:	pkgconfig(libatasmart)
BuildRequires:	pkgconfig(libparted)
BuildRequires:	pkgconfig(Qt5Core) >= 5.3.0
BuildRequires:	pkgconfig(Qt5Gui) >= 5.3.0
BuildRequires:	pkgconfig(Qt5Widgets) >= 5.3.0
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Service)
Requires:	%{libname} = %{EVRD}
Requires:	parted
Requires:       e2fsprogs
Requires:       xfsprogs
Requires:       jfsutils
Requires:       reiserfsprogs
Requires:       ntfs-3g
Requires:       dosfstools
Requires:       btrfs-progs
Requires:       f2fs-tools
Requires:       gptfdisk
Requires:       exfat-utils
Requires:       lvm2

%description
Library for managing partitions.
Common code for KDE Partition Manager and other projects.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Main library for %{name}

%package -n %{develname}
Summary:	Development library for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{develname}
Development library for %{name}

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}

%files -f %{name}.lang
%{_qt5_plugindir}/*.so
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservicetypes5/*.desktop

%files -n %{libname}
%{_libdir}/lib*%{name}.so.%{major}*

%files -n %{develname}
%dir %{_libdir}/cmake/KPMcore
%dir %{_includedir}/%{name}
%{_libdir}/cmake/KPMcore/*.cmake
%{_includedir}/%{name}/*
%{_libdir}/lib*%{name}.so
