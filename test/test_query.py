from graphql.execution.executors.asyncio import AsyncioExecutor


def test_create_user(client):
    query = """
    {
  getData(desc: "the king") {
    name
    description
    }
    }

    """

    result = client.execute(query, executor=AsyncioExecutor())
    assert result["data"]["getData"][0]["name"] == "Human Web Agent"
