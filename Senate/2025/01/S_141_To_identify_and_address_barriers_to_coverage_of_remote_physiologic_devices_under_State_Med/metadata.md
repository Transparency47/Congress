# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/141?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/141
- Title: Connected MOM Act
- Congress: 119
- Bill type: S
- Bill number: 141
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2025-12-05T21:45:06Z
- Update date including text: 2025-12-05T21:45:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Finance.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/141",
    "number": "141",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Connected MOM Act",
    "type": "S",
    "updateDate": "2025-12-05T21:45:06Z",
    "updateDateIncludingText": "2025-12-05T21:45:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T22:20:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NH"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "GA"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IN"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s141is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 141\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Cassidy (for himself, Ms. Hassan , Mr. Warnock , and Mr. Young ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo identify and address barriers to coverage of remote physiologic devices under State Medicaid programs to improve maternal and child health outcomes for pregnant and postpartum women.\n#### 1. Short title\nThis Act may be cited as the Connected Maternal Online Monitoring Act or the Connected MOM Act .\n#### 2. Coverage of remote physiologic monitoring devices and impact on maternal and child health outcomes under Medicaid\n##### (a) Report to Congress\nNot later than 18 months after the date of enactment of this Act, the Secretary of Health and Human Services shall submit to Congress a report containing information on authorities and State practices for covering remote physiological monitoring devices, including limitations and barriers to such coverage and the impact on maternal health outcomes, and to the extent appropriate, recommendations on how to address such limitations or barriers related to coverage of remote physiologic devices under State Medicaid programs, including, but not limited to, pulse oximeters, blood pressure cuffs, scales, and blood glucose monitors, with the goal of improving maternal and child health outcomes for pregnant and postpartum women enrolled in State Medicaid programs.\n##### (b) State resources\nNot later than 6 months after the submission of the report required by subsection (a), the Secretary shall update resources for State Medicaid programs, such as State Medicaid telehealth toolkits, to be consistent with the recommendations provided in such report.",
      "versionDate": "2025-01-16",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-08-15",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "4977",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Connected MOM Act",
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
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-13T15:58:37Z"
          },
          {
            "name": "Appropriations",
            "updateDate": "2025-03-13T15:58:37Z"
          },
          {
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-03-13T15:58:37Z"
          },
          {
            "name": "Emergency medical services and trauma care",
            "updateDate": "2025-03-13T15:58:37Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-03-13T15:58:37Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-13T15:58:37Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-03-13T15:58:37Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-03-13T15:58:37Z"
          },
          {
            "name": "Infectious and parasitic diseases",
            "updateDate": "2025-03-13T15:58:37Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-03-13T15:58:37Z"
          },
          {
            "name": "Public transit",
            "updateDate": "2025-03-13T15:58:37Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2025-03-13T15:58:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-01T14:55:29Z"
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
          "measure-id": "id119s141",
          "measure-number": "141",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s141v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Connected Maternal Online Monitoring Act or the Connected MOM Act</b></p> <p>This bill requires the Centers for Medicare & Medicaid Services to report, and provide resources for states, on coverage of remote physiologic devices and related services (e.g., blood glucose monitors) under Medicaid, so as to improve maternal and child health outcomes for pregnant and postpartum women.</p>"
        },
        "title": "Connected MOM Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s141.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Connected Maternal Online Monitoring Act or the Connected MOM Act</b></p> <p>This bill requires the Centers for Medicare & Medicaid Services to report, and provide resources for states, on coverage of remote physiologic devices and related services (e.g., blood glucose monitors) under Medicaid, so as to improve maternal and child health outcomes for pregnant and postpartum women.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119s141"
    },
    "title": "Connected MOM Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Connected Maternal Online Monitoring Act or the Connected MOM Act</b></p> <p>This bill requires the Centers for Medicare & Medicaid Services to report, and provide resources for states, on coverage of remote physiologic devices and related services (e.g., blood glucose monitors) under Medicaid, so as to improve maternal and child health outcomes for pregnant and postpartum women.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119s141"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s141is.xml"
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
      "title": "Connected MOM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Connected MOM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-27T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Connected Maternal Online Monitoring Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-27T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to identify and address barriers to coverage of remote physiologic devices under State Medicaid programs to improve maternal and child health outcomes for pregnant and postpartum women.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-27T03:18:22Z"
    }
  ]
}
```
