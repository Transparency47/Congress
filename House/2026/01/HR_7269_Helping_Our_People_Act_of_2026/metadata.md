# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7269?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7269
- Title: Helping Our People Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7269
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-02-23T23:34:31Z
- Update date including text: 2026-02-23T23:34:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2026-01-27: Introduced in House

## Actions

- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7269",
    "number": "7269",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "R000621",
        "district": "6",
        "firstName": "Emily",
        "fullName": "Rep. Randall, Emily [D-WA-6]",
        "lastName": "Randall",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Helping Our People Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-23T23:34:31Z",
    "updateDateIncludingText": "2026-02-23T23:34:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
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
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T17:31:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
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
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7269ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7269\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Ms. Randall (for herself and Ms. Strickland ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Puyallup Tribe of Indians Settlement Act of 1989 to clarify that amounts in the Puyallup Tribe of Indians Settlement Trust Fund may be withdrawn by the Puyallup Tribe of Indians, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helping Our People Act of 2026 or the k\u02b7ax\u02b7ad tii\u026b \u0294iis\u030c\u0259dc\u030c\u0259\u026b Act of 2026 .\n#### 2. Withdrawal of trust fund by Puyallup Tribe of Indians\n##### (a) Permanent trust fund for Tribal members\nSection 6(b) of the Puyallup Tribe of Indians Settlement Act of 1989 ( Public Law 101\u201341 ; 103 Stat. 87) is amended by adding at the end the following:\n(6) Amounts in the trust fund may be withdrawn by the Tribe pursuant to the American Indian Trust Fund Management Reform Act of 1994 ( 25 U.S.C. 4001 et seq. ) under a management plan approved by the Secretary under that Act. .\n##### (b) Savings provision\nThe Puyallup Tribe of Indians Settlement Act of 1989 ( Public Law 101\u201341 ; 103 Stat. 83) is amended by adding at the end the following:\n14. Savings provision Nothing in this Act prevents the United States from engaging with the Tribe, on the same basis as other federally recognized Indian Tribes, under any Federal law enacted after the date of enactment of this Act. .",
      "versionDate": "2026-01-27",
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
        "actionDate": "2026-02-03",
        "text": "Read twice and referred to the Committee on Indian Affairs."
      },
      "number": "3769",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Helping Our People Act of 2026",
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
        "name": "Native Americans",
        "updateDate": "2026-02-11T21:36:33Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7269ih.xml"
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
      "title": "Helping Our People Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "k\u02b7ax\u02b7ad tii\u026b \u0294iis\u030c\u0259dc\u030c\u0259\u026b Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping Our People Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Puyallup Tribe of Indians Settlement Act of 1989 to clarify that amounts in the Puyallup Tribe of Indians Settlement Trust Fund may be withdrawn by the Puyallup Tribe of Indians, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T04:48:20Z"
    }
  ]
}
```
