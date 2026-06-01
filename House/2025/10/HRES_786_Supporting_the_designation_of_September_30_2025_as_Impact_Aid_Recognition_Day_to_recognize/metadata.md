# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/786?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/786
- Title: Supporting the designation of September 30, 2025, as "Impact Aid Recognition Day" to recognize and celebrate the 75th anniversary of the establishment of the Impact Aid program.
- Congress: 119
- Bill type: HRES
- Bill number: 786
- Origin chamber: House
- Introduced date: 2025-10-03
- Update date: 2025-12-12T15:56:20Z
- Update date including text: 2025-12-12T15:56:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-03: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-10-03 - IntroReferral: Submitted in House
- 2025-10-03 - IntroReferral: Submitted in House
- Latest action: 2025-10-03: Submitted in House

## Actions

- 2025-10-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-10-03 - IntroReferral: Submitted in House
- 2025-10-03 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/786",
    "number": "786",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "N000189",
        "district": "4",
        "firstName": "Dan",
        "fullName": "Rep. Newhouse, Dan [R-WA-4]",
        "lastName": "Newhouse",
        "party": "R",
        "state": "WA"
      }
    ],
    "title": "Supporting the designation of September 30, 2025, as \"Impact Aid Recognition Day\" to recognize and celebrate the 75th anniversary of the establishment of the Impact Aid program.",
    "type": "HRES",
    "updateDate": "2025-12-12T15:56:20Z",
    "updateDateIncludingText": "2025-12-12T15:56:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-10-03T19:32:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CT"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "TX"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "ID"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "IL"
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
      "sponsorshipDate": "2025-10-03",
      "state": "GA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NE"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "IL"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "IL"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "TX"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "HI"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "WA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres786ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 786\nIN THE HOUSE OF REPRESENTATIVES\nOctober 3, 2025 Mr. Newhouse (for himself, Mr. Courtney , Ms. Stefanik , Mr. Castro of Texas , Mr. Simpson , Mr. Foster , Mr. Carter of Georgia , Mr. Thompson of California , Mr. Bacon , Mr. Peters , Mr. Bost , Mr. Davis of Illinois , Mr. Williams of Texas , Mr. Case , Ms. Strickland , Mr. Huffman , and Mr. Levin ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nSupporting the designation of September 30, 2025, as Impact Aid Recognition Day to recognize and celebrate the 75th anniversary of the establishment of the Impact Aid program.\nThat the House of Representatives\u2014\n**(1)**\nsupports Impact Aid Recognition Day to recognize the 75th anniversary of the establishment of the Impact Aid program; and\n**(2)**\nrecognizes the importance of\u2014\n**(A)**\nthe Impact Aid program under title VII of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7701 et seq. ); and\n**(B)**\nthe objective of that program to ensure that all children educated in Federally impacted school districts receive a high-quality education and have access to the opportunities needed to reach their full potential.",
      "versionDate": "2025-10-03",
      "versionType": "IH"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-10-06",
        "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S6959; text: CR 9/18/2025 S6737)"
      },
      "number": "406",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution designating September 30, 2025, as \"Impact Aid Recognition Day\" to recognize and celebrate the 75th anniversary of the establishment of the Impact Aid program.",
      "type": "SRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-11-13T20:09:18Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-11-13T20:09:18Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-11-13T20:09:18Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-11-13T20:09:18Z"
          },
          {
            "name": "Property tax",
            "updateDate": "2025-11-13T20:09:18Z"
          },
          {
            "name": "State and local taxation",
            "updateDate": "2025-11-13T20:09:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-12-12T15:56:20Z"
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
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres786ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting the designation of September 30, 2025, as \"Impact Aid Recognition Day\" to recognize and celebrate the 75th anniversary of the establishment of the Impact Aid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T10:18:24Z"
    },
    {
      "title": "Supporting the designation of September 30, 2025, as \"Impact Aid Recognition Day\" to recognize and celebrate the 75th anniversary of the establishment of the Impact Aid program.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T08:05:40Z"
    }
  ]
}
```
