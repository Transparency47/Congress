# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4799?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4799
- Title: Ban Corporate PACs Act
- Congress: 119
- Bill type: HR
- Bill number: 4799
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2026-03-31T15:33:29Z
- Update date including text: 2026-03-31T15:33:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4799",
    "number": "4799",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Ban Corporate PACs Act",
    "type": "HR",
    "updateDate": "2026-03-31T15:33:29Z",
    "updateDateIncludingText": "2026-03-31T15:33:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "ME"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NH"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4799ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4799\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Mr. Harder of California (for himself and Mr. Golden of Maine ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to limit the authority of corporations to establish and operate separate segregated funds utilized for political purposes, including the establishment or operation of a political committee, to nonprofit corporations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ban Corporate PACs Act .\n#### 2. Limiting authority of corporations to establish or operate separate segregated funds for political purposes to nonprofit corporations\n##### (a) Limitation\n**(1) In general**\nSection 316(b)(2)(C) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30118(b)(2)(C) ) is amended by striking a corporation and inserting a nonprofit corporation .\n**(2) Definition**\nSection 316(b) of such Act ( 52 U.S.C. 30118(b) ) is amended by adding at the end the following new paragraph:\n(8) For purposes of this section, the term nonprofit corporation means a corporation described in section 501(c) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code, other than a corporation which is ineligible to be exempt from taxation under section 501(a) of such Code if it establishes a separate segregated fund under this subsection. .\n##### (b) Permitting solicitation of contributions only from executive and administrative personnel\nSection 316(b) of such Act ( 52 U.S.C. 30118(b) ) is amended\u2014\n**(1)**\nin paragraph (4)(A)(i), by striking its stockholders and their families and ;\n**(2)**\nin paragraph (4)(B)\u2014\n**(A)**\nby striking a corporation the first place it appears and inserting a nonprofit corporation ;\n**(B)**\nby striking any stockholder, executive or administrative personnel, and inserting any executive or administrative personnel ; and\n**(C)**\nby striking stockholders, executive or administrative personnel, and inserting executive or administrative personnel ;\n**(3)**\nin paragraph (4)(D)\u2014\n**(A)**\nby striking stockholders and ;\n**(B)**\nby striking such stockholders or personnel and inserting such personnel ; and\n**(C)**\nby striking such stockholders and personnel and inserting such personnel ; and\n**(4)**\nin paragraph (5), by striking stockholders and .\n##### (c) Treatment of government contractors\nSection 317(b) of such Act ( 52 U.S.C. 30119(b) ) is amended\u2014\n**(1)**\nby striking any corporation and inserting any nonprofit corporation ; and\n**(2)**\nby striking a corporation and inserting a nonprofit corporation .\n#### 3. Effective date; transition for existing funds and committees\n##### (a) Effective date\nThe amendments made by this Act shall take effect on the date of the enactment of this Act.\n##### (b) Transition for existing funds and committees\nIn the case of a separate segregate fund established and operating under section 316(b)(2)(C) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30118(b)(2)(C) ) as of the date of the enactment of this Act which is not a fund of a nonprofit corporation as defined in section 316(b)(8) of such Act (as added by section 2(a)(2)), the fund shall terminate and disburse its entire balance not later than 1 year after the date of the enactment of this Act.",
      "versionDate": "2025-07-29",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-07-29",
        "text": "Read twice and referred to the Committee on Rules and Administration."
      },
      "number": "2515",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Ban Corporate PACs Act",
      "type": "S"
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-08-07T16:32:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-29",
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
          "measure-id": "id119hr4799",
          "measure-number": "4799",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-29",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4799v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-07-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Ban Corporate PACs Act </b></p> <p>This bill prohibits for-profit corporations from establishing or operating a separate segregated political fund (commonly known as a political action committee or PAC). Existing funds must terminate not later than one year after the date of enactment of this bill.</p>"
        },
        "title": "Ban Corporate PACs Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4799.xml",
    "summary": {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Ban Corporate PACs Act </b></p> <p>This bill prohibits for-profit corporations from establishing or operating a separate segregated political fund (commonly known as a political action committee or PAC). Existing funds must terminate not later than one year after the date of enactment of this bill.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4799"
    },
    "title": "Ban Corporate PACs Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Ban Corporate PACs Act </b></p> <p>This bill prohibits for-profit corporations from establishing or operating a separate segregated political fund (commonly known as a political action committee or PAC). Existing funds must terminate not later than one year after the date of enactment of this bill.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4799"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4799ih.xml"
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
      "title": "Ban Corporate PACs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T12:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ban Corporate PACs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T12:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Election Campaign Act of 1971 to limit the authority of corporations to establish and operate separate segregated funds utilized for political purposes, including the establishment or operation of a political committee, to nonprofit corporations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T12:18:20Z"
    }
  ]
}
```
