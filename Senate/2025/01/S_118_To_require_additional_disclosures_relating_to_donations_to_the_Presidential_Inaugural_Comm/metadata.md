# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/118?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/118
- Title: Inaugural Committee Transparency Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 118
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/118",
    "number": "118",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Inaugural Committee Transparency Act of 2025",
    "type": "S",
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
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T18:20:03Z",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "RI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MD"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s118is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 118\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Ms. Cortez Masto (for herself, Mr. Whitehouse , Mr. Van Hollen , Mr. Markey , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require additional disclosures relating to donations to the Presidential Inaugural Committee, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Inaugural Committee Transparency Act of 2025 .\n#### 2. Disclosure of certain donations to and spending by the Presidential Inaugural Committee\nSection 510 of title 36, United States Code, is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by inserting , and disclosing any disbursement made in an amount equal to or greater than $200 and the purpose of each disbursement before the period at the end; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (B), by striking and at the end;\n**(ii)**\nin subparagraph (C), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(D) for any disbursement in an amount equal to or greater than $200 that is made, including any such disbursement made after the end of the inaugural period\u2014 (i) the name and address of the person to whom the disbursement was made; (ii) the date on which the disbursement was made; and (iii) the total amount and purpose of the disbursement. ;\n**(2)**\nby amending subsection (c) to read as follows:\n(c) Prohibition (1) In general It shall be unlawful\u2014 (A) for an Inaugural Committee to solicit, accept, or receive a donation from a foreign national; (B) for a person\u2014 (i) to make a donation to an Inaugural Committee in the name of another person, or to knowingly authorize his or her name to be used to effect such a donation; or (ii) to knowingly accept a donation to an Inaugural Committee made by a person in the name of another person; (C) for a foreign national to, directly or indirectly, make a donation, or make an express or implied promise to make a donation, to an Inaugural Committee; or (D) to convert a donation to an Inaugural Committee to personal use as described in paragraph (3). (2) Definition of foreign national In this subsection, the term foreign national has the meaning given the term in section 319(b) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30121(b) ). (3) Conversion of donation to personal use For purposes of paragraph (1)(D), a donation shall be considered to be converted to personal use if any part of the donated amount is used to fulfill a commitment, obligation, or expense of a person that would exist irrespective of the responsibilities of the Inaugural Committee. ; and\n**(3)**\nby adding at the end the following:\n(d) Requirement (1) In general Not later than the date that is 90 days after the date of the Presidential inaugural ceremony, the Inaugural Committee shall disburse any remaining donated funds to an organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code. (2) Extension (A) Request Upon request from the Inaugural Committee, the Federal Election Commission may extend the 90-day period described in paragraph (1). (B) Supplemental report In the case of an extension under subparagraph (A), the Inaugural Committee shall, not later than the last day of the extension period, file a supplement to the report required under subsection (b)(1). .",
      "versionDate": "2025-01-16",
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
            "name": "Charitable contributions",
            "updateDate": "2025-05-09T20:08:21Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-05-09T20:08:21Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-05-09T20:08:21Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-05-09T20:08:21Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-05-09T20:08:21Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-05-09T20:08:21Z"
          },
          {
            "name": "Tax-exempt organizations",
            "updateDate": "2025-05-09T20:08:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-01T20:47:05Z"
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
          "measure-id": "id119s118",
          "measure-number": "118",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-05-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s118v00",
            "update-date": "2025-05-05"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Inaugural Committee Transparency Act of 2025</strong></p><p>This bill requires the presidential inaugural committee to disclose to the Federal Election Commission, by 90 days after the presidential inaugural ceremony, any disbursement made in an amount equal to or greater than $200 and the purpose of each disbursement. The committee must also disclose the name and address of the person to whom the disbursement was made, the date of the disbursement, and the total amount and purpose of the disbursement.</p><p>The bill prohibits (1) an inaugural committee from soliciting or receiving a donation from a foreign national, in addition to the current ban on a committee accepting such a donation; (2) a person from making a donation to an inaugural committee in the name of another; (3) a foreign national from making a donation or making a promise to make a donation to such a committee; or (4) converting a donation to an inaugural committee to personal use.</p><p>The committee must disburse any remaining donated funds not later than 90 days after the inaugural ceremony to tax-exempt charitable organizations, but may request an extension of such 90-day period.</p>"
        },
        "title": "Inaugural Committee Transparency Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s118.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Inaugural Committee Transparency Act of 2025</strong></p><p>This bill requires the presidential inaugural committee to disclose to the Federal Election Commission, by 90 days after the presidential inaugural ceremony, any disbursement made in an amount equal to or greater than $200 and the purpose of each disbursement. The committee must also disclose the name and address of the person to whom the disbursement was made, the date of the disbursement, and the total amount and purpose of the disbursement.</p><p>The bill prohibits (1) an inaugural committee from soliciting or receiving a donation from a foreign national, in addition to the current ban on a committee accepting such a donation; (2) a person from making a donation to an inaugural committee in the name of another; (3) a foreign national from making a donation or making a promise to make a donation to such a committee; or (4) converting a donation to an inaugural committee to personal use.</p><p>The committee must disburse any remaining donated funds not later than 90 days after the inaugural ceremony to tax-exempt charitable organizations, but may request an extension of such 90-day period.</p>",
      "updateDate": "2025-05-05",
      "versionCode": "id119s118"
    },
    "title": "Inaugural Committee Transparency Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Inaugural Committee Transparency Act of 2025</strong></p><p>This bill requires the presidential inaugural committee to disclose to the Federal Election Commission, by 90 days after the presidential inaugural ceremony, any disbursement made in an amount equal to or greater than $200 and the purpose of each disbursement. The committee must also disclose the name and address of the person to whom the disbursement was made, the date of the disbursement, and the total amount and purpose of the disbursement.</p><p>The bill prohibits (1) an inaugural committee from soliciting or receiving a donation from a foreign national, in addition to the current ban on a committee accepting such a donation; (2) a person from making a donation to an inaugural committee in the name of another; (3) a foreign national from making a donation or making a promise to make a donation to such a committee; or (4) converting a donation to an inaugural committee to personal use.</p><p>The committee must disburse any remaining donated funds not later than 90 days after the inaugural ceremony to tax-exempt charitable organizations, but may request an extension of such 90-day period.</p>",
      "updateDate": "2025-05-05",
      "versionCode": "id119s118"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s118is.xml"
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
      "title": "Inaugural Committee Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-19T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Inaugural Committee Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require additional disclosures relating to donations to the Presidential Inaugural Committee, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:20Z"
    }
  ]
}
```
