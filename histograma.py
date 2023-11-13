from manim import *

class MyOwnCriature(VGroup):
    CONFIG = {
        "torse": [1.4, 2],
        "arm": [.7, 1.7],
        "leg": [.7, 1.7],
        "head_body": .67,
        "body_kwargs": {
            "stroke_width": 2,
            "stroke_color": BLACK,
            "fill_color": WHITE,
            "fill_opacity": 1
        }
    }

    def __init__(self, scale, **kwargs):
        VGroup.__init__(self, **kwargs)
        torse = self.my_torse()
        arms = self.my_arms(torse)
        legs = self.my_legs(torse)
        head = self.my_head(torse)
        self.add(torse, arms, legs, head)
        self.scale(scale)

    def my_torse(self):
        return Rectangle(width=self.CONFIG['torse'][0], height=self.CONFIG['torse'][1], **self.CONFIG['body_kwargs'])

    def my_arms(self, torse):
        arm1 = Rectangle(width=self.CONFIG['arm'][0],
                         height=self.CONFIG['arm'][1], **self.CONFIG['body_kwargs'])
        arm2 = arm1.copy()
        return VGroup(arm1, arm2).arrange(RIGHT, buff=self.CONFIG['torse'][0]+0.16)\
            .move_to(torse.get_center())

    def my_legs(self, torse):
        leg1 = Rectangle(width=self.CONFIG['leg'][0],
                         height=self.CONFIG['leg'][1], **self.CONFIG['body_kwargs'])
        leg2 = leg1.copy()
        my_legs = VGroup(leg1, leg2).arrange(RIGHT, buff=0.07)\
            .next_to(torse, DOWN, buff=0.08)
        return my_legs

    def my_head(self, torse):
        return Circle(radius=self.CONFIG['head_body'], **self.CONFIG['body_kwargs'])\
            .next_to(torse, UP, buff=0.08)


class HistogramCovid19(Scene):
    CONFIG = {
        'axis_config': {
            'x_range': [0, 5, 1],
            'x_axis_config': {
                # 'tick_frequency': 1,
                'unit_size': 1
            },
            'y_range': [0, .7, .1],
            'y_axis_config': {
                # 'tick_frequency': .2,
                'unit_size': 7,
            },
            'stroke_width': 2,
            'color': RED,
            # 'center_point': 6*LEFT+2*DOWN,
        },
        'countries': ['Brazil', 'EEUU', 'Iran', 'China'],
        'colors': [GREEN, RED, YELLOW, BLUE, ORANGE],
        'rect_kwargs': {
            'x_range': [0, 4],
            # 'exclude_zero_from_default_numbers': True,
            # 'leftmost_tick': 1,
            'stroke_width': 1
        },
    }

    def construct(self):
        axes = self.get_axes()
        bars = self.get_bars(axes)
        countries = self.get_tex_with_color(bars, axes)
        anims = [axes, bars, countries[0]]
        essaies = 10000
        my_scores = np.array([self.random_points() for x in range(essaies)])
        index_traker = ValueTracker(essaies)

        def get_index():
            value = index_traker.get_value()
            return int(value)
        bars.add_updater(lambda t: self.set_histogram_bars(
            t, my_scores[:get_index()], axes))
        for anim in anims:
            self.play(Create(anim))
        self.wait()
        self.add(bars)
        for t in range(len(countries[0])):
            self.play(TransformFromCopy(countries[0][t], countries[1][t]))
        self.wait()
        my_rects = self.get_rects(bars)
        my_criatures = self.get_my_people(countries[1], my_rects)
        my_criatures.add_updater(
            lambda t: self.set_my_people_update(t, my_scores[:get_index()]))
        titulo = Tex('Covid-19').to_edge(UP, buff=0.4)
        for mob in [titulo]:
            self.play(FadeIn(mob))
        my_rects.next_to(countries[1], RIGHT, buff=.3)
        my_ghost_lines = self.get_my_ghost_rects(my_rects)
        my_ghost_lines_neg = self.get_my_ghost_rects(my_rects, health=False)
        my_ghost_lines.add_updater(
            lambda t: self.set_my_ghost_rects(t, my_scores[:get_index()]))
        my_ghost_lines_neg.add_updater(
            lambda t: self.set_my_ghost_rects_ill(t, my_ghost_lines))
        self.play(*[FadeIn(mob) for mob in [my_rects, my_criatures,
                  my_ghost_lines, my_ghost_lines_neg]])
        for value in [10, 100, 1000, 10000]:
            anims = [
                ApplyMethod(
                    index_traker.set_value, value,
                    rate_func=linear,
                    run_time=14
                )
            ]
            self.play(*anims)
        self.wait()

    def get_axes(self):
        axes = Axes(**self.CONFIG['axis_config'])
        title_x_axis = Tex('Countries').scale(.5)
        title_x_axis.next_to(axes.x_axis, RIGHT, buff=0.1)
        title_y_axis = Tex('Frequency').scale(.5)
        title_y_axis.next_to(axes.y_axis, UP, buff=0.1)
        axes.title_x_axis = title_x_axis
        axes.title_y_axes = title_y_axis
        axes.add(title_x_axis, title_y_axis)
        return axes

    def get_bars(self, axes):
        bars = VGroup()
        bars.axes = axes
        for x in range(
                self.CONFIG['axis_config']['x_range'][0]+1,
                self.CONFIG['axis_config']['x_range'][1],
                self.CONFIG['axis_config']['x_axis_config']['unit_size']
        ):
            bar = Rectangle(width=axes.x_axis.unit_size)
            bar.move_to(axes.coords_to_point(x, 0), DOWN)
            bar.x = x
            bars.add(bar)
        self.get_color_bar(bars)
        return bars

    def get_color_bar(self, bars):
        for bar, color in zip(bars, self.CONFIG['colors']):
            bar.set_fill(color=color, opacity=1)
            bar.set_stroke(width=.5, color=BLACK)
            bar.color = color
        return bars

    def get_tex_with_color(self, bars, axes):
        teXs = VGroup()
        teXs_copy = VGroup()
        for bar, country in zip(bars, self.CONFIG['countries']):
            teX = Tex(country)
            teX.set_color(bar.color)
            teX.scale(0.6)
            teX_copy = teX.copy()
            teX.next_to(bars.axes.c2p(bar.x), DOWN, buff=.5)
            teX.rotate(PI/2)
            teX.bar = bar
            teXs_copy.add(teX_copy)
            teXs.add(teX)
        teXs_copy.arrange(DOWN, buff=1)
        teXs_copy.move_to(ORIGIN+RIGHT)
        return VGroup(teXs, teXs_copy)

    def get_relative_proporticon(self, all_changes):
        my_ponds = set(all_changes)
        n_changes = len(all_changes)
        return dict([
            (p, np.sum(all_changes == p)/n_changes)
            for p in my_ponds
        ])

    def set_histogram_bars(self, bars, scores, axes):
        prop_map = self.get_relative_proporticon(scores)
        epsilon = 1e-5
        for bar in bars:
            prop = prop_map.get(bar.x, epsilon)
            bar.stretch_to_fit_height(
                prop*axes.y_axis.unit_size,
                about_edge=DOWN
                # {
                #        'stretch':True,        ##no funciona con esto
                #        'about_edge':DOWN
                # }
            )

    def random_points(self):
        score = 1
        radius = 1
        while True:
            hit_radius = np.linalg.norm(np.random.uniform(-1, 1, size=2))
            if hit_radius > radius:
                return score
            else:
                score += 1
                radius = np.sqrt(1-hit_radius**2)

    def get_rects(self, bars):
        rects = VGroup()
        for bar in bars:
            rect = NumberLine(**self.CONFIG['rect_kwargs']).fade(.5)
            rect.set_width(5)
            rect.bar = bar
            rects.add(rect)
        rects.arrange(DOWN, buff=1)
        return rects

    def get_my_people(self, mob_color, rects):
        my_criatures = VGroup()
        for rect in rects:
            my_criature = MyOwnCriature(.2).scale(.4)
            my_criature.set_fill(rect.bar.color)
            my_criature.rect = rect
            my_criatures.add(my_criature)
        return my_criatures

    def set_my_people_update(self, criatures, score):
        my_promps = self.get_relative_proporticon(score)
        epsilon = 5
        for criature in criatures:
            my_promp = my_promps.get(criature.rect.bar.x, epsilon)
            copy_criature = VGroup(*[(criature) for _ in range(len(criature))])
            for criat in copy_criature:
                criat.move_to(criature.rect.number_to_point(my_promp*5)+0.3*UP)

    def get_my_ghost_rects(self, rects, health=True):
        my_lines = VGroup()
        for rect in rects:
            if health:
                my_line = Line()
                my_line.set_stroke(color=BLUE, opacity=0.5, width=15)
                my_line.move_to(rect.number_to_point(0), my_line.get_start())
                my_line.rect = rect
                my_lines.add(my_line)
            else:
                my_line = Line()
                my_line.set_stroke(color=RED, opacity=0.5, width=15)
                my_line.move_to(rect.number_to_point(4), my_line.get_start())
                my_line.rotate(PI)
                my_line.rect = rect
                my_lines.add(my_line)
        return my_lines

    def set_my_ghost_rects(self, lines, scores):
        my_promps = self.get_relative_proporticon(scores)
        epsilon = 4
        for line in lines:
            my_promp = my_promps.get(line.rect.bar.x, epsilon)
            line.stretch_to_fit_width(my_promp*6.2, #stretch=True,
                           about_point=line.rect.number_to_point(0))

    def set_my_ghost_rects_ill(self, lines, healths):
        for line, health in zip(lines, healths):
            line.put_start_and_end_on(
                health.get_right(), line.rect.number_to_point(4))
