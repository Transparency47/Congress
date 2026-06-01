# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8572?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8572
- Title: Gas Prices Relief Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8572
- Origin chamber: House
- Introduced date: 2026-04-29
- Update date: 2026-05-20T19:51:09Z
- Update date including text: 2026-05-20T19:51:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-29: Introduced in House

## Actions

- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8572",
    "number": "8572",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Gas Prices Relief Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-20T19:51:09Z",
    "updateDateIncludingText": "2026-05-20T19:51:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-29",
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
          "date": "2026-04-29T13:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "WA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8572ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8572\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2026 Mr. Harder of California (for himself and Ms. Schrier ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide a gasoline tax holiday.\n#### 1. Short title\nThis Act may be cited as the Gas Prices Relief Act of 2026 .\n#### 2. 2026 gasoline tax holiday\n##### (a) In general\nIn the case of gasoline removed, entered, or sold on or after the date of the enactment of this Act and before January 1, 2027\u2014\n**(1)**\nthe rate of tax under section 4081(a)(2)(A)(i) of the Internal Revenue Code of 1986 shall be zero, and\n**(2)**\nthe Leaking Underground Storage Tank Trust Fund financing rate under section 4081(a)(2) of such Code shall not apply to gasoline to which the rate under paragraph (1) applies.\n##### (b) Transfers to Trust Fund\n**(1) In general**\nThe Secretary of the Treasury (or the Secretary\u2019s delegate) shall transfer from the general fund to the Highway Trust Fund established under section 9503(a) of the Internal Revenue Code of 1986 and the Leaking Underground Storage Tank Trust Fund established under section 9508(a) of such Code amounts equal to the reduction in amounts credited (but for this subsection) to each such Trust Fund by reason of subsection (a).\n**(2) Coordination rules**\n**(A) Leaking Underground Storage Tank Trust Fund**\nAmounts transferred to the Leaking Underground Storage Tank Trust Fund under paragraph (1) shall be treated for purposes of sections 9503(b)(1) and 9508(b)(2) of such Code as taxes received in the Treasury under section 4081 of such Code attributable to the Leaking Underground Storage Tank Trust Fund financing rate.\n**(B) Highway Trust Fund**\nAmounts transferred to the Highway Trust Fund under paragraph (1) shall be treated for purposes of section 9503(b)(1) of such Code as taxes received in the Treasury under section 4081 of such Code which are not attributable to the Leaking Underground Storage Tank Trust Fund financing rate.\n##### (c) Benefits of tax reduction should be passed on to consumers\n**(1)**\nIt is the policy of Congress that\u2014\n**(A)**\nconsumers immediately receive the benefit of the reduction in taxes resulting from the application of subsection (a), and\n**(B)**\ntransportation motor fuels producers and other dealers take such actions as necessary to reduce transportation motor fuels prices to reflect such reduction.\n**(2) Enforcement**\nThe Secretary of the Treasury (or the Secretary\u2019s delegate) may use all applicable authorities to ensure that the benefit of the reduction in taxes resulting from the application of subsection (a) is received by consumers.",
      "versionDate": "2026-04-29",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-06-05",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "3768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Gas Prices Relief Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-09",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4032",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Gas Prices Relief Act of 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-12",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "7919",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Gas Prices Relief Act of 2026",
      "type": "HR"
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
        "name": "Taxation",
        "updateDate": "2026-05-20T19:51:09Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8572ih.xml"
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
      "title": "Gas Prices Relief Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gas Prices Relief Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide a gasoline tax holiday.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:37Z"
    }
  ]
}
```
