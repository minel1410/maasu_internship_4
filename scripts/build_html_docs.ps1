Push-Location $pwd\docs\

# Removing apidoc-generated output dirs
Remove-Item source\apidoc -Recurse -Force -ErrorAction SilentlyContinue

# Running APIDOC
sphinx-apidoc.exe --module-first --implicit-namespaces --separate -f -o source\apidoc ..\src
if ($LASTEXITCODE -gt 0) { throw "Execution of sphinx-apidoc.exe failed" }

# Running CLEAN
.\make clean
if ($LASTEXITCODE -gt 0) { throw "Execution of .\make clean failed" }

# Building HTML
.\make html
if ($LASTEXITCODE -gt 0) { throw "Execution of .\make html failed" }

Pop-Location