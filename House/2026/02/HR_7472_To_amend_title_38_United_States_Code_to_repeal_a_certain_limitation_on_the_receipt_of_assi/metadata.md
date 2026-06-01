# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7472?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7472
- Title: To amend title 38, United States Code, to repeal a certain limitation on the receipt of assistance under both the Department of Veterans Affairs Veteran Readiness and Employment program and Department of Veterans Affairs educational assistance programs.
- Congress: 119
- Bill type: HR
- Bill number: 7472
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-03-07T09:06:33Z
- Update date including text: 2026-03-07T09:06:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-02 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2026-02-10: Introduced in House

## Actions

- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-02 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7472",
    "number": "7472",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000608",
        "district": "50",
        "firstName": "Scott",
        "fullName": "Rep. Peters, Scott H. [D-CA-50]",
        "lastName": "Peters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To amend title 38, United States Code, to repeal a certain limitation on the receipt of assistance under both the Department of Veterans Affairs Veteran Readiness and Employment program and Department of Veterans Affairs educational assistance programs.",
    "type": "HR",
    "updateDate": "2026-03-07T09:06:33Z",
    "updateDateIncludingText": "2026-03-07T09:06:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-02",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T15:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-02T15:16:54Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7472ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7472\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2026 Mr. Peters (for himself, Mr. Rutherford , and Mr. McGarvey ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to repeal a certain limitation on the receipt of assistance under both the Department of Veterans Affairs Veteran Readiness and Employment program and Department of Veterans Affairs educational assistance programs.\n#### 1. Repeal of certain limitation on receipt of assistance under both Department of Veterans Affairs Veteran Readiness and Employment program and Department of Veterans Affairs educational assistance programs\nSection 3695 of title 38, United States Code, is amended\u2014\n**(1)**\nby striking subsection (b); and\n**(2)**\nby redesignating subsection (c) as subsection (b).",
      "versionDate": "2026-02-10",
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
        "actionDate": "2026-02-10",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "3818",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Ensuring Benefits for Disabled Veterans Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-02-24T18:37:40Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7472ih.xml"
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
      "title": "To amend title 38, United States Code, to repeal a certain limitation on the receipt of assistance under both the Department of Veterans Affairs Veteran Readiness and Employment program and Department of Veterans Affairs educational assistance programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-23T13:18:27Z"
    },
    {
      "title": "To amend title 38, United States Code, to repeal a certain limitation on the receipt of assistance under both the Department of Veterans Affairs Veteran Readiness and Employment program and Department of Veterans Affairs educational assistance programs.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T09:06:24Z"
    }
  ]
}
```
