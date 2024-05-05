'use client'

import {
  Box,
  Flex,
  Heading,
  Container,
  Text,
  Button,
  Stack,
  Icon,
  useColorModeValue,
  createIcon,
  Input,
  InputGroup,
  InputLeftElement,
  InputRightElement,
  Image,
  Center,
  Select,
  RangeSlider,
  RangeSliderFilledTrack,
  RangeSliderThumb,
  RangeSliderTrack,
  Grid,
  GridItem,
} from '@chakra-ui/react'

import { SearchIcon } from '@chakra-ui/icons'
import { useParams, Link, useLocation } from 'react-router-dom';
import React, { useEffect, useState, useMemo } from 'react';

export default function SearchResultsPage() {
  const location = useLocation();
  const { initialSearchData } = location.state || {};

  const [searchResults, setSearchResults] = React.useState<Deal[]>([]);
  const [groceryItem, setGroceryItem] = React.useState('');
  const [selectedStore, setSelectedStore] = React.useState('');
  const [zipCode, setZipCode] = React.useState('');

  const [sortOption, setSortOption] = useState('');
  const [sliderValue, setSliderValue] = useState([0, 100]);

  interface Deal {
    title: string;
    description: string;
    price: string;
  }
  
  interface DealResults {
    deals: Deal[];
  }

  function formatStoreName(storeName: string) {
    return storeName.toLowerCase().replace(/\s+/g, '-');
  }

  const handleSortOption = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSortOption(event.target.value);
  };

  const handleSliderChange = (value: number[]) => {
    setSliderValue(value);
  };

  const fetchData = async (store: string, zipCode: string, groceryItem: string): Promise<void> => {
    try {
      const storeName = formatStoreName(store);
      const response = await fetch(`http://13.59.59.93:5000/${storeName}?zip_code=${zipCode}`, {
        method: 'GET',
      });
      if (response.ok) {
        const results = await response.json(); 
        let filteredResults = []
        for (let i = 0; i < results["deals"].length; i++) {
          if (results["deals"][i]["title"].toLowerCase().includes(groceryItem.toLowerCase())) {
            console.log(results["deals"][i]["title"] + " includes " + groceryItem)
              filteredResults.push({
              title: results["deals"][i]["title"],
              description: results["deals"][i]["description"],
              price: results["deals"][i]["price"], 
              store: store,
            });
          }
          setSearchResults(filteredResults);
        }
      } else {
        throw new Error('Network response was not ok');
      }
    } catch (error) {
      console.error('Error fetching store info:', error);
    }
  };

  const renderResults = useMemo(() => {
    if (!sortOption) {
      return searchResults; // Return original results if no sort option selected
    }
    let sorted = [...searchResults]; 
    if (sortOption === 'priceLowToHigh') {
      sorted.sort((a, b) => parseFloat(a.price) - parseFloat(b.price));
    } else if (sortOption === 'priceHighToLow') {
      sorted.sort((a, b) => parseFloat(b.price) - parseFloat(a.price));
    } else if (sortOption === 'nameAZ') {
      sorted.sort((a, b) => a.title.localeCompare(b.title));
    } else if (sortOption === 'nameZA') {
      sorted.sort((a, b) => b.title.localeCompare(a.title));
    }
    return sorted;
  }, [searchResults, sortOption]);
  

  // Initial fetch based on initialSearchData
  useEffect(() => {
    const groceryItem = initialSearchData.groceryItem
    const selectedStore = initialSearchData.selectedStore;
    const zipCode = initialSearchData.zipCode;

    setGroceryItem(groceryItem);
    setSelectedStore(selectedStore);
    setZipCode(zipCode);

    fetchData(selectedStore, zipCode, groceryItem);
  }, [location.state]);

  // Handles searching again for another item
  // const [urlstring, setUrlstring] = React.useState('/result/');
  // const handleItemSearchAgain = (event: React.ChangeEvent<HTMLInputElement>) => {
  //   const searchedAgainItem = event.target.value;
  //   setGroceryItem(searchedAgainItem);
  //   setUrlstring('/result/' + searchedAgainItem);
  // }

  // const handleSearchSubmit = (event: React.MouseEvent<HTMLButtonElement>) => {
  //   fetchData(selectedStore, zipCode);
  // }

  return (
    <>
      <Container maxW={'3xl'}>
        <Stack
          as={Box}
          textAlign={'center'}
          spacing={{ base: 8, md: 14 }}
          py={{ base: 20, md: 36 }}
        >
          <Heading
            fontWeight={600}
            fontSize={{ base: '2xl', sm: '4xl', md: '6xl' }}
            lineHeight={'110%'}
          >
            Search Results for{' '}
            <Text as="span" color="green.400">
              {groceryItem}
            </Text>
            {' '}at{' '}
            <Text as="span" color="green.400">
              {selectedStore}
            </Text>:
          </Heading>

          {/* <Flex align="center" justify="center" mt={8}>
            <InputGroup>
              <InputLeftElement pointerEvents="none">
                <SearchIcon color="gray.300" />
              </InputLeftElement>
              <Input type="text" placeholder="Search for another item!" 
                 value={groceryItem}
                 onChange={handleItemSearchAgain}
              />
            </InputGroup>
            <Link to ={urlstring}>
              <Button
                onClick = {handleSearchSubmit}
                colorScheme="green"
                bg="green.400"
                rounded="full"
                px={6}
                ml={2}
                _hover={{
                  bg: 'green.500',
                }}
              >
                Search
              </Button>
            </Link>
          </Flex> */}
        
          <Box mt={8} p={5} boxShadow="md" borderWidth="1px">

            <Text fontSize="xl" mb={4} textAlign="center">
              Apply Filters
            </Text>

            <Flex direction={{ base: 'column', md: 'row' }} align="center" gap={6}>
              
              <Box w={{ base: '100%', md: '50%' }}>
                <Text mb={2}>Sort By</Text>
                <Select placeholder="Select option"
                  value={sortOption}
                  onChange={handleSortOption} 
                >

                  <option value="priceLowToHigh">Price: Low to High</option>
                  <option value="priceHighToLow">Price: High to Low</option>
                  <option value="nameAZ">Name: A-Z</option>
                  <option value="nameZA">Name: Z-A</option>
                
                </Select>
              </Box>

              <Box w={{ base: '100%', md: '50%' }}>
                <Text mb={2}>Filter By Price</Text>
                <RangeSlider
                    defaultValue={[0, 100]}
                    value={sliderValue}
                    min={0}
                    max={100}
                    step={1}
                    onChange={handleSliderChange}
                  >
                  <RangeSliderTrack bg="gray.200">
                    <RangeSliderFilledTrack bg="green.400" />
                  </RangeSliderTrack>
                  <RangeSliderThumb boxSize={6} index={0} />
                  <RangeSliderThumb boxSize={6} index={1} />
                </RangeSlider>

                <Flex justifyContent="space-between" mt={2}>
                  <Text>${sliderValue[0]}</Text>
                  <Text>${sliderValue[1]}</Text>
                </Flex>
              </Box>

            </Flex>
          </Box>

          <Grid templateColumns="repeat(auto-fit, minmax(250px, 1fr))" gap={6}>
            {renderResults.map((result: Deal, index: number) => (
              <GridItem>
                <Box p={5} shadow="md" borderWidth="1px" borderRadius="md">
                  <Text fontSize="xl" fontWeight="bold" mt={4}>
                    {result.title}
                  </Text>
                  <Text color="gray.600" fontSize="md" mt={2}>
                    {result.description}
                  </Text>
                  <Flex justify="space-between" mt={4}>
                    <Text fontSize="lg" fontWeight="bold">
                      {result.price}
                    </Text>
                    <Text fontSize="lg">{selectedStore}</Text>
                  </Flex>
                </Box>
              </GridItem>
            ))}
          </Grid>

          <Flex justify="center" mt={8}>
            <Link to="/">
              <Button
                colorScheme="green"
                bg="green.400"
                rounded="full"
                px={6}
                _hover={{
                  bg: 'green.500',
                }}
              >
                Search For Another Item!
              </Button>
            </Link>
          </Flex>

        </Stack>
      </Container>
    </>
  );
}

