// detect/detect.go
package detect

import (
	"fmt"
	"net/http"
	"strings"
	"time"

	"github.com/PuerkitoBio/goquery"
)

// PerformanceMetrics struct to hold performance-related information
type PerformanceMetrics struct {
	NumRequests int
	TotalSize   int64
}

// DetectWebTechnologies performs web technology detection and analysis
func DetectWebTechnologies(target string) (string, error) {
	startTime := time.Now()

	// Example: Fetch the HTML content of the target website
	response, err := http.Get(target)
	if err != nil {
		return "", fmt.Errorf("failed to fetch website: %v", err)
	}
	defer response.Body.Close()

	// Parse HTML using goquery
	doc, err := goquery.NewDocumentFromReader(response.Body)
	if err != nil {
		return "", fmt.Errorf("failed to parse HTML: %v", err)
	}

	// Extract the website title
	title := doc.Find("title").Text()

	// Extract the web server information
	server := response.Header.Get("Server")

	// Extract the IP address information
	ipAddress := extractIPAddress(response.Request.Host)

	// Extract and list all meta tags
	var metaTags []string
	doc.Find("head meta").Each(func(i int, s *goquery.Selection) {
		metaTag := s.AttrOr("name", "") + ": " + s.AttrOr("content", "")
		metaTags = append(metaTags, metaTag)
	})

	// Extract and list all scripts
	var scripts []string
	doc.Find("script[src]").Each(func(i int, s *goquery.Selection) {
		script := s.AttrOr("src", "")
		if script != "" {
			scripts = append(scripts, script)
		}
	})

	// Extract and list all linked CSS files
	var cssFiles []string
	doc.Find("link[rel=stylesheet]").Each(func(i int, s *goquery.Selection) {
		cssFile := s.AttrOr("href", "")
		if cssFile != "" {
			cssFiles = append(cssFiles, cssFile)
		}
	})

	// Perform CSS analysis to detect frameworks
	cssFrameworks := detectCSSFrameworks(cssFiles)

	// Perform JavaScript analysis to detect frameworks
	jsFrameworks := detectJavaScriptFrameworks(scripts)

	// Calculate performance metrics
	performanceMetrics := calculatePerformanceMetrics(response)

	elapsedTime := time.Since(startTime).Milliseconds()

	// Construct the result string with formatted sections
	result := fmt.Sprintf("Website: %s\nTitle: %s\nWeb Server: %s\nIP Address: %s\n\nMeta Tags:\n%s\n\nScripts:\n%s\nCSS Files:\n%s\n\nCSS Frameworks:\n%s\nJavaScript Frameworks:\n%s\n\nPerformance Metrics:\nRequests: %d\nTotal Size: %s\nElapsed Time: %d ms",
		target, title, server, ipAddress, formatList(metaTags), formatList(scripts), formatList(cssFiles), formatList(cssFrameworks), formatList(jsFrameworks), performanceMetrics.NumRequests, formatTotalSize(performanceMetrics.TotalSize), elapsedTime)

	return result, nil
}

// Helper function to calculate performance metrics
func calculatePerformanceMetrics(response *http.Response) PerformanceMetrics {
	var metrics PerformanceMetrics

	// Count the number of requests
	metrics.NumRequests = 1 // Initial request

	// Calculate the total size of resources
	metrics.TotalSize = response.ContentLength

	// Example: You can extend this function to iterate through resources and calculate more detailed metrics

	return metrics
}

// Helper function to format a list of strings with newlines
func formatList(items []string) string {
	return strings.Join(items, "\n")
}

// Helper function to format the total size
func formatTotalSize(size int64) string {
	if size == -1 {
		return "Unknown"
	}
	return fmt.Sprintf("%d bytes", size)
}

// Helper function to extract IP address from the given hostname
func extractIPAddress(hostname string) string {
	// Example: Split the hostname to extract the IP address
	parts := strings.Split(hostname, ":")
	return parts[0]
}

// Helper function to detect CSS frameworks
func detectCSSFrameworks(cssFiles []string) []string {
	var cssFrameworks []string
	for _, cssFile := range cssFiles {
		if strings.Contains(cssFile, "bootstrap") {
			cssFrameworks = append(cssFrameworks, "Bootstrap")
		} else if strings.Contains(cssFile, "foundation") {
			cssFrameworks = append(cssFrameworks, "Foundation")
		} else if strings.Contains(cssFile, "bulma") {
			cssFrameworks = append(cssFrameworks, "Bulma")
		} else if strings.Contains(cssFile, "tailwind") {
			cssFrameworks = append(cssFrameworks, "Tailwind CSS")
		} else if strings.Contains(cssFile, "materialize") {
			cssFrameworks = append(cssFrameworks, "Materialize")
		}
		// Example: if strings.Contains(cssFile, "bulma") { cssFrameworks = append(cssFrameworks, "Bulma") }
		// ...

	}
	return cssFrameworks
}

// Helper function to detect JavaScript frameworks
func detectJavaScriptFrameworks(scripts []string) []string {
	var jsFrameworks []string
	for _, script := range scripts {
		if strings.Contains(script, "jquery") {
			jsFrameworks = append(jsFrameworks, "jQuery")
		} else if strings.Contains(script, "react") {
			jsFrameworks = append(jsFrameworks, "React")
		} else if strings.Contains(script, "angular") {
			jsFrameworks = append(jsFrameworks, "Angular")
		} else if strings.Contains(script, "vue") {
			jsFrameworks = append(jsFrameworks, "Vue.js")
		} else if strings.Contains(script, "backbone") {
			jsFrameworks = append(jsFrameworks, "Backbone.js")
		} else if strings.Contains(script, "ember") {
			jsFrameworks = append(jsFrameworks, "Ember.js")
		} else if strings.Contains(script, "d3") {
			jsFrameworks = append(jsFrameworks, "D3.js")
		} else if strings.Contains(script, "lodash") {
			jsFrameworks = append(jsFrameworks, "Lodash")
		} else if strings.Contains(script, "moment") {
			jsFrameworks = append(jsFrameworks, "Moment.js")
		} else if strings.Contains(script, "axios") {
			jsFrameworks = append(jsFrameworks, "Axios")
		}
		// Example: if strings.Contains(script, "angular") { jsFrameworks = append(jsFrameworks, "Angular") }
		// ...

	}
	return jsFrameworks
}
