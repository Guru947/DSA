package main

import "fmt"

type node struct {
	prev    *node
	element int
	next    *node
}
type dlinkedlist struct {
	head   *node
	tail   *node
	length int
}

func (d *dlinkedlist) addfirst(e int) {
	n := node{nil, e, nil}
	if d.head == nil {
		d.head = &n
		d.tail = &n

	} else {
		n.next = d.head
		d.head.prev = &n
		d.head = &n
	}
	d.length++
}
func (d *dlinkedlist) addlast(e int) {
	n := node{nil, e, nil}
	if d.head == nil {
		d.head = &n
		d.tail = &n

	} else {
		d.tail.next = &n
		n.prev = d.tail
		d.tail = &n
	}
	d.length++

}
func (d *dlinkedlist) addany(e, pos int) {
	n := node{nil, e, nil}
	if d.head == nil {
		d.head = &n
		d.tail = &n
		d.length++
		return
	}
	var p = d.head
	var i = 1
	for i < pos-1 {
		p = p.next
		i++
	}
	n.next = p.next
	n.prev = p
	p.next = &n
	d.length++

}
func (d *dlinkedlist) deletefirst() {
	if d.head == nil {
		fmt.Println("double linked list is empty")
	} else {
		d.head.next.prev = nil
		d.head = d.head.next
		d.length--
	}
}
func (d *dlinkedlist) deletelast() {
	if d.head == nil {
		fmt.Println("double linked list is empty")
	} else {
		d.tail.prev.next = nil
		d.tail = d.tail.prev
		d.length--
	}

}
func (d *dlinkedlist) deleteany(position int) {
	if d.head == nil {
		fmt.Println("double linked list is empty")
	} else {
		p := d.head
		i := 1
		for i < position-1 {
			p = p.next
			i++
		}
		e := p.next.element
		p.next = p.next.next
		p.next.next.prev = p
		d.length--
		fmt.Println(e)

	}

}
func (d *dlinkedlist) display() {
	var p = d.head
	for {
		fmt.Printf("%d <-->", p.element)
		p = p.next
		if p.next == nil {
			break
		}
	}

}
func (d *dlinkedlist) search(e int) string {
	var p = d.head
	for {
		if p.element == e {
			return "element found "
		}
		p = p.next
	}
	return "element not found"

}

func main() {
	dl := dlinkedlist{}

	dl.addfirst(34)
	dl.addfirst(33)
	dl.addfirst(32)
	dl.addfirst(31)
	dl.addlast(35)
	dl.addlast(36)
	dl.addany(32, 3)
	dl.display()
	fmt.Println()
	dl.deletefirst()
	fmt.Println()
	dl.display()

	dl.deletelast()
	fmt.Println()
	dl.display()

	dl.deleteany(3)
	dl.display()
	fmt.Println()
	print(dl.length)
	// print(dl.search(0))
	fmt.Println()

}
