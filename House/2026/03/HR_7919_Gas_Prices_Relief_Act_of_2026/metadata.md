# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7919?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7919
- Title: Gas Prices Relief Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7919
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-05-20T19:51:02Z
- Update date including text: 2026-05-20T19:51:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-12: Introduced in House

## Actions

- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7919",
    "number": "7919",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Gas Prices Relief Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-20T19:51:02Z",
    "updateDateIncludingText": "2026-05-20T19:51:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
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
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T13:34:50Z",
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
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "OH"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7919ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7919\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Mr. Pappas introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a gasoline tax holiday.\n#### 1. Short title\nThis Act may be cited as the Gas Prices Relief Act of 2026 .\n#### 2. 2026 gasoline tax holiday\n##### (a) In general\nIn the case of gasoline removed, entered, or sold on or after the date of the enactment of this Act and before October 1, 2026\u2014\n**(1)**\nthe rate of tax under section 4081(a)(2)(A)(i) of the Internal Revenue Code of 1986 shall be zero, and\n**(2)**\nthe Leaking Underground Storage Tank Trust Fund financing rate under section 4081(a)(2)(B) of such Code shall not apply to gasoline to which the rate under paragraph (1) applies.\n##### (b) Transfers to Trust Fund\n**(1) In general**\nThe Secretary of the Treasury shall transfer from the general fund to the Highway Trust Fund established under section 9503(a) of the Internal Revenue Code of 1986 and the Leaking Underground Storage Tank Trust Fund established under section 9508(a) of such Code amounts equal to the reduction in amounts credited (but for this subsection) to each such Trust Fund by reason of subsection (a).\n**(2) Coordination rules**\n**(A) Leaking Underground Storage Tank Trust Fund**\nAmounts transferred to the Leaking Underground Storage Tank Trust Fund under paragraph (1) shall be treated for purposes of sections 9503(b)(1) and 9508(b)(2) of such Code as taxes received in the Treasury under section 4081 of such Code attributable to the Leaking Underground Storage Tank Trust Fund financing rate.\n**(B) Highway Trust Fund**\nAmounts transferred to the Highway Trust Fund under paragraph (1) shall be treated for purposes of section 9503(b)(1) of such Code as taxes received in the Treasury under section 4081 of such Code which are not attributable to the Leaking Underground Storage Tank Trust Fund financing rate.\n##### (c) Benefits of tax reduction should be passed on to consumers\n**(1)**\nIt is the policy of Congress that\u2014\n**(A)**\nconsumers immediately receive the benefit of the reduction in taxes resulting from the application of subsection (a),\n**(B)**\ntransportation motor fuels producers and other dealers take such actions as necessary to reduce transportation motor fuels prices to reflect such reduction, and\n**(C)**\ntransportation motor fuels producers and other dealers that fail to reduce transportation motor fuels prices to reflect such reduction shall be subject to monetary penalties which are not less than the amount of the reduction in taxes which should have been passed on to consumers.\n**(2) Enforcement**\nThe Secretary of the Treasury shall use all applicable authorities to ensure that the benefit of the reduction in taxes resulting from the application of subsection (a) is received by consumers.",
      "versionDate": "2026-03-12",
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
        "actionDate": "2026-03-09",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4032",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Gas Prices Relief Act of 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-29",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "8572",
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
        "updateDate": "2026-04-27T22:24:17Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7919ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gas Prices Relief Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-22T06:53:35Z"
    },
    {
      "title": "Gas Prices Relief Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T06:53:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a gasoline tax holiday.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-22T06:47:23Z"
    }
  ]
}
```
