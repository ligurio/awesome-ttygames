package main

import (
	"fmt"
	"gopkg.in/yaml.v2"
	"html/template"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
)

type Game struct {
	Name       string
	Info       string
	URL        string
	Screencast string
	Play       string
}

func Read() []string {
	a := []string{"tetris", "orange", "pear"}
	return a
}

func main() {

	var data = "games.yaml"
	var html = "template.html"

	if _, err := os.Stat(data); os.IsNotExist(err) {
		fmt.Printf("File %v doesn't exist.\n", data)
		os.Exit(1)
	}

	f, _ := filepath.Abs(data)
	yamlFile, err := ioutil.ReadFile(f)

	if err != nil {
		panic(err)
	}

	games := []Game{}
	type GameList []Game

	err = yaml.Unmarshal(yamlFile, &games)
	if err != nil {
		log.Fatalf("error: %v", err)
	}

	f, _ = filepath.Abs(html)
	htmltmpl, err := ioutil.ReadFile(html)

	if err != nil {
		panic(err)
	}

	t := template.Must(template.New("tmpl").Parse(string(htmltmpl)))
	t.Execute(os.Stdout, games)
}
