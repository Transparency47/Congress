# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5026?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5026
- Title: ALCATRAZ Act
- Congress: 119
- Bill type: HR
- Bill number: 5026
- Origin chamber: House
- Introduced date: 2025-08-22
- Update date: 2025-09-19T16:54:46Z
- Update date including text: 2025-09-19T16:54:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-22: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-08-22: Introduced in House

## Actions

- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-22",
    "latestAction": {
      "actionDate": "2025-08-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5026",
    "number": "5026",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001240",
        "district": "6",
        "firstName": "Addison",
        "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
        "lastName": "McDowell",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "ALCATRAZ Act",
    "type": "HR",
    "updateDate": "2025-09-19T16:54:46Z",
    "updateDateIncludingText": "2025-09-19T16:54:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-22",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-22",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-22",
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
          "date": "2025-08-22T13:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-22T13:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "AL"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "CO"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "FL"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "FL"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "NC"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "NC"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "IN"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "NC"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5026ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5026\nIN THE HOUSE OF REPRESENTATIVES\nAugust 22, 2025 Mr. McDowell (for himself, Mr. Moore of Alabama , Ms. Boebert , Ms. Lee of Florida , Mr. Donalds , Mr. Harrigan , and Mr. Moore of North Carolina ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Appropriations , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish in the Department of Homeland Security a grant program to reimburse States the costs incurred by such States relating to the detention of migrants at detention facilities in such States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accelerated Logistics and Coordination for Arresting, Transporting, and Removing Aliens Zones Act or the ALCATRAZ Act .\n#### 2. DHS grant program relating to detention of migrants\n##### (a) In general\nThere is established in the Department of Homeland Security a grant program, to be known as the Detention and Logistics Program (in this section referred to as the Program ), to reimburse States and local governments the costs incurred, on and after January 20, 2025, by such States or local governments, as the case may be, relating to the detention of migrants at detention facilities in such States.\n##### (b) Application\nTo be eligible for reimbursement under the Program, a State or local government, as the case may be, shall submit to the Secretary of Homeland Security an application at such time, in such manner, and containing such information as the Secretary may require.\n##### (c) Funding\nThe Secretary of Homeland Security shall transfer the unobligated balances of all amounts made available as of the date of the enactment of this Act to the Shelter and Services Program administered by the Federal Emergency Management Agency to, and merge such balances with, appropriate accounts of the Department of Homeland Security to carry out the Program.\n##### (d) Report\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Homeland Security shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report that includes the following:\n**(1)**\nA plan for\u2014\n**(A)**\ncoordinating with States to rapidly construct new migrant detention facilities; and\n**(B)**\nidentifying Federal or State properties that might be used for such construction.\n**(2)**\nThe identification of underutilized, wasteful, or redundant accounts the funding of which could be better utilized by the Detention and Logistics Program of the Department of Homeland Security.",
      "versionDate": "2025-08-22",
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
        "name": "Immigration",
        "updateDate": "2025-09-19T16:54:46Z"
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
      "date": "2025-08-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5026ih.xml"
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
      "title": "ALCATRAZ Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-23T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ALCATRAZ Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-23T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Accelerated Logistics and Coordination for Arresting, Transporting, and Removing Aliens Zones Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-23T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish in the Department of Homeland Security a grant program to reimburse States the costs incurred by such States relating to the detention of migrants at detention facilities in such States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-23T08:18:26Z"
    }
  ]
}
```
