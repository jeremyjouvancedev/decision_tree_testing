import dtree

tree = dtree.dtree()
attractive,classes,features = tree.read_data('attractive.data')
t=tree.make_tree(attractive,classes,features)
tree.printTree(t,' ')

print(tree.classifyAll(t,attractive))

for i in range(len(attractive)):
    tree.classify(t,attractive[i])

print ("True Classes")
print (classes)
