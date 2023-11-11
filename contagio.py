from manim import *
import itertools as it
import random as rn
import operator as op
FRAME_HEIGHT=config['frame_height']
FRAME_WIDTH=FRAME_HEIGHT*19/6
FRAME_X_RADIUS=FRAME_WIDTH/2
FRAME_Y_RADIUS=FRAME_HEIGHT/2
LISTA_1=[
        1,
        0,
        2,
        10,
        10,
        20,
        42,
        50,
        160,
        200
]
class MiGrafico2(Scene):
        CONFIG={
                'axis_config':{
                        'center_point':LEFT*4+DOWN*(FRAME_Y_RADIUS-1),
                        'x_min':0,
                        'x_max':10,
                        'y_min':0,
                        'y_max':210,
                        'color':RED
                }
        }
        def  construct(self):
                axes=self.get_my_axes()
                axes[1].set_opacity(0)
                self.play(ShowCreation(axes[0]))
                self.add(axes[1])
                for i in it.count():
                        if i==len(axes[1]):
                                break
                        self.play(ShowCreation(axes[1][i]),axes[1][i].set_opacity,1,run_time=0.3)
                        if axes[1][i].get_center()[1]>FRAME_HEIGHT-2:
                                self.play(axes[0].set_height,FRAME_HEIGHT-1,\
                                        {'stretch':True,'about_point':axes[0].coords_to_point(0,0)},run_time=3)
                self.wait()
        def get_my_axes(self):
                axes=Axes(**self.axis_config)
                dots=VGroup()
                for i,t in zip(it.count(),LISTA_1):
                        dot=Dot().move_to(axes.coords_to_point(i,t))
                        dots.add(dot)
                def update(dots):
                        for dot,x,y in zip(dots,it.count(),LISTA_1):
                                dot.move_to(axes.coords_to_point(x,y))
                dots.add_updater(update)
                return VGroup(axes,dots)
        def get_my_dots(self,axes):
                pass

class MyGroupScene(Scene):
        TEXTS={
                'text1':"Healthy Peaople",
                'text2':'people with the illness',
                'text3':'pass away :('
        }
        def construct(self):
                def my_mobs(mob):
                        mob.scale(2)
                        mob.set_color(BLUE)
                        return mob
                def my_mobs_2(mob):
                        mob.scale(1.5)
                        mob.set_color(RED)
                        return mob
                my_dots=self.get_my_sort_dots()
                my_objects=VGroup().center()
                for dot in my_dots.family_members_with_points():
                        my_objects.add(dot)
                first_phrase=Tex(self.TEXTS['text1']).to_edge(UP,buff=0.4).set_color(BLUE_B)
                second_phrase=Tex(self.TEXTS['text2']).to_edge(UP,buff=0.4).set_color(RED)
                thrid_phrase=Tex(self.TEXTS['text3']).to_edge(UP,buff=0.4)
                self.play(ShowCreation(my_objects),Write(first_phrase))
                self.play(
                        LaggedStart(*[
                                ApplyFunction(my_mobs,my_objects[t],rate_func=there_and_back)
                                for t in rn.sample(set(np.arange(0,len(my_objects))),len(my_objects))
                        ]),
                )
                self.wait()
                self.play(
                        LaggedStart(*[
                                ApplyFunction(my_mobs_2,my_objects[t],rate_func=there_and_back)
                                for t in rn.sample(set(np.arange(0,len(my_objects))),len(my_objects))
                        ]),
                        ReplacementTransform(first_phrase,second_phrase)
                )
                self.wait()
                self.covid_19(my_objects,[1,4,35,67,97,140,156,103])
                self.play(ReplacementTransform(second_phrase,thrid_phrase))
                self.wait
        def get_my_sort_dots(self):
                first_row_dot=VGroup(*[Dot() for _ in range(20)]).arrange(RIGHT,buff=0.01)
                second_row_dot=VGroup(*[Dot() for _ in range(29)]).arrange(RIGHT,buff=0.01).move_to(first_row_dot[0].get_width()*UR)
                third_row_dot=VGroup(*[Dot() for _ in range(27)]).arrange(RIGHT,buff=0.01).move_to(2*first_row_dot[0].get_width()*UP+first_row_dot[0].get_width()/2*LEFT)
                fourth_row_dot=VGroup(*[Dot() for _ in range(21)]).arrange(RIGHT,buff=0.01).move_to(3*first_row_dot[0].get_width()*UP)
                fifth_row_dot=VGroup(*[Dot() for _ in range(31)]).arrange(RIGHT,buff=0.01).move_to(4*first_row_dot[0].get_width()*UP+first_row_dot[0].get_width()/2*LEFT)
                sixth_row_dot=VGroup(*[Dot() for _ in range(31)]).arrange(RIGHT,buff=0.01).move_to(5*first_row_dot[0].get_width()*UP)
                seventh_row_dot=VGroup(*[Dot() for _ in range(21)]).arrange(RIGHT,buff=0.01).move_to(6*first_row_dot[0].get_width()*UP+first_row_dot[0].get_width()/2*LEFT)
                ninth_row_dot=VGroup(*[Dot() for _ in range(31)]).arrange(RIGHT,buff=0.01).move_to(7*first_row_dot[0].get_width()*UP)
                tenth_row_dot=VGroup(*[Dot() for _ in range(31)]).arrange(RIGHT,buff=0.01).move_to(8*first_row_dot[0].get_width()*UP+first_row_dot[0].get_width()/2*LEFT)
                eleventh_row_dot=VGroup(*[Dot() for _ in range(31)]).arrange(RIGHT,buff=0.01).move_to(9*first_row_dot[0].get_width()*UP)
                twelveth_row_dot=VGroup(*[Dot() for _ in range(31)]).arrange(RIGHT,buff=0.01).move_to(10*first_row_dot[0].get_width()*UP+first_row_dot[0].get_width()/2*LEFT)
                return VGroup(
                        first_row_dot,second_row_dot,third_row_dot,fourth_row_dot,
                        fifth_row_dot,sixth_row_dot,seventh_row_dot,ninth_row_dot,
                        tenth_row_dot,eleventh_row_dot,twelveth_row_dot
                )
        def covid_19(self,my_dots,lista):
                def my_mob(mob):
                        mob.fade(1)
                        mob.set_color(RED)
                        return mob
                my_deaths=VGroup()
                for i in lista:
                        my_death=(my_dots[i])
                        my_deaths.add(my_death)
                self.play(LaggedStart(
                        *[ApplyFunction(my_mob,my_death,run_time=1)
                        for my_death in my_deaths]
                ))
class MakePhase(Scene):
        def construct(self):
                my_points=self.get_points(100)
                self.play(ShowCreation(my_points))
                self.wait()
        def get_points(self,number):
                points=VGroup(*[Dot() for _ in range(number)]).arrange_in_grid()
                return points
class MakingCircle(Scene):
        def construct(self):
                def mob_func(mob):
                        mob.scale(1.5)
                        mob.set_color(RED)
                        return mob
                my_dots=self.get_my_circles(0.1,ORIGIN,6)
                my_dots.save_state()
                self.play(ShowCreation(my_dots))
                self.play(LaggedStart(*[
                        ApplyFunction(
                                mob_func,my_dot,run_time=3,rate_func=there_and_back)
                                for my_dot in my_dots
                        ]
                ))
                self.get_contagious()
        def get_my_circles(self,radio,center,number):
                first_dot=Dot(radius=radio+0.01).move_to(center)
                first_dot.radio=radio
                second_place=[rotate_vector(2*RIGHT*first_dot.radio,TAU*n/number) for n in range(number)]
                dots_1=VGroup(*[Dot(radius=first_dot.radio).move_to(place) for place in second_place])
                third_place=[rotate_vector(4*RIGHT*first_dot.radio,(TAU)*n/12+TAU/6) for n in range(12)]
                dots_2=VGroup(*[Dot(radius=first_dot.radio).move_to(place) for place in third_place])
                place_3=[rotate_vector(6*RIGHT*first_dot.radio,(TAU)*n/18) for n in range(18)]
                dots_3=VGroup(*[Dot(radius=first_dot.radio).move_to(place) for place in place_3])
                place_4=[rotate_vector(8*RIGHT*first_dot.radio,(TAU)*n/24+TAU/6) for n in range(24)]
                dots_4=VGroup(*[Dot(radius=first_dot.radio).move_to(place) for place in place_4])
                place_5=[rotate_vector(10*RIGHT*first_dot.radio,(TAU)*n/30) for n in range(30)]
                dots_5=VGroup(*[Dot(radius=first_dot.radio).move_to(place) for place in place_5])
                place_6=[rotate_vector(12*RIGHT*first_dot.radio,(TAU)*n/36) for n in range(36)]
                dots_6=VGroup(*[Dot(radius=first_dot.radio).move_to(place) for place in place_6])
                place_7=[rotate_vector(14*RIGHT*first_dot.radio,(TAU)*n/42) for n in range(42)]
                dots_7=VGroup(*[Dot(radius=first_dot.radio).move_to(place) for place in place_7])
                place_8=[rotate_vector(16*RIGHT*first_dot.radio,(TAU)*n/48) for n in range(48)]
                dots_8=VGroup(*[Dot(radius=first_dot.radio).move_to(place) for place in place_8])
                place_9=[rotate_vector(18*RIGHT*first_dot.radio,(TAU)*n/54) for n in range(54)]
                dots_9=VGroup(*[Dot(radius=first_dot.radio).move_to(place) for place in place_9])
                place_10=[rotate_vector(20*RIGHT*first_dot.radio,(TAU)*n/60) for n in range(60)]
                dots_10=VGroup(*[Dot(radius=first_dot.radio).move_to(place) for place in place_10])
                return VGroup(first_dot,dots_1,dots_2,dots_3,dots_4,dots_5,dots_6,dots_7,dots_8,dots_9,dots_10)
        def get_contagious(self):
                my_dots=self.get_my_circles(0.1,ORIGIN,6)
                indices=len(my_dots)
                index_partials=[]
                for group in self.get_my_circles(0.1,ORIGIN,6):
                        index=len(group)
                        index_partials.append(index)
                my_dots.save_state()
                for t,i in zip(range(len(my_dots)),[0,4,5,8,6,2,7,25,15,32,29]):        
                        self.play(my_dots[t][i].set_color,RED_C)
                self.play(my_dots.restore)
                for t in range(len(my_dots)):        
                        self.play(my_dots[t].set_color,RED_C)
class MyOwnCriature(VGroup):
        CONFIG={
                "torse":[1.4,2],
                "arm":[.7,1.7],
                "leg":[.7,1.7],
                "head_body":.67,
                "body_kwargs":{
                        "stroke_width":2,
                        "stroke_color":BLACK,
                        "fill_color":WHITE,
                        "fill_opacity":1
                }
        }
        def __init__(self,scale,**kwargs):
                VGroup.__init__(self,**kwargs)
                torse=self.my_torse()
                arms=self.my_arms(torse)
                legs=self.my_legs(torse)
                head=self.my_head(torse)
                self.add(torse,arms,legs,head)
                self.scale(scale)
        def my_torse(self):
                return Rectangle(width=self.torse[0],height=self.torse[1],**self.body_kwargs)
        def my_arms(self,torse):
                arm1=Rectangle(width=self.arm[0],height=self.arm[1],**self.body_kwargs)
                arm2=arm1.copy()
                return VGroup(arm1,arm2).arrange(RIGHT,buff=self.torse[0]+0.16)\
                        .move_to(torse.get_center())
        def my_legs(self,torse):
                leg1=Rectangle(width=self.leg[0],height=self.leg[1],**self.body_kwargs)
                leg2=leg1.copy()
                my_legs=VGroup(leg1,leg2).arrange(RIGHT,buff=0.07)\
                        .next_to(torse,DOWN,buff=0.08)
                return my_legs
        def my_head(self,torse):
                return Circle(radius=self.head_body,**self.body_kwargs)\
                        .next_to(torse,UP,buff=0.08)

class MakeLastScene(Scene):
        CONFIG={
                'amplitud':2
        }
        def construct(self):
                my_person=self.get_my_path(PI/6)
                self.play(ShowCreation(my_person))
        def get_my_path(self,angle):
                circle=Circle(radius=self.amplitud)
                my_person=MyOwnCriature(.3)
                my_person.rotate((-angle%(2*PI))+(2*PI),about_point=my_person.get_center())
                my_person.circle=circle
                my_person.circle.rotate(angle,about_point=my_person.circle.get_center())
                my_person.shift(my_person.circle.point_from_proportion(0))
                return my_person

class MakeMyScene(Scene):
        CONFIG={
                'amplitude':3,
                'tex_0':'Covid-19',
                'tex_1':'Peste Justiniana',
                'tex_2':'VIH/Sida',
                'tex_3':'Gripe Española',
                'tex_4':'Viruela',
                'tex_5':'Peste Negra',
        }
        def construct(self):
                my_first_body=MyOwnCriature(.3)
                my_bodies=self.get_my_bodies(7)
                my_first_body.move_to(my_bodies.get_center())
                self.play(ShowCreation(my_bodies),DrawBorderThenFill(my_first_body))
                anims=[]
                for t in range(len(my_bodies)):
                        anim=self.get_angles(my_bodies[t],0)
                        anims.append(anim)
                self.play(*anims,run_time=10)
                self.wait()
                self.play(my_first_body.set_fill,{'color':RED_D,'opacity':1})
                self.wait()
                for t in range(len(my_bodies)):
                        self.play(my_first_body.move_to,my_bodies[t],rate_func=there_and_back)
                        self.play(my_bodies[t].set_fill,{'color':RED_D,'opacity':1})
                for t in [0,2,5,6]:
                        self.play(my_bodies[t].set_fill,{'color':WHITE,'opacity':1})
                for mob in [my_first_body,my_bodies]:
                        self.play(FadeOut(mob))
                my_bodies_2=VGroup()
                my_angles_2=[]
                for i in [5,7,8,12,18,24]:
                        angles=[(TAU*t/i) for t in range(i)]
                        my_angles_2.append(angles)
                for n in [5,7,8,12,18,24]:
                        my_body=self.get_my_bodies(n)
                        my_bodies_2.add(my_body)
                my_bodies_2.scale(0.3)
                my_bodies_2.arrange(RIGHT)
                self.play(ShowCreation(my_bodies_2))
                anims_1=[]
                anims_2=[]
                anims_3=[]
                anims_4=[]
                anims_5=[]
                anims_6=[]
                for t in range(len(my_bodies_2[0])):
                        anim_1=self.get_angles_2(my_bodies_2[0][t],my_bodies_2[0].get_center(),3*.3,0)
                        anims_1.append(anim_1)
                for t in range(len(my_bodies_2[1])):
                        anim_2=self.get_angles_2(my_bodies_2[1][t],my_bodies_2[1].get_center(),3*.3,0)
                        anims_2.append(anim_2)
                for t in range(len(my_bodies_2[2])):
                        anim_3=self.get_angles_2(my_bodies_2[2][t],my_bodies_2[2].get_center(),3*.3,0)
                        anims_3.append(anim_3)
                for t in range(len(my_bodies_2[3])):
                        anim_4=self.get_angles_2(my_bodies_2[3][t],my_bodies_2[3].get_center(),3*.3,0)
                        anims_4.append(anim_4)
                for t in range(len(my_bodies_2[4])):
                        anim_5=self.get_angles_2(my_bodies_2[4][t],my_bodies_2[4].get_center(),3*.3,0)
                        anims_5.append(anim_5)
                for t in range(len(my_bodies_2[5])):
                        anim_6=self.get_angles_2(my_bodies_2[5][t],my_bodies_2[5].get_center(),3*.3,0)
                        anims_6.append(anim_6)
                self.play(*anims_1,*anims_2,*anims_3,*anims_4,*anims_5,*anims_6,run_time=10)
                for i in range(len(my_bodies_2)):
                        letter=getattr(self,'tex_{}'.format(i))
                        letter_tex=Tex(letter)
                        letter_tex.next_to(my_bodies_2[i],DOWN,buff=0.6)
                        letter_tex.match_width(my_bodies_2[i])
                        self.play(Write(letter_tex))
                self.wait()
                for i in range(len(my_bodies_2)):
                        self.get_center_body(my_bodies_2[i])
                self.wait()
        def get_my_bodies(self,numbers):
                positions=[rotate_vector(self.amplitude*RIGHT,TAU*t/numbers) for t in range(numbers)]
                bodies=VGroup(*[MyOwnCriature(0.3).\
                        move_to(position) for _,position in zip(range(numbers),positions)])
                return bodies
        def get_angles(self,point_mob,d_theta):
                curr_angle=angle_of_vector(point_mob.get_center())
                d_theta=(d_theta+np.pi)%(2*PI)-(2*np.pi)
                new_theta=curr_angle+d_theta
                def update_point(point_mob,alpha):
                        theta=interpolate(curr_angle,new_theta,3*alpha)
                        point_mob.move_to(self.amplitude*RIGHT*np.cos(theta)+self.amplitude*UP*np.sin(theta))
                        return point_mob
                return UpdateFromAlphaFunc(point_mob,update_point)
        def get_angles_2(self,point_mob,center,amplitud,d_theta):
                curr_angle=angle_of_vector(point_mob.get_center()-center)
                d_theta=(d_theta+np.pi)%(2*PI)-(2*np.pi)
                new_theta=curr_angle+d_theta
                def update_point(point_mob,alpha):
                        theta=interpolate(curr_angle,new_theta,3*alpha)
                        point_mob.move_to(center+amplitud*RIGHT*np.cos(theta)+amplitud*UP*np.sin(theta))
                        return point_mob
                return UpdateFromAlphaFunc(point_mob,update_point)
        def get_center_body(self,group_mob):
                center=group_mob.get_center()
                my_body_center=MyOwnCriature(.3**2).move_to(center)
                self.play(FadeIn(my_body_center))
                self.play(my_body_center.set_fill,{'color':RED_B,'opacity':1})
                for i in range(len(group_mob)):
                        self.play(my_body_center.move_to,group_mob[i],rate_func=there_and_back,run_time=.3)
                        self.play(group_mob[i].set_fill,{'color':RED_B,'opacity':1},run_time=.3) 

class GhostLine(Line):
        def __init__(self,init,end,**kwargs):
                super().__init__(init,end,color=RED)
                self.fade(0)
                rectangle=self.get_rectangle()
                self.add(rectangle)
        def get_rectangle(self):
                rectangle=Rectangle(
                        stroke_width=1,
                        stroke_color=WHITE,
                        fill_color=ORANGE,
                        fill_opacity=0.8,
                        height=0.4
                )
                rectangle.match_width(self)
                rectangle.move_to(self)
                return  rectangle
class MyGraph(Scene):
        CONFIG={
                'line_kwargs':{
                        'x_min':0,
                        'x_max':100,
                        'stroke_width':2,
                        'stroke_color':BLUE,
                        'unit_size':1,
                        'include_numbers':False,
                        'exclude_zero_from_default_numbers':False,
                        'step_label':5
                },
                'line_ill_kwargs':{
                        'stroke_width':25,
                        'stroke_opacity':0.4,
                }
        }
        def construct(self):
                self.texto=Tex('Covid 19').to_edge(UP,buff=0.4)
                axes=self.get_my_number_line(self.CONFIG['line_kwargs']['x_min'],self\
                        .CONFIG['line_kwargs']['x_max'],self.CONFIG['line_kwargs']['step_label'])
                rect_ill=self.get_my_rectangles(axes[0],0,5)
                rect_health=self.get_my_rectangles(axes[0],5,100,BLUE_C)
                self.play(Write(self.texto))
                self.play(ShowCreation(axes),ShowCreation(rect_ill),ShowCreation(rect_health))
                self.play(axes[0].set_width,.5*FRAME_WIDTH,{'about_edge':axes[0]\
                        .number_to_point(0),'stretch':True,},run_time=5,rate_func=smooth)
                self.wait()
                people=self.my_people(10)
                my_pack=VGroup(people,axes,rect_health,rect_ill)
                #colored_people=self.get_infected(people)
                self.play(ShowCreation(people))
                self.add(my_pack)
                my_pack.add_updater(self.get_update_people)
                self.wait(16)
        def get_my_number_line(self,x_min,x_max,step_label):
                my_number_line=NumberLine(**self.line_kwargs)
                my_number_line.move_to(1.5*UP).to_edge(LEFT)
                if my_number_line.get_width()<FRAME_WIDTH:
                        my_number_line.set_width(FRAME_WIDTH)
                my_numbers=VGroup()
                for x in range(x_min,x_max+1,step_label):
                        my_number=MathTex(f'{x}')
                        my_number.scale(0.7)
                        my_number.next_to(my_number_line.number_to_point(x),DOWN,buff=0.2)
                        my_numbers.add(my_number)
                def get_update(my_numbers):
                        for i,my_number in zip(range(x_min,x_max+1,step_label),my_numbers):
                                my_number.next_to(my_number_line.number_to_point(i),DOWN,buff=0.2)
                my_numbers.add_updater(get_update)
                return VGroup(my_number_line,my_numbers)
        def get_my_rectangles(self,axes,init,end,color=RED_A):
                ghost_line=Line(axes.n2p(init),axes.n2p(end),stroke_color=color,**self.line_ill_kwargs)
                def get_update_group(line):
                        line.put_start_and_end_on(axes.n2p(init),axes.n2p(end))
                ghost_line.add_updater(get_update_group)
                return ghost_line
        def my_people(self,number):
                people=VGroup(*[MyOwnCriature(0.2) for _ in range(number)])
                masses=[np.random.uniform(1,5) for _ in range(number)]
                self.buff=people.get_width()/2
                L=FRAME_WIDTH-1
                for person,mass in zip(people,masses):
                        person.buff=self.buff
                        person.mass=mass
                        person.center=op.add(
                                np.random.uniform(-FRAME_X_RADIUS-2,FRAME_X_RADIUS-2)*RIGHT,
                                DOWN*2
                        )
                        person.velocity=rotate_vector(
                                np.random.uniform(-1,1)*RIGHT,0
                        )
                        person.move_to(person.center)
                people.move_to(DOWN*2)
                return people
        def get_update_people(self,pack,dt):
                people,axes,rect_health,rect_ill=pack
                for person in people:
                        person.center+=person.velocity*dt
                        if abs(person.center[0])+self.buff>FRAME_X_RADIUS-2:
                                person.center[0]=np.sign(person.center[0])*(FRAME_X_RADIUS-2-self.buff)
                                person.velocity[0]*=-1*op.mul(np.sign(person.velocity[0]),np.sign(person.center[0]))
                        person.move_to(person.center)
                self.get_infected(people,axes,rect_health,rect_ill)
                return pack
        def get_infected(self,people,axes,health,ill):#,ill_bar,health_bar):
                person_infected=people[0].set_fill(opacity=1,color=RED)
                #for t in lista:
                #        contagious.add(person_contagious)
                for person in people:
                        person.is_infected=False
                        dist=get_norm(person.center-person_infected.center)
                        person.will_be_infected=dist<=person.buff+person_infected.buff
                        if not(person.is_infected) and person.will_be_infected:
                                person.set_fill(color=RED,opacity=1)
                                health.set_width(axes[0].unit_size,)
                        person.will_be_infected=person.is_infected
                return VGroup(people,axes,health,ill)

class ProofColor(Scene):
        CONFIG={
                "my_zero":0
        }
        def construct(self):
                square1=Square(fill_color=RED,fill_opacity=.5)
                square1.velocity=RIGHT
                square1.center=4*LEFT
                square1.move_to(square1.center)
                square2=Square(fill_color=BLUE,fill_opacity=.5)
                square2.velocity=LEFT
                square2.center=4*RIGHT
                square1.radius=square1.get_width()/2
                square2.radius=square2.get_width()/2
                square2.move_to(square2.center)
                squares=VGroup(square1,square2)
                def get_update(mobs,dt):
                        mob_0=mobs[0]
                        for mob in mobs:
                                mob.center+=mob.velocity*dt #modifique esto porque de lo contrario si coloco la linea eliminanda de abajo solo se mueve un cuadro
                                mob.move_to(mob.center+self.my_zero)
                                mob.is_infected=False
                                dist=get_norm(mob_0.center-mob.center)
                                mob.will_be_infected=dist<=(mob_0.radius+mob.radius)
                                if not(mob.is_infected) and mob.will_be_infected:
                                        mob.set_color(YELLOW)
                                else:
                                        mob.set_color(BLUE)
                                mob.is_infected=mob.will_be_infected
                                #self.my_zero+=mob.center
                        return mobs
                squares.add_updater(get_update)
                self.add(squares)
                self.wait(10)

class MyProofColor2(Scene):
        CONFIG={
                'cero':0
        }
        def construct(self):
                my_squares=[]
                for side in [LEFT,RIGHT]:
                        my_square=self.get_my_square(side)
                        self.add(my_square)
                        my_square.add_updater(self.get_my_square_update)
                        self.add(my_square)
                        my_squares.append(my_square)
                self.wait()
        def get_my_square(self,position):
                my_square=Square()
                my_square.set_fill(BLUE)
                my_square.set_opacity(.5)
                my_square.center=3*position
                my_square.velocity=-position*0.5
                my_square.radius=my_square.get_width()/2
                my_square.move_to(my_square.center)
                return my_square
        def get_my_square_update(self,square,dt):
                square.center+=square.velocity*dt
                square.move_to(square.center+self.cero)
                return square
        def get_my_count(self,squares):
                for square_1 in squares:
                        pass

class PruebaAnchura(Scene):
        def construct(self):
                axes=NumberLine()
                rect=Rectangle(width=abs(axes.n2p(8)[0]))
                rect.move_to(axes.n2p(-3),rect.get_left())
                def update_rect(rect_0):
                        rect_0.move_to(axes.n2p(-3),rect_0.get_left())
                        rect_0.set_width(abs(axes.n2p(8)[0]),{'stretch':True})
                rect.add_updater(update_rect)
                self.play(ShowCreation(axes),ShowCreation(rect))
                self.play(axes.set_width,FRAME_X_RADIUS-2,{'stretch':True})
                self.wait()

class PruebaAnchura2(Scene):
        def construct(self):
                axes=NumberLine(x_min=0,x_max=7)
                axes.to_edge(LEFT)
                rectangle=GhostLine(axes.n2p(0),axes.n2p(4))
                def update_line(line_0):
                        line_0.put_start_and_end_on(axes.n2p(0),axes.n2p(4))
                rectangle.add_updater(update_line)
                self.play(ShowCreation(axes),ShowCreation(rectangle))
                self.play(axes.set_width,FRAME_X_RADIUS-2,{'stretch':True,'about_point':axes.n2p(0)})
                self.wait()

class PartToPart(Scene):
        def construct(self):
                cuadro=Square()
                doos=VGroup(*[Dot() for _ in range(8)]).arrange(RIGHT)
                circulo=Circle()
                cuadro.add(circulo,doos)
                self.play(ShowCreation(cuadro))
                self.wait()

class ProofWithReverse(Scene):
        def construct(self):
                pass
        def get_rect(self):
                rect=NumberLine()
                return line
        def get_dot(self,rect):
                dots=VGroup(*[Dot() for _ in range(5)])
                for dot in dots:
                        dot.center=rect.n2p(np.random.random())
                        dot.velocity=np.random.uniform(-1,1)*RIGHT
                dot.rect=rect
                return dot
        def get_dot_update(self,dot):
                dot.center+=dot.velocity*RIGHT
class Definitely(Scene):
        CONFIG={
                'my_zero':0,
                'square_kwargs':{
                        'color_fill':YELLOW,
                        'opacity_fill':.6
                }
        }
        def construct(self):
                square_1=self.get_atributes(LEFT,color=RED,pivot=True)
                square_2=self.get_atributes(RIGHT,color=RED)
                count=self.my_count(square_2)
                my_axes=self.get_my_axes(square_2)
                my_bar=self.get_bar(my_axes,square_2)
                self.add(count,square_1,square_2,my_axes,my_bar)
                self.wait(7)
        def get_atributes(self,side,color=RED,pivot=False):
                square=Square(**self.square_kwargs)
                square.radius=square.get_width()/2
                square.color=color
                square.center=4*side
                square.velocity=-side
                square.is_pivot=False
                if pivot:
                        self.square=square
                square.move_to(square.center)
                square.add_updater(self.get_update)
                return square
        def get_update(self,square,dt):
                square.center+=square.velocity*dt
                square.move_to(square.center)
                dist=get_norm(self.square.center-square.center)
                square.will_be_pivot=dist<=self.square.radius+square.radius
                if (square.is_pivot) or square.will_be_pivot: ###elimine el not
                        square.set_fill(color=GREEN,opacity=0.6)
                else:
                        square.set_fill(color=RED,opacity=.6)
        def my_count(self,square):
                count=Integer(1)
                count.to_edge(UR)
                count.square=square
                count.add_updater(self.get_update_count)
                return count
        def get_update_count(self,count):
                dist=get_norm(self.square.center-count.square.center)
                count.square.will_be_pivot=dist<=self.square.radius+count.square.radius # si se pone un 1 ahi si resulta
                if (not count.square.is_pivot) and count.square.will_be_pivot:
                        count.increment_value()
                count.square.is_pivot=count.square.will_be_pivot
        def get_my_axes(self,square):
                axes=NumberLine(x_min=0,x_max=8,include_numbers=True)
                axes.to_corner(DL)
                axes.square=square
                return axes
        def get_bar(self,axes,square):
                line=Line(axes.n2p(0),axes.n2p(0.001),unit_size=1)
                line.set_stroke(width=14)
                line.axes=axes
                line.set_opacity(0.6)
                line.square=square
                line.add_updater(self.get_update_line)
                line.move_to(axes.n2p(0),line.get_left())
                return line
        def get_update_line(self,line):
                line.move_to(line.axes.n2p(0),line.get_left())
                dist=get_norm(line.square.center-self.square.center)
                line.will_be_pivot=dist<=line.square.radius+self.square.radius
                if not(line.square.is_pivot) and line.will_be_pivot:
                        line.set_width(line.axes.unit_size,{'stretch':True,'about_point':line.axes.number_to_point(0)})
                line.square.is_pivot=line.will_be_pivot

class MyContagious(Scene):
        CONFIG={
                'rect_kwargs':{
                        'x_min':0,
                        'x_max':100,
                        'tick_frequency':5,
                        'step_label':5,
                        'stroke_width':2,
                        'stroke_color':BLUE_A
                },
                'line_kwargs':{
                        'stroke_width':15,
                        'stroke_opacity':0.5
                }
        }
        def construct(self):
                my_rect=self.get_my_rect()
                healthy_people=VGroup(*[self.get_person() for _ in range(20)])
                ill_people=VGroup(*[self.get_person(health=False) for _ in range(2)])
                people=VGroup(healthy_people,ill_people)
                healthy_people.my_rect=my_rect
                ill_people.my_rect=my_rect
                well_bar=self.get_my_lines(people,my_rect)
                bad_bar=self.get_my_lines(people,my_rect,False)
                anims=[
                        my_rect,
                        well_bar,
                        bad_bar,
                        people,
                ]
                for anim in anims:
                        self.add(anim)
                people.add_updater(self.get_person_update)
                self.play(my_rect[0].set_width,.5*FRAME_WIDTH,{'about_edge':my_rect[0].n2p(0),'stretch':True,})
                self.wait(10)
        def get_my_rect(self):
                my_rect=NumberLine(**self.rect_kwargs)
                my_rect.move_to(0.4*UP)
                my_rect.to_edge(LEFT)
                numbers=VGroup()
                for x in range(self.CONFIG['rect_kwargs']['x_min'],self.\
                        CONFIG['rect_kwargs']['x_max']+1,self.CONFIG['rect_kwargs']['step_label']):
                        number=MathTex(f'{x}')
                        number.scale(0.5)
                        number.next_to(my_rect.number_to_point(x),DOWN,buff=0.3)
                        numbers.add(number)
                def get_update_number(numbers):
                        for i,number in zip(range(self.CONFIG['rect_kwargs']['x_min'],self.\
                                CONFIG['rect_kwargs']['x_max']+1,self.CONFIG['rect_kwargs']['step_label']),numbers):
                                number.next_to(my_rect.n2p(i),DOWN,buff=.3)
                numbers.add_updater(get_update_number)
                return VGroup(my_rect,numbers)
        def get_person(self,health=True):
                person=MyOwnCriature(0.4)
                person.scale(0.4)
                person.center=np.random.uniform(-FRAME_X_RADIUS/2,FRAME_X_RADIUS/2)*RIGHT+DOWN*2
                weight=np.random.uniform(-1,1)*5
                person.velocity=RIGHT*weight
                person.buff=person.get_width()/2
                if health:
                        person.set_fill(BLUE_B)
                else:
                        person.set_fill(RED_B)
                person.move_to(person.center)
                person.is_infected=False
                return person
        def get_person_update(self,people,dt):
                count=Integer(1)
                people.count=count
                people_health,people_ill=people
                for person_health in people_health:
                        for person_ill in people_ill:
                                if person_health is person_ill:
                                        continue
                                dist=get_norm(person_health.center-person_ill.center)
                                person_health.will_be_infected=dist<person_health.buff+person_ill.buff+3
                                if person_health.will_be_infected:
                                        person_health.set_fill(RED_B)
                                        count.increment_value()
                                else:
                                        person_health.set_fill(BLUE_B)
                for person_health in people[0]:
                        person_health.center+=person_health.velocity*dt
                        if abs(person_health.center[0])>FRAME_X_RADIUS/2:
                                person_health.center[0]=np.sign(
                                        person_health.center[0])*(FRAME_X_RADIUS/2
                                )
                                person_health.velocity[0]*=-1*op.mul(
                                        np.sign(person_health.velocity[0]),np.sign(person_health.center[0])
                                )
                        person_health.move_to(person_health.center)
                return people
        def get_my_lines(self,people,line,heath=True):
                line_population=Line()
                line_population.people=people
                if heath:
                        line_population.set_style(**self.line_kwargs)
                        line_population.put_start_and_end_on(line[0].n2p(0),line[0].n2p(5))
                        line_population.set_color(BLUE_B)
                        line_population.move_to(line[0].number_to_point(0),line_population.get_left())
                        line_population.add_updater(lambda t: t.put_start_and_end_on(line[0].n2p(0),line[0].n2p(5)))
                        line_population.add_updater(self.get_people_update)
                else:
                        line_population.set_style(**self.line_kwargs)
                        line_population.put_start_and_end_on(line[0].n2p(5),line[0].n2p(100))
                        line_population.set_color(RED_B)
                        line_population.move_to(line[0].number_to_point(100),line_population.get_right())
                        line_population.add_updater(lambda t: t.put_start_and_end_on(line[0].n2p(5),line[0].n2p(100)))
                return line_population

class HistogramCovid19(Scene):
        CONFIG={
                'axis_config':{
                        'x_min':0,
                        'x_max':5,
                        'x_axis_config':{
                                'tick_frequency':1,
                                'unit_size':1
                        },
                        'y_min':0,
                        'y_max':.7,
                        'y_axis_config':{
                                'tick_frequency':.2,
                                'unit_size':7,
                        },
                        'stroke_width':2,
                        'color':RED,
                        'center_point':6*LEFT+2*DOWN,
                },
                'countries':['Brazil','EEUU','Iran','China'],
                'colors':[GREEN,RED,YELLOW,BLUE,ORANGE],
                'rect_kwargs':{
                        'x_min':0,
                        'x_max':4,
                        'exclude_zero_from_default_numbers':True,
                        'leftmost_tick':1,
                        'stroke_width':1
                },
        }
        def construct(self):
                axes=self.get_axes()
                bars=self.get_bars(axes)
                countries=self.get_tex_with_color(bars,axes)
                anims=[axes,bars,countries[0]]
                essaies=10000
                my_scores=np.array([self.random_points() for x in range(essaies)])
                index_traker=ValueTracker(essaies)
                def get_index():
                        value=index_traker.get_value()
                        return int(value)
                bars.add_updater(lambda t: self.set_histogram_bars(t,my_scores[:get_index()],axes))
                for anim in anims:
                        self.play(ShowCreation(anim))
                self.wait()
                self.add(bars)
                for t in range(len(countries[0])):
                        self.play(TransformFromCopy(countries[0][t],countries[1][t]))
                self.wait()
                my_rects=self.get_rects(bars)
                my_criatures=self.get_my_people(countries[1],my_rects)
                my_criatures.add_updater(lambda t: self.set_my_people_update(t,my_scores[:get_index()]))
                titulo=Tex('Covid-19').to_edge(UP,buff=0.4)
                for mob in [titulo]:
                        self.play(FadeIn(mob))
                my_rects.next_to(countries[1],RIGHT,buff=.3)
                my_ghost_lines=self.get_my_ghost_rects(my_rects)
                my_ghost_lines_neg=self.get_my_ghost_rects(my_rects,health=False)
                my_ghost_lines.add_updater(lambda t: self.set_my_ghost_rects(t,my_scores[:get_index()]))
                my_ghost_lines_neg.add_updater(lambda t: self.set_my_ghost_rects_ill(t,my_ghost_lines))
                self.play(*[FadeIn(mob) for mob in [my_rects,my_criatures,my_ghost_lines,my_ghost_lines_neg]])
                for value in [10,100,1000,10000]:
                        anims=[
                                ApplyMethod(
                                        index_traker.set_value,value,
                                        rate_func=linear,
                                        run_time=14
                                )
                        ]
                        self.play(*anims)
                self.wait()
        def get_axes(self):
                axes=Axes(**self.axis_config)
                title_x_axis=Tex('Countries').scale(.5)
                title_x_axis.next_to(axes.x_axis,RIGHT,buff=0.1)
                title_y_axis=Tex('Frequency').scale(.5)
                title_y_axis.next_to(axes.y_axis,UP,buff=0.1)
                axes.title_x_axis=title_x_axis
                axes.title_y_axes=title_y_axis
                axes.add(title_x_axis,title_y_axis)
                return axes
        def get_bars(self,axes):
                bars=VGroup()
                bars.axes=axes
                for x in range(
                        self.CONFIG['axis_config']['x_min']+1,
                        self.CONFIG['axis_config']['x_max'],
                        self.CONFIG['axis_config']['x_axis_config']['unit_size']
                ):
                        bar=Rectangle(width=axes.x_axis.unit_size)
                        bar.move_to(axes.coords_to_point(x,0),DOWN)
                        bar.x=x
                        bars.add(bar)
                self.get_color_bar(bars)
                return bars
        def get_color_bar(self,bars):
                for bar,color in zip(bars,self.colors):
                        bar.set_fill(color=color,opacity=1)
                        bar.set_stroke(width=.5,color=BLACK)
                        bar.color=color
                return bars
        def get_tex_with_color(self,bars,axes):
                teXs=VGroup()
                teXs_copy=VGroup()
                for bar,country in zip(bars,self.countries):
                        teX=Tex(country)
                        teX.set_color(bar.color)
                        teX.scale(0.6)
                        teX_copy=teX.copy()
                        teX.next_to(bars.axes.c2p(bar.x),DOWN,buff=.5)
                        teX.rotate(PI/2)
                        teX.bar=bar
                        teXs_copy.add(teX_copy)
                        teXs.add(teX)
                teXs_copy.arrange(DOWN,buff=1.3)
                teXs_copy.move_to(ORIGIN+RIGHT)
                return VGroup(teXs,teXs_copy)
        def get_relative_proporticon(self,all_changes):
                my_ponds=set(all_changes)
                n_changes=len(all_changes)
                return dict([
                        (p,np.sum(all_changes==p)/n_changes)
                        for p in my_ponds
                ])
        def set_histogram_bars(self,bars,scores,axes):
                prop_map=self.get_relative_proporticon(scores)
                epsilon=1e-5
                for bar in bars:
                        prop=prop_map.get(bar.x,epsilon)
                        bar.set_height(
                                prop*axes.y_axis.unit_size,
                                stretch=True,
                                about_edge=DOWN
                                #{
                                #        'stretch':True,        ##no funciona con esto
                                #        'about_edge':DOWN
                                #}
                        )
        def random_points(self):
                score=1
                radius=1
                while True:
                        hit_radius=get_norm(np.random.uniform(-1,1,size=2))
                        if hit_radius>radius:
                                return score
                        else:
                                score+=1
                                radius=np.sqrt(1-hit_radius**2)
        def get_rects(self,bars):
                rects=VGroup()
                for bar in bars:
                        rect=NumberLine(**self.rect_kwargs).fade(.5)
                        rect.set_width(5)
                        rect.bar=bar
                        rects.add(rect)
                rects.arrange(DOWN,buff=1)
                return rects
        def get_my_people(self,mob_color,rects):
                my_criatures=VGroup()
                for rect in rects:
                        my_criature=MyOwnCriature(.2).scale(.4)
                        my_criature.set_fill(rect.bar.color)
                        my_criature.rect=rect
                        my_criatures.add(my_criature)
                return my_criatures
        def set_my_people_update(self,criatures,score):
                my_promps=self.get_relative_proporticon(score)
                epsilon=5
                for criature in criatures:
                        my_promp=my_promps.get(criature.rect.bar.x,epsilon)
                        copy_criature=VGroup(*[(criature) for _ in range(len(criature))])
                        for criat in copy_criature:
                                criat.move_to(criature.rect.number_to_point(my_promp*5)+0.3*UP)
        def get_my_ghost_rects(self,rects,health=True):
                my_lines=VGroup()
                for rect in rects:
                        if health:
                                my_line=Line()
                                my_line.set_stroke(color=BLUE,opacity=0.5,width=15)
                                my_line.move_to(rect.number_to_point(0),my_line.get_start())
                                my_line.rect=rect
                                my_lines.add(my_line)
                        else:
                                my_line=Line()
                                my_line.set_stroke(color=RED,opacity=0.5,width=15)
                                my_line.move_to(rect.number_to_point(4),my_line.get_start())
                                my_line.rotate(PI)
                                my_line.rect=rect
                                my_lines.add(my_line)
                return my_lines
        def set_my_ghost_rects(self,lines,scores):
                my_promps=self.get_relative_proporticon(scores)
                epsilon=4
                for line in lines:
                        my_promp=my_promps.get(line.rect.bar.x,epsilon)
                        line.set_width(my_promp*6.2,stretch=True,about_point=line.rect.number_to_point(0)) 
        def set_my_ghost_rects_ill(self,lines,healths):
                for line,health in zip(lines,healths):
                        line.put_start_and_end_on(health.get_right(),line.rect.number_to_point(4))