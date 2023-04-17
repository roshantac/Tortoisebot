import RPi.GPIO as GPIO
import time



class motorControll:
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		#pin configuration
		self.leftEn       = 13 #purple
		self.rightEn      = 12 #red
		self.leftForward  = 6  #Green 
		self.leftBackward = 5  #blue
		self.rightForward = 16 #yellow
		self.rightBackward= 20 #orange
		
		self.max_pwm_val = 100.0
		self.min_pwm_val = 0.0
		
		self.motor_rpm = 60.0
		self.wheel_diameter = 0.065
		self.wheel_separation = 0.17
		
		self.wheel_radius = self.wheel_diameter/2
		self.circumference_of_wheel = 2*3.14*self.wheel_radius
		self.maxSpeed = (self.circumference_of_wheel*self.motor_rpm)/60.0
		
					
		GPIO.setup(self.leftEn, GPIO.OUT)
		GPIO.setup(self.rightEn, GPIO.OUT)
		GPIO.setup(self.leftForward, GPIO.OUT)
		GPIO.setup(self.leftBackward, GPIO.OUT)
		GPIO.setup(self.rightForward, GPIO.OUT)
		GPIO.setup(self.rightBackward, GPIO.OUT)
		#pwm init
		self.pwmL = GPIO.PWM(self.leftEn, 100)
		self.pwmR = GPIO.PWM(self.rightEn,100)
		self.pwmL.start(0)
		self.pwmR.start(0)
		#self.stop()
	


	def stop(self):
		self.pwmL.ChangeDutyCycle(0)
		self.pwmR.ChangeDutyCycle(0)	
		GPIO.output(self.leftForward, GPIO.HIGH)
		GPIO.output(self.leftBackward, GPIO.HIGH)	
		
		GPIO.output(self.rightForward, GPIO.HIGH)
		GPIO.output(self.rightBackward, GPIO.HIGH)
	
	def move(self,leftSpeed, rightSpeed):
		#calculate PWM value from speed
		leftSpeedPWM =  max(min((abs(leftSpeed)/self.maxSpeed)*self.max_pwm_val, self.max_pwm_val), self.min_pwm_val)
		rightSpeedPWM =  max(min((abs(rightSpeed)/self.maxSpeed)*self.max_pwm_val, self.max_pwm_val), self.min_pwm_val)
		#change pwm
		print(" leftSpeedPWM : " , leftSpeedPWM)
		print(" rightSpeedPWM : " , rightSpeedPWM)
		
		self.pwmL.ChangeDutyCycle(int(leftSpeedPWM))
		self.pwmR.ChangeDutyCycle(int(rightSpeedPWM))
		# controlling forward and backward rotation
		if leftSpeed>=0:
			GPIO.output(self.leftForward, GPIO.HIGH)
			GPIO.output(self.leftBackward, GPIO.LOW)
		else:
			GPIO.output(self.leftForward, GPIO.LOW)
			GPIO.output(self.leftBackward, GPIO.HIGH)
			
		if rightSpeed>=0:
			GPIO.output(self.rightForward, GPIO.HIGH)
			GPIO.output(self.rightBackward, GPIO.LOW)
		else:
			GPIO.output(self.rightForward, GPIO.LOW)
			GPIO.output(self.rightBackward, GPIO.HIGH)



test = motorControll()
test.move(-60, -60)		
time.sleep(2)
test.stop()		
		
		
		
		
		
		
		
		
		
	

