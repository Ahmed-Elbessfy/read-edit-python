
import csv
from os.path import exists as file_exists


def analyzeData():
    # variables
    # input file name
    fileName = ""
    # store count for each product to produce first table
    productsCounts = {}
    # to get the average quantity of the product purchased per order.
    totalProductsNumber = 0

    # store products each brand count to produce second table
    productsBrands = {}

    # Most popular product to store final product and most popular brand
    mostPopularProduct = {}



    # get file path from user
    path = input("Path or name of file: ")
    # validate input and check if file exists

    if file_exists(path):

        # get file name
        # split path then get last item
        fileName = path.split("/")[-1]

        # read data from file
        # open file
        with open(fileName, "r") as file:
            # read data
            products = csv.reader(file)
            for product in products:

                # increment total count of orders 
                totalProductsNumber = totalProductsNumber + 1
                # collect products data

                # get the average quantity of the product purchased per order.
                # for validation: I assumed that all fields are mandatory to be counted
                if len(product[1]) > 0 and len(product[2]) > 0 and int(product[3]) > 0 and len(product[4]) > 0: 
                    ################### PRODUCT COUNTS LOGIC ###################
                    # if product is already counted
                    if product[2] in productsCounts:
                        productsCounts[product[2]] += int(product[3])
                    else:
                      # if product is count for the first time 
                        productsCounts[product[2]] = int(product[3])


                    ################### PRODUCT BRANDS LOGIC ###################
                    # get the most popular Brand for that product.
                    # pseudo code steps:
                    # check if productsBrands has current order product
                    # - if yes, then
                    # -- check if current order product dict has current order brand,
                    # --- if yes, increment brand count
                    # --- else, initiate count with 1
                    # -- if current order product dict does not have current order brand, initiate current order brand key in brand dict with value = 1
                    # if productsBrands does not have the current order product, then initiate a nested dict with current order 
                    # product as a key and value of a dict contains current order brand as a keu and value = 1 which is its count

                    # if product is already included
                    if product[2] in productsBrands:
                      # check if brand is included or not
                      if product[4] in productsBrands[product[2]]:
                          productsBrands[product[2]][product[4]] += 1
                      else:
                          productsBrands[product[2]][product[4]] = 1

                    else:
                      # if product is get included for the first time, then add product and its brand for the first time
                        productsBrands[product[2]] = {product[4]:1}



            for product in productsCounts:

                productsCounts[product] /= totalProductsNumber
                # print(f"{product}: {productsCounts[product]}")

            # pseudo code steps:
            # loop over each product
            # - loop over each brand 
            # - if current brand count > max count then 
            # -- set max to be current brand count
            # -- set most popular brand (popBrand variable) to be current brand 
            # - store current product and most popular brand in the corresponding dictionary
            for product in productsBrands:
                # placeholder for maximum count of products per brand
                max  = 0
                # to store the most popular brand name
                popBrand = ""
                for brand in productsBrands[product]:
                    if productsBrands[product][brand] > max:
                        popBrand = brand
                        max = productsBrands[product][brand]
                mostPopularProduct[product] = popBrand


        #writing data to output files
        with open("0_" + fileName, "w") as file:
            # writer = csv.writer(file)
            # for product in productsCounts:
            #     print(product)
            #     writer.writerow(product)
            writer = csv.writer(file)
            for key, value in productsCounts.items():
              writer.writerow([key, value])

        with open("1_" + fileName, "w") as file:
            # writer = csv.writer(file)
            # for product in productsCounts:
            #     print(product)
            #     writer.writerow(product)
            writer = csv.writer(file)
            for key, value in mostPopularProduct.items():
              writer.writerow([key, value])

        print(productsCounts , mostPopularProduct)

        return 0
    else:
        print("No such file name ")
        return 1


analyzeData()



# productsCount = {
#   prodcut1: count,
#   prodcut2: count,
#   prodcut3: count,
# }


# productsBrands = {
#   product1: {
#     brand1:count,
#     brand2:count
#     },
#   product2: {
#     brand1:count,
#     brand2:count
#     },

#   product3: {
#     brand1:count,
#     brand2:count
#     },
# }
