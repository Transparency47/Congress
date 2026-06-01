# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5728?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5728
- Title: Rural Homeownership Continuity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5728
- Origin chamber: House
- Introduced date: 2025-10-10
- Update date: 2025-12-09T19:36:49Z
- Update date including text: 2025-12-09T19:36:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-10: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-10-10: Introduced in House

## Actions

- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-10",
    "latestAction": {
      "actionDate": "2025-10-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5728",
    "number": "5728",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
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
    "title": "Rural Homeownership Continuity Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-09T19:36:49Z",
    "updateDateIncludingText": "2025-12-09T19:36:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-10",
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
          "date": "2025-10-10T16:32:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "NE"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "CA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "VT"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "OR"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CO"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "OH"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5728ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5728\nIN THE HOUSE OF REPRESENTATIVES\nOctober 10, 2025 Mr. Costa (for himself, Mr. Bacon , Mr. LaMalfa , Ms. Balint , Mr. Sherman , Ms. Salinas , Ms. Pettersen , Mrs. Beatty , and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Housing Act of 1949 to permit the assumption of loans under the Doug Bereuter Section 502 Single Family Housing Loan Guarantee Program.\n#### 1. Short title\nThis Act may be cited as the Rural Homeownership Continuity Act of 2025 .\n#### 2. Assumption of loans under the Doug Bereuter Section 502 Single Family Housing Loan Guarantee Program\n##### (a) In general\nSection 502(h)(10) of the Housing Act of 1949 ( 42 U.S.C. 1472(h)(10) ) is amended to read as follows:\n(10) Assumption (A) In general The Secretary may provide for the assumption of a current guaranteed loan made under this subsection by any individual qualified to receive a guaranteed loan under this subsection upon the transfer to that individual of the property for which the guaranteed loan was made. (B) Release from liability If a borrower of a guaranteed loan under this subsection transfers the property for which the guaranteed loan was made to an individual who assumes the guaranteed loan under subparagraph (A), the transferor, and any co-borrower or guarantor of the transferor, shall be relieved of liability with respect to the guaranteed loan. (C) Assumption of obligations, rights, and interests The Secretary shall provide in each assumption under subparagraph (A) for the assumption of the obligations, rights, and interests under the terms of the guaranteed loan or such other terms as the Secretary determines appropriate. .\n##### (b) Applicability\nThe amendment made by subsection (a) shall apply with respect to loans guaranteed under section 502 of the Housing Act of 1949 ( 42 U.S.C. 1472 ) on or after the date of enactment of this Act.\n##### (c) Rulemaking\nThe Secretary of Agriculture may issue a rule to allow servicers of loans guaranteed under section 502 of the Housing Act of 1949 ( 42 U.S.C. 1472 ) to charge fees to borrowers for transaction costs associated with the loan.",
      "versionDate": "2025-10-10",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-09T19:36:49Z"
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
      "date": "2025-10-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5728ih.xml"
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
      "title": "Rural Homeownership Continuity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Homeownership Continuity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Housing Act of 1949 to permit the assumption of loans under the Doug Bereuter Section 502 Single Family Housing Loan Guarantee Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:18:27Z"
    }
  ]
}
```
