"""Runs protoc with the gRPC plugin to generate messages and gRPC stubs."""

from grpc.tools import protoc

protoc.main(
    (
	'',
	'-I=protos',
	'--python_out=out',
	'--grpc_python_out=out',
	'protos/shared.proto',
    )
)

protoc.main(
    (
	'',
	'-I=protos',
	'--python_out=out',
	'--grpc_python_out=out',
	'protos/front_end.proto',
    )
)

protoc.main(
    (
	'',
	'-I=protos',
	'--python_out=out',
	'--grpc_python_out=out',
	'protos/back_end.proto',
    )
)
