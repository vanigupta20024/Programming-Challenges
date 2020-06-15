/*
	Includes various array functions:
	1. Insert
	2. Display
	3. Append
	4. Delete
	5. Linear search
	6. Binary search
	7. Get item
	8. Set item
	9. Reverse
	10. Is sorted?
	11. Rearrange
	12. Merge, intersection and difference
	
*/

#include<stdio.h>
#include<stdlib.h>

struct array{
	int *a;
	int size;
	int length;
};

void display1(struct array *arr){
	for(int i = 0; i < arr->length; i++){
		printf("%d ", arr->a[i]);
	}
}

void insert(struct array *arr, int index, int element){
	if(arr->length < arr->size && index <= arr->length && index <= 0){
		for(int i = arr->length; i > index; i--){
			arr->a[i] = arr->a[i-1];
		}
		arr->a[index] = element;
		arr->length++;
	}
}

void append(struct array *arr, int element){
	if(arr->length < arr->size){
		arr->a[arr->length] = element;
		arr->length++;
	}
}

int Delete(struct array *arr, int index){
	if(arr->length > index && index >= 0){
		int num = arr->a[index];
		for(int i = index; i < arr->length-1; i++){
			arr->a[i] = arr->a[i+1];
		}
		arr->length--;
		return num;
	}
	return -1;
}

void swap(int *x, int *y){
	int temp = *x;
	*x = *y;
	*y = temp;
}

void display(struct array arr){
	for(int i = 0; i < arr.length; i++){
		printf("%d ", arr.a[i]);
	}
}

int LinearS(struct array *arr, int element){
	for(int i = 0; i < arr->length; i++){
		if(arr->a[i] == element) return i;
	}
	return -1;
}

int BinaryS(struct array *arr, int element){
	
	int l = 0;
	int r = arr->length-1;
	int mid;
	while(l<r){
		mid = (l+r)/2;
		if(element == arr->a[mid]) return mid;
		else if(element > arr->a[mid]) l = mid+1;
		else r = mid-1;
	}
	return -1;
}

int recBinary(struct array arr, int element, int l, int h){
	if(l<=h){
		int mid = (l+h)/2;
		if(arr.a[mid] == element) return mid;
		else if(element > arr.a[mid]) recBinary(arr, element, l, mid-1);
		else recBinary(arr, element, mid+1, h);
	}
}

int get(struct array arr, int index){
	if(index>=0 && index<arr.length){
		return arr.a[index];
	}
	return -1;
}

void set(struct array *arr, int index, int element){
	if(index>=0 && index<arr->length){
		arr->a[index] = element;
	}
}

void reverse1(struct array *arr){
	int *b = (int *)malloc(arr->length*sizeof(int));
	for(int i = arr->length-1, j = 0; i >= 0; i--, j++) b[j] = arr->a[i];
	for(int i = 0; i < arr->length; i++) arr->a[i] = b[i];
}

void reverse2(struct array *arr){
	int l = 0;
	int r = arr->length-1;
	while(l<=r){
		swap(&arr->a[l], &arr->a[r]);
		l++;
		r--;
	}
}

int isSorted(struct array arr){
	for(int i = 1; i < arr.length; i++){
		if(arr.a[i-1] > arr.a[i]) return -1;
	}
	return 0;
}

void rearrangeNegPos(struct array *arr){
	int i = 0, j = arr->length - 1;
	while(i < j){
		while(arr->a[i] < 0) i++;
		while(arr->a[j] > 0) j--;
		if(i<j) swap(&arr->a[i], &arr->a[j]);
	}
}

struct array *merge(struct array arr1, struct array arr2){
	int i=0, j=0, k=0;
	struct array *arr3 = (struct array *)malloc(sizeof(struct array));
	arr3->length = arr1.length + arr2.length;
	arr3->size = arr1.size + arr2.size;
	
	while(i<arr1.length && j<arr2.length){
		if(arr1.a[i] < arr2.a[j]){
			arr3->a[k] = arr1.a[i];
			i++;
			k++;
		}
		else if(arr1.a[i] > arr2.a[j]){
			arr3->a[k] = arr2.a[j];
			k++;
			j++;
		}
		else{
			arr3->a[k] = arr1.a[i];
			k++; 
			j++;
			i++;
		}
	}	
	while(i<arr1.length){
		arr3->a[k] = arr1.a[i];
		k++;
		i++;
	}
	while(j<arr2.length){
		arr3->a[k] = arr2.a[j];
		k++;
		i++;
	}
	
	return arr3;
}

struct array *intersection(struct array arr1, struct array arr2){
	int i=0, j=0, k=0;
	struct array *arr3 = (struct array *)malloc(sizeof(struct array));
	while(i<arr1.length && j<arr2.length){
		if(arr1.a[i] < arr2.a[j]){
			i++;
		}
		else if(arr1.a[i] > arr2.a[j]){
			j++;
		}
		else{
			arr3->a[k] = arr1.a[i];
			i++;
			k++;
			j++;
		}
	}
	arr3->size = arr1.size;
	arr3->length = k+1;
}

struct array *difference(struct array arr1, struct array arr2){
	int i=0, j=0, k=0;
	struct array *arr3 = (struct array *)malloc(sizeof(struct array));
	while(i<arr1.length && j<arr2.length){
		if(arr1.a[i] < arr2.a[j]){
			arr3->a[k] = arr1.a[i];
			k++;
			i++;
		}
		else if(arr1.a[i] > arr2.a[j]){
			j++;
		}
		else{
			i++;
			j++;
		}
	}
	arr3->size = arr1.size;
	arr3->length = k+1;
}

int main(){
	
	int choice, index, element, x=0,y;
	struct array arr;
	struct array arr2;
	struct array *arr3;
	printf("\nEnter size of array: ");
	scanf("%d", &arr.size);
	printf("\nEnter number of elements: ");
	scanf("%d", &arr.length);
	arr.a = (int *)malloc(arr.length*sizeof(int));
	printf("\nEnter values: ");
	for(int i = 0; i < arr.length; i++) scanf("%d", &arr.a[i]);
	while(x != -1){
		printf("\nEnter choice:\n");
		printf("\n_________Menu___________\n");
		printf("1. Insert\n");
		printf("2. Display\n");
		printf("3. Append\n");
		printf("4. Delete\n");
		printf("5. Linear search\n");
		printf("6. Binary search\n");
		printf("7. Get item\n");
		printf("8. Set item\n");
		printf("9. Reverse\n");
		printf("10. Is sorted?\n");
		printf("11. Rearrange\n");
		printf("12. Merge, intersection and difference\n");
		scanf("%d", &choice);
		switch(choice){

			case 1:
				printf("\nEnter index at which you want to enter: ");
				scanf("%d", &index);
				printf("\nEnter element to enter: ");
				scanf("%d", &element);
				insert(&arr, index, element);
				display(arr);
				break;
			case 2:
				display(arr);
				break;
			case 3:
				printf("\nEnter element to append: ");
				scanf("%d", &element);
				append(&arr, element);
				break;
			case 4:
				printf("\nEnter index you want to delete the element from: ");
				scanf("%d", &index);
				y = Delete(&arr, index);
				if (y==-1){
					printf("\nIndex not found");
				}
				else printf("\nItem deleted: %d.", y);
				break;
			case 5:
				printf("\nEnter the element you want to find: ");
				scanf("%d", &element);
				y = LinearS(&arr, element);
				if(y==-1) printf("\nElement not found.");
				else printf("\nElement found at %d." , y);
				break;
			case 6:
				printf("\nEnter element you want to find: ");
				scanf("%d", &element);
				y = BinaryS(&arr, element);
				if(y==-1) printf("\nElement not found.");
				else printf("\nElement found at %d." , y);
				printf("\nUsing recusion: ");
				y = recBinary(arr, element, 0, arr.length);
				if(y==-1) printf("\nElement not found.");
				else printf("\nElement found at %d." , y);
				break;
			case 7:
				printf("\nEnter index you want to get: ");
				scanf("%d", &index);
				y = get(arr, index);
				if(y==-1) printf("\n Unsuccessfull.");
				else printf("\nElement found is %d." , y);
				break;
			case 8:
				printf("\nEnter element, index to set: ");
				scanf("%d%d", &element, &index);
				set(&arr, index, element);
				break;
			case 9:
				reverse1(&arr);
				display(arr);
				printf("\n");
				reverse2(&arr);
				display(arr);
				break;
			case 10:
				y = isSorted(arr);
				if(y==-1) printf("\nNo");
				else printf("\nYes");
				break;
			case 11:
				rearrangeNegPos(&arr);
				break;
			case 12:
				printf("\nEnter number of elements in 2nd array: ");
				scanf("%d", &arr2.length);
				printf("\nEnter elements: ");
				for(int i=0;i<arr2.length;i++) {
					scanf("%d", &arr2.a[i]);
				}
				printf("\nArray 2 is: ");
				display(arr2);
				arr3 = merge(arr, arr2);
				printf("\nArray 3 after merging is:");
				display1(arr3);
				arr3 = intersection(arr, arr2);
				printf("\nArray 3 after intersection:");
				display1(arr3);
				arr3 = difference(arr, arr2);
				printf("\nArray 3 after difference: ");
				display1(arr3);
				break;
			default:
				printf("\nWrong choice entered.");
		}
		printf("\nEnter -1 to exit: ");
		scanf("%d", &x);
	}
	return 0;
}
