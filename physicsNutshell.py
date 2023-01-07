import math
class physics:
    class kinematics:
        def find_speed_using_s_t(distance,time):
            return distance/time
        def find_speed_using_a_u_t(accleration,initial_velocity,time):
            return initial_velocity+accleration*time
        def find_speed_using_u_a_s(accleration,initial_velocity,distance):
            return math.sqrt(initial_velocity*initial_velocity+2*accleration*distance)
        def help():
            print('''
Here u means initial velocity a mean accleration t means time.
Note:
1.if you want give decleration then use - sign before accleration
            ''')
    class newton_Law:
        def find_force_using_m_a(mass,accleration):
            return mass*accleration
        def find_tension_pully(mass1,mass2):
            return (2*mass2*mass1*9.8)/(mass1+mass2)
        def help():
            print('''
Here m means  mass and a means accleration.
Note:
1.Here all the surface are taken frictionless.
2.Here gravitational accleration is taken as 9.8m/s^2.
            ''')
    class friction:
        def find_friction(friction_cofficient,Normal_force):
            return friction_cofficient*Normal_force
    class circular_motion:
        def find_centipetal_force(mass,velocity,radius):
            return (mass*velocity*velocity)/radius
        def angular_velocity(time_period):
            return 2*math.pi/time_period
        def help():
            print('''
Note:
1.Here pi is taken as 3.141592653589793
            ''')
    class energy_power_work:
        def find_kinetic_energy(mass,velocity):
            return 0.5*mass*velocity*velocity
        def find_gravitational_accleration(mass,height):
            return mass*height*9.8
        def find_work(force,displacement):
            return force*displacement
        def find_power(work,time):
            return work/time
    class rotational_mechanics:
        pass
    class gravitation:
        def find_gravitational_force(mass1,mass2,distance):
            return (mass1*mass2)/(distance*distance)
    class hydrodynamics:
        pass
    class heat:
        pass
    class harmonic_motion:
        pass
    class sound:
        def find_sound_speed(frequency,wavelength):
            return frequency*wavelength
    class eletrostatics:
        def find_eletrostatic_force(charge1,charge2,distance):
            return (9*math.pow(10,9)*charge1*charge2)/(distance*distance)
        def help():
            pass
    class capacitor:
        def find_capacitance_using_q_v(charge,voltage):
            return charge/voltage
        def find_parallal_capacitance(all_capacitance_in_list):
            l=list(all_capacitance_in_list)
            s=0
            for i in l:
                s=s+i
            return s
        def find_series_capacitance(all_capacitance_in_list):
            l=list(all_capacitance_in_list)
            s=0
            for i in l:
                s=s+1/i
            return 1/s
    class ohm_law:
        def find_resistance_using_v_i(voltage,current):
            return voltage/current
        def find_series_resistance(all_resistance_in_list):
            l=list(all_resistance_in_list)
            s=0
            for i in l:
                s=s+i
            return s
        def find_parallal_resistance(all_resistance_in_list):
            l=list(all_resistance_in_list)
            s=0
            for i in l:
                s=s+1/i
            return 1/s
        def find_resistance_using_rho_l_a(rho,length,area):
            return rho*(length/area)
        def find_current_density(current,area):
            return current/area
        def find_current_for_drift_velocity(concentration_of_electron,cross_section_area,drift_velocity):
            return concentration_of_electron*1.6*math.pow(10,-19),cross_section_area,drift_velocity
    class magnetism:
        pass
    class induction:
        def find_magnetic_flux(magnetic_field,area):
            return magnetic_field*area
    class alternating_current:
        pass
    class electromagnetic_wave:
        pass
    class optics:
        def refractive_index(speed_of_light_in_medium):
            return  299792458/speed_of_light_in_medium
    class quantum_mechanics:
        pass
    class atom:
        pass
    class semiconductor_physics:
        pass
    class digital_circuit:
        pass
    class commnication_physics:
        pass
    def ask_physics_question(enter_question):
        import webbrowser
        webbrowser.open("https://www.google.com/search?q="+enter_question)   
    def help():
        print("help")
