# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3173?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3173
- Title: Stop 8(a) Contracting Fraud Act
- Congress: 119
- Bill type: S
- Bill number: 3173
- Origin chamber: Senate
- Introduced date: 2025-11-10
- Update date: 2025-12-11T18:26:41Z
- Update date including text: 2025-12-11T18:26:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-10: Introduced in Senate
- 2025-11-10 - IntroReferral: Introduced in Senate
- 2025-11-10 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-12-10 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- Latest action: 2025-11-10: Introduced in Senate

## Actions

- 2025-11-10 - IntroReferral: Introduced in Senate
- 2025-11-10 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-12-10 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3173",
    "number": "3173",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Stop 8(a) Contracting Fraud Act",
    "type": "S",
    "updateDate": "2025-12-11T18:26:41Z",
    "updateDateIncludingText": "2025-12-11T18:26:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-10",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-10",
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
            "date": "2025-12-10T19:30:04Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-11-10T23:16:46Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3173is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3173\nIN THE SENATE OF THE UNITED STATES\nNovember 10, 2025 Ms. Ernst introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo prohibit the Small Business Administration from awarding sole source contracts until the Administration conducts a full audit of and submits to Congress a report on the business development program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop 8(a) Contracting Fraud Act .\n#### 2. Moratorium on sole source contracts\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe terms Administration and Administrator mean the Small Business Administration and the Administrator thereof, respectively; and\n**(2)**\nthe term Deputy Administrator means the Deputy Administrator of the Administration.\n##### (b) Moratorium\nThe Administration may not award sole source contracts under section 8(a)(16) of the Small Business Act ( 15 U.S.C. 637(a)(16) ) during the period beginning on the date of enactment of this Act and ending on the date on which the Administration\u2014\n**(1)**\ncompletes the audit of the business development program under such section 8(a) ordered to be conducted by the Administrator on June 27, 2025; and\n**(2)**\nsubmits to the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Small Business of the House of Representatives a report that includes the findings of the audit described in paragraph (1).\n##### (c) Waiver\n**(1) In general**\nIf a contracting officer determines that it is in the interest of national security to conduct a sole source contract under section 8(a) of the Small Business Act ( 15 U.S.C. 637(a) ), the contracting officer may seek a waiver of the moratorium under subparagraph (b).\n**(2) Submission of request**\n**(A) In general**\n**(i) Submission to head acquisition officer**\nThe contracting officer may submit a request for a waiver to the head acquisition officer (or equivalent) for the agency of the contracting officer.\n**(ii) Submission to Administrator**\nFollowing approval of a submission under clause (i), the head acquisition officer (or equivalent) shall submit the request for a waiver to the Administrator or Deputy Administrator.\n**(B) Contents of request**\nA request for a waiver submitted under subparagraph (A) shall include a justification explaining\u2014\n**(i)**\nthe reason the use of the waiver authority is imperative for national security purposes; and\n**(ii)**\nthe reason the work cannot be performed by any other small business concern.\n**(C) Form of request and approval**\n**(i) Request**\nThe justification required under subparagraph (B) shall be submitted in writing.\n**(ii) Approval**\nThe Administrator or Deputy Administrator may approve a request for a waiver.\n**(3) Nondelegation**\nThe waiver authority established under paragraph (1) may not be delegated.",
      "versionDate": "2025-11-10",
      "versionType": "Introduced in Senate"
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
            "name": "Accounting and auditing",
            "updateDate": "2025-12-11T18:26:34Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-11T18:26:41Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-12-11T18:12:22Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-12-11T18:12:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-11-19T14:57:45Z"
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
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3173is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Stop 8(a) Contracting Fraud Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop 8(a) Contracting Fraud Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T06:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the Small Business Administration from awarding sole source contracts until the Administration conducts a full audit of and submits to Congress a report on the business development program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T06:33:14Z"
    }
  ]
}
```
