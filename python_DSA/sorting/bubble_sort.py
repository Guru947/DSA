func BabbleSort(arr []int) {
    //pass3 so loop will run lenth-1
	for i := 0; i < len(arr)-1; i++ {
        //value a is bool- if no swap dont require to run loop
		var a bool
        //last value atomatically bubble so lenth-1 and last element sorted so I need to reduce i times
		for j := 0; j < len(arr)-1-i; j++ {
            //if arr[j] element greater then arr[j+1] element
           // if condition is true swap else dont swap
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				a = true
			}
		}
		if !a {
			break
		}
	}

}   