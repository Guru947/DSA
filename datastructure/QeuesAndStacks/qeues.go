package main

import "fmt"

type node struct {
	element int
	next    *node
}

type qeues struct {
	head *node

	size int
}

func (p *qeues) insert(e int) {
	var newest *node = &node{e, nil}
	if p.head == nil {
		p.head = newest

	} else {
		newest.next = p.head
		p.head = newest
	}
	p.size++
}

func (p *qeues) delete() {
	q := p.head
	for {
		if q.next.next == nil {
			break
		}
		q = q.next
	}
	q.next = nil
}

func (p *qeues) display() {
	q := p.head
	for {
		fmt.Printf("%d -->", q.element)
		if q.next == nil {
			break
		}
		q = q.next
	}
}

func main() {
	q := qeues{}
	q.insert(10)
	q.insert(20)
	q.insert(30)
	q.insert(40)
	q.display()
	fmt.Println()
	q.delete()
	// q.delete()
	q.delete()
	q.delete()

	q.display()

}
