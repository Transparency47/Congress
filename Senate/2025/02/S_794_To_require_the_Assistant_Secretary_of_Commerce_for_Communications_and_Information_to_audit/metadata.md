# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/794?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/794
- Title: A bill to require the Assistant Secretary of Commerce for Communications and Information to audit Federal spectrum.
- Congress: 119
- Bill type: S
- Bill number: 794
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2025-05-27T14:12:56Z
- Update date including text: 2025-05-27T14:12:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/794",
    "number": "794",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A bill to require the Assistant Secretary of Commerce for Communications and Information to audit Federal spectrum.",
    "type": "S",
    "updateDate": "2025-05-27T14:12:56Z",
    "updateDateIncludingText": "2025-05-27T14:12:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T18:38:33Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s794is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 794\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Lee introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Assistant Secretary of Commerce for Communications and Information to audit Federal spectrum.\n#### 1. Federal spectrum audit\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term Assistant Secretary means the Assistant Secretary of Commerce for Communications and Information; and\n**(2)**\nthe term Federal entity has the meaning given the term in section 113(l) of the National Telecommunications and Information Administration Organization Act ( 47 U.S.C. 923(l) ).\n##### (b) Audit and report\nNot later than 18 months after the date of enactment of this Act, the Assistant Secretary, in consultation with the head of each Federal entity, shall\u2014\n**(1)**\nconduct an audit of the electromagnetic spectrum that is assigned or otherwise allocated to each Federal entity as of the date of the audit; and\n**(2)**\nsubmit to Congress, and make available to each Member of Congress upon request, a report containing the results of the audit conducted under paragraph (1).\n##### (c) Contents of report\nThe Assistant Secretary shall include in the report submitted under subsection (b)(2), with respect to the electromagnetic spectrum that is assigned or otherwise allocated to a Federal entity as of the date of the audit\u2014\n**(1)**\neach particular band of spectrum being used by the Federal entity;\n**(2)**\na description of each purpose for which a particular band described in paragraph (1) is being used, and how much of the band is being used for that purpose;\n**(3)**\nthe State or other geographic area in which a particular band described in paragraph (1) is assigned or allocated for use;\n**(4)**\nwhether a particular band described in paragraph (1) is used exclusively by the Federal entity or shared with another Federal entity or a non-Federal entity; and\n**(5)**\nany portion of the spectrum that is not being used by the Federal entity.\n##### (d) Form of report\nThe report required under subsection (b)(2) shall be submitted in unclassified form but may include a classified annex.\n##### (e) Relation to Department of Transportation Spectrum Audit\nThe Assistant Secretary shall coordinate with the Secretary of Transportation to ensure that the audit conducted under this section does not duplicate the audit conducted under section 27003 of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ; 135 Stat. 884).",
      "versionDate": "2025-02-27",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-26T12:55:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119s794",
          "measure-number": "794",
          "measure-type": "s",
          "orig-publish-date": "2025-02-27",
          "originChamber": "SENATE",
          "update-date": "2025-05-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s794v00",
            "update-date": "2025-05-20"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill requires the National Telecommunications and Information Administration to audit and report to Congress on electromagnetic spectrum that is assigned or allocated to federal entities. The report must identify each spectrum band used by a federal entity and detail where, how, and to what extent each such band is being used.\u00a0</p>"
        },
        "title": "A bill to require the Assistant Secretary of Commerce for Communications and Information to audit Federal spectrum."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s794.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill requires the National Telecommunications and Information Administration to audit and report to Congress on electromagnetic spectrum that is assigned or allocated to federal entities. The report must identify each spectrum band used by a federal entity and detail where, how, and to what extent each such band is being used.\u00a0</p>",
      "updateDate": "2025-05-20",
      "versionCode": "id119s794"
    },
    "title": "A bill to require the Assistant Secretary of Commerce for Communications and Information to audit Federal spectrum."
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill requires the National Telecommunications and Information Administration to audit and report to Congress on electromagnetic spectrum that is assigned or allocated to federal entities. The report must identify each spectrum band used by a federal entity and detail where, how, and to what extent each such band is being used.\u00a0</p>",
      "updateDate": "2025-05-20",
      "versionCode": "id119s794"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s794is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Assistant Secretary of Commerce for Communications and Information to audit Federal spectrum.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:26Z"
    },
    {
      "title": "A bill to require the Assistant Secretary of Commerce for Communications and Information to audit Federal spectrum.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T11:56:30Z"
    }
  ]
}
```
