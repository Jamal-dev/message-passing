import grpc

import location_pb2
import location_pb2_grpc

"""
Simulates user mobiles sending coordinates to gRPC
"""

print("Coordinates sending...")

channel = grpc.insecure_channel("127.0.0.1:30003")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
user_coordinates = location_pb2.LocationMessage(
    id=100,
    longitude=45,
    latitude=-45,
)

user_coordinates_2 = location_pb2.LocationMessage(
    id=1001,
    longitude=15,
    latitude=-15,
)

response_1 = stub.Create(user_coordinates)
response_2 = stub.Create(user_coordinates_2)


print("Coordinates sent...")
print(user_coordinates, user_coordinates_2)