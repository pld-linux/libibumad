Summary:	Userspace InfiniBand MAD library
Summary(pl.UTF-8):	Biblioteka InfiniBand MAD dla przestrzeni użytkownika
Name:		libibumad
Version:	1.3.10.1
Release:	2
License:	BSD or GPL v2
Group:		Libraries
Source0:	https://www.openfabrics.org/downloads/management/%{name}-%{version}.tar.gz
# Source0-md5:	2fa06c98f025f2153621d66b16203405
URL:		https://www.openfabrics.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libibumad provides the user MAD library functions which sit on top of
the user MAD modules in the kernel. These are used by the IB
diagnostic and management tools, including OpenSM.

%description -l pl.UTF-8
libibumad to biblioteka udostępniająca funkcje MAD w przestrzeni
użytkownika, komunikująca się z modułami MAD w jądrze. Jest używana
przez narzędzia diagnostyczne oraz zarządzające IB, w tym OpenSM.

%package devel
Summary:	Header files for libibumad library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libibumad
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
# for dir and other IB functionality
Requires:	libibverbs-devel

%description devel
Header files for libibumad library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libibumad.

%package static
Summary:	Static libibumad library
Summary(pl.UTF-8):	Statyczna biblioteka libibumad
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static libibumad library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę libibumad.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libibumad.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibumad.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibumad.so
%{_libdir}/libibumad.la
%{_includedir}/infiniband/umad.h
%{_includedir}/infiniband/umad_*.h
%{_mandir}/man3/umad_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libibumad.a
