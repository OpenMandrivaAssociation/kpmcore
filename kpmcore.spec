%define major 8
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Library for managing partitions
Name:		kpmcore
Version:	4.0.1
Release:	2
License:	GPLv3
Group:		System/Libraries
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/kpmcore/%{version}/src/%{name}-%{version}.tar.xz
Patch0:	https://git.stikonas.eu/andrius/kpmcore/commit/13beb9931951cf5972e341a871263146d2bdafbe.patch
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(blkid) >= 2.33.2
BuildRequires:	pkgconfig(libatasmart)
BuildRequires:	pkgconfig(libparted)
BuildRequires:	pkgconfig(Qt5Core) >= 5.3.0
BuildRequires:	pkgconfig(Qt5DBus) >= 5.3.0
BuildRequires:	pkgconfig(Qt5Gui) >= 5.3.0
BuildRequires:	pkgconfig(Qt5Widgets) >= 5.3.0
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(Qca-qt5)
Requires:	%{libname} = %{EVRD}

%description
Library for managing partitions.
Common code for KDE Partition Manager and other projects.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Requires:	%{_lib}qca2-plugin-openssl
Requires:	e2fsprogs
Requires:	dosfstools
Requires:	fatresize
Requires:	xfsprogs
Suggests:	jfsutils
Suggests:	reiserfsprogs
Suggests:	ntfs-3g
Requires:	btrfs-progs
Suggests:	f2fs-tools
Requires:	gptfdisk
Requires:	exfat-utils
Requires:	lvm2

%description -n %{libname}
Main library for %{name}.

%package -n %{develname}
Summary:	Development library for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{develname}
Development library for %{name}.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}

%files -f %{name}.lang
%{_qt5_plugindir}/*.so
%{_datadir}/dbus-1/system.d/org.kde.kpmcore.applicationinterface.conf
%{_datadir}/dbus-1/system.d/org.kde.kpmcore.externalcommand.conf
%{_datadir}/dbus-1/system.d/org.kde.kpmcore.helperinterface.conf
%{_libdir}/libexec/kauth/kpmcore_externalcommand
%{_datadir}/dbus-1/system-services/org.kde.kpmcore.externalcommand.service
%{_datadir}/polkit-1/actions/org.kde.kpmcore.externalcommand.policy

%files -n %{libname}
%{_libdir}/lib*%{name}.so.%{major}*
%{_libdir}/lib*%{name}.so.4.*

%files -n %{develname}
%dir %{_libdir}/cmake/KPMcore
%dir %{_includedir}/%{name}
%{_libdir}/cmake/KPMcore/*.cmake
%{_includedir}/%{name}/*
%{_libdir}/lib*%{name}.so
