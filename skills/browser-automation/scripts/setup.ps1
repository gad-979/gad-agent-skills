#requires -Version 5
# Read-only availability check. Installation is a separate user decision.
$ErrorActionPreference = 'Stop'
foreach ($tool in @('node', 'npm', 'npx', 'agent-browser')) {
    $found = Get-Command $tool -ErrorAction SilentlyContinue
    if ($found) { Write-Output ($tool + ': available') }
    else { Write-Output ($tool + ': not found') }
}
Write-Output 'This check does not verify browser runtimes, connections, or desktop automation.'
