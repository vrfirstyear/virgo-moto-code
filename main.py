maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 100)
basic.pause(1000)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 100)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 100)
basic.pause(1000)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 100)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 100)
basic.pause(1000)
maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 100)
basic.pause(1000)
maqueen.motor_stop(maqueen.Motors.ALL)