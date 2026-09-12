
from typing import Annotated 
from typing import get_type_hints,get_origin,get_args 


x: Annotated[int, "some metadata"] = 42
# mypy/pyright 只看到 int，以下操作完全合法
y: int = x  # ✅ 无错误
z: str = x  # ❌ 类型错误

hints=get_type_hints(func)