%include	/usr/lib/rpm/macros.perl
Summary:	Memoize perl module
Summary(pl):	Modu� perla Memoize
Name:		perl-Memoize
Version:	0.52
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Memoize/Memoize-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memoize - makes your functions faster by trading space for time.

%description -l pl
Memoize - umo�liwia przyspieszenie wykonywania funkcji kosztem
przestrzeni.

%prep
%setup -q -n Memoize-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO WHATSNEW

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Memoize.pm
%{perl_sitelib}/Memoize
%{perl_sitelib}/demo.pl
%{perl_sitelib}/demo2.pl
%{_mandir}/man3/*
