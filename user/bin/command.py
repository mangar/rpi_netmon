//
// Screen Scraping in Go Lang
//
// Lib:
// go get github.com/PuerkitoBio/goquery
//
package main

import (
	"fmt"
	"log"

	"github.com/PuerkitoBio/goquery"
)

func postScrape() {
	doc, err := goquery.NewDocument("https://github.com/PuerkitoBio/goquery")
	if err != nil {
		log.Fatal(err)
	}

	// use CSS selector found with the browser inspector
	// for each, use index and item
	doc.Find(".markdown-body h2").Each(func(index int, item *goquery.Selection) {

		title := item.Text()
		linkTag := item.Find("a")
		link, _ := linkTag.Attr("href")
		fmt.Printf("Post #%d: %s - %s\n", index, title, link)
	})

}

func main() {
	fmt.Println("> > > > > > > > > > > > > > > > > > > > > \n")
	postScrape()
	fmt.Println("\n< < < < < < < < < < < < < < < < < < < < < ")

}
