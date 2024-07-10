import pytest
from typing import NamedTuple


class TestData(NamedTuple):
	data: tuple
	exception: Exception | None


def pytest_addoption(parser):
	parser.addoption('--mode', default='fast', choices=('fast', 'slow'))


@pytest.fixture
def mode(request):
	return request.config.getoption('--mode')


#floats testing data generator
def float_tuples_gen(mode):
	#invalid kwargs
	yield TestData((-0.1, 0.1, 0.1), ValueError)
	yield TestData((0.1, -0.1, 0.1), ValueError)
	yield TestData((0.1, 0.1, -0.1), ValueError)
	yield TestData((1.1, 0.1, 0.1), ValueError)
	yield TestData((0.1, 1.1, 0.1), ValueError)
	yield TestData((0.1, 0.1, 1.1), ValueError)
	yield TestData((0.1, 0.1, 0.1, -0.1), ValueError)
	yield TestData((0.1, 0.1, 0.1, 1.1), ValueError)
	yield TestData(('0.1', 0.1, 0.1), TypeError)
	yield TestData((0.1, '0.1', 0.1), TypeError)
	yield TestData((0.1, 0.1, '0.1'), TypeError)
	yield TestData((0.1, 0.1, 0.1, '0.1'), TypeError)

	#valid data
	n = 10
	if mode == 'slow':
		n = 100
	alphas = [None]
	for a in range(n+1):
		alphas.append(a/n)
	for x in range(n+1):
		for y in range(n+1):
			for z in range(n+1):
				yield TestData((x/n, y/n, z/n), None)
				for a in alphas:
					yield TestData((x/n, y/n, z/n, a), None)


@pytest.fixture
def float_tuples(mode):
	return float_tuples_gen(mode)


#integers for rgb testing data generator
def int_rgb_tuples_gen(mode):
	#invalid data`
	yield TestData((-1, 1, 1), ValueError)
	yield TestData((1, -1, 1), ValueError)
	yield TestData((1, 1, -1), ValueError)
	yield TestData((256, 255, 255), ValueError)
	yield TestData((255, 256, 255), ValueError)
	yield TestData((255, 255, 256), ValueError)
	yield TestData((1, 1, 1, -0.1), ValueError)
	yield TestData((1, 1, 1, 1.1), ValueError)
	yield TestData((255, 255, 255, -0.1), ValueError)
	yield TestData((255, 255, 255, 1.1), ValueError)

	#valid data
	rng = list(range(0, 256, 8))
	rng.append(255)
	if mode == 'slow':
		rng = range(256)
	n = 10
	if mode == 'slow':
		n = 100
	alphas = [None]
	for a in range(n+1):
		alphas.append(a/n)
	for x in rng:
		for y in rng:
			for z in rng:
				yield TestData((x, y, z), None)
				for a in alphas:
					yield TestData((x, y, z, a), None)


@pytest.fixture
def int_rgb_tuples(mode):
	return int_rgb_tuples_gen(mode)


#integers for hsl and hsv testing data generator
def int_hslv_tuples_gen(mode):
	#invalid data
	yield TestData((-1, 1, 1), ValueError)
	yield TestData((1, -1, 1), ValueError)
	yield TestData((1, 1, -1), ValueError)
	yield TestData((361, 360, 360), ValueError)
	yield TestData((360, 361, 360), ValueError)
	yield TestData((360, 360, 361), ValueError)
	yield TestData((1, 1, 1, -0.1), ValueError)
	yield TestData((1, 1, 1, 1.1), ValueError)
	yield TestData((360, 360, 360, -0.1), ValueError)
	yield TestData((360, 360, 360, 1.1), ValueError)

	#valid data
	rng = list(range(0, 361, 8))
	rngslv = list(range(0, 101, 5))
	if mode == 'slow':
		rng = range(361)
		rngslv = range(101)
	n = 10
	if mode == 'slow':
		n = 100
	alphas = [None]
	for a in range(n+1):
		alphas.append(a/n)
	for x in rng:
		for y in rngslv:
			for z in rngslv:
				yield TestData((x, y, z), None)
				for a in alphas:
					yield TestData((x, y, z, a), None)


@pytest.fixture
def int_hslv_tuples(mode):
	return int_hslv_tuples_gen(mode)
