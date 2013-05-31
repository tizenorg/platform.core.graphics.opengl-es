%ifarch %{ix86}
%define PKGPATH "pkgconfig_i686"
%else
%define PKGPATH "pkgconfig_arm"
%endif

Name:       opengl-es
Summary:    Meta Package for the OpenGL ES library
Version:    0.1.1
Release:    4
Group:      Graphics/Library
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
%ifarch %{ix86}
Requires:   simulator-opengl
%else
Requires:   opengl-es-drv
%endif


%description
metapackage for the OpenGL ES library
 This is a meta package that will point to the latest OpenGL ES driver.
 .
 It does not provide any drivers itself..

%package devel
Summary:    Meta Package for development files of the OpenGL ES library
Group:      Development/Graphics
Requires:   %{name} = %{version}-%{release}

%ifarch %{ix86}
Requires:   simulator-opengl-devel
%else
Requires:   opengl-es-drv-devel
%endif

%description devel
metapackage for development files of the OpenGL ES library
 This is a meta package that will point to the latest development libraries,
 header files needed by programs that want to compile with OpenGL ES.
 .
 It does not provide any development files itself..



%prep
%setup -q


%build


%install

mkdir -p %{buildroot}%{_libdir}/pkgconfig
cp -a ./%{PKGPATH}/*.pc %{buildroot}%{_libdir}/pkgconfig/


%files
%license LICENSE
%manifest opengl-es.manifest
%defattr(-,root,root,-)

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/opengl-es-11.pc
%{_libdir}/pkgconfig/opengl-es-20.pc
