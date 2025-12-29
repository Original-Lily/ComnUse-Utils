// main.go
package main

import (
	"flag"
	"fmt"
	"os"

	"GoScan/detect"
)

func main() {
	// Define command-line flags
	targetURL := flag.String("target", "", "Specify the target website for technology detection.")
	outputFormat := flag.String("output", "text", "Specify the output format (json, text).")
	help := flag.Bool("h", false, "Show this help message and exit.")

	// Parse command-line flags
	flag.Parse()

	// Display help message if requested
	if *help {
		flag.Usage()
		os.Exit(0)
	}

	// Check if a target URL is provided
	if *targetURL == "" {
		fmt.Println("Error: Please provide a target URL using the -target flag.")
		flag.Usage()
		os.Exit(1)
	}

	// Perform web technology detection
	result, err := detect.DetectWebTechnologies(*targetURL)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		os.Exit(1)
	}

	// Output result based on the specified format
	switch *outputFormat {
	case "json":
		fmt.Println("Output format: JSON")
		// Implement JSON output logic here (you can use encoding/json package)
		fmt.Println(result) // For now, just print the result in text format
	default:
		fmt.Println("Output format: Text")
		fmt.Println(result)
	}
}
