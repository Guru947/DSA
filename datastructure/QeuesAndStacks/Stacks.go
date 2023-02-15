package main

import "fmt"

type Node struct {
	element int
	next    *Node
}

type Stack struct {
	head   *Node
	length int
}

func (s *Stack) insert(e int) {
	var newwst *Node = &Node{e, nil}
	newwst.next = s.head
	s.head = newwst

}
func (s *Stack) delete() {
	s.head = s.head.next
}
func (s *Stack) display() {
	p := s.head
	for {
		fmt.Printf("%d -->", p.element)
		if p.next == nil {
			break
		}
		p = p.next
	}
}

func main() {
	s := new(Stack)
	s.insert(40)
	s.insert(30)
	s.insert(20)
	s.insert(10)
	s.display()
	fmt.Println()
	s.delete()
	s.delete()
	s.delete()
	s.display()

}
