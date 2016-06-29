%define major 3
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Library for managing partitions
Name:		kpmcore
Version:	2.2.0
Release:	3
License:	GPLv3
Group:		System/Libraries
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/kpmcore/%{version}/src/%{name}-%{version}.tar.xz
# (tpg) from upstream git
Patch0:		0000-Make-sure-file-system-is-not-mounted-before-deleting.patch
Patch1:		0001-Whitespace-fixes.patch
Patch2:		0002-Fix-memory-leaks.patch
Patch3:		0003-Reduce-maximum-capacity-of-FAT16-file-systems-by-1-M.patch
Patch4:		0004-Also-reduce-max-capacity-for-ext2-and-ext3-file-syst.patch
Patch5:		0005-Adjust-maximum-capacity-for-fat32-jfs-and-reiserfs.patch
Patch6:		0006-Use-diskdev_cmds-instead-of-obsolete-hfsplusutils-fo.patch
Patch7:		0007-Also-check-whether-HFS-shrink-support-is-available.patch
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
Requires:	e2fsprogs
Requires:	xfsprogs
Requires:	jfsutils
Requires:	reiserfsprogs
Requires:	ntfs-3g
Requires:	dosfstools
Requires:	btrfs-progs
Requires:	f2fs-tools
Requires:	gptfdisk
Requires:	exfat-utils
Requires:	lvm2

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
%{_libdir}/lib*%{name}.so.%{version}

%files -n %{develname}
%dir %{_libdir}/cmake/KPMcore
%dir %{_includedir}/%{name}
%{_libdir}/cmake/KPMcore/*.cmake
%{_includedir}/%{name}/*
%{_libdir}/lib*%{name}.so
