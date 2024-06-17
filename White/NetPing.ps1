$subnet = "192.168.1"
$startRange = 1
$endRange = 254

for ($i = $startRange; $i -le $endRange; $i++) {
    $ip = "$subnet.$i"
    $result = Test-Connection -ComputerName $ip -Count 1 -Quiet
    if ($result) {
        Write-Host "Host $ip is online."
    } else {
        Write-Host "Host $ip is offline."
    }
}
