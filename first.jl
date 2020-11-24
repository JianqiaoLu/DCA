x =1 
print(typeof(x))
function  foo(x)
    x+1
    return x
    
end
foo2(x) = x+2
print(foo2(1))
function loop(x)
    for k in x:10
        @show k
    end
    
end
function loop2(x)
    k = x
    while (k < 10 )
        @show(k)
        k= k +1
    end

end
struct Cat
    name::String
end
struct Complex{T <: Number}
    real::T
    imag::T
end
struct MyArray{T, N}
    storage::Ptr{T}
    size::NTuple{N, Int}
    strides::NTuple{N, Int}
end
abstract type Operator end
abstract type AbstractNode end
mutable struct Variable{T} <: AbstractNode
    value::T
    grad::T

    Variable(val::T) where T = new{T}(val, zero(val))
end
struct Node{FT <: Operator, ArgsT <: Tuple, KwargsT <: NamedTuple} <: AbstractNode
    f::FT
    args::ArgsT
    kwargs::KwargsT
end


module Trait
import YAAD: Operator

struct Method{FT} <: Operator
    f::FT
end

struct Broadcasted{FT} <: Operator
    f::FT
end
end # Trait


Node(f::Function, args, kwargs) = Node(Trait.Method(f), args, kwargs)
Node(op, args) = Node(op, args, NamedTuple())
mutable struct CachedNode{NT <: AbstractNode, OutT} <: AbstractNode
    node::NT
    output::OutT
end
function CachedNode(f, args...; kwargs...)
    node = Node(f, args, kwargs.data) # this constructs a Node
    output = forward(node)
    CachedNode(node, output)
end

struct Linear <: Operator
    w::Matrix{Float64}
    b::Vector{Float64}
  end
  
  
forward(op::Linear, x::Vector{Float64}) = op.w * x + b

linear = Linear
linear.w = [1]
linear.b = [2]
forward(linear, 1)