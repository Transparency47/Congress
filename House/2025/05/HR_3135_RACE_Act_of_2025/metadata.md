# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3135?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3135
- Title: RACE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3135
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-04-14T20:31:12Z
- Update date including text: 2026-04-14T20:31:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3135",
    "number": "3135",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "RACE Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T20:31:12Z",
    "updateDateIncludingText": "2026-04-14T20:31:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T13:07:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3135ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3135\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Barr introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Securities Act of 1933 to automatically qualify offering statements filed with the Securities and Exchange Commission in connection with certain securities issued under Regulation A tier 2, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Regulation Advancement for Capital Enhancement Act of 2025 or the RACE Act of 2025 .\n#### 2. Offering of substantially similar securities\nSection 3(b) of the Securities Act of 1933 ( 15 U.S.C. 77c(b) ) is amended by adding at the end the following:\n(6) Offering of substantially similar securities (A) In general With respect to a person who has issued a class of securities (whether preferred, common, or convertible securities) exempted under paragraph (2) and has filed an offering statement with the Commission with respect to such class that was qualified by the Commission, an offering statement filed with the Commission in connection with an additional class of securities issued by the person and exempted under paragraph (2) shall be deemed qualified by the Commission upon filing, if\u2014 (i) the securities in the additional class are substantially similar to, and have predefined characteristics in common with, the securities in the original class; (ii) the offering amount of each such class is less than $5,000,000; and (iii) the aggregate offering amount of the securities in all such additional classes that are offered and sold within the prior 12-month period in reliance on the exemption provided under this paragraph does not exceed the dollar limit provided for the aggregate offering amount for securities that are offered and sold within the prior 12-month period in reliance on the exemption provided under paragraph (2). (B) No requirement to have the same nature or terms For purposes of subparagraph (A)(ii), a security can be substantially similar to another security without having the same nature or terms. .",
      "versionDate": "2025-05-01",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-21T12:18:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-01",
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
          "measure-id": "id119hr3135",
          "measure-number": "3135",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-01",
          "originChamber": "HOUSE",
          "update-date": "2026-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3135v00",
            "update-date": "2026-04-14"
          },
          "action-date": "2025-05-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Regulation Advancement for Capital Enhancement Act of 2025 or the RACE Act of 2025</strong></p><p>This bill allows issuers with offerings that were previously exempted from securities registration requirements to issue an additional class of securities if certain criteria are met.</p><p>Specifically, this bill allows an issuer who issued securities under Regulation A\u00a0(a small offering of securities exempt from registration requirements)\u00a0to issue an additional class of securities if the securities in the additional class are substantially similar to the original class and the offering amount does not exceed specified dollar limits. However, the securities offered in the additional class are not required to have the same nature or terms.\u00a0</p>"
        },
        "title": "RACE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3135.xml",
    "summary": {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Regulation Advancement for Capital Enhancement Act of 2025 or the RACE Act of 2025</strong></p><p>This bill allows issuers with offerings that were previously exempted from securities registration requirements to issue an additional class of securities if certain criteria are met.</p><p>Specifically, this bill allows an issuer who issued securities under Regulation A\u00a0(a small offering of securities exempt from registration requirements)\u00a0to issue an additional class of securities if the securities in the additional class are substantially similar to the original class and the offering amount does not exceed specified dollar limits. However, the securities offered in the additional class are not required to have the same nature or terms.\u00a0</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr3135"
    },
    "title": "RACE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Regulation Advancement for Capital Enhancement Act of 2025 or the RACE Act of 2025</strong></p><p>This bill allows issuers with offerings that were previously exempted from securities registration requirements to issue an additional class of securities if certain criteria are met.</p><p>Specifically, this bill allows an issuer who issued securities under Regulation A\u00a0(a small offering of securities exempt from registration requirements)\u00a0to issue an additional class of securities if the securities in the additional class are substantially similar to the original class and the offering amount does not exceed specified dollar limits. However, the securities offered in the additional class are not required to have the same nature or terms.\u00a0</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr3135"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3135ih.xml"
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
      "title": "RACE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RACE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Regulation Advancement for Capital Enhancement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Securities Act of 1933 to automatically qualify offering statements filed with the Securities and Exchange Commission in connection with certain securities issued under Regulation A tier 2, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:48:30Z"
    }
  ]
}
```
