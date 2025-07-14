#
# Conditional build:
%bcond_with	tests		# do perform "make test"

%define		pdir	FFI
Summary:	FFI - Perl Foreign Function Interface based on GNU ffcall
Name:		perl-FFI
Version:	1.10
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	2ec37468af2b5b820ec716ab557ddf58
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-xs.patch
URL:		http://search.cpan.org/dist/FFI/
BuildRequires:	ffcall-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a low-level foreign function interface to Perl.
It allows the calling of any function for which the user can supply
an address and calling signature. Furthermore, it provides a method
of encapsulating Perl subroutines as callback functions whose
addresses can be passed to C code.

%prep
%setup -q -n %{pdir}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md TODO
%{perl_vendorarch}/FFI.pm
%{perl_vendorarch}/FFI/Library.pm
%attr(755,root,root) %{perl_vendorarch}/auto/FFI/*.so
%{_mandir}/man3/*.3pm*
