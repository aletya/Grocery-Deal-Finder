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
import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';


export default function SearchResultsPage() {
  const { data } = useParams(); // held in the variable {data}
  const [searchResults, setSearchResults] = useState([]);
  let jsonreal = "hey";
  useEffect(() => {
    fetch('13.59.59.93:5000/county-market?zip_code=60521')
      .then(response => {
        if (!response.ok) {
         throw new Error('Network response was not ok');
        }
        return response.json(); // Parse the response body as JSON
      })
      .then((json) => {
        let results = [];
        jsonreal = json;
        // console.log(json);
        for (let i = 0; i < json["deals"].length; i++) {
          console.log(json["deals"][i]["title"]);
          if (json["deals"][i]["title"] === data) {
            console.log("WE GOT IT");
            jsonreal = json["deals"][i]["title"];

            results.push({
              id: i,
              name: json["deals"][i]["title"],
              description: 'temp description', // ["deals"][i]["description"]
              image: 'product1.jpg', // Update with actual image URL
              price: 5,  //Number(json["deals"][i]["price"]) json["deals"][i]["price"]
              store: 'County Market', // Update with actual store name
            });
            setSearchResults(results);
            break;
          }
        }
      })
      .catch(error => {
        console.error('There was a problem fetching the JSON:', error);
      });
    }, []);
  // let jsonreal = "hey";
  // fetch('http://13.59.59.93:5000/test')
  //   .then(response => {
  //     if (!response.ok) {
  //       throw new Error('Network response was not ok');
  //     }
  //     return response.json(); // Parse the response body as JSON
  //   })
  //   .then((json) => {
  //     // traverse the json to find where 
  //     // for (let i = 0; i < json.length; i++) {
  //     //   if (json[i]["title"] === data) {
  //     //     // fill variables with information
  //     //     // break? 
  //     //   }
  //     // }
  //     jsonreal = json;
  //     window.alert(jsonreal); // Update jsonreal inside the callback
  //   })
  //   .catch(error => {
  //     console.error('There was a problem fetching the JSON:', error);
  //   });


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
            Search Results
          </Heading>

          <Flex align="center" justify="center" mt={8}>
            <InputGroup>
              <InputLeftElement pointerEvents="none">
                <SearchIcon color="gray.300" />
              </InputLeftElement>
              <Input type="text" placeholder="Search for another item!" />
            </InputGroup>
            <Button
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
          </Flex>
        
          <Box mt={8} p={5} boxShadow="md" borderWidth="1px">
            <Text fontSize="xl" mb={4} textAlign="center">
              Apply Filters
            </Text>
            <Flex direction={{ base: 'column', md: 'row' }} align="center" gap={6}>
              
              <Box w={{ base: '100%', md: '50%' }}>
                <Text mb={2}>Sort By</Text>
                <Select placeholder="Select option">
                  <option value="price">Price: Low to High</option>
                  <option value="price">Price: High to Low</option>
                  <option value="name">Name: A-Z</option>
                  <option value="name">Name: Z-A</option>
                
                </Select>
              </Box>

              <Box w={{ base: '100%', md: '50%' }}>
                <Text mb={2}>Filter By Price</Text>
                <RangeSlider defaultValue={[0, 100]} min={0} max={100} step={1}>
                  <RangeSliderTrack bg="gray.200">
                    <RangeSliderFilledTrack bg="green.400" />
                  </RangeSliderTrack>
                  <RangeSliderThumb boxSize={6} index={0} />
                  <RangeSliderThumb boxSize={6} index={1} />
                </RangeSlider>

                <Flex justifyContent="space-between" mt={2}>
                      <Text>$0</Text>
                      <Text>$100</Text>
                </Flex>

              </Box>
            </Flex>
          </Box>

          <Grid templateColumns="repeat(auto-fit, minmax(250px, 1fr))" gap={6}>
            {searchResults.map((result) => (
              <GridItem key={result.id}>
                <Box p={5} shadow="md" borderWidth="1px" borderRadius="md">
                  <Image src={result.image} alt={result.name} borderRadius="md" />
                  <Text fontSize="xl" fontWeight="bold" mt={4}>
                    {result.name}
                  </Text>
                  <Text color="gray.600" fontSize="md" mt={2}>
                    {result.description}
                  </Text>
                  <Flex justify="space-between" mt={4}>
                    <Text fontSize="lg" fontWeight="bold">
                      ${result.price.toFixed(2)}
                    </Text>
                    <Text fontSize="lg">{result.store}</Text>
                  </Flex>
                </Box>
              </GridItem>
            ))}
          </Grid>
        </Stack>
      </Container>
    </>
  );
}
