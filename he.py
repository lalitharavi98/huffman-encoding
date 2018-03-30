class Node:
	def __init__(self,symbol,freq):
		self.symbol=symbol
		self.freq=freq
		self.left=None
		self.right=None
		self.code=""
class Node2:
	def __init__(self,sym,code):
		self.sym=sym
		self.code=code
class HuffmanEncoding:
	def __init__(self,n,S,F):
		self.n=n
		self.S=S
		self.F=F
		self.array=[]
	def insert(self,node):
		self.array.append(node)
		self.buildheap()
	def heapify(self,i):
		parent=i
		left=2*i+1
		right=2*i+2
		if left<len(self.array) and self.array[parent].freq>self.array[left].freq:
			parent=left
		if right < len(self.array) and self.array[parent].freq>self.array[right].freq:
			parent=right
		if parent!=i:
			temp=self.array[i]
			self.array[i]=self.array[parent]
			self.array[parent]=temp
			self.heapify(parent)
	def buildheap(self):
		for i in range(len(self.array)//2-1,-1,-1):
			self.heapify(i)
	def extract_min(self):
		min=self.array[0]
		self.array[0]=self.array[len(self.array)-1]
		self.array.pop()
		self.buildheap()
		return min


def main():
	S=['a','b','c','d','e','f']
	F=['13','9','12','5','16','45']
	n=len(S)
	H=HuffmanEncoding(n,S,F)
	for i in range(n):
			H.array.append(Node(S[i],int(F[i])))
	H.buildheap()
	for i in range(n):
		print(H.array[i].symbol," ",H.array[i].freq)
	for i in range(n-1):
		x=H.extract_min()
		y=H.extract_min()
		node=Node(None,(x.freq+y.freq))
		node.left=x
		node.right=y
		H.insert(node)
	root=H.extract_min()
	a=[]
	traverse(root,a)
	print(root.freq)
	filesize=0
	for i in range(len(a)):
		filesize=filesize+len(a[i].code)
		print(a[i].sym," ",a[i].code)
	print("size of the file:",filesize)
def traverse(root,a):
	if root==None:
		return;
	if root.left==None and root.right==None:
		a.append(Node2(root.symbol,root.code))
	
	if root.left!=None:
		root.left.code=root.code+"0"
		traverse(root.left,a)
	if root.right!=None:
		root.right.code=root.code+"1"
		traverse(root.right,a)


	

	


main()
