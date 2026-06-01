# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6689?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6689
- Title: ETHICAL Procurement Act
- Congress: 119
- Bill type: HR
- Bill number: 6689
- Origin chamber: House
- Introduced date: 2025-12-12
- Update date: 2026-01-07T23:12:24Z
- Update date including text: 2026-01-07T23:12:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-12: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-12-12: Introduced in House

## Actions

- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-12",
    "latestAction": {
      "actionDate": "2025-12-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6689",
    "number": "6689",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001066",
        "district": "4",
        "firstName": "Steven",
        "fullName": "Rep. Horsford, Steven [D-NV-4]",
        "lastName": "Horsford",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "ETHICAL Procurement Act",
    "type": "HR",
    "updateDate": "2026-01-07T23:12:24Z",
    "updateDateIncludingText": "2026-01-07T23:12:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
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
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-12",
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
          "date": "2025-12-12T14:02:30Z",
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
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6689ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6689\nIN THE HOUSE OF REPRESENTATIVES\nDecember 12, 2025 Mr. Horsford (for himself and Mr. Cisneros ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo prohibit the Secretary of Defense from awarding contracts to entities of which certain current Government employees are officers or owners, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring Transparency, Honesty, and Integrity for Contracting, Acquisition, and Lifecycle Procurement Act or the ETHICAL Procurement Act .\n#### 2. Prohibition on eligibility for defense contracts for certain entities\n##### (a) In general\nNotwithstanding any other provision of law, the Secretary of Defense may not enter into, renew, or extend any contract or other agreement for the acquisition of any good or service produced or provided by an entity if\u2014\n**(1)**\nan officer, director, partner, or majority owner of such entity\u2014\n**(A)**\nholds a position to which such individual was appointed by the President by and with the advice and consent of the Senate;\n**(B)**\nholds a position in the executive branch of the Government of a confidential or policy-determining character under schedule C of subpart C of part 213 of title 5, Code of Federal Regulations;\n**(C)**\nis a special Government employee; or\n**(D)**\nholds a position in the Senior Executive Service (as defined in section 2101a of title 5, United States Code); or\n**(2)**\nan individual who is an immediate family member of the President, an individual holding a position described in subparagraph (A) or (B) or paragraph (1), or a special Government employee\u2014\n**(A)**\nis a officer, director, or partner of such entity; or\n**(B)**\nholds a significant ownership interest in such entity or would derive a substantial financial benefit from the Secretary entering into, renewing, or extending such contract or other agreement, as determined by the Secretary.\n##### (b) Regulations\nNot later than 30 days after the date of the enactment of this Act, the Secretary of Defense shall issue regulations to implement this section, including definitions, thresholds, and procedures for identifying individuals and entities with respect to which the prohibition under subsection (a) applies.\n##### (c) Definitions\nIn this section:\n**(1) Immediate family member**\nThe term immediate family member means a parent, child, sibling, spouse, or domestic partner.\n**(2) Special Government employee**\nThe term special Government employee has the meaning given such term in section 202 of title 18, United States Code.",
      "versionDate": "2025-12-12",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-07T23:12:24Z"
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
      "date": "2025-12-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6689ih.xml"
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
      "title": "ETHICAL Procurement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:24:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ETHICAL Procurement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring Transparency, Honesty, and Integrity for Contracting, Acquisition, and Lifecycle Procurement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Secretary of Defense from awarding contracts to entities of which certain current Government employees are officers or owners, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:21Z"
    }
  ]
}
```
