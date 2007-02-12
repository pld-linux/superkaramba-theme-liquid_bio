%define		theme	liquid_bio

Summary:	superkaramba - liquid_bio theme
Summary(pl.UTF-8):	superkaramba - motyw liquid_bio
Name:		superkaramba-theme-%{theme}
Version:	0.1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://kde-look.org/content/files/23449-liquid_bio.tar.gz
# Source0-md5:	cadd07d52deb196f91d782e851d5e8e1
Patch0:		superkaramba-theme-liquid_bio.theme.patch
URL:		http://www.kde-look.org/content/show.php?content=23449
Requires:	superkaramba
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Based on bioramba by arutkowski
(http://www.kde-look.org/content/show.php?content=23437).
Shows one's biorhythm. I don't know if it's accurate :-)

%description -l pl.UTF-8
Bazuje na bioramba arutkowskiego
(http://www.kde-look.org/content/show.php?content=23437).
Pokazuje Twój biorytm. Nie wiem czy jest to wierne.


%prep
%setup -q -c
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_bio
install *.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_bio

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/superkaramba/liquid_bio
