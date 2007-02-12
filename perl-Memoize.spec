#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Memoize perl module
Summary(pl.UTF-8):   Moduł Perla Memoize
Name:		perl-Memoize
Version:	1.01
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Memoize/Memoize-%{version}.tar.gz
# Source0-md5:	8cf94cf8e9e24763ef7455c2bb0ad458
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreq	'perl(NDBM_File)'

%description
Memoize - makes your functions faster by trading space for time.

%description -l pl.UTF-8
Memoize - umożliwia przyspieszenie wykonywania funkcji kosztem
przestrzeni.

%prep
%setup -q -n Memoize-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO *.html
%{perl_vendorlib}/Memoize.pm
%{perl_vendorlib}/Memoize
%{_mandir}/man3/*
