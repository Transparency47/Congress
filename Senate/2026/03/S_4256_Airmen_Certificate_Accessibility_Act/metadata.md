# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4256?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4256
- Title: Airmen Certificate Accessibility Act
- Congress: 119
- Bill type: S
- Bill number: 4256
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-16T16:55:28Z
- Update date including text: 2026-04-16T16:55:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4256",
    "number": "4256",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Airmen Certificate Accessibility Act",
    "type": "S",
    "updateDate": "2026-04-16T16:55:28Z",
    "updateDateIncludingText": "2026-04-16T16:55:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T20:36:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4256is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4256\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Sheehy (for himself and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 49, United States Code, to establish acceptable formats for presentation of airman certificates to the Federal Aviation Administration.\n#### 1. Short title\nThis Act may be cited as the Airmen Certificate Accessibility Act .\n#### 2. Acceptable forms of certification\n##### (a) In general\nSection 44703 of title 49, United States Code, is amended by adding at the end the following:\n(m) Sufficiency of digital and physical airman certificates An individual issued a certificate pursuant to this section (including a medical certificate) may present such certificate to an inspector of the Federal Aviation Administration in any of the following formats: (1) A physical certificate issued by the Administrator (or his or her designee). (2) A digital certificate issued by the Administrator that is stored on an electronic device or, in areas where there is sufficient connectivity to do so, a cloud-based system, and presented in accordance with authentication and verification requirements established by the Administrator. .\n##### (b) Rulemaking\nNot later than November 30, 2028, the Administrator of the Federal Aviation Administration shall issue a final rule to update regulations in parts 61, 63, 65, 67, and 107 of title 14, Code of Federal Regulations, to implement the amendment made by this section, and any applicable guidance and policies.",
      "versionDate": "2026-03-26",
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
        "actionDate": "2026-03-25",
        "text": "Received in the Senate and Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "2247",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Airmen Certificate Accessibility Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2026-04-13T13:31:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-26",
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
          "measure-id": "id119s4256",
          "measure-number": "4256",
          "measure-type": "s",
          "orig-publish-date": "2026-03-26",
          "originChamber": "SENATE",
          "update-date": "2026-04-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4256v00",
            "update-date": "2026-04-16"
          },
          "action-date": "2026-03-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Airmen Certificate Accessibility Act</strong></p><p>This bill allows a pilot to present a digital copy of certain certificates (e.g., an airman certificate or a\u00a0medical certificate) when required to present such documentation by a\u00a0Federal Aviation Administration (FAA) inspector.</p><p>Under current FAA regulations, a pilot must present for inspection a physical copy of an airman certificate and other paperwork upon a request from the FAA; a federal, state, or local law enforcement officer; or an authorized representative of the Transportation Security Administration or the National Transportation Safety Board. This bill allows a pilot to present a\u00a0certificate such as an airman certificate or a medical\u00a0certificate to an FAA inspector as (1) a physical certificate, or (2) a digital copy stored on an electronic device or cloud storage platform.</p><p>The FAA must update current regulations to implement this change.</p>"
        },
        "title": "Airmen Certificate Accessibility Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4256.xml",
    "summary": {
      "actionDate": "2026-03-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Airmen Certificate Accessibility Act</strong></p><p>This bill allows a pilot to present a digital copy of certain certificates (e.g., an airman certificate or a\u00a0medical certificate) when required to present such documentation by a\u00a0Federal Aviation Administration (FAA) inspector.</p><p>Under current FAA regulations, a pilot must present for inspection a physical copy of an airman certificate and other paperwork upon a request from the FAA; a federal, state, or local law enforcement officer; or an authorized representative of the Transportation Security Administration or the National Transportation Safety Board. This bill allows a pilot to present a\u00a0certificate such as an airman certificate or a medical\u00a0certificate to an FAA inspector as (1) a physical certificate, or (2) a digital copy stored on an electronic device or cloud storage platform.</p><p>The FAA must update current regulations to implement this change.</p>",
      "updateDate": "2026-04-16",
      "versionCode": "id119s4256"
    },
    "title": "Airmen Certificate Accessibility Act"
  },
  "summaries": [
    {
      "actionDate": "2026-03-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Airmen Certificate Accessibility Act</strong></p><p>This bill allows a pilot to present a digital copy of certain certificates (e.g., an airman certificate or a\u00a0medical certificate) when required to present such documentation by a\u00a0Federal Aviation Administration (FAA) inspector.</p><p>Under current FAA regulations, a pilot must present for inspection a physical copy of an airman certificate and other paperwork upon a request from the FAA; a federal, state, or local law enforcement officer; or an authorized representative of the Transportation Security Administration or the National Transportation Safety Board. This bill allows a pilot to present a\u00a0certificate such as an airman certificate or a medical\u00a0certificate to an FAA inspector as (1) a physical certificate, or (2) a digital copy stored on an electronic device or cloud storage platform.</p><p>The FAA must update current regulations to implement this change.</p>",
      "updateDate": "2026-04-16",
      "versionCode": "id119s4256"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4256is.xml"
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
      "title": "Airmen Certificate Accessibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-09T02:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Airmen Certificate Accessibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T02:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 49, United States Code, to establish acceptable formats for presentation of airman certificates to the Federal Aviation Administration.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-09T02:18:27Z"
    }
  ]
}
```
