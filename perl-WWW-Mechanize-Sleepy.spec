%define real_name WWW-Mechanize-Sleepy

Summary:	WWW::Mechanize::Sleepy - A Sleepy Mechanize Agent
Name:		perl-%{real_name}
Version:	0.6
Release: %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/%{real_name}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Sometimes when testing the behavior of a webserver it is important
to be able to space out your requests in order to simulate a
person reading, thinking (or sleeping) at the keyboard.

WWW::Mechanize::Sleepy subclasses WWW::Mechanize to provide pauses
between your server requests. Use it just like you would use
WWW::Mechanize.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

# make test don't work...
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/WWW/Mechanize/Sleepy.pm
%{_mandir}/*/*

