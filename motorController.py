import RPi.GPIO as GPIO
import time



class motorControll():
	def __init__(self):
		GPIO.setmod(GPIO.BCM)
		GPIO.setwarning(False)
		self.pinconfig()
		
		GPIO.setup(self.leftEn, GPIO.OUT)
		GPIO.setup(self.rightEn, GPIO.OUT)
		GPIO.setup(self.leftForward, GPIO.OUT)
		GPIO.setup(self.leftBackward, GPIO.OUT)
		GPIO.setup(self.rightForward, GPIO.OUT)
		GPIO.setup(self.rightBackward, GPIO.OUT)
	
	def pinConfig(self):
		self.leftEn       = 13 #purple
		self.rightEn      = 12 #red
		self.leftForward  = 6  #Green 
		self.leftBackward = 5  #blue
		self.rightForward = 16 #yellow
		self.rightBackward= 20 #orange
	def pwmInit(self):
		self.pwml = GPIO.PWM(self.leftEn, 100)
		self.pwmr = GPIO.PWM(self.rightEn,100)
	
	def move(direction, leftSpeed, rightSpeed):
		global max_pwm_val
		global min_pwm_val
		#calculate PWM value from speed
		leftSpeedPWM =  max(min(abs(leftSpeed/maxSpeed)*max_pwm_val,max_pwm_val), min_pwm_val)
		rightSpeedPWM =  max(min(abs(rightSpeed/maxSpeed)*max_pwm_val,max_pwm_val), min_pwm_val)
		#change pwm
		
		
		
		
	

