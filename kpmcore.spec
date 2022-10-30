%define major 12
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Library for managing partitions
Name:		kpmcore
Version:	22.08.2
Release:	2
License:	GPLv3
Group:		System/Libraries
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(PolkitQt5-1)
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
Requires:	f2fs-tools
Requires:	gptfdisk
Requires:	exfat-utils
Requires:	lvm2
Requires:	util-linux

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

%find_lang %{name} --all-name

%files -f %{name}.lang
%{_qt5_plugindir}/kpmcore
%{_libdir}/libexec/kpmcore_externalcommand
%{_datadir}/dbus-1/system-services/org.kde.kpmcore.helperinterface.service
%{_datadir}/dbus-1/system.d/org.kde.kpmcore.helperinterface.conf
%{_datadir}/polkit-1/actions/org.kde.kpmcore.externalcommand.policy

%files -n %{libname}
%{_libdir}/lib*%{name}.so.%{major}*
%{_libdir}/lib*%{name}.so.%(echo %{version}|cut -d. -f1).*

%files -n %{develname}
%dir %{_libdir}/cmake/KPMcore
%dir %{_includedir}/%{name}
%{_libdir}/cmake/KPMcore/*.cmake
%{_includedir}/%{name}/*
%{_libdir}/lib*%{name}.so
