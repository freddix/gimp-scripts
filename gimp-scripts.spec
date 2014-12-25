Summary:	Set of GIMP scripts
Name:		gimp-scripts
Version:	41
Release:	1
License:	GPL/other
Group:		Applications
Source0:	http://www.gimphelp.org/DL/gimp_scripts-2.8.tar.bz2
# Source0-md5:	4d1444fb590271ff585a14340c1b2f65
BuildRequires:	gimp-devel
BuildArch:	noarch
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gimp_datadir	    %(gimptool --gimpdatadir)

%description
A set of verious and useful GIMP scripts.

%prep
%setup -qn gimp_scripts-2.8

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{gimp_datadir}/{scripts,gimpressionist/Presets,gradients/PictureFrames,patterns}

install *.scm $RPM_BUILD_ROOT%{gimp_datadir}/scripts
install gimpressionist/Presets/*.txt $RPM_BUILD_ROOT%{gimp_datadir}/gimpressionist/Presets
install gradients/PictureFrames/*.ggr $RPM_BUILD_ROOT%{gimp_datadir}/gradients/PictureFrames
install patterns/*.pat $RPM_BUILD_ROOT%{gimp_datadir}/patterns

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{gimp_datadir}/gimpressionist/Presets/*.txt
%{gimp_datadir}/gradients/PictureFrames
%{gimp_datadir}/patterns/*.pat
%{gimp_datadir}/scripts/*.scm

