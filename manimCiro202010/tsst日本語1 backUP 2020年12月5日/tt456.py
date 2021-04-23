from big_ol_pile_of_manim_imports import *

class graph(GraphScene):
    def construct(self):
      self.setup_axes(animate=True)
      aa=self.get_graph(lambda x: x)

      # self.add(aa)
      # self.wait()

      self.play(Write(aa))
      self.wait()



class bar(Scene):
    def construct(self):
        aa=BarChart(
        values=[.1,.2,.3],
        bar_names=[
        "a",
        "b","bar"]
        )
        # self.add(aa.scale(.3))
        # self.wait()

        # aa.set_height(1)


        self.play(Write(aa), rate_func=smooth)
        self.wait()

def get_binomial(self):
        k_range = list(range(11))
        dists = [
        get_binomial_distribution(10, p)
        for p in (0.2, 0.8, 0.5)
        ]
        # def get_binomial_distribution(n, p):
        #     return lambda k : choose(n, k)*(p**(k))*((1-p)**(n-k))

        values_list = [
        list(map(dist, k_range))
        for dist in dists
        ]
        chart = BarChart(
        values = values_list[-1],
        bar_names = k_range
        )
        chart.set_height(self.chart_height)
        chart.values_list = values_list
        return chart




class aaz(Scene):
    def construct(self):
      dot=Dot()
      self.add(dot)


from grid import *

class ggg(Scene):
    def construct(self):
      dot=Dot()
      self.add(dot)
      aa=ScreenGrid()
      self.add(aa)
      self.play(ShowCreation(aa))
