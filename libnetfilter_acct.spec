%define major 1
%define libname %mklibname netfilter_acct %{major}
%define libnamedevel %mklibname netfilter_acct -d

Summary:	Netfilter extended accounting infrastructure library
Name:		libnetfilter_acct
Version:	1.0.1
Release:	1
Group:		System/Libraries
License:	GPL
URL:		http://www.netfilter.org/projects/libnetfilter_acct/index.html
Source0:	http://www.netfilter.org/projects/libnetfilter_acct/files/libnetfilter_acct-%{version}.tar.bz2
Source1:	http://www.netfilter.org/projects/libnetfilter_acct/files/libnetfilter_acct-%{version}.tar.bz2.sig
BuildRequires:	pkgconfig(libmnl) >= 1.0.0

%description
libnetfilter_acct is the userspace library providing interface to extended
accounting infrastructure.

%package -n %{libname}
Summary:	Netfilter extended accounting infrastructure library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Provides:	netfilter_acct = %{version}-%{release}

%description -n %{libname}
libnetfilter_acct is the userspace library providing interface to extended
accounting infrastructure.

%package -n %{libnamedevel}
Summary:        Development files for %{name}
Group:          System/Libraries
Provides:	netfilter_acct-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{libnamedevel}
This package contains the development files for %{name}.

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc COPYING README
%{_libdir}/*.so.%{major}*

%files -n %{libnamedevel}
%{_includedir}/libnetfilter_acct
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnetfilter_acct.pc



%changelog
* Mon Apr 16 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1
+ Revision: 791236
- import libnetfilter_acct


* Mon Apr 16 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1
- initial Mandriva package
