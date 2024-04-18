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


export default function SearchResultsPage() {
  const { data } = useParams(); // held in the variable {data}
  let jsonreal = "";
  fetch('http://13.59.59.93:5000/test')
    .then((response) => response.json())
    .then((json) => {
      // traverse the json to find where 
      for (let i = 0; i < json.length; i++) {
        if (json[i]["title"] === data) {
          // fill variables with information
          // break? 
        }
      }
      jsonreal = json[0]["title"]; // Update jsonreal inside the callback
      console.log(jsonreal); // Log jsonreal after it has been updated
    })
    .catch(error => {
      console.error('There was a problem fetching the JSON:', error);
    });

  const searchResults = [
    {
      id: 1,
      name: jsonreal,
      description: 'Description of Product 1.',
      image: 'product1.jpg',
      price: 10.99,
      store: 'Store A',
    },
    {
      id: 2,
      name: 'Product 2',
      description: 'Description of Product 2.',
      image: 'product2.jpg',
      price: 15.49,
      store: 'Store B',
    },
    //can add more search results here in the future
  ];

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
