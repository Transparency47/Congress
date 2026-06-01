# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5355?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5355
- Title: Ian Kalvinskas Pediatric Liver Cancer Early Detection and Screening Act
- Congress: 119
- Bill type: HR
- Bill number: 5355
- Origin chamber: House
- Introduced date: 2025-09-15
- Update date: 2026-05-14T08:08:05Z
- Update date including text: 2026-05-14T08:08:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-15: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-18 - IntroReferral: Sponsor introductory remarks on measure. (CR H4418)
- Latest action: 2025-09-15: Introduced in House

## Actions

- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-18 - IntroReferral: Sponsor introductory remarks on measure. (CR H4418)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5355",
    "number": "5355",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001059",
        "district": "21",
        "firstName": "Jim",
        "fullName": "Rep. Costa, Jim [D-CA-21]",
        "lastName": "Costa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Ian Kalvinskas Pediatric Liver Cancer Early Detection and Screening Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:05Z",
    "updateDateIncludingText": "2026-05-14T08:08:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H4418)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-15",
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
      "actionDate": "2025-09-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-15",
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
          "date": "2025-09-15T16:04:30Z",
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
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "DC"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "MI"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "FL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NJ"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "MI"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "NE"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "MI"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "PA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5355ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5355\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 15, 2025 Mr. Costa (for himself and Ms. Van Duyne ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to carry out activities to promote screenings for liver diseases in newborns, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ian Kalvinskas Pediatric Liver Cancer Early Detection and Screening Act .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe life of California teenager Ian Kalvinskas\u2014who received a liver transplant, fulfilled his goal of interning on Capitol Hill, and died from cancer on June 27, 2025\u2014demonstrates the urgent need for earlier detection of pediatric liver disease, lifelong follow-up, and wider access to donor organs;\n**(2)**\npediatric primary liver tumors are among the fastest-rising childhood cancers in the United States, with hepatoblastoma increasing by approximately 2 percent per year to and now approaching 1.7 cases per million children; although the overall 5-year relative survival rate from a pediatric primary liver tumor is about 77 percent, survival falls below 60 percent for adolescents and for tumors diagnosed with distant metastases;\n**(3)**\nbiliary atresia, a neonatal malformation of the bile ducts occurring in roughly 1 in 12,000 live births and the leading indication for infant liver transplantation, shows transplant-free survival that roughly doubles when a Kasai portoenterostomy is performed before 60 days of life;\n**(4)**\nclinically validated early-warning tools can detect cholestatic liver disease in time for therapeutic intervention, including\u2014\n**(A)**\nroutine direct-bilirubin measurement in the newborn heel-stick panel, which when used in multi-center, United States pilots detected 100 percent of biliary-atresia cases with minimal false positives; and\n**(B)**\nimproved education of pediatric primary care providers to be alert to early warning signs of biliary atresia with expedited referral to pediatric liver specialists;\n**(5)**\ndespite recent liver donor allocation reforms, more than 1 in 10 infants and more than 1 in 20 older children on the United States liver-transplant wait list die before receiving a graft;\n**(6)**\nliving-donor liver transplantation expands the pediatric organ pool and delivers equivalent or superior 1-year, 3-year, and 5-year graft and patient survival compared with deceased-donor grafts; and\n**(7)**\nmany children with rare liver diseases, including liver cancer, are only able to receive timely transplants through physician advocacy to petition for exceptions to the standard listing practices.\n#### 3. Pediatric liver disease outcomes and newborn screening panels\n##### (a) GAO Study\nThe Comptroller General of the United States shall conduct a study on\u2014\n**(1)**\nfederally funded initiatives to improve early detection and treatment of pediatric liver tumors, including education programs for healthcare providers, as well as research to identify risk factors and innovative therapeutic strategies;\n**(2)**\nto the extent reliable data are available, what is known about trends in pediatric liver-transplant wait-list mortality, including a breakdown by geography, race, insurance status, diagnosis, and severity of illness; and\n**(3)**\nto the extent reliable data are available, what is known about the cost effectiveness of adding direct-bilirubin as a screening test for biliary atresia and other cholestatic liver diseases to State newborn-screening panels.\n##### (b) Report to Congress\nNot later than one year after the date of enactment of this Act, the Comptroller General shall transmit to Congress a report on the results of the study.\n#### 4. Public education program\n##### (a) In general\nThe Secretary of Health and Human Services, acting through the Administrator for the Health Resources and Services Administration, in consultation with the Director of the Centers for Disease Control and Prevention (in this section referred to as the CDC ), shall carry out a public education program under which the Secretary shall develop and disseminate plain-language materials on\u2014\n**(1)**\nearly signs of pediatric liver disease; and\n**(2)**\nthe option and safety of living liver donation.\n##### (b) Implementation\nIn carrying out the program under subsection (a), the Secretary may\u2014\n**(1)**\ncoordinate implementation of the program with programs of the CDC, including the National Comprehensive Cancer Control Program (or any successor campaign); and\n**(2)**\nin addition to the program referred to in paragraph (1), disseminate materials developed under this section through any other public-education initiative of the Department of Health and Human Services that promotes liver-disease prevention, pediatric cancer awareness, or living-organ donation.\n##### (c) GAO report to Congress\nNot later than 3 years after the date on which the Secretary initiates the program under subsection (a), the Comptroller General of the United States shall transmit to Congress a report on the results of the program.\n##### (d) Funding\nNo additional funds are authorized to be appropriated for the purpose of carrying out this section.",
      "versionDate": "2025-09-15",
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
        "name": "Health",
        "updateDate": "2025-09-25T13:59:43Z"
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
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5355ih.xml"
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
      "title": "Ian Kalvinskas Pediatric Liver Cancer Early Detection and Screening Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-24T06:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ian Kalvinskas Pediatric Liver Cancer Early Detection and Screening Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-24T06:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to carry out activities to promote screenings for liver diseases in newborns, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T06:33:16Z"
    }
  ]
}
```
