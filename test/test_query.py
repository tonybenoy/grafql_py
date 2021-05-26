from graphql.execution.executors.asyncio import AsyncioExecutor

from src.schema import Query


def test_desc_match(client):
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


def test_name_match(client):
    query = """
    {
    getData(name: "the king") {
    name
    description
    }
    }
    """

    result = client.execute(query, executor=AsyncioExecutor())
    assert (
        result["data"]["getData"][0]["name"]
        == "The Lord of the Rings: The Return of the King"
    )
    assert len(result["data"]["getData"]) == 2


def test_name_match_exact_none(client):

    query = """{
    getData(name: "\\"the king\\"") {
    name
    description
    }
    }
    """

    result = client.execute(query, executor=AsyncioExecutor())
    assert len(result["data"]["getData"]) == 0


def test_name_match_exact(client):
    query = """
    {
    getData(name: "\\"The Lion King\\"") {
    name
    description
    }
    }
    """

    result = client.execute(query, executor=AsyncioExecutor())
    assert len(result["data"]["getData"]) == 1
    assert result["data"]["getData"][0]["name"] == "The Lion King"


def test_first(client):
    query = """
    {
    getData(first:5) {
    name
    description
    }
    }
    """

    result = client.execute(query, executor=AsyncioExecutor())
    assert len(result["data"]["getData"]) == 5


def test_sort(client):
    query = """
    {
    getData(sort:"name") {
    name
    description
    }
    }
    """

    result = client.execute(query, executor=AsyncioExecutor())
    assert result["data"]["getData"][0]["name"] == "Central Creative Producer"


def test_sort_date(client):
    query = """
     {
    getData(sort:"dateLastEdited") {
    name
    description
      dateLastEdited
    }
    }
    """

    result = client.execute(query, executor=AsyncioExecutor())
    assert result["data"]["getData"][0]["name"] == "Chief Brand Orchestrator"


def test_pagination(client):
    query = """
    {
    getData(sort:"name",page:40) {
    name
    description
      dateLastEdited
    }
    }

    """
    result = client.execute(query, executor=AsyncioExecutor())
    assert result["data"]["getData"][0]["name"] == "Future Marketing Representative"
    assert len(result["data"]["getData"]) == 10
