# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/8?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sjres/8
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Homeland Security relating to "Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants".
- Congress: 119
- Bill type: SJRES
- Bill number: 8
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-30",
    "latestAction": {
      "actionDate": "2025-01-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sjres/8",
    "number": "8",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Homeland Security relating to \"Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants\".",
    "type": "SJRES",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-30",
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
        "item": {
          "date": "2025-01-30T20:15:26Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "FL"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres8is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 8\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Mr. Kennedy (for himself and Mr. Scott of Florida ) introduced the following joint resolution; which was read twice and referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Homeland Security relating to Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants .\nThat Congress disapproves the rule submitted by the Department of Homeland Security relating to Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants (89 Fed. Reg. 101208 (December 13, 2024)), and such rule shall have no force or effect.",
      "versionDate": "2025-01-30",
      "versionType": "IS"
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
        "actionDate": "2025-01-16",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "23",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants\".",
      "type": "HJRES"
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
        "name": "Immigration",
        "updateDate": "2025-02-21T13:05:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-30",
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
          "measure-id": "id119sjres8",
          "measure-number": "8",
          "measure-type": "sjres",
          "orig-publish-date": "2025-01-30",
          "originChamber": "SENATE",
          "update-date": "2025-05-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres8v00",
            "update-date": "2025-05-28"
          },
          "action-date": "2025-01-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution nullifies the final rule issued by the Department of Homeland Security titled <em>Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants</em> and published on December 13, 2024. This rule makes permanent the increase\u00a0of the automatic extension period from 180 days to 540 days for expiring employment authorization documents. The extension applies to eligible noncitizens who renew these authorizations on time.</p>"
        },
        "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Homeland Security relating to \"Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres8.xml",
    "summary": {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution nullifies the final rule issued by the Department of Homeland Security titled <em>Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants</em> and published on December 13, 2024. This rule makes permanent the increase\u00a0of the automatic extension period from 180 days to 540 days for expiring employment authorization documents. The extension applies to eligible noncitizens who renew these authorizations on time.</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119sjres8"
    },
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Homeland Security relating to \"Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants\"."
  },
  "summaries": [
    {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution nullifies the final rule issued by the Department of Homeland Security titled <em>Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants</em> and published on December 13, 2024. This rule makes permanent the increase\u00a0of the automatic extension period from 180 days to 540 days for expiring employment authorization documents. The extension applies to eligible noncitizens who renew these authorizations on time.</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119sjres8"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres8is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Homeland Security relating to \"Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T04:48:26Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Homeland Security relating to \"Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T11:56:26Z"
    }
  ]
}
```
