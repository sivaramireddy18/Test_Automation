from pathlib import Path
from framework.ir import ApiIR, Function, Parameter
from framework.generator import generate_c, generate_python

def test_generators(tmp_path: Path):
    ir = ApiIR(functions=[Function(name="HAL_Delay", return_type="void", parameters=[Parameter("Delay", "uint32_t", "in")])])
    generate_c(ir, tmp_path / "c")
    generate_python(ir, tmp_path / "python")
    assert (tmp_path / "c/include/stm32_generated.h").exists()
    assert (tmp_path / "c/src/stm32_generated.c").exists()
    assert (tmp_path / "python/stm32_api.py").exists()
