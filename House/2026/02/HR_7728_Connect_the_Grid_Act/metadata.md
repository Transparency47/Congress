# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7728?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7728
- Title: Connect the Grid Act
- Congress: 119
- Bill type: HR
- Bill number: 7728
- Origin chamber: House
- Introduced date: 2026-02-26
- Update date: 2026-04-14T08:05:22Z
- Update date including text: 2026-04-14T08:05:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-26: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-26: Introduced in House

## Actions

- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7728",
    "number": "7728",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001131",
        "district": "35",
        "firstName": "Greg",
        "fullName": "Rep. Casar, Greg [D-TX-35]",
        "lastName": "Casar",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Connect the Grid Act",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:22Z",
    "updateDateIncludingText": "2026-04-14T08:05:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-26",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-26",
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
          "date": "2026-02-26T14:31:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "WA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "MN"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7728ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7728\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2026 Mr. Casar (for himself, Ms. Ocasio-Cortez , Ms. Escobar , Ms. Garcia of Texas , Mr. Green of Texas , Mr. Doggett , Ms. Crockett , Mr. Castro of Texas , Mr. Espaillat , Mr. Garcia of California , Mr. Frost , Ms. Tlaib , Ms. Jayapal , and Mrs. Ramirez ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo interconnect the Electric Reliability Council of Texas to its neighbors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Connect the Grid Act .\n#### 2. Jurisdiction with respect to ERCOT\n##### (a) Application of part\nSection 201(b)(2) of the Federal Power Act ( 16 U.S.C. 824(b)(2) ) is amended by\u2014\n**(1)**\nstriking 210, 211, 211A, 212 the second place it appears; and\n**(2)**\nstriking an electric utility or other entity and inserting any entity that is otherwise exempt under section 201(f) .\n##### (b) Public utility definition\nSection 201(e) of the Federal Power Act ( 16 U.S.C. 824(e) ) is amended by striking 210, 211, 211A, 212, .\n##### (c) Repeal of ERCOT Exemptions\n**(1)**\nSection 212 of the Federal Power Act ( 16 U.S.C. 824k ) is amended by striking subsection (k).\n**(2)**\nSection 216 of the Federal Power Act ( 16 U.S.C. 824p ) is amended by striking subsection (k).\n**(3)**\nSection 217 of the Federal Power Act ( 16 U.S.C. 824q ) is amended by striking subsection (h).\n**(4)**\nSection 220 of the Federal Power Act ( 16 U.S.C. 824t ) is amended by striking subsection (f).\n##### (d) Technical conference\nNot later than 6 months after the date of enactment of this Act, the Commission shall convene a technical conference to assist entities affected by the amendments made by this section with compliance with any requirements pursuant to such amendments, including by publishing the steps necessary for such compliance.\n#### 3. Electric reliability\n##### (a) Amendments\nSection 215 of the Federal Power Act ( 16 U.S.C. 824o ) is amended\u2014\n**(1)**\nin subsection (a)(3), by striking enlarge such facilities or to construct new transmission capacity or generation capacity and inserting construct new generation capacity ; and\n**(2)**\nin subsection (i)(2), by striking or transmission .\n##### (b) Reliability standard for total transfer capability\n**(1) In general**\nNot later than 30 days after the date of enactment of this Act, the Commission shall order the Electric Reliability Organization to submit to the Commission a proposed reliability standard that requires minimum total transfer capability of\u2014\n**(A)**\nbetween 4.3 and 12.6 gigawatts between the area under functional control of ERCOT and the area under functional control of SPP;\n**(B)**\nbetween 2.5 and 16.2 gigawatts between the area under functional control of ERCOT and the area under functional control of MISO; and\n**(C)**\nbetween 2.6 and 7.9 gigawatts between the area under functional control of ERCOT and the Western Interconnection.\n**(2) Contents**\nThe Commission may only approve a proposed reliability standard described in paragraph (1) if such reliability standard\u2014\n**(A)**\nrequires minimum total transfer capability as described in paragraph (1); and\n**(B)**\nrequires each of ERCOT and SPP, ERCOT and MISO, and ERCOT and 1 or more neighboring balancing authorities in the Western Interconnection (as determined by the Electric Reliability Organization), to jointly submit, not later than 1 year after the date of enactment of this Act, a plan that\u2014\n**(i)**\ndesignates 1 or more entities to site and construct new transmission facilities, or modify existing transmission facilities, to achieve the applicable minimum total transfer capability; and\n**(ii)**\nincludes a timeline for such siting and construction or modification, which timeline shall include that such siting and construction or modification be completed by January 1, 2037.\n**(3) Priority**\nAny plan for the siting and construction or modification of transmission facilities described in paragraph (2)(B) shall prioritize\u2014\n**(A)**\nuse of grid-enhancing technologies;\n**(B)**\nuse of existing rights-of-ways, such as highways and railroads, to site and construct new transmission facilities;\n**(C)**\nsiting and construction of new transmission facilities on degraded land, including sites on the National Priorities List, brownfield sites, landfills, abandoned mine land, and contaminated or abandoned agricultural lands;\n**(D)**\nsiting and construction of new transmission facilities that expands access to renewable energy sources, including wind, solar, and geothermal sources;\n**(E)**\nproviding meaningful community involvement opportunities, including conducting outreach to\u2014\n**(i)**\nenvironmental justice communities, including conducting planning meetings, set at times and places to maximize the number of community members who can conveniently attend, with appropriate services, including translation and interpreting services and virtual attendance, in such environmental justice communities;\n**(ii)**\nTribal and Indigenous Communities;\n**(iii)**\nTribal Governments; and\n**(iv)**\nrelevant labor organizations; and\n**(F)**\nthe use of registered apprenticeship programs and prevailing wages, as determined by the Secretary of Labor in accordance with subchapter IV of chapter 31 of title 40, United States Code.\n**(4) Environmental review**\nAny project to site, construct, or modify transmission facilities that is conducted to comply with the reliability standard described in paragraph (1) shall be subject to the requirements of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) and the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ).\n##### (c) Consideration for national interest electric transmission corridor\nIn carrying out section 216 of the Federal Power Act ( 16 U.S.C. 824p ), the Secretary of Energy shall consider designating as a national interest electric transmission corridor any area in which transmission facilities will be sited and constructed or modified pursuant to this section.\n#### 4. Increased borrowing authority under the Transmission Facilitation Program\nSection 40106(d)(2) of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18713(d)(2) ) is amended by striking $2,500,000,000 and inserting $13,500,000,000 .\n#### 5. Study on benefits of interconnection with Mexico\nNot later than one year after the date of enactment of this Act, the Secretary of Energy shall conduct a study and submit to Congress a report on the reliability, climate, and cost benefits of interconnection of facilities for the generation, transmission, and sale of electric energy with such facilities in Mexico and the siting and construction, or modification, of such facilities that will bring the most cumulative benefits.\n#### 6. Definitions\nIn this Act:\n**(1) Abandoned mine land**\nThe term abandoned mine land means land, water, or a watershed that is contaminated or scarred by extraction, beneficiation, or processing of ores or minerals (which may include phosphate, but does not include coal).\n**(2) Brownfield site**\nThe term brownfield site has the meaning given such term in section 101(39) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9601(39) ).\n**(3) Commission**\nThe term Commission means the Federal Energy Regulatory Commission.\n**(4) Electric Reliability Organization**\nThe term Electric Reliability Organization has the meaning given such term in section 215(a)(2) of the Federal Power Act ( 16 U.S.C. 824o(a)(2) ).\n**(5) Environmental justice community**\nThe term environmental justice community means a community with significant representation of communities of color, low-income communities, or Tribal and Indigenous communities that experiences, or is at risk of experiencing higher or more adverse human health or environmental effects.\n**(6) ERCOT**\nThe term ERCOT means the Electric Reliability Council of Texas.\n**(7) Grid-enhancing technology**\nThe term grid-enhancing technology means a solution that increases the transfer capability of high-voltage transmission facilities.\n**(8) MISO**\nThe term MISO means the Midcontinent Independent System Operator transmission organization.\n**(9) National Priorities List**\nThe term National Priorities List means the National Priorities List developed by the President in accordance with section 105(a)(8)(B) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9605(a)(8)(B) ).\n**(10) Registered apprenticeship program**\nThe term registered apprenticeship program means an apprenticeship registered under the National Apprenticeship Act that meets the standards of subpart A of part 29, and part 30, of title 29, Code of Federal Regulations.\n**(11) Reliability standard**\nThe term reliability standard has the meaning given such term in section 215(a)(3) of the Federal Power Act ( 16 U.S.C. 824o(a)(3) ).\n**(12) SPP**\nThe term SPP means the Southwest Power Pool transmission organization.\n**(13) Total transfer capability**\nThe term total transfer capability has the meaning given such term in section 37.6(b)(1)(vi) of title 18, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(14) Transmission facility**\nThe term transmission facility means a facility that is used for the transmission of electric energy in interstate commerce, including transmission lines.\n**(15) Transmission organization**\nThe term transmission organization has the meaning given such term in section 215(a)(6) of the Federal Power Act ( 16 U.S.C. 824o(a)(6) ).\n**(16) Tribal and Indigenous community**\nThe term Tribal and Indigenous community means a population of people who are members of\u2014\n**(A)**\na federally recognized Indian Tribe;\n**(B)**\na State-recognized Indian Tribe;\n**(C)**\nan Alaska Native or Native Hawaiian community or organization; or\n**(D)**\nany other community of Indigenous people located in a State.\n**(17) Tribal Government**\nThe term Tribal Government means the governing body of an Indian Tribe.\n**(18) Western Interconnection**\nThe term Western Interconnection means the synchronously operated electric transmission grid located in the western part of North America, including parts of Montana, Nebraska, New Mexico, South Dakota, Texas, Wyoming and Mexico and all of Arizona, California, Colorado, Idaho, Nevada, Oregon, Utah, Washington and the Canadian Provinces of British Columbia and Alberta.",
      "versionDate": "2026-02-26",
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
        "name": "Energy",
        "updateDate": "2026-03-04T15:53:49Z"
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
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7728ih.xml"
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
      "title": "Connect the Grid Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Connect the Grid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-03T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To interconnect the Electric Reliability Council of Texas to its neighbors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-03T06:18:27Z"
    }
  ]
}
```
