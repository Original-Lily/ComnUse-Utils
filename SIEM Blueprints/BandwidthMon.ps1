$interface = "Ethernet"

while ($true) {
    $networkInterface = Get-NetAdapter | Where-Object { $_.Name -eq $interface -and $_.Status -eq 'Up' }
    if ($networkInterface) {
        try {
            $stats = $networkInterface | Get-NetAdapterStatistics
            $bytesSent = $stats.BytesSentPerSec
            $bytesReceived = $stats.BytesReceivedPerSec
            Write-Host "Current bandwidth usage on ${interface}: Sent: $($bytesSent/1KB) KB/s, Received: $($bytesReceived/1KB) KB/s"
        } catch {
            Write-Host "Error retrieving network statistics for interface '$interface': $_"
        }
    } else {
        Write-Host "Network interface '$interface' not found or not connected."
    }
    Start-Sleep -Seconds 5 
}
