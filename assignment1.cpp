#include <iostream>
using namespace std;

class Simulation
{
public:
    int Iyy, stepsize;
    float torque, time_step;
    double time, yaw, yaw_rate, acceleration;

    void calculate()
    {
        Iyy = 3800, // moment of intertia
        stepsize = 1000; 
        torque = 0.3,
        time_step = 0.01; //  1000ms = 1s -> 10ms = 0.01s
        time = 0, yaw = 0, yaw_rate = 0, acceleration = 0;

        for (int i = 0; i <= stepsize; i++)
        {

            //computing the acceleration
            acceleration = (torque * time) / Iyy;
            // implementing the Euler integration
            yaw_rate = yaw_rate + (acceleration * time_step);
            yaw = yaw + (yaw_rate * time_step);

            if (i % 100 == 0)
            {
                cout << "Time: " << time << " Yaw: " << yaw << endl;
            }
            time = time + time_step;
        }
    }
};
