# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6211?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6211
- Title: Medical Professional Access Act
- Congress: 119
- Bill type: HR
- Bill number: 6211
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-02-05T09:06:31Z
- Update date including text: 2026-02-05T09:06:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6211",
    "number": "6211",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001218",
        "district": "7",
        "firstName": "Richard",
        "fullName": "Rep. McCormick, Richard [R-GA-7]",
        "lastName": "McCormick",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Medical Professional Access Act",
    "type": "HR",
    "updateDate": "2026-02-05T09:06:31Z",
    "updateDateIncludingText": "2026-02-05T09:06:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "FL"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "MP"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6211ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6211\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. McCormick (for himself, Mr. Donalds , and Mrs. King-Hinds ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 41, United States Code, to expand license portability for health care professionals providing health care services in response to a Federal emergency declaration pursuant to a contract with the Federal Government, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Medical Professional Access Act .\n#### 2. Portability of licensure of health care professionals serving pursuant to a Federal contract\n##### (a) In general\nSubtitle IV of title 41, United States Code, is amended by adding at the end the following:\n89 Portability of licensure of health care professionals serving pursuant to a Federal contract Sec. 8901. Licensure of health care professionals serving pursuant to a Federal contract. 8901. Licensure of health care professionals serving pursuant to a Federal contract (a) In general Notwithstanding any State law regarding the licensure of health care professionals, a health care professional may provide health care services pursuant to a contract or subcontract with the Federal Government at any location in any State, the District of Columbia, or a commonwealth, territory, or possession of the United States, so long as such services are\u2014 (1) in response to a federally declared emergency; and (2) within the scope of the authorized duties under such contract. (b) Definitions In this section: (1) The term federally declared emergency includes\u2014 (A) an emergency or major disaster declared by the President under the Robert T. Stafford Disaster Relief and Emergency Assistance Act; (B) a public health emergency declared by the Secretary of Health and Human Services under section 319 of the Public Health Service Act; and (C) any other national emergency or crisis requiring a Federal response, as certified in a written notice published in the Federal Register by the head of an Executive Department (as specified in section 101 of title 5). (2) The term health care professional means an individual licensed, registered, or certified under Federal or State laws or regulations to provide health care services. .\n##### (b) Table of chapters amendment\nThe table of chapters at the beginning of subtitle IV of title 41, United States Code, is amended by adding at the end the following:\n89. Licensure of health care professionals serving pursuant to a Federal contract 8901 .",
      "versionDate": "2025-11-20",
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
        "updateDate": "2025-12-10T16:28:20Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6211ih.xml"
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
      "title": "Medical Professional Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medical Professional Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 41, United States Code, to expand license portability for health care professionals providing health care services in response to a Federal emergency declaration pursuant to a contract with the Federal Government, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:20Z"
    }
  ]
}
```
