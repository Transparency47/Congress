# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4512?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4512
- Title: TRANS MICE Act
- Congress: 119
- Bill type: HR
- Bill number: 4512
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2026-05-22T08:07:52Z
- Update date including text: 2026-05-22T08:07:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4512",
    "number": "4512",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "TRANS MICE Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:52Z",
    "updateDateIncludingText": "2026-05-22T08:07:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "AZ"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "TX"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "CO"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "TN"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "PA"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4512ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4512\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Ms. Mace (for herself, Mr. Gosar , Mr. Gill of Texas , and Ms. Boebert ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo prohibit the availability of Federal funds for certain animal research, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transgender Research on Animals Now Stops and Money for Ideological Cruelty Eliminated Act or the TRANS MICE Act .\n#### 2. Prohibition on availability of Federal funds for certain animal research\n##### (a) In general\nNotwithstanding any other provision of law, no Federal funds may be made available to conduct, support, or fund (directly or indirectly) any covered research on a qualified animal.\n##### (b) Definitions\nIn this section:\n**(1) Covered research**\nThe term covered research means any research to study the effects of drugs, hormones, surgery, or other interventions to alter the body of a qualified animal to no longer correspond to the biological sex of such animal, including by\u2014\n**(A)**\ndisrupting the development of an animal\u2019s body;\n**(B)**\ninhibiting the natural functions of the animal\u2019s body; or\n**(C)**\nmodifying the physical appearance of an animal.\n**(2) Excepted animal**\nThe term excepted animal means any non-human vertebrate that\u2014\n**(A)**\nchanges sex during its lifetime; or\n**(B)**\nnaturally possesses both male and female reproductive organs.\n**(3) Qualified animal**\nThe term qualified animal means any non-human vertebrate species (other than excepted animals). Such term includes mammals, birds, fish, reptiles, and amphibians.",
      "versionDate": "2025-07-17",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Animal protection and human-animal relationships",
            "updateDate": "2025-09-12T17:09:11Z"
          },
          {
            "name": "Medical ethics",
            "updateDate": "2025-09-12T17:09:44Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-09-12T17:09:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-09-11T14:23:17Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4512ih.xml"
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
      "title": "TRANS MICE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:38:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TRANS MICE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transgender Research on Animals Now Stops and Money for Ideological Cruelty Eliminated Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the availability of Federal funds for certain animal research, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T12:33:52Z"
    }
  ]
}
```
