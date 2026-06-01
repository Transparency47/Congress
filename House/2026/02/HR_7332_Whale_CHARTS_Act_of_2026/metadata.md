# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7332?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7332
- Title: Whale CHARTS Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7332
- Origin chamber: House
- Introduced date: 2026-02-03
- Update date: 2026-03-04T15:54:31Z
- Update date including text: 2026-03-04T15:54:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-03: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-03 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-02-03: Introduced in House

## Actions

- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-03 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-03",
    "latestAction": {
      "actionDate": "2026-02-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7332",
    "number": "7332",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "M001163",
        "district": "7",
        "firstName": "Doris",
        "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
        "lastName": "Matsui",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Whale CHARTS Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-04T15:54:31Z",
    "updateDateIncludingText": "2026-03-04T15:54:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-03",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-03",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-02-03T15:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-03T15:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "NY"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "OR"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "FL"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "MD"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "GA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "OR"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "FL"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "IL"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "AS"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "MP"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "MA"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "FL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "IL"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "VA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "PA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "WA"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "GU"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NY"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "SC"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NJ"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "CA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-02-17",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "NY"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7332ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7332\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 3, 2026 Ms. Matsui (for herself, Ms. Malliotakis , Ms. Dexter , Mr. Buchanan , Ms. Elfreth , Mr. Carter of Georgia , Ms. Bonamici , Mr. Rutherford , Mr. Quigley , Mrs. Radewagen , Mr. Huffman , Ms. King-Hinds , Mr. Moulton , Mr. Bilirakis , Mr. Krishnamoorthi , Mrs. Kiggans of Virginia , Ms. Brownley , Mr. Fitzpatrick , Mr. Smith of Washington , Mr. Moylan , Mr. Suozzi , and Ms. Mace ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 to provide for a mapping, surveying, monitoring, and mitigation program for migratory whales and other large cetaceans.\n#### 1. Short title\nThis Act may be cited as the Whale CHARTS Act of 2026 .\n#### 2. Mapping, surveying, monitoring, and mitigation program for migratory whales and other large cetaceans\n##### (a) In general\nSection 11303 of the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 ( 16 U.S.C. 1391 ) is amended\u2014\n**(1)**\nin the heading, by striking NEAR REAL-TIME MONITORING AND MITIGATION PROGRAM FOR and inserting MAPPING, SURVEYING, MONITORING, AND MITIGATION PROGRAM FOR MIGRATORY WHALES AND OTHER ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby striking near real-time monitoring and inserting mapping, surveying, monitoring, ;\n**(B)**\nby striking (referred to in this section as the Program ) ; and\n**(C)**\nby striking threatened or endangered and inserting migratory whales and other large ;\n**(3)**\nin subsection (b)\u2014\n**(A)**\nby inserting migratory whales and other before large cetaceans posed ;\n**(B)**\nby inserting migratory whales and other before large cetaceans through ; and\n**(C)**\nby striking the use of near real-time location monitoring and location information and inserting the following:\nincreased and improved data collection, including\u2014 (1) mapping and surveying of migratory whales; (2) monitoring of large cetaceans; and (3) the development of detection technologies for migratory whales and other large cetaceans. ;\n**(4)**\nby redesignating subsections (e) through (i) as subsections (g) through (k), respectively;\n**(5)**\nby redesignating subsection (c) as subsection (f);\n**(6)**\nin subsection (f), as so redesignated\u2014\n**(A)**\nin the heading, by striking REQUIREMENTS and inserting NEAR REAL-TIME MONITORING AND MITIGATION SUBPROGRAM FOR LARGE CETACEANS ;\n**(B)**\nby redesignating paragraphs (1) through (6) as subparagraphs (A) through (F), respectively (and by adjusting the margins of such subparagraphs accordingly);\n**(C)**\nby striking The Program and inserting the following:\n(3) Requirements The Subprogram ;\n**(D)**\nby inserting before paragraph (3), as so redesignated, the following:\n(1) Establishment The Under Secretary, in coordination with the heads of other relevant Federal agencies, shall design and deploy a cost-effective, efficient, and results-oriented near real-time monitoring and mitigation subprogram for threatened or endangered cetaceans. (2) Purpose The purpose of the Subprogram shall be to reduce the risk to large cetaceans posed by vessel collisions and to minimize other impacts on large cetaceans through the use of near real-time location monitoring and location information. ; and\n**(E)**\nin paragraph (3)(F), as so redesignated, by striking subsection (d) and inserting paragraph (4) ;\n**(7)**\nin subsection (d)(4)(B)(ii)(II)(bb), to read as follows:\n(bb) a strategic plan to expand the pilot project to provide near real-time monitoring and mitigation measures to additional large cetaceans of concern for which such measures would reduce risk of serious injury or death and in important feeding, breeding, calving, rearing, or migratory habitats of large cetaceans that co-occur with areas of high risk of mortality or serious injury from vessel strikes or disturbance; ;\n**(8)**\nby redesignating subsection (d) as paragraph (4) of subsection (f), as so redesignated (and by adjusting the margin of paragraph (4) accordingly);\n**(9)**\nin subsection (f)(4), as so redesignated\u2014\n**(A)**\nin the heading, by striking PILOT PROJECT and inserting PILOT PROJECT ;\n**(B)**\nby redesignating paragraphs (1) through (4) as subparagraphs (A) through (D), respectively (and by redesignating any subdivisions under such subparagraphs (as so redesignated) to include adjusting the margins of such subparagraphs (and their subdivisions) accordingly);\n**(C)**\nby striking Program each place it appears and inserting Subprogram ;\n**(D)**\nin subparagraph (C), as so redesignated, by striking paragraph (2) each place it appears and inserting subparagraph (B) ; and\n**(E)**\nin subparagraph (D)\u2014\n**(i)**\nin clause (i)(II), as so redesignated, by striking clause (i) and inserting subclause (I) ; and\n**(ii)**\nin clause (ii)(II)\u2014\n**(I)**\nby striking clause (i) and inserting subclause (I) ; and\n**(II)**\nin item (aa), by striking subparagraph (A) and inserting clause (i) ;\n**(10)**\nby inserting after subsection (b) the following:\n(c) Distribution mapping of migratory whales (1) In general The Under Secretary, in consultation with the Marine Mammal Commission, shall produce for stocks, populations, or species, as the Under Secretary determines appropriate, of migratory whales within waters under the jurisdiction of the United States\u2014 (A) distribution maps of high accuracy and spatial and temporal resolution; and (B) predictive distribution maps of high accuracy and spatial and temporal resolution that take into account expected future environmental conditions. (2) Duties In carrying out paragraph (1), the Under Secretary\u2014 (A) shall\u2014 (i) use the best scientific information available; (ii) conduct or support research to identify and fill knowledge gaps, which may include\u2014 (I) developing novel sources of data, such as passive acoustic monitoring, detection through satellite or drone imagery, and other on-water asset-based sensors; and (II) developing innovative methodologies\u2014 (aa) to combine different sources of migratory whale detection data; or (bb) to improve migratory whale distribution and habitat modeling; (iii) include in each map produced under such paragraph, as applicable\u2014 (I) calving grounds; (II) mating grounds; (III) feeding grounds; (IV) migration routes; and (V) other habitat uses; (iv) as needed, use novel sources of data described in clause (ii)(I) in addition to current sources of data, such as visual detection of migratory whales using aerial- and vessel-based surveys; (v) make each map produced under such paragraph available\u2014 (I) through\u2014 (aa) electronic and machine readable formats that can be integrated into on-board vessel navigation systems, including\u2014 (AA) electronic navigational products of the National Oceanic and Atmospheric Administration, as appropriate; (BB) an online platform for the general public; and (CC) in coordination with the Commandant of the Coast Guard, carriage requirements set by the Commandant of the Coast Guard for commercial or recreational vessels; (bb) in coordination with the Commandant of the Coast Guard, other formats not specified under item (aa) that may be required in carriage requirements set by the Commandant of the Coast Guard for commercial or recreational vessels, as appropriate; and (cc) other formats the Under Secretary determines appropriate; and (II) to other entities that produce products or publications included in the carriage requirements set by the Commandant of the Coast Guard for commercial or recreational vessels, as appropriate; and (vi) require the heads of the National Oceanic and Atmospheric Administration line offices to coordinate the work of such offices, as needed; and (B) may, in consultation with the Marine Mammal Commission and non-Federal stakeholders, including State and local governments, research institutions, industry groups, and nongovernmental organizations, determine\u2014 (i) which stocks, populations, or species of migratory whales to prioritize under paragraph (1); and (ii) whether to prioritize the collection and aggregation of new data or the processing, analysis, aggregation, and modeling of existing data. (3) Review Not later than 3 years after the date of the enactment of this subsection and triennially thereafter, the Under Secretary shall, in consultation with the Marine Mammal Commission and non-Federal stakeholders, including State and local governments, research institutions, industry groups, and nongovernmental organizations, carry out a review regarding whether the Under Secretary should update any map produced under paragraph (1) or produce any new map under paragraph (1). (d) Understudied species surveys (1) In general The Under Secretary, in consultation with the Marine Mammal Commission, shall conduct surveys specific to understudied stocks, populations, or species, as the Under Secretary determines appropriate, of migratory whales within waters under the jurisdiction of the United States to estimate the abundance and distribution of each such stock, population, or species. (2) Duties In carrying out paragraph (1), the Under Secretary\u2014 (A) shall\u2014 (i) identify in each survey conducted under such paragraph, as applicable, potential\u2014 (I) calving grounds; (II) mating grounds; (III) feeding grounds; (IV) migration routes; and (V) other habitat uses; (ii) indicate in each such survey the degree of scientific certainty associated with the identification of each area described in subclauses (I) through (V) of clause (i); and (iii) as needed, use current and novel sources of data; and (B) may\u2014 (i) as the Under Secretary determines appropriate, collect opportunistic data on other marine species; and (ii) determine, in consultation with the Marine Mammal Commission and non-Federal stakeholders, including State and local governments, research institutions, industry groups, and nongovernmental organizations, which stocks, populations, or species of migratory whales to prioritize under paragraph (1). (e) Grant program for detection technologies (1) In general Not later than 180 days after the date of the enactment of this subsection, the Under Secretary shall establish a competitive grant program to award amounts, on an annual basis, to eligible entities for the eligible uses described in paragraph (5). (2) Administration The Under Secretary shall enter into a cooperative agreement with the Foundation pursuant to the National Fish and Wildlife Foundation Establishment Act ( 16 U.S.C. 3701 et seq. ) for the Foundation to manage and administer the grant program. (3) Applications To be eligible for a grant pursuant to this subsection, an eligible entity shall submit to the Foundation an application in such form, at such time, and containing such information as the Foundation determines appropriate. (4) Funding (A) In general After the Under Secretary enters into a cooperative agreement with the Foundation under paragraph (2)\u2014 (i) for each fiscal year, the Under Secretary shall provide to the Foundation the amounts made available under this section in an advance payment of the entire amount on October 1, or as soon as practicable thereafter, of each such fiscal year; and (ii) the Foundation shall invest and reinvest excess such amounts for the benefit of the grant program. (B) Application of national fish and wildlife foundation establishment act Amounts received by the Foundation under this subsection shall be subject to the National Fish and Wildlife Foundation Establishment Act ( 16 U.S.C. 3701 et seq. ), except for section 10(a) of that Act ( 16 U.S.C. 3709(a) ). (5) Eligible uses Funds made available for award under this subsection may be spent to develop, assess, and carry out activities that reduce lethal and sub-lethal interactions between ocean users and migratory whales and other large cetaceans, including\u2014 (A) funding research to develop, deploy, or test innovative detection technologies that reduce or eliminate harmful interactions between ocean users and migratory whales and other large cetaceans; (B) efforts to enhance awareness of existing management measures for migratory whales and other large cetaceans; (C) developing on-the-water approaches to support the coexistence of ocean users and migratory whales and other large cetacean species; (D) funding the expansion of infrastructure and capacity to disseminate management and other relevant information that reduces harmful interactions between ocean users and migratory whales and other large cetaceans, especially such interactions that can lead to lethal or sub-lethal injury; and (E) other uses the Foundation, in consultation with the Under Secretary and relevant eligible entities, determines appropriate. (6) Priority In awarding grants under this subsection, the Foundation shall give priority to applications\u2014 (A) with a substantial likelihood of reducing lethal and sub-lethal interactions between ocean users and migratory whales and other large cetaceans; (B) that include cooperation among ocean users; and (C) that demonstrate, or have the potential to provide, economic benefits to small businesses reliant upon fishing, tourism, and maritime-related activities based in the United States. (7) Prohibited use (A) In general An eligible entity that is awarded a grant under this subsection may not use such grant to distribute resources to an entity or individual that is not a United States person, except as provided in subparagraph (B). (B) Exception An eligible entity that is awarded a grant under this subsection may use such grant to distribute resources to a partnership that includes an entity or individual that is not a United States person if the resources are distributed directly to a partner in the partnership that is a United States person. .\n**(11)**\nin subsection (k), as so redesignated, to read as follows:\n(k) Funding (1) In general There are authorized to be appropriated to the Under Secretary for each of fiscal years 2026 through 2030\u2014 (A) to carry out subsection (c), $2,000,000; (B) to carry out subsection (d), $1,000,000; and (C) to carry out subsection (f), $5,000,000. (2) Grant program There are authorized to be appropriated to the Under Secretary to carry out subsection (e), $10,000,000 to remain available until expended. (3) Administrative expenses Each fiscal year, of the amounts made available to carry out subsection (e), the Foundation may use not more than 5 percent or $80,000, whichever is greater, of such amounts for administrative expenses. ; and\n**(12)**\nby adding at the end the following:\n(l) Report Not later than 2 years after the date of the enactment of this subsection, and every 3 years thereafter, the Under Secretary, in consultation with the Marine Mammal Commission, shall submit to Congress and make available to the public a report regarding\u2014 (1) activities carried out under subsections (c) and (d); (2) knowledge gaps identified in carrying out subsection (c); (3) progress made in filling knowledge gaps identified in carrying out subsection (c); and (4) the results and effectiveness of projects carried out with a grant awarded under the grant program. (m) Construction with other laws (1) In general The Under Secretary shall carry out this section notwithstanding any planning or ongoing actions, including rulemakings, under any other provision of law. (2) Rules of construction Nothing in this section may be construed to\u2014 (A) affect the authority or duty of the Under Secretary to issue timely regulations under any provision of law; or (B) allow the Under Secretary to delay any action, order, or rulemaking process under any provision of law. (n) Definitions In this section: (1) Eligible entity The term eligible entity means\u2014 (A) a State, regional, local, or Tribal government; (B) a non-profit organization or research institution with expertise in monitoring or detecting migratory whales or other large cetaceans; (C) any individual or entity the Under Secretary and the Foundation jointly determine appropriate, including ocean users in the fishing, tourism, fishing tackle manufacturing, boating, shipping, marine electronics, ship piloting, vessel towing, and other maritime sectors; and (D) a consortium of 2 or more entities described in any of subparagraphs (A) through (C). (2) Foundation The term Foundation means the National Fish and Wildlife Foundation. (3) Grant program The term grant program means the grant program established under subsection (e)(1). (4) Marine mammal commission The term Marine Mammal Commission means the Marine Mammal Commission established by section 201(a) of the Marine Mammal Protection Act of 1972 ( 16 U.S.C. 1401(a) ). (5) Migratory whale The term migratory whale means all species within either\u2014 (A) the suborder Mysticeti; or (B) the genus Physeter. (6) Pilot project The term pilot project means the pilot monitoring and mitigation project established under subsection (f)(4)(A). (7) Program The term Program means the program established under subsection (a). (8) Subprogram The term Subprogram means the subprogram established under subsection (f)(1). (9) United states person The term United States person has the meaning given the term in section 7701(a)(3) of the Internal Revenue Code of 1986. (10) Waters under the jurisdiction of the united states The term waters under the jurisdiction of the United States has the meaning given the term in section 3 of the Marine Mammal Protection Act of 1972 ( 16 U.S.C. 1362 ). .\n##### (b) Marine mammal stock assessment requirement\nSection 117 of the Marine Mammal Protection Act of 1972 ( 16 U.S.C. 1386 ) is amended by adding at the end the following:\n(f) Use of certain distribution maps In preparing, publishing, or reviewing a stock assessment under this section, the Secretary shall consider each applicable distribution map produced under section 11303(c) of the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 ( 16 U.S.C. 1391(c) ). .",
      "versionDate": "2026-02-03",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2026-03-04T15:54:31Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7332ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Whale CHARTS Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T06:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Whale CHARTS Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-03T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 to provide for a mapping, surveying, monitoring, and mitigation program for migratory whales and other large cetaceans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-03T06:18:27Z"
    }
  ]
}
```
