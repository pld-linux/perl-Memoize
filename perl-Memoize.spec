%include	/usr/lib/rpm/macros.perl
Summary:	Memoize perl module
Summary(pl):	Modu³ perla Memoize
Name:		perl-Memoize
Version:	1.01
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Memoize/Memoize-%{version}.tar.gz
# Source0-md5:	8cf94cf8e9e24763ef7455c2bb0ad458
BuildRequires:	perl-devel >= 5.005_03-10
BuildRequires:	perl-Storable
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memoize - makes your functions faster by trading space for time.

%description -l pl
Memoize - umo¿liwia przyspieszenie wykonywania funkcji kosztem
przestrzeni.

%prep
%setup -q -n Memoize-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO *.html
%{perl_vendorlib}/Memoize.pm
%{perl_vendorlib}/Memoize
%{_mandir}/man3/*
