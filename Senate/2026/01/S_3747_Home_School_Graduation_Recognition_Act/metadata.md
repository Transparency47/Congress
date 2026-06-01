# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3747?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3747
- Title: Home School Graduation Recognition Act
- Congress: 119
- Bill type: S
- Bill number: 3747
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-04-21T11:03:28Z
- Update date including text: 2026-04-21T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-02-26 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported without amendment favorably.
- 2026-03-11 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy without amendment. Without written report.
- 2026-03-11 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy without amendment. Without written report.
- 2026-03-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 354.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-02-26 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported without amendment favorably.
- 2026-03-11 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy without amendment. Without written report.
- 2026-03-11 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy without amendment. Without written report.
- 2026-03-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 354.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3747",
    "number": "3747",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Home School Graduation Recognition Act",
    "type": "S",
    "updateDate": "2026-04-21T11:03:28Z",
    "updateDateIncludingText": "2026-04-21T11:03:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 354.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-03-11",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-03-11",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-26",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2026-03-11T20:19:01Z",
            "name": "Reported By"
          },
          {
            "date": "2026-02-26T15:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-29T23:03:14Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "IN"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "WY"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "NC"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "UT"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3747is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3747\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mrs. Moody (for herself and Mr. Banks ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Higher Education Act of 1965 to recognize students who have completed secondary school education in a home school setting as high school graduates, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Home School Graduation Recognition Act .\n#### 2. Recognizing Home School Graduates\nSection 484(d) of the Higher Education Act of 1965 ( 20 U.S.C. 1091(d) ) is amended\u2014\n**(1)**\nin the heading of such subsection, by striking Who Are Not High School Graduates and inserting From Non-Traditional Settings ; and\n**(2)**\nby adding at the end the following:\n(3) High school graduate For purposes of this title, a student who has completed a secondary school education in a home school setting that is treated as a home school or private school under State law shall be considered a high school graduate. .",
      "versionDate": "2026-01-29",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3747rs.xml",
      "text": "II\nCalendar No. 354\n119th CONGRESS\n2d Session\nS. 3747\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mrs. Moody (for herself, Mr. Banks , Ms. Lummis , Mr. Budd , and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nMarch 11, 2026 Reported by Mr. Cassidy , without amendment\nA BILL\nTo amend the Higher Education Act of 1965 to recognize students who have completed secondary school education in a home school setting as high school graduates, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Home School Graduation Recognition Act .\n#### 2. Recognizing Home School Graduates\nSection 484(d) of the Higher Education Act of 1965 ( 20 U.S.C. 1091(d) ) is amended\u2014\n**(1)**\nin the heading of such subsection, by striking Who Are Not High School Graduates and inserting From Non-Traditional Settings ; and\n**(2)**\nby adding at the end the following:\n(3) High school graduate For purposes of this title, a student who has completed a secondary school education in a home school setting that is treated as a home school or private school under State law shall be considered a high school graduate. .",
      "versionDate": "2026-01-29",
      "versionType": "Reported in Senate"
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
        "actionDate": "2026-03-17",
        "text": "Read twice. Placed on Senate Legislative Calendar under General Orders. Calendar No. 358."
      },
      "number": "6392",
      "relationshipDetails": {
        "item": [
          {
            "identifiedBy": "CRS",
            "type": "Related bill"
          },
          {
            "identifiedBy": "House",
            "type": "Related bill"
          }
        ]
      },
      "title": "Home School Graduation Recognition Act",
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
      "legislativeSubjects": {
        "item": {
          "name": "Elementary and secondary education",
          "updateDate": "2026-02-27T19:51:19Z"
        }
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2026-02-25T17:49:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-29",
    "originChamber": "Senate",
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
          "measure-id": "id119s3747",
          "measure-number": "3747",
          "measure-type": "s",
          "orig-publish-date": "2026-01-29",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3747v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2026-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Home School Graduation Recognition Act</strong></p><p>This bill clarifies that students who complete their secondary education in a home school setting recognized under state law are\u00a0high school graduates for purposes of eligibility for federal student aid.</p>"
        },
        "title": "Home School Graduation Recognition Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3747.xml",
    "summary": {
      "actionDate": "2026-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Home School Graduation Recognition Act</strong></p><p>This bill clarifies that students who complete their secondary education in a home school setting recognized under state law are\u00a0high school graduates for purposes of eligibility for federal student aid.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s3747"
    },
    "title": "Home School Graduation Recognition Act"
  },
  "summaries": [
    {
      "actionDate": "2026-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Home School Graduation Recognition Act</strong></p><p>This bill clarifies that students who complete their secondary education in a home school setting recognized under state law are\u00a0high school graduates for purposes of eligibility for federal student aid.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s3747"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3747is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3747rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Home School Graduation Recognition Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T11:03:28Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Home School Graduation Recognition Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-03-13T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Home School Graduation Recognition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Higher Education Act of 1965 to recognize students who have completed secondary school education in a home school setting as high school graduates, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T11:18:24Z"
    }
  ]
}
```
