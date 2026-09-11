from bakery import assert_equal
from drafter import *
from dataclasses import dataclass

@dataclass
class State:
    count: int

@route
def index(state: State) -> Page:
    return Page(state, [
        "Current count: " + str(state.count) + "\n",
        Button("+1", "increment"),
        Button("-1", "decrement"),
        Button("+10", "increment_10"),
        Button("Reset", "reset_count")
        ])

@route
def increment(state: State) -> Page:
    state.count = state.count + 1
    return index(state)

@route
def increment_10(state: State) -> Page:
    state.count = state.count + 10
    return index(state)

@route
def decrement(state: State) -> Page:
    state.count = state.count - 1
    return index(state)

@route
def reset_count(state: State) -> Page:
    state.count = 0
    return index(state)

assert_state(increment(State(0)), State(1))
assert_state(reset_count(State(7)), State(0))
assert_has(index(State(3)), "Current count: 3")

set_website_title("My First Counter")
set_site_information(
    author="Jacob Gordon",
    description="Counter increases and decreases when you click corresponding button.",
    sources="Thanks to the Drafter docs and my study group.",
    planning="plan.pdf",
    links=["https://github.com/"]
)
hide_debug_information()
set_website_framed(False)

start_server(State(0))
