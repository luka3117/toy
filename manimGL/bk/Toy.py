

    def construct(self):
        self.setup_axes()
        a = self.get_graph(lambda x : x)
        self.play(Write(a))
