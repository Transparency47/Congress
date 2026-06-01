# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3946?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3946
- Title: Tribal Firearm Access Act
- Congress: 119
- Bill type: S
- Bill number: 3946
- Origin chamber: Senate
- Introduced date: 2026-02-26
- Update date: 2026-04-10T14:05:58Z
- Update date including text: 2026-04-10T14:05:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-26: Introduced in Senate
- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-02-26: Introduced in Senate

## Actions

- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3946",
    "number": "3946",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "M001190",
        "district": "",
        "firstName": "Markwayne",
        "fullName": "Sen. Mullin, Markwayne [R-OK]",
        "lastName": "Mullin",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Tribal Firearm Access Act",
    "type": "S",
    "updateDate": "2026-04-10T14:05:58Z",
    "updateDateIncludingText": "2026-04-10T14:05:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-26",
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
      "actionDate": "2026-02-26",
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
          "date": "2026-02-26T18:31:53Z",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3946is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3946\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2026 Mr. Mullin (for himself and Mr. Daines ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo allow members of federally recognized Tribes to use their Tribal government identification documents in obtaining a firearm from a federally licensed firearms dealer.\n#### 1. Short title\nThis Act may be cited as the Tribal Firearm Access Act .\n#### 2. Allowing members of federally recognized Tribes to use their Tribal government identification documents in obtaining a firearm from a federally licensed firearms dealer\n##### (a) In general\nSection 922(t)(1)(D) of title 18, United States Code, is amended by inserting , or a valid identification document issued by a Tribal government before the period.\n##### (b) Definition\nSection 921(a) of such title is amended by adding at the end the following:\n(39) The term Tribal government means the recognized governing body of any Indian or Alaska Native Tribe, band, nation, pueblo, village, community, component band, or component reservation, individually identified (including parenthetically) in the list published most recently as of the date of the enactment of this paragraph pursuant to section 104(a) of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131(a) ). .\n##### (c) Effective date\nThe amendments made by this section shall take effect on the date that is 90 days after the date of enactment of this Act.",
      "versionDate": "2026-02-26",
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
        "actionDate": "2026-02-25",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "7698",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Tribal Firearm Access Act",
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
        "name": "Native Americans",
        "updateDate": "2026-03-24T01:34:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-26",
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
          "measure-id": "id119s3946",
          "measure-number": "3946",
          "measure-type": "s",
          "orig-publish-date": "2026-02-26",
          "originChamber": "SENATE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3946v00",
            "update-date": "2026-04-10"
          },
          "action-date": "2026-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Tribal Firearm Access Act</b></p> <p>This bill allows members of federally recognized Indian tribes to use their valid identification documents issued by tribal governments to obtain a firearm from a federally licensed dealer.</p>"
        },
        "title": "Tribal Firearm Access Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3946.xml",
    "summary": {
      "actionDate": "2026-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Tribal Firearm Access Act</b></p> <p>This bill allows members of federally recognized Indian tribes to use their valid identification documents issued by tribal governments to obtain a firearm from a federally licensed dealer.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119s3946"
    },
    "title": "Tribal Firearm Access Act"
  },
  "summaries": [
    {
      "actionDate": "2026-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Tribal Firearm Access Act</b></p> <p>This bill allows members of federally recognized Indian tribes to use their valid identification documents issued by tribal governments to obtain a firearm from a federally licensed dealer.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119s3946"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3946is.xml"
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
      "title": "Tribal Firearm Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tribal Firearm Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to allow members of federally recognized Tribes to use their Tribal government identification documents in obtaining a firearm from a federally licensed firearms dealer.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:37Z"
    }
  ]
}
```
