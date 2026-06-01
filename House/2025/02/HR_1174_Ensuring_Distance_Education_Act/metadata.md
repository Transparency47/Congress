# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1174?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1174
- Title: Ensuring Distance Education Act
- Congress: 119
- Bill type: HR
- Bill number: 1174
- Origin chamber: House
- Introduced date: 2025-02-10
- Update date: 2026-01-23T18:38:18Z
- Update date including text: 2026-01-23T18:38:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-02-10: Introduced in House

## Actions

- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1174",
    "number": "1174",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "O000086",
        "district": "4",
        "firstName": "Burgess",
        "fullName": "Rep. Owens, Burgess [R-UT-4]",
        "lastName": "Owens",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Ensuring Distance Education Act",
    "type": "HR",
    "updateDate": "2026-01-23T18:38:18Z",
    "updateDateIncludingText": "2026-01-23T18:38:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-10",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-10",
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
          "date": "2025-02-10T17:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1174ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1174\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2025 Mr. Owens introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to provide that non-Federal revenue generated through certain distance education programs may be counted for purposes of the non-Federal revenue requirements applicable to proprietary institutions of higher education (commonly known as the 90/10 rule ).\n#### 1. Short title\nThis Act may be cited as the Ensuring Distance Education Act .\n#### 2. Treatment of revenue from certain distance education programs for purposes of the 90/10 rule\nSection 487(d)(1)(B)(iii) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(d)(1)(B)(iii) ) is amended by inserting (which may include funds paid for a program offered in whole or in part through distance education regardless of the location from which such program is carried out) after under this title .",
      "versionDate": "2025-02-10",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Educational technology and distance education",
            "updateDate": "2026-01-23T18:38:18Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2026-01-23T18:38:01Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-01-23T18:37:45Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2026-01-23T18:37:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-17T15:14:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
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
          "measure-id": "id119hr1174",
          "measure-number": "1174",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-10",
          "originChamber": "HOUSE",
          "update-date": "2025-06-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1174v00",
            "update-date": "2025-06-16"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Ensuring Distance Education Act</strong></p><p>This bill treats revenue from distance education programs as nonfederal revenue for purposes of the 90/10 rule.</p><p>Generally, the 90/10 rule requires a for-profit institution of higher education (IHE) to derive at least 10% of its revenue from sources other than federal financial aid. Under current Department of Education regulations, for-profit IHEs are prohibited from including revenue from distance education programs (including hybrid distance education programs) as nonfederal revenue that meets this 10% requirement. The bill removes the prohibition and allows for distance education programs to be counted as nonfederal revenue for purposes of the rule.</p>"
        },
        "title": "Ensuring Distance Education Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1174.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ensuring Distance Education Act</strong></p><p>This bill treats revenue from distance education programs as nonfederal revenue for purposes of the 90/10 rule.</p><p>Generally, the 90/10 rule requires a for-profit institution of higher education (IHE) to derive at least 10% of its revenue from sources other than federal financial aid. Under current Department of Education regulations, for-profit IHEs are prohibited from including revenue from distance education programs (including hybrid distance education programs) as nonfederal revenue that meets this 10% requirement. The bill removes the prohibition and allows for distance education programs to be counted as nonfederal revenue for purposes of the rule.</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr1174"
    },
    "title": "Ensuring Distance Education Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ensuring Distance Education Act</strong></p><p>This bill treats revenue from distance education programs as nonfederal revenue for purposes of the 90/10 rule.</p><p>Generally, the 90/10 rule requires a for-profit institution of higher education (IHE) to derive at least 10% of its revenue from sources other than federal financial aid. Under current Department of Education regulations, for-profit IHEs are prohibited from including revenue from distance education programs (including hybrid distance education programs) as nonfederal revenue that meets this 10% requirement. The bill removes the prohibition and allows for distance education programs to be counted as nonfederal revenue for purposes of the rule.</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr1174"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1174ih.xml"
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
      "title": "To amend the Higher Education Act of 1965 to provide that non-Federal revenue generated through certain distance education programs may be counted for purposes of the non-Federal revenue requirements applicable to proprietary institutions of higher education (commonly known as the \"90/10 rule\").",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T08:05:17Z"
    },
    {
      "title": "Ensuring Distance Education Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring Distance Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:38:16Z"
    }
  ]
}
```
