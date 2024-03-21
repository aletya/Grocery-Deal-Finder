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

export default function SearchResultsPage() {

  const searchResults = [
    {
      id: 1,
      name: 'Product 1',
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
      <Heading>
        <title>Search Results</title>
        <meta name="description" content="Search results page" />
      </Heading>
      <Container maxW={'3xl'}>
        <Stack
          as={Box}
          textAlign={'center'}
          spacing={{ base: 8, md: 14 }}
          py={{ base: 20, md: 36 }}>
          <Heading
            fontWeight={600}
            fontSize={{ base: '2xl', sm: '4xl', md: '6xl' }}
            lineHeight={'110%'}>
            Search Results
          </Heading>
          <Grid templateColumns="repeat(auto-fit, minmax(250px, 1fr))" gap={6}>
            {searchResults.map((result) => (
              <GridItem key={result.id}>
                <Box p={5} shadow="md" borderWidth="1px" borderRadius="md">
                  <Image src={result.image} alt={result.name} borderRadius="md" />
                  <Text fontSize="xl" fontWeight="bold" mt={4}>{result.name}</Text>
                  <Text color="gray.600" fontSize="md" mt={2}>{result.description}</Text>
                  <Flex justify="space-between" mt={4}>
                    <Text fontSize="lg" fontWeight="bold">${result.price.toFixed(2)}</Text>
                    <Text fontSize="lg">{result.store}</Text>
                  </Flex>
                </Box>
              </GridItem>
            ))}
          </Grid>
        </Stack>
      </Container>
    </>
  )
}
