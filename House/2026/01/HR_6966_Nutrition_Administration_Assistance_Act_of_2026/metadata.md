# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6966?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6966
- Title: Nutrition Administration Assistance Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 6966
- Origin chamber: House
- Introduced date: 2026-01-07
- Update date: 2026-05-22T08:07:17Z
- Update date including text: 2026-05-22T08:07:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2026-01-07: Introduced in House

## Actions

- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-07",
    "latestAction": {
      "actionDate": "2026-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6966",
    "number": "6966",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000273",
        "district": "3",
        "firstName": "Teresa",
        "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
        "lastName": "Leger Fernandez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Nutrition Administration Assistance Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:17Z",
    "updateDateIncludingText": "2026-05-22T08:07:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-07",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-07",
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
          "date": "2026-01-07T15:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-20T14:39:10Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6966ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6966\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2026 Ms. Leger Fernandez (for herself and Ms. Stansbury ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo provide additional funds to States for administration of certain nutrition programs.\n#### 1. Short title\nThis Act may be cited as the Nutrition Administration Assistance Act of 2026 .\n#### 2. Additional funds for administration costs\n##### (a) Commodity supplemental food program\nIn addition to funds otherwise made available to State agencies to pay administration costs incurred by State agencies to carry out section 5 of the Agriculture and Consumer Protection Act of 1973 ( 7 U.S.C. 612c note), 70 percent of the funds appropriated under section 3 shall be provided to States for such administration costs.\n##### (b) Emergency Food Assistance Act of 1983\nIn addition to funds otherwise made available to States to pay administration costs incurred by States to carry out State plans under section 203A of the Emergency Food Assistance Act of 1983 ( 7 U.S.C. 7504 ), 20 percent of the funds appropriated under section 3 shall be provided to States for such administration costs.\n##### (c) Seniors farmers\u2019 market nutrition program\nIn addition to funds otherwise made available to the Secretary of Agriculture for administration costs to carry out section 4402 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 3007 ), 10 percent of the funds appropriated under section 3 shall be provided to States for such administration costs.\n#### 3. Authorization of appropriations\nThere is authorized to be appropriated to carry out this Act $1,000,000 for each of the fiscal years 2026 through 2030.",
      "versionDate": "2026-01-07",
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
        "actionDate": "2026-01-07",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "3594",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Nutrition Administration Assistance Act of 2026",
      "type": "S"
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
        "name": "Agriculture and Food",
        "updateDate": "2026-01-20T15:39:07Z"
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
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6966ih.xml"
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
      "title": "Nutrition Administration Assistance Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-17T06:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Nutrition Administration Assistance Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T06:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide additional funds to States for administration of certain nutrition programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-17T06:18:34Z"
    }
  ]
}
```
