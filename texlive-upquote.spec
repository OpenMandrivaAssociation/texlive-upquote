# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/upquote/upquote.sty
# catalog-date 2009-10-10 17:55:02 +0200
# catalog-license lppl1.2
# catalog-version v1.1
Name:		texlive-upquote
Version:	v1.1
Release:	1
Summary:	Show "realistic" quotes in verbatim
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/upquote/upquote.sty
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/upquote.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Computer Modern Typewriter is the best font for program
listings, but it prints ` and ' as bent opening and closing
single quotes. Other fonts, and most programming languages,
print ` as a grave accent and ' upright; ' is used both to open
and to close quoted strings. This package switches the
typewriter font to Computer Modern Typewriter (regardless of
other fonts in use, so long as this package is called
afterward) and modifies the behavior of verbatim, verbatim*,
verb, and verb* to print ` and ' the desired way. The package
does not affect \tt, \texttt, etc.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/upquote/upquote.sty
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
