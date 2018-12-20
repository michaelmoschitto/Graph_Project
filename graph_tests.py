import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
    # 
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())
    
    def test_file3(self):
        g = Graph('file3.txt')
        # print(g.conn_components())
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8'], ['v10', 'v11', 'v9'], ['v13', 'v14', 'v15', 'v16'], ['v20']])
        self.assertFalse(g.is_bipartite())
#         this is a test
    
    def test_file4(self):
        g = Graph('file4.txt')
        # print(g.conn_components())
        # self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8'], ['v10', 'v11', 'v9'], ['v13', 'v14', 'v15', 'v16'], ['v20']])
        self.assertFalse(g.is_bipartite())
        
    def test_cov(self):
        g = Graph('file4.txt')
        self.assertEqual(g.get_vertex('v4').id, 'v4')
        g.get_vertex_list()
        g.print_graph()
        

        # self.asser


if __name__ == '__main__':
   unittest.main()
