package main

import (
	"fmt"
	"math"
	"os"
	"path/filepath"
	"strings"
)

// ANSI color escape codes
const (
	colorReset  = "\033[0m"
	colorRed    = "\033[31m"
	colorGreen  = "\033[32m"
	colorYellow = "\033[33m"
	colorBlue   = "\033[34m"
	colorPurple = "\033[35m"
	colorCyan   = "\033[36m"
)

// VulnerabilityScore calculates the system's vulnerability score based on the number of vulnerable files found
func VulnerabilityScore(numVulnerableFiles int) float64 {
	const k = 0.1 // Decay constant
	return 100.0 * math.Exp(-k*float64(numVulnerableFiles))
}

func isPrimeTarget(filePath string) (bool, string) {
	// Define criteria for identifying prime targets
	primeExtensions := map[string]string{
		".conf":     colorRed,    // Configuration files
		".cfg":      colorRed,    // Configuration files
		".tar":      colorGreen,  // Archive files
		".gz":       colorGreen,  // Archive files
		".sql":      colorYellow, // Database files
		".mdb":      colorYellow, // Database files
		".db":       colorYellow, // Database files
		".log":      colorPurple, // Log files
		".rsa":      colorBlue,   // RSA encrypted key files
		".pub":      colorBlue,   // RSA encrypted key files
		".pem":      colorBlue,   // RSA encrypted key files
		".ppk":      colorBlue,   // PuTTY private key files
		".key":      colorBlue,   // SSH private key files
		".cer":      colorBlue,   // Certificate files
		".crt":      colorBlue,   // Certificate files
		".p12":      colorBlue,   // PKCS #12 files
		".pfx":      colorBlue,   // PKCS #12 files
		".jks":      colorBlue,   // Java KeyStore files
		".keystore": colorBlue,   // Java KeyStore files
	}

	// Check if file extension is in primeExtensions
	ext := strings.ToLower(filepath.Ext(filePath))
	if color, ok := primeExtensions[ext]; ok {
		return true, color
	}

	return false, ""
}

func scanDirectory(root string) (int, int) {
	numVulnerableFiles := 0
	numFilesScanned := 0

	filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			fmt.Println(err)
			return nil
		}
		if !info.IsDir() {
			numFilesScanned++
			if isVulnerable, color := isPrimeTarget(path); isVulnerable {
				numVulnerableFiles++
				relativePath := strings.TrimPrefix(path, root)
				relativePath = strings.TrimPrefix(relativePath, string(filepath.Separator)) // Remove leading directory separator
				fmt.Printf("%sPotential Vulnerable File: %s%s\n", color, relativePath, colorReset)
			}
		}
		return nil
	})

	return numVulnerableFiles, numFilesScanned
}

func main() {
	directory := "C:/Users/buddi/OneDrive/Desktop/Computer Science Revision/Home"
	numVulnerableFiles, numFilesScanned := scanDirectory(directory)

	vulnerabilityScore := VulnerabilityScore(numVulnerableFiles)
	fmt.Printf("\nScan Complete\nTotal Files Scanned: %d\nVulnerable Files Found: %d\nSystem Vulnerability Score: %.2f%%\n", numFilesScanned, numVulnerableFiles, vulnerabilityScore)
}
