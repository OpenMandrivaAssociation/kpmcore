%define major 12
%define libname %mklibname %{name}-kf6
%define devname %mklibname %{name}-kf6 -d
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Library for managing partitions
Name:		plasma6-kpmcore
Version:	24.01.75
Release:	%{?git:0.%{git}.}1
License:	GPLv3
Group:		System/Libraries
Url:		https://www.kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/system/kpmcore/-/archive/master/kpmcore-master.tar.bz2#/kpmcore-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kpmcore-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(blkid) >= 2.33.2
BuildRequires:	qt6-qtbase-tools
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(PolkitQt6-1)
Requires:	%{libname} = %{EVRD}
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
Requires:	exfatprogs
Requires:	lvm2
Requires:	util-linux
Requires:	systemd
Requires:	coreutils
Requires:	smartmontools
Requires:	mdadm
Requires:	udftools

%description
Library for managing partitions.
Common code for KDE Partition Manager and other projects.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
Main library for %{name}.

%package -n %{devname}
Summary:	Development library for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development library for %{name}.

%prep
%autosetup -p1 -n kpmcore-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name

%files -f %{name}.lang
%{_qtdir}/plugins/kpmcore
%{_libdir}/libexec/kpmcore_externalcommand
%{_datadir}/dbus-1/system-services/org.kde.kpmcore.helperinterface.service
%{_datadir}/dbus-1/system.d/org.kde.kpmcore.helperinterface.conf
%{_datadir}/polkit-1/actions/org.kde.kpmcore.externalcommand.policy

%files -n %{libname}
%{_libdir}/libkpmcore.so.%{major}*
%{_libdir}/libkpmcore.so.%(echo %{version}|cut -d. -f1).*

%files -n %{devname}
%{_includedir}/kpmcore
%{_libdir}/libkpmcore.so
%{_libdir}/cmake/KPMcore
