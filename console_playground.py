from L_graph_system import LGraph,load_graph,save_graph
import unittest

c = LGraph()
# c.add_vertex('a')
# .add_vertex('b')
c.add_arc('a', 'a', 'a', '(')
c.add_arc('a', 'b', 'b', ')')
c.add_arc('b', 'b', 'b', ')')
c.add_arc('b', 'c', 'c')
# c.remove_arc('4')
# c.remove_vertex('b')
# print(c)

d = LGraph()
d.generate_from_grammar(['P->S@', 'S->aSb|dA', 'A->dA|e'])
#print(d)

k = LGraph()
k.generate_from_grammar(['S->aA|b', 'A->aS|b'])
#print(k)
#s = "ab"
#print(k.solve(s))
#print(k.solve(s, arc_trace=True))
#print(k.solve(s, vertex_trace=True))
#print()
#print(k.cycles())
#print(k.arc_cycles())
#print()

constructed = LGraph()
#constructed.add_arc('0','1','=','')
constructed.add_arc('1','1','a','[')
constructed.add_arc('1','2','b',']')
constructed.add_arc('2','2','b',']')
constructed.set_start('1')
constructed.set_finish('2')
#print('Pre-constructed C-f L-graph:')
#print(constructed)
s ="aab"
#print(constructed.solve(s))
#print(constructed.arc_cycles())
#print(constructed.core(0,2))

constructed2 = LGraph()
constructed2.add_arc('1','1','a','[')
constructed2.add_arc('1','2','b','(]')
constructed2.add_arc('2','2','b','(]')
constructed2.add_arc('2','3','c',')')
constructed2.add_arc('3','3','c',')')
constructed2.set_start('1')
constructed2.set_finish('3')
#print('Pre-constructed C-d L-graph:')
#print(constructed2)
s ="abc"
#print(constructed2.solve(s))

multiply6 = LGraph()
multiply6.add_arc('1','1','I','[1')
multiply6.add_arc('1','2','x','')
multiply6.add_arc('2','2','I','[2')
multiply6.add_arc('2','3','=','')
multiply6.add_arc('3','4','','(1')
multiply6.add_arc('4','4','I','(0]2')
multiply6.add_arc('4','5','',']1')
multiply6.add_arc('5','5','','[2)0')
#multiply6.add_arc('5','3','',')1')
multiply6.add_arc('3','6','','')
multiply6.add_arc('6','6','',']2')
multiply6.set_start('1')
multiply6.set_finish('6')
s='IIxII=IIII'
#print(multiply6.type_def())
#print('Strange multiply:')
#print(multiply6.solve(s))
#print(multiply6.solve(s,vertex_trace=True))
#print(['1'] in [['1'],['2']])
#print(multiply6.arc_cycles())
#print(multiply6.core(1,0))
#print(multiply6.dead_ends())
#print(multiply6.unattainable())
#print(multiply6.remove_unusable())


for_reduction = LGraph()
for_reduction.add_arc('0','1','a','')
#for_reduction.add_arc('1','1','a','')
for_reduction.add_arc('1','2','',')')
#print(for_reduction)
for_reduction.reduction()
#print(for_reduction)

f = LGraph()
f.generate_from_grammar(['S->Ab', 'A->aA|e'])
print(f)
f.reduction()
g = f
print('NEW')
print(g)
#save_graph(g,'test.lg')
#print(g.solve('eb',arc_trace=True))
#print(f.type_def())