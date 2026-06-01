# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5988?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5988
- Title: CORRUPT Act
- Congress: 119
- Bill type: HR
- Bill number: 5988
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2025-12-03T09:06:19Z
- Update date including text: 2025-12-03T09:06:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5988",
    "number": "5988",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "CORRUPT Act",
    "type": "HR",
    "updateDate": "2025-12-03T09:06:19Z",
    "updateDateIncludingText": "2025-12-03T09:06:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-07",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:06:20Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "DC"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "LA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "IL"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MN"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "NJ"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "IN"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MI"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "NY"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "TX"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "PA"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5988ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5988\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Mrs. Watson Coleman (for herself, Ms. Norton , Mr. Fields , Mr. Moulton , Mr. Jackson of Illinois , Ms. Craig , Mrs. McIver , Mr. Carson , Ms. Tlaib , Ms. Clarke of New York , Mr. Green of Texas , and Ms. Lee of Pennsylvania ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend section 2680 of title 18, United States Code, to provide for an exception to the Federal Tort Claims Act.\n#### 1. Short title\nThis Act may be cited as the Ceasing Outrageous Restitution and Reimbursement Under President Trump Act or the CORRUPT Act .\n#### 2. Exception to Federal tort claims act\nSection 2680 of title 18, United States Code, is amended by adding at the end the following:\n(o) Any claim brought by the President of the United States or a covered relative of such President during the term for which such President shall have been elected. For the purposes of this subsection, a covered relative means a spouse, child, sibling, or in-law of the President. .",
      "versionDate": "2025-11-07",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-11-19T12:52:30Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5988ih.xml"
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
      "title": "CORRUPT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CORRUPT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ceasing Outrageous Restitution and Reimbursement Under President Trump Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 2680 of title 18, United States Code, to provide for an exception to the Federal Tort Claims Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:03:28Z"
    }
  ]
}
```
