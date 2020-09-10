from silver_service_taxi import SilverServiceTaxi

if __name__ == '__main__':

    test_silver = SilverServiceTaxi("Test", 100, 2)
    test_silver.drive(18)
    print(test_silver)
    print(test_silver.get_fare())

