from big_ol_pile_of_manim_imports import * 

class test(GraphScene):
    
    def fun(self, x):
        return x**2
    
    def construct(self):
        aa = Circle()

        dot = Circle()
        self.setup_axes()
        # a = 
        
        # for i in range(10):
        self.play(ShowCreation(self.get_graph(self.fun)
                        , rate_fun=rush_into)
        
        )
               
        self.wait()
        self.add(aa)
        self.wait()


        self.add(Rectangle())
        
        self.add(aa.scale(1/2).surround(Rectangle()))
        
        
        
        self.add(aa)
        self.wait()
