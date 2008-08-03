%define name xmms-mad
%define version 0.10
%define release %mkrel 6

Summary: XMMS MPEG audio input plugin based on MAD
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/xmms-mad/%{name}-%{version}.tar.bz2
License: GPL
Group: Sound
URL:   http://xmms-mad.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: xmms
BuildRequires: libxmms-devel 
BuildRequires: mad-devel >= 0.14.2b-4mdk
BuildRequires: libid3tag-devel

%description
xmms-mad is an input plugin for xmms (http://www.xmms.org/) that uses
libmad (http://mad.sourceforge.net/) to decode MPEG layer 1/2/3 file
and streams.

Current features include:
 * local mp3 file playback
 * shoutchast/icecast stream playback
 * ID3 tag parsing
 * play time calculation (slow)
 * http header parsing

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%if %_lib != lib
mv %buildroot%_prefix/lib %buildroot%_libdir
%endif
rm -f %buildroot%{_libdir}/xmms/Input/libxmmsmad.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_libdir}/xmms/Input/libxmmsmad.so


