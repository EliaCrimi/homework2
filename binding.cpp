#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/variant.h>
#include <pybind11/optional.h>

#include "interpolation.hpp"
#include "LinearInterpolation.hpp"
#include "PolynomialInterpolation.hpp"
#include "Statistics.hpp"

namespace py = pybind11;

PYBIND11_MODULE(statistics, m) {

	py::class_<Interpolation>(m, "Interpolation")
		.def("__call__", &Interpolation::operator());


	py::class_<LinearInterpolation, Interpolation>(m, "LinearInterpolation")
		.def(py::init<const std::map<double, double>&>())
		.def("__call__", &LinearInterpolation::operator());

	
	py::class_<PolynomialInterpolation, Interpolation>(m, "PolynomialInterpolation")
		.def(py::init<const std::map<double, double>&>())
		.def("__call__", &PolynomialInterpolation::operator());


	py::class_<LoadStatistics>(m, "LoadStatistics")
		.def(py::init<>())
		.def("loadCSV", &LoadStatistics::loadCSV)
		.def("printTXT", &LoadStatistics::printTXT)
		.def("getColumn", &LoadStatistics::getColumn)
		.def("getRowsNumber", &LoadStatistics::getRowsNumber)
		.def("getColsNumber", &LoadStatistics::getColsNumber);


	m.def("mean", &statistics::mean);
	m.def("median", &statistics::median);
	m.def("variance", &statistics::variance);
	m.def("standardDeviation", &statistics::standardDeviation);
	m.def("frequencyCount", &statistics::frequencyCount);
	m.def("classification", &statistics::classification);
}
