from universalcolor import Color
import pytest


# test internal color type convesrsions
def compareColors(c0: Color, c1: Color, c2: Color) -> bool:
	if abs(c0.red - c1.red) > 1 or abs(c0.red - c2.red) > 1:
		print(0, c0, c1, c2)
		return False
	if abs(c0.green - c1.green) > 1 or abs(c0.green - c2.green) > 1:
		print(1, c0, c1, c2)
		return False
	if abs(c0.blue - c1.blue) > 1 or abs(c0.blue - c2.blue) > 1:
		print(2, c0, c1, c2)
		return False
	if c1.hslLight > 0 and c1.hslLight < 1:
		if abs(c0.hslHue - c1.hslHue) > 1 or abs(c0.hslHue - c2.hslHue) > 1:
			print(3, c0, c1, c2)
			return False
		if abs(c0.hslSat - c1.hslSat) > 1 or abs(c0.hslSat - c2.hslSat) > 1:
			print(4, c0, c1, c2)
			return False
		if abs(c0.hslLight - c1.hslLight) > 1 or abs(c0.hslLight - c2.hslLight) > 1:
			print(5, c0, c1, c2)
			return False
	if c2.hsvValue > 0 and c2.hsvValue < 1:
		if abs(c0.hsvHue - c1.hsvHue) > 1 or abs(c0.hsvHue - c2.hsvHue) > 1:
			print(6, c0, c1, c2)
			return False
		if abs(c0.hsvSat - c1.hsvSat) > 1 or abs(c0.hsvSat - c2.hsvSat) > 1:
			print(7, c0, c1, c2)
			return False
		if abs(c0.hsvValue - c1.hsvValue) > 1 or abs(c0.hsvValue - c2.hsvValue) > 1:
			print(8, c0, c1, c2)
			return False
	if c0.alpha != c1.alpha or c0.alpha != c2.alpha:
		print(9, c0, c1, c2)
		return False

	return True


# kwargs rgb floats constructor
@pytest.mark.rgb
@pytest.mark.floats
@pytest.mark.kwargs
def test_rgb_floats(float_tuples):
	print('')
	for td in float_tuples:
		print(td)
		# test exceptions
		if td.exception:
			with pytest.raises(td.exception):
				if len(td.data) == 3:
					Color(red=td.data[0], green=td.data[1], blue=td.data[2])
				else:
					Color(red=td.data[0], green=td.data[1], blue=td.data[2], alpha=td.data[3])
		#test by data range and conversions validation
		else:
			if len(td.data) == 3:
				rgb = Color(red=td.data[0], green=td.data[1], blue=td.data[2])
				tpl = rgb.asHSL(True)
				hsl = Color(hslHue=tpl[0], hslSat=tpl[1], hslLight=tpl[2])
				tpl = rgb.asHSV(True)
				hsv = Color(hsvHue=tpl[0], hsvSat=tpl[1], hsvValue=tpl[2])
				assert compareColors(rgb, hsl, hsv)
			else:
				rgb = Color(red=td.data[0], green=td.data[1], blue=td.data[2], alpha=td.data[3])
				tpl = rgb.asHSL()
				hsl = Color(hslHue=tpl[0], hslSat=tpl[1], hslLight=tpl[2], alpha=tpl[3])
				tpl = rgb.asHSV()
				hsv = Color(hsvHue=tpl[0], hsvSat=tpl[1], hsvValue=tpl[2], alpha=tpl[3])
				assert compareColors(rgb, hsl, hsv)


# kwargs rgb integers constructor
@pytest.mark.rgb
@pytest.mark.ints
@pytest.mark.kwargs
def test_rgb_ints(int_rgb_tuples):
	print('')
	for td in int_rgb_tuples:
		print(td)
		# test exceptions
		if td.exception:
			with pytest.raises(td.exception):
				if len(td.data) == 3:
					Color(red=td.data[0], green=td.data[1], blue=td.data[2])
				else:
					Color(red=td.data[0], green=td.data[1], blue=td.data[2], alpha=td.data[3])
		#test by data range and conversions validation
		else:
			if len(td.data) == 3:
				rgb = Color(red=td.data[0], green=td.data[1], blue=td.data[2])
				tpl = rgb.asHSL(True)
				hsl = Color(hslHue=tpl[0], hslSat=tpl[1], hslLight=tpl[2])
				tpl = rgb.asHSV(True)
				hsv = Color(hsvHue=tpl[0], hsvSat=tpl[1], hsvValue=tpl[2])
				assert compareColors(rgb, hsl, hsv)
			else:
				rgb = Color(red=td.data[0], green=td.data[1], blue=td.data[2], alpha=td.data[3])
				tpl = rgb.asHSL()
				hsl = Color(hslHue=tpl[0], hslSat=tpl[1], hslLight=tpl[2], alpha=tpl[3])
				tpl = rgb.asHSV()
				hsv = Color(hsvHue=tpl[0], hsvSat=tpl[1], hsvValue=tpl[2], alpha=tpl[3])
				assert compareColors(rgb, hsl, hsv)


# kwargs hsl floats constructor
@pytest.mark.hsl
@pytest.mark.kwargs
@pytest.mark.floats
def test_hsl(float_tuples):
	print('')
	for td in float_tuples:
		print(td)
		# test exceptions
		if td.exception:
			with pytest.raises(td.exception):
				if len(td.data) == 3:
					Color(hslHue=td.data[0], hslSat=td.data[1], hslLight=td.data[2])
				else:
					Color(hslHue=td.data[0], hslSat=td.data[1], hslLight=td.data[2], alpha=td.data[3])
		#test by data range and conversions validation
		else:
			if len(td.data) == 3:
				hsl = Color(hslHue=td.data[0], hslSat=td.data[1], hslLight=td.data[2])
				tpl = hsl.asRGB(True)
				rgb = Color(red=tpl[0], green=tpl[1], blue=tpl[2])
				tpl = hsl.asHSV(True)
				hsv = Color(hsvHue=tpl[0], hsvSat=tpl[1], hsvValue=tpl[2])
				assert compareColors(rgb, hsl, hsv)
			else:
				hsl = Color(hslHue=td.data[0], hslSat=td.data[1], hslLight=td.data[2], alpha=td.data[3])
				tpl = hsl.asRGB()
				rgb = Color(red=tpl[0], green=tpl[1], blue=tpl[2], alpha=td.data[3])
				tpl = hsl.asHSV()
				hsv = Color(hsvHue=tpl[0], hsvSat=tpl[1], hsvValue=tpl[2], alpha=td.data[3])
				assert compareColors(rgb, hsl, hsv)


# kwargs hsl integers constructor
@pytest.mark.hsl
@pytest.mark.ints
@pytest.mark.kwargs
def test_hsl_ints(int_hslv_tuples):
	print('')
	for td in int_hslv_tuples:
		print(td)
		# test exceptions
		if td.exception:
			with pytest.raises(td.exception):
				if len(td.data) == 3:
					Color(hslHue=td.data[0], hslSat=td.data[1], hslLight=td.data[2])
				else:
					Color(hslHue=td.data[0], hslSat=td.data[1], hslLight=td.data[2], alpha=td.data[3])
		#test by data range and conversions validation
		else:
			if len(td.data) == 3:
				hsl = Color(hslHue=td.data[0], hslSat=td.data[1], hslLight=td.data[2])
				tpl = hsl.asRGB(True)
				rgb = Color(red=tpl[0], green=tpl[1], blue=tpl[2])
				tpl = hsl.asHSV(True)
				hsv = Color(hsvHue=tpl[0], hsvSat=tpl[1], hsvValue=tpl[2])
				assert compareColors(rgb, hsl, hsv)
			else:
				hsl = Color(hslHue=td.data[0], hslSat=td.data[1], hslLight=td.data[2], alpha=td.data[3])
				tpl = hsl.asRGB()
				rgb = Color(red=tpl[0], green=tpl[1], blue=tpl[2], alpha=td.data[3])
				tpl = hsl.asHSV()
				hsv = Color(hsvHue=tpl[0], hsvSat=tpl[1], hsvValue=tpl[2], alpha=td.data[3])
				assert compareColors(rgb, hsl, hsv)



# kwargs hsv floats constructor
@pytest.mark.hsv
@pytest.mark.floats
@pytest.mark.kwargs
def test_hsv(float_tuples):
	print('')
	for td in float_tuples:
		print(td)
		# test exceptions
		if td.exception:
			with pytest.raises(td.exception):
				if len(td.data) == 3:
					Color(hsvHue=td.data[0], hsvSat=td.data[1], hsvValue=td.data[2])
				else:
					Color(hsvHue=td.data[0], hsvSat=td.data[1], hsvValue=td.data[2], alpha=td.data[3])
		else:
		#test by data range and conversions validation
			if len(td.data) == 3:
				hsv = Color(hsvHue=td.data[0], hsvSat=td.data[1], hsvValue=td.data[2])
				tpl = hsv.asRGB(True)
				rgb = Color(red=tpl[0], green=tpl[1], blue=tpl[2])
				tpl = hsv.asHSL(True)
				hsl = Color(hslHue=tpl[0], hslSat=tpl[1], hslLight=tpl[2])
				assert compareColors(rgb, hsl, hsv)
			else:
				hsv = Color(hsvHue=td.data[0], hsvSat=td.data[1], hsvValue=td.data[2], alpha=td.data[3])
				tpl = hsv.asRGB()
				rgb = Color(red=tpl[0], green=tpl[1], blue=tpl[2], alpha=td.data[3])
				tpl = hsl.asHSL()
				hsl = Color(hslHue=tpl[0], hslSat=tpl[1], hslLight=tpl[2], alpha=td.data[3])
				assert compareColors(rgb, hsl, hsv)


# kwargs hsv integers constructor
@pytest.mark.hsv
@pytest.mark.ints
@pytest.mark.kwargs
def test_hsv_ints(int_hslv_tuples):
	print('')
	for td in int_hslv_tuples:
		print(td)
		# test exceptions
		if td.exception:
			with pytest.raises(td.exception):
				if len(td.data) == 3:
					Color(hsvHue=td.data[0], hsvSat=td.data[1], hsvValue=td.data[2])
				else:
					Color(hsvHue=td.data[0], hsvSat=td.data[1], hsvValue=td.data[2], alpha=td.data[3])
		else:
		#test by data range and conversions validation
			if len(td.data) == 3:
				hsv = Color(hsvHue=td.data[0], hsvSat=td.data[1], hsvValue=td.data[2])
				tpl = hsv.asRGB(True)
				rgb = Color(red=tpl[0], green=tpl[1], blue=tpl[2])
				tpl = hsv.asHSL(True)
				hsl = Color(hslHue=tpl[0], hslSat=tpl[1], hslLight=tpl[2])
				assert compareColors(rgb, hsl, hsv)
			else:
				hsv = Color(hsvHue=td.data[0], hsvSat=td.data[1], hsvValue=td.data[2], alpha=td.data[3])
				tpl = hsv.asRGB()
				rgb = Color(red=tpl[0], green=tpl[1], blue=tpl[2], alpha=td.data[3])
				tpl = hsl.asHSL()
				hsl = Color(hslHue=tpl[0], hslSat=tpl[1], hslLight=tpl[2], alpha=td.data[3])
				assert compareColors(rgb, hsl, hsv)
