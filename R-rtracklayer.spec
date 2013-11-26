%define		packname	rtracklayer

Summary:	R interface to genome browsers and their annotation tracks
Name:		R-%{packname}
Version:	1.22.0
Release:	1
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	1dad994b4779769e935902e9c8384959
Patch0:		bogus-deps.patch
URL:		http://www.bioconductor.org/packages/release/bioc/html/rtracklayer.html
BuildRequires:	R
BuildRequires:	R-GenomicRanges >= 1.11.12
BuildRequires:	R-BSgenome
BuildRequires:	R-Rsamtools-devel >= 1.7.3
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-GenomicRanges >= 1.11.12
Requires:	R-BSgenome
Requires:	R-Rsamtools >= 1.7.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extensible framework for interacting with multiple genome browsers
(currently UCSC built-in) and manipulating annotation tracks in
various formats (currently GFF, BED, bedGraph, BED15, WIG, BigWig
and 2bit built-in). The user may export/import tracks to/from
the supported browsers, as well as query and modify the browser
state, such as the current viewport.

%prep
%setup -q -c -n %{packname}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/CITATION
%doc %{_libdir}/R/library/%{packname}/NEWS
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/notes
%dir %{_libdir}/R/library/%{packname}
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/demo
%{_libdir}/R/library/%{packname}/tests
%{_libdir}/R/library/%{packname}/unitTests
%{_libdir}/R/library/%{packname}/scripts
%{_libdir}/R/library/%{packname}/extdata
%dir %{_libdir}/R/library/%{packname}/libs
%attr(755,root,root) %{_libdir}/R/library/%{packname}/libs/%{packname}.so
