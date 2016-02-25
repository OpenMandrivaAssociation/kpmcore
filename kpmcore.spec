%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Library for managing partitions
Name:		kpmcore
Version:	2.0.2
Release:	1
License:	GPLv3
Group:		System/Libraries
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/kpmcore/%{version}/src/%{name}-%{version}.tar.gz
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

%files
%{_qt5_plugindir}/*.so
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservicetypes5/*.desktop

%files -n %{libname}
%{_libdir}/lib*%{name}.so.%{major}*
# (tpg) wtf is this ?
%{_libdir}/lib*%{name}.so.2*

%files -n %{develname}
%dir %{_libdir}/cmake/KPMcore
%dir %{_includedir}/%{name}
%{_libdir}/cmake/KPMcore/*.cmake
%{_includedir}/%{name}/*
%{_libdir}/lib*%{name}.so
