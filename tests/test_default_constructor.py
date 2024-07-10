from universalcolor import Color
from universalcolor.colordata.colornames import colornames
import pytest


#alpha kwargs generator
def alpha_rng(mode):
	if mode == 'slow':
		for a in range(101):
			yield a/100
	else:
		for a in range(11):
			yield a/10


#test by name constructor and asName method
@pytest.mark.default
@pytest.mark.names
def test_names(mode):
	print('')
	#for all supported color names
	for name in colornames:
		print(name)
		assert Color(name).asHEX() == colornames[name]
		for a in alpha_rng(mode):
			print(name, f'alpha={a}')
			assert Color(name, alpha=a).asHEX(True) == colornames[name]
			with pytest.raises(ValueError):
				Color(name, alpha=-0.1)
			with pytest.raises(ValueError):
				Color(name, alpha=1.1)
			with pytest.raises(TypeError):
				Color(name, alpha='0.1')

	# test asName method
	assert Color(hslHue=0.0, hslSat=1.0, hslLight=0.5).asName() == 'red'
	assert Color(hslHue=0.0, hslSat=1.0, hslLight=0.1).asName() is None

	#invalid data
	with pytest.raises(ValueError):
		Color('')
	with pytest.raises(ValueError):
		Color('unknown')
	with pytest.raises(TypeError):
		Color(123)


@pytest.mark.default
@pytest.mark.lsl
#test by lsl color string constructor and asLSL method
def test_lsl(float_tuples):
	print('')
	for td in float_tuples:
		print(td)
		color = str(td.data[:3]).replace('(', '<').replace(')', '>')

		# test exceptions
		if td.exception:
			with pytest.raises((ValueError, td.exception)):
				if len(td.data) == 3:
					Color(color)
				else:
					Color(color, alpha=td.data[3])

		#test data
		else:
			if len(td.data) == 3:
				assert Color(color).asLSL() == color
			else:
				c = Color(color, alpha=td.data[3])
				assert c.asLSL() == color
				assert c.alpha == td.data[3]


@pytest.mark.default
@pytest.mark.css
@pytest.mark.rgb
#test by CSS RGB string constructor and asCSSRGB method
def test_css_rgb(int_rgb_tuples):
	print('')
	for td in int_rgb_tuples:
		print(td)
		color = 'rgb'
		if len(td.data) == 4 and isinstance(td.data[3], float):
			color += 'a'
			color += str(td.data)
		else:
			color += str(td.data[:3])

		# test exceptions
		if td.exception:
			with pytest.raises(td.exception):
				Color(color)

		#test data
		else:
			assert Color(color).asCSSRGB() == color


@pytest.mark.default
@pytest.mark.css
@pytest.mark.hsl
#test by CSS HSL string constructor and asCSSRGB method
def test_css_hsl(int_hslv_tuples):
	print('')
	for td in int_hslv_tuples:
		print(td)
		color = 'hsl'
		vals = [td.data[0], f'{td.data[1]}%', f'{td.data[2]}%']
		if len(td.data) == 4 and isinstance(td.data[3], float):
			color += 'a'
			vals.append(td.data[3])
		color += str(tuple(vals)).replace("'", '')

		# test exceptions
		if td.exception:
			with pytest.raises(td.exception):
				Color(color)

		#test data
		else:
			assert Color(color).asCSSHSL() == color


@pytest.mark.default
@pytest.mark.hex
#test by HEX string constructor and asHEX method
def test_hex(int_rgb_tuples):
	print('')
	for td in int_rgb_tuples:
		print(td)
		color = '#' + ''.join(tuple(map(lambda h: f'{h:02x}', td.data[:3])))
		if len(td.data) == 4 and isinstance(td.data[3], float):
			color += f'{round(td.data[3] * 255):02x}'

		# test exceptions
		if td.exception:
			with pytest.raises(td.exception):
				Color(color)

		#test data
		else:
			assert Color(color).asHEX() == color
