from framework.ir import ApiIR, Function, Parameter

def test_ir_serialization():
    ir = ApiIR(functions=[Function(name="HAL_GPIO_WritePin", return_type="void", parameters=[Parameter("GPIOx", "GPIO_TypeDef *", "in", 1)])])
    data = ir.to_dict()
    assert data["functions"][0]["name"] == "HAL_GPIO_WritePin"
    assert data["functions"][0]["parameters"][0]["pointer_depth"] == 1
