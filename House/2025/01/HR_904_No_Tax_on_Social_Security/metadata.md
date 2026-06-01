# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/904?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/904
- Title: No Tax on Social Security
- Congress: 119
- Bill type: HR
- Bill number: 904
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-09-12T20:37:00Z
- Update date including text: 2025-09-12T20:37:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/904",
    "number": "904",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "No Tax on Social Security",
    "type": "HR",
    "updateDate": "2025-09-12T20:37:00Z",
    "updateDateIncludingText": "2025-09-12T20:37:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:04:05Z",
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
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "KY"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr904ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 904\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Van Drew introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to repeal the inclusion in gross income of Social Security benefits.\n#### 1. Short title\nThis Act may be cited as the No Tax on Social Security .\n#### 2. Repeal of inclusion of social security benefits in adjusted gross income\n##### (a) In general\nSection 86 of the Internal Revenue Code of 1986 (relating to social security benefits) is amended by adding at the end the following new subsection:\n(g) Termination This section shall not apply to any taxable year beginning after the date of the enactment of this subsection. .\n##### (b) Social security trust funds held harmless\nThere are hereby appropriated (out of any money in the Treasury not otherwise appropriated) for each fiscal year to each fund under the Social Security Act (including the Federal Hospital Insurance Trust Fund) or the Railroad Retirement Act of 1974 an amount equal to the reduction in the transfers to such fund for such fiscal year by reason of section 86(g) of the Internal Revenue Code of 1986.",
      "versionDate": "2025-01-31",
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
        "actionDate": "2025-09-04",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2716",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "You Earned It, You Keep It Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Disability assistance",
            "updateDate": "2025-04-07T15:23:15Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-04-07T15:23:02Z"
          },
          {
            "name": "Income tax exclusion",
            "updateDate": "2025-04-07T15:22:56Z"
          },
          {
            "name": "Social security and elderly assistance",
            "updateDate": "2025-04-07T15:23:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-03-06T13:07:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr904",
          "measure-number": "904",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr904v00",
            "update-date": "2025-03-21"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Tax on Social Security </strong></p><p>This bill excludes Social Security and Tier I railroad retirement benefits from gross income for purposes of federal income taxes. The bill also provides funds to cover reductions in transfers to the Social Security, Medicare, and Railroad Retirement trust funds resulting from the enactment of this bill.</p>"
        },
        "title": "No Tax on Social Security"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr904.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Tax on Social Security </strong></p><p>This bill excludes Social Security and Tier I railroad retirement benefits from gross income for purposes of federal income taxes. The bill also provides funds to cover reductions in transfers to the Social Security, Medicare, and Railroad Retirement trust funds resulting from the enactment of this bill.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119hr904"
    },
    "title": "No Tax on Social Security"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Tax on Social Security </strong></p><p>This bill excludes Social Security and Tier I railroad retirement benefits from gross income for purposes of federal income taxes. The bill also provides funds to cover reductions in transfers to the Social Security, Medicare, and Railroad Retirement trust funds resulting from the enactment of this bill.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119hr904"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr904ih.xml"
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
      "title": "No Tax on Social Security",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T12:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Tax on Social Security",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to repeal the inclusion in gross income of Social Security benefits.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:18Z"
    }
  ]
}
```
