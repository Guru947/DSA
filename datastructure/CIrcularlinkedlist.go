package main

import "fmt"

type linkedlist struct {
	element int
	next    *linkedlist
}

func createNode(e int) *linkedlist {
	p := &linkedlist{
		element: e,
		next:    nil,
	}
	return p
}

func (node *linkedlist) insertlast(num int) {

	var temp *linkedlist = createNode(num)

	if node == nil {
		node = temp
		// lastNode := temp
	} else {
		var p = &linkedlist{}
		p = node

		for p.next != nil {
			p = p.next
		}
		p.next = temp
	}
}

func (node *linkedlist) insertfirst(num int) {

	var temp *linkedlist = createNode(num)

	if node == nil {
		node = temp
		// lastNode := temp
	} else {
		var p = &linkedlist{}
		p = node

		for p.next != nil {
			p = p.next
		}
		p.next = temp
	}
}

func main() {
	circle := &linkedlist{}
	circle.insertfirst(10)
	circle.insertfirst(20)
	circle.insertfirst(30)
	circle.insertfirst(40)

	circle.display()

}

func (node *linkedlist) display() {
	var p = &linkedlist{}
	p = node.next
	for p != nil {
		fmt.Printf("%d -->", p.element)
		p = p.next
	}

}
