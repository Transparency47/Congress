# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1555?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1555
- Title: Bureau of Land Management Mineral Spacing Act
- Congress: 119
- Bill type: HR
- Bill number: 1555
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2026-04-01T16:21:48Z
- Update date including text: 2026-04-01T16:21:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-18 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2026-03-25 - Committee: Subcommittee Hearings Held
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-18 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2026-03-25 - Committee: Subcommittee Hearings Held

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1555",
    "number": "1555",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Bureau of Land Management Mineral Spacing Act",
    "type": "HR",
    "updateDate": "2026-04-01T16:21:48Z",
    "updateDateIncludingText": "2026-04-01T16:21:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy and Mineral Resources.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
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
      "text": "Referred to the House Committee on Natural Resources.",
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
          "date": "2025-02-25T15:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-25T14:15:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-18T15:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
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
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "ND"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "TX"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1555ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1555\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mrs. Bice introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Mineral Leasing Act to streamline the oil and gas permitting process and to recognize fee ownership for certain oil and gas drilling or spacing units, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bureau of Land Management Mineral Spacing Act .\n#### 2. Access to federal energy resources from non-federal surface estate\nSection 17 of the Mineral Leasing Act ( 30 U.S.C. 226 ) is amended by adding at the end the following:\n(r) No federal permit required for oil and gas activities on certain land (1) In general The Secretary shall not require an operator to obtain a Federal drilling permit for oil and gas exploration and production activities conducted on non-Federal surface estate, provided that\u2014 (A) the United States holds an ownership interest of less than 50 percent of the subsurface mineral estate to be accessed by the proposed action; and (B) the operator submits to the Secretary a State permit to conduct oil and gas exploration and production activities on the non-Federal surface estate. (2) No federal action An oil and gas exploration and production activity carried out under paragraph (1)\u2014 (A) shall not be considered a major Federal action for the purposes of section 102(2)(C) of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332 ); (B) shall require no additional Federal action; (C) may commence 30 days after submission of the State permit to the Secretary; and (D) shall not be subject to\u2014 (i) section 306108 of title 54, United States Code (commonly known as the National Historic Preservation Act of 1966); and (ii) section 7 of the Endangered Species Act of 1973 ( 16 U.S.C. 1536 ). (3) Royalties and production accountability (A) Nothing in this subsection shall affect the amount of royalties due to the United States under this Act from the production of oil and gas, or alter the Secretary\u2019s authority to conduct audits and collect civil penalties pursuant to the Federal Oil and Gas Royalty Management Act of 1982 ( 30 U.S.C. 1701 et seq. ). (B) The Secretary may conduct onsite reviews and inspections to ensure proper accountability, measurement, and reporting of production of Federal oil and gas, and payment of royalties. (4) Nonapplicability to Indian lands This subsection shall not apply to Indian lands. (5) Indian land In this subsection, the term Indian land means\u2014 (A) any land located within the boundaries of an Indian reservation, pueblo, or rancheria; and (B) any land not located within the boundaries of an Indian reservation, pueblo, or rancheria, the title to which is held\u2014 (i) in trust by the United States for the benefit of an Indian tribe or an individual Indian; (ii) by an Indian tribe or an individual Indian, subject to restriction against alienation under laws of the United States; or (iii) by a dependent Indian community. .",
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
            "name": "Energy revenues and royalties",
            "updateDate": "2026-04-01T16:00:56Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2026-04-01T16:21:48Z"
          },
          {
            "name": "Mining",
            "updateDate": "2026-03-31T18:13:59Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2026-03-31T18:13:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-03-18T14:15:36Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1555ih.xml"
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
      "title": "Bureau of Land Management Mineral Spacing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bureau of Land Management Mineral Spacing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Mineral Leasing Act to streamline the oil and gas permitting process and to recognize fee ownership for certain oil and gas drilling or spacing units, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:29Z"
    }
  ]
}
```
