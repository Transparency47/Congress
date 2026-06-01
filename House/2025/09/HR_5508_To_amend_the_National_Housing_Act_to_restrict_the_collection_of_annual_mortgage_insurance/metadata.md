# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5508?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5508
- Title: Mortgage Insurance Freedom Act
- Congress: 119
- Bill type: HR
- Bill number: 5508
- Origin chamber: House
- Introduced date: 2025-09-19
- Update date: 2025-12-04T09:07:17Z
- Update date including text: 2025-12-04T09:07:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-09-19: Introduced in House

## Actions

- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5508",
    "number": "5508",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001137",
        "district": "5",
        "firstName": "Gregory",
        "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
        "lastName": "Meeks",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Mortgage Insurance Freedom Act",
    "type": "HR",
    "updateDate": "2025-12-04T09:07:17Z",
    "updateDateIncludingText": "2025-12-04T09:07:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-19",
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
      "actionDate": "2025-09-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T13:02:35Z",
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
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "TX"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "LA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5508ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5508\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 19, 2025 Mr. Meeks (for himself and Mr. Sessions ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the National Housing Act to restrict the collection of annual mortgage insurance premiums when a 78 percent loan-to value ratio is reached, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mortgage Insurance Freedom Act .\n#### 2. Restriction of collection of annual mortgage insurance premiums\n##### (a) In general\nSection 203(c)(2) of the National Housing Act ( 12 U.S.C. 1709(c)(2) ) is amended\u2014\n**(1)**\nin subparagraph (B)\u2014\n**(A)**\nin clause (i), by striking For any and inserting Subject to subparagraph (D), for any ; and\n**(B)**\nin clause (ii), by striking For any and inserting Subject to subparagraph (D), for any ;\n**(2)**\nin subparagraph (C)(i), by striking In addition and inserting Subject to subparagraph (D), in addition ; and\n**(3)**\nby adding at the end the following:\n(D) Restriction on annual premium collection (i) In general The Secretary may not collect any annual premiums under this paragraph with respect to a mortgage at any time that the remaining insured principal balance (excluding the portion of the remaining balance attributable to the premium collected under subparagraph (A)) is 78 percent or less than the lower of\u2014 (I) the sales price of the dwelling at the sale in connection with which the mortgage was made; or (II) the appraised value of the dwelling at the time of the origination of the mortgage. (ii) Exception If the capital ratio of the Mutual Mortgage Insurance Fund falls below 2 percent\u2014 (I) clause (i) shall not apply with respect to any mortgage with respect the Secretary was collecting premiums on the date on which the capital ratio of the Mutual Mortgage Insurance Fund fell below 2 percent; and (II) clause (i) shall continue to apply to any mortgage with respect to which the Secretary had stopped collecting premiums under this paragraph before the date on which the capital ratio of the Mutual Mortgage Insurance Fund fell below 2 percent because the remaining insured principal balance met the requirements described in clause (i). (iii) Rulemaking The Secretary shall, not later than 180 days after the enactment of this subparagraph, issue such rules to carry out this subparagraph and such rules shall include a process for mortgagors of mortgages insured under this title to use to demonstrate to the Secretary that the insured principal balance of the mortgage of such mortgagor is 78 percent or less than the lower of\u2014 (I) the sales price of the dwelling at the sale in connection with which the mortgage was made; or (II) the appraised value of the dwelling at the time of the origination of the mortgage. (iv) Outreach and education The Secretary shall conduct outreach and educational activities to inform mortgagors of mortgages insured under this title about\u2014 (I) the restriction on premium collection imposed by clause (i); and (II) and the processes the mortgagor may use to demonstrate to the Secretary that the insured principal balance of the mortgage of such mortgagor is 78 percent or less than the lower of\u2014 (bb) the sales price of the dwelling at the sale in connection with which the mortgage was made; or (cc) the appraised value of the dwelling at the time of the origination of the mortgage. .\n##### (b) Applicability\nThe amendments made by subsection (a) shall apply with respect only to mortgages endorsed for insurance by the Secretary of Housing and Urban Development after the date of the enactment of this Act.",
      "versionDate": "2025-09-19",
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
        "updateDate": "2025-11-18T18:25:25Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5508ih.xml"
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
      "title": "Mortgage Insurance Freedom Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mortgage Insurance Freedom Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Housing Act to restrict the collection of annual mortgage insurance premiums when a 78 percent loan-to value ratio is reached, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T04:48:14Z"
    }
  ]
}
```
