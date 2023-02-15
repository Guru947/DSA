package main

// /* CIRCULAR SINGLULAR LINKED LIST */

import "fmt"

type node struct {
	element int
	next    *node
}
type linkedlist struct {
	head *node
	tail *node
	size int
}

func (l *linkedlist) addfirst(e int) {
	newest := node{e, nil}
	if l.head == nil {
		l.head = &newest
		l.tail = &newest

	} else {
		newest.next = l.head
		l.head = &newest
		l.tail.next = l.head
	}
	l.size++
}
func (l *linkedlist) addlast(e int) {
	newest := node{e, nil}
	if l.head == nil {
		l.head = &newest
		l.tail = &newest

	} else {
		newest.next = l.head
		l.tail.next = &newest
		l.tail = &newest
	}
	l.size++

}
func (l *linkedlist) addany(e, position int) {
	newest := node{e, nil}
	if l.head == nil {
		l.head = &newest
		l.tail = &newest

	}
	p := l.head
	i := 1
	for i < position-1 {
		p = p.next
		i++
	}
	newest.next = p.next
	p.next = &newest
	l.size++
}

func (l *linkedlist) deletefirst() {
	if l.head == nil {
		fmt.Println("linked list is empty")
		return
	}

	l.head = l.head.next
	l.tail.next = l.head
	l.size--
}
func (l *linkedlist) deletelast() {
	if l.head == nil {
		fmt.Println("linked list is empty")
		return
	}
	p := l.head
	for {
		if p.next.next == l.head {
			p.next = l.head
			break
		}
		p = p.next
	}
	l.size--

}
func (l *linkedlist) deleteany(postion int) {
	if l.head == nil {
		fmt.Println("linked list is empty")
		return
	}
	p := l.head
	i := 1
	for i < postion-1 {
		p = p.next
		i++
	}
	p.next = p.next.next
}

func (l *linkedlist) isCircular() {
	if l.head == l.tail.next {
		fmt.Println("True")
	} else {
		fmt.Println("false")
	}
}

func (l *linkedlist) display() {
	var p = l.head
	for {
		fmt.Printf("%d -->", p.element)
		if p.next == l.head {
			break
		}
		p = p.next
	}

}
func main() {
	li := linkedlist{}
	li.addfirst(30)
	li.addfirst(20)
	li.addfirst(10)
	li.display()
	fmt.Println()
	li.addlast(70)
	li.addlast(80)
	li.addlast(90)
	li.display()
	li.addany(40, 4)
	fmt.Println()
	li.display()
	li.deletefirst()
	fmt.Println()
	li.display()
	li.deletelast()
	fmt.Println()
	li.display()
	fmt.Println()
	li.deleteany(3)
	li.display()
	li.deleteany(3)
	fmt.Println()
	li.isCircular()
	fmt.Println(li.size)

}
