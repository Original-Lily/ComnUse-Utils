$root = Join-Path $PSScriptRoot 'images'
$manifestPath = Join-Path $PSScriptRoot 'images_manifest.json'

function Get-ImageManifest {
    param(
        [Parameter(Mandatory)][string]$Directory,
        [string]$RelativePath
    )

    $entries = @()
    $items = Get-ChildItem -LiteralPath $Directory | Sort-Object Name

    foreach ($item in $items) {
        if ($item.PSIsContainer) {
            $childRelative = if ($RelativePath) { "$RelativePath/$($item.Name)" } else { $item.Name }
            $entries += [pscustomobject]@{
                name     = $item.Name
                type     = 'folder'
                path     = "/images/$childRelative"
                children = Get-ImageManifest -Directory $item.FullName -RelativePath $childRelative
            }
            continue
        }

        $extension = $item.Extension.TrimStart('.').ToLower()
        switch ($extension) {
            'png'  { $label = 'PNG Image' }
            'jpg'  { $label = 'JPEG Image' }
            'jpeg' { $label = 'JPEG Image' }
            'gif'  { $label = 'GIF Image' }
            'svg'  { $label = 'SVG Asset' }
            default {
                if ($extension) { $label = "$($extension.ToUpper()) File" } else { $label = 'File' }
            }
        }

        $filePath = if ($RelativePath) { "/images/$RelativePath/$($item.Name)" } else { "/images/$($item.Name)" }

        $entries += [pscustomobject]@{
            name      = $item.Name
            type      = 'file'
            path      = $filePath
            extension = $label
            modified  = $item.LastWriteTime.ToString('MMM dd yyyy HH:mm')
        }
    }

    return $entries
}

if (-not (Test-Path $root)) {
    Write-Error "Images directory not found at $root"
    exit 1
}

$manifest = [pscustomobject]@{
    name     = 'images'
    type     = 'folder'
    path     = '/images'
    children = Get-ImageManifest -Directory $root -RelativePath ''
}

$manifest | ConvertTo-Json -Depth 100 | Set-Content -LiteralPath $manifestPath -Encoding UTF8
Write-Host "Updated manifest at $manifestPath"