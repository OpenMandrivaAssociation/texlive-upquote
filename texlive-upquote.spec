Name:		texlive-upquote
Version:	1.3
Release:	3
Summary:	Show "realistic" quotes in verbatim
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/upquote
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/upquote.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/upquote.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/upquote.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Typewriter-style fonts are best for program listings, but
Computer Modern Typewriter prints ` and ' as bent opening and
closing single quotes. Other fonts, and most programming
languages, print ` as a grave accent and ' upright; ' is used
both to open and to close quoted strings. The package switches
the typewriter font to Computer Modern Typewriter in OT1
encoding, and modifies the behaviour of verbatim, verbatim*,
\verb, and \verb* to print in the "` and ' way". It does
thisregardless of other fonts or encodings in use, so long as
the package is loaded after the other fonts were. The package
does not affect \tt, \texttt, etc.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/upquote/upquote.sty
%doc %{_texmfdistdir}/doc/latex/upquote/README
%doc %{_texmfdistdir}/doc/latex/upquote/upquote.pdf
#- source
%doc %{_texmfdistdir}/source/latex/upquote/upquote.dtx
%doc %{_texmfdistdir}/source/latex/upquote/upquote.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
