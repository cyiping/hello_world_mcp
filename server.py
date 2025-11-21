from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My First Demo")

@mcp.tool()
def calculate_bmi(height_cm: float, weight_kg: float) -> str:
    """
    計算 BMI 的工具。
    Args:
        height_cm: 身高 (公分)
        weight_kg: 體重 (公斤)
    """
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return f"你的 BMI 是 {bmi:.2f}"

if __name__ == "__main__":
    mcp.run()