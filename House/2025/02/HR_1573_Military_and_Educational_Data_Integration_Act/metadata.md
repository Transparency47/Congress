# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1573?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1573
- Title: Military and Educational Data Integration Act
- Congress: 119
- Bill type: HR
- Bill number: 1573
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2026-04-10T16:59:41Z
- Update date including text: 2026-04-10T16:59:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1573",
    "number": "1573",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000590",
        "district": "3",
        "firstName": "Susie",
        "fullName": "Rep. Lee, Susie [D-NV-3]",
        "lastName": "Lee",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Military and Educational Data Integration Act",
    "type": "HR",
    "updateDate": "2026-04-10T16:59:41Z",
    "updateDateIncludingText": "2026-04-10T16:59:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T15:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "KS"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "MI"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "TN"
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
      "sponsorshipDate": "2025-02-25",
      "state": "GU"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "HI"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "GA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "KS"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "LA"
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
      "sponsorshipDate": "2025-02-25",
      "state": "AS"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "IL"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1573ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1573\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Ms. Lee of Nevada (for herself, Mr. Schmidt , Mr. Bergman , Mr. Fleischmann , Mr. Moylan , Mr. Case , Mr. McCormick , Mr. Moulton , Ms. Davids of Kansas , Mr. Fields , Mrs. Radewagen , and Mr. Sorensen ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo establish a process to furnish to State educational agencies certain demographic data regarding members of the Armed Forces.\n#### 1. Short title\nThis Act may be cited as the Military and Educational Data Integration Act .\n#### 2. Process to furnish certain demographic data regarding members of the Armed Forces to State educational agencies\n##### (a) Establishment\nThe Secretaries concerned, in consultation with the Secretary of Education, State educational agencies, local educational agencies, and experts in student data and privacy, shall, not later than 18 months after the date of enactment of this Act, establish a data sharing process that enables a State educational agency to\u2014\n**(1)**\naccess data described in subsection (b) attributable to individuals who graduated high school in the State of such State educational agency; and\n**(2)**\nintegrate such data into\u2014\n**(A)**\nsuch State\u2019s statewide longitudinal data system; or\n**(B)**\nan alternate data system operated by such State.\n##### (b) Data described\nThe data described in this paragraph may include the following information:\n**(1)**\nWith respect to an individual who is a member of an Armed Force who graduated from secondary school:\n**(A)**\nThe highest level of education attained.\n**(B)**\nThe name and location of the educational institution where the member received education described in subparagraph (A).\n**(C)**\nThe name and location of the secondary school from which the individual graduated.\n**(D)**\nScore on the Armed Forces Qualification Test.\n**(E)**\nThe date the member joined an Armed Force.\n**(F)**\nThe Armed Force of the member.\n**(G)**\nRank.\n**(H)**\nThe area of expertise or military occupational specialty.\n**(I)**\nThe date of separation, if applicable.\n**(J)**\nAny other information determined appropriate by the Secretary concerned.\n**(2)**\nWith respect to an individual who graduated from secondary school and whose application to join an Armed Force was denied:\n**(A)**\nThe highest level of education attained.\n**(B)**\nThe name and location of the school where the individual received education described in subparagraph (A).\n**(C)**\nThe name and location of the secondary school from which the individual graduated.\n**(D)**\nScore on the Armed Forces Qualification Test.\n##### (c) Privacy\n**(1) Confidentiality**\nData transmitted through the data sharing process under subsection (a) shall be transmitted confidentially and using the most current standards for data security at the time of transmission.\n**(2) Protection of individual privacy and data security**\nThe Secretaries concerned shall carry out subsection (a) in a manner that protects individual privacy and data security, in accordance with applicable Federal, State, and local privacy laws.\n**(3) Data security practices**\nEach Secretary concerned and each State educational agency that accesses data under subsection (a) shall establish, implement, and maintain reasonable data security practices to protect\u2014\n**(A)**\nthe confidentiality, integrity, and availability of data; and\n**(B)**\ndata against unauthorized access.\n##### (d) Definitions\nIn this section:\n**(1)**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of Defense; or\n**(B)**\nthe Secretary of Homeland Security.\n**(2)**\nThe terms local educational agency , secondary school , and State educational agency have the meanings given such terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).",
      "versionDate": "2025-02-25",
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
            "name": "Computer security and identity theft",
            "updateDate": "2025-07-24T14:15:43Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-10T16:59:41Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-07-24T14:15:33Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2025-07-24T14:15:37Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-24T14:15:22Z"
          },
          {
            "name": "Student records",
            "updateDate": "2025-07-24T14:15:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-13T18:52:09Z"
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
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1573ih.xml"
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
      "title": "Military and Educational Data Integration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T13:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Military and Educational Data Integration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a process to furnish to State educational agencies certain demographic data regarding members of the Armed Forces.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T13:03:51Z"
    }
  ]
}
```
