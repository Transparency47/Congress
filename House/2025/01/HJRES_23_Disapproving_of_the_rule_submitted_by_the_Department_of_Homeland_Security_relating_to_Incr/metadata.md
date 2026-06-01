# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/23?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/23
- Title: Disapproving of the rule submitted by the Department of Homeland Security relating to "Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants".
- Congress: 119
- Bill type: HJRES
- Bill number: 23
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-02-21T13:05:29Z
- Update date including text: 2025-02-21T13:05:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/23",
    "number": "23",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants\".",
    "type": "HJRES",
    "updateDate": "2025-02-21T13:05:29Z",
    "updateDateIncludingText": "2025-02-21T13:05:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:10:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres23ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 23\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Arrington (for himself, Mr. Self , and Mr. Moore of West Virginia ) submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nDisapproving of the rule submitted by the Department of Homeland Security relating to Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants .\nThat Congress disapproves the rule submitted by the Department of Homeland Security relating to Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants (89 Fed. Reg. 101208), and such rule shall have no force or effect.",
      "versionDate": "2025-01-16",
      "versionType": "IH"
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
        "actionDate": "2025-01-30",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "8",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Homeland Security relating to \"Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants\".",
      "type": "SJRES"
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
        "updateDate": "2025-01-21T13:00:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hjres23",
          "measure-number": "23",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-02-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres23v00",
            "update-date": "2025-02-07"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution nullifies the final rule issued by the Department of Homeland Security titled <em>Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants</em> and published on December 13, 2024. This rule makes permanent the increase\u00a0of the automatic extension period from 180 days to 540 days for expiring employment authorization documents. The extension applies to eligible noncitizens who renew these authorizations on time.</p>"
        },
        "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres23.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the final rule issued by the Department of Homeland Security titled <em>Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants</em> and published on December 13, 2024. This rule makes permanent the increase\u00a0of the automatic extension period from 180 days to 540 days for expiring employment authorization documents. The extension applies to eligible noncitizens who renew these authorizations on time.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hjres23"
    },
    "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants\"."
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the final rule issued by the Department of Homeland Security titled <em>Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants</em> and published on December 13, 2024. This rule makes permanent the increase\u00a0of the automatic extension period from 180 days to 540 days for expiring employment authorization documents. The extension applies to eligible noncitizens who renew these authorizations on time.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hjres23"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres23ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-17T09:18:22Z"
    },
    {
      "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Increase of the Automatic Extension Period of Employment Authorization and Documentation for Certain Employment Authorization Document Renewal Applicants\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-17T09:05:26Z"
    }
  ]
}
```
