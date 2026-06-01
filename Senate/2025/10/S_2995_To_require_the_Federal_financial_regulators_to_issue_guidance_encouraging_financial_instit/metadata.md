# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2995?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2995
- Title: Shutdown Guidance for Financial Institutions Act
- Congress: 119
- Bill type: S
- Bill number: 2995
- Origin chamber: Senate
- Introduced date: 2025-10-09
- Update date: 2025-10-24T13:31:47Z
- Update date including text: 2025-10-24T13:31:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-09: Introduced in Senate
- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-10-09: Introduced in Senate

## Actions

- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-09",
    "latestAction": {
      "actionDate": "2025-10-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2995",
    "number": "2995",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Shutdown Guidance for Financial Institutions Act",
    "type": "S",
    "updateDate": "2025-10-24T13:31:47Z",
    "updateDateIncludingText": "2025-10-24T13:31:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-09",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-09",
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
          "date": "2025-10-09T17:39:51Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "MD"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "VA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "VA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "NY"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "NJ"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2995is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2995\nIN THE SENATE OF THE UNITED STATES\nOctober 9, 2025 Mr. Van Hollen (for himself, Ms. Alsobrooks , Mr. Kaine , Mr. Warner , Mrs. Gillibrand , Mr. Booker , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Federal financial regulators to issue guidance encouraging financial institutions to work with consumers and businesses affected by a Federal Government shutdown, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shutdown Guidance for Financial Institutions Act .\n#### 2. Shutdown guidance for financial institutions\n##### (a) Definitions\nIn this section:\n**(1) Consumer affected by a shutdown**\nThe term consumer affected by a shutdown means an individual who is an employee of\u2014\n**(A)**\nthe Federal Government, and who is furloughed or excepted from a furlough during a shutdown;\n**(B)**\nthe District of Columbia, and who is not receiving pay because of a shutdown; or\n**(C)**\na Federal contractor or other business, and who has experienced a substantial reduction in pay due to the shutdown.\n**(2) Consumers and businesses affected by a shutdown**\nThe term consumers and businesses affected by a shutdown means\u2014\n**(A)**\na consumer affected by a shutdown; and\n**(B)**\na Federal contractor (as defined under section 7101 of title 41, United States Code) or other business that has experienced a substantial reduction in income due to the shutdown.\n**(3) Federal contractor**\nThe term Federal contractor has the meaning given the term contractor in section 7101 of title 41, United States Code.\n**(4) Federal financial regulators**\nThe term Federal financial regulators means the Board of Governors of the Federal Reserve System, the Bureau of Consumer Financial Protection, the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration.\n**(5) Shutdown**\nThe term shutdown means any period in which there is more than a 24-hour lapse in appropriations as a result of a failure to enact a regular appropriations bill or continuing resolution.\n##### (b) Guidance\nNot later than the end of the 180-day period beginning on the date of enactment of this Act, the Federal financial regulators jointly, in consultation with State banking regulators and other appropriate Federal and State agencies, shall issue shutdown guidance to the financial institutions they regulate encouraging the financial institutions to\u2014\n**(1)**\nwork with consumers and businesses affected by a shutdown;\n**(2)**\nrecognize that consumers and businesses affected by a shutdown may lose access to credit and face temporary hardship in making payments on debts such as mortgages, student loans, car loans, business loans, or credit cards;\n**(3)**\nconsider prudent efforts to modify terms on existing loans or extend new credit to help consumers and businesses affected by a shutdown, consistent with safe-and-sound lending practices; and\n**(4)**\ntake steps to prevent adverse information being reported in a manner that harms consumers affected by a shutdown, including by preventing modified credit arrangements intended to help consumers fulfill their financial obligations from being reported to, and coded by, consumer reporting agencies on a consumer report in a manner that hurts the creditworthiness of the consumer.\n##### (c) Notice of guidance during a shutdown\nNot later than the end of the 24-hour period beginning at the start of a shutdown, the Federal financial regulators jointly shall issue a press release to alert financial institutions, consumers, and businesses to the existence and content of the guidance issued under to subsection (b).\n##### (d) Post-Shutdown report to Congress and updated guidance\n**(1) In general**\nNot later than the end of the 90-day period beginning on the date on which a shutdown ends, the Federal financial regulators jointly shall submit to Congress a report that contains an analysis of the effectiveness of the guidance issued pursuant to subsection (b).\n**(2) Updated guidance**\nNot later than the end of the 180-day period beginning on the date on which a report is issued under paragraph (1), the Federal financial regulators shall update the guidance required under subsection (b) if any shortcomings are identified in the report.",
      "versionDate": "2025-10-09",
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
        "actionDate": "2025-10-03",
        "text": "Referred to the Committee on Financial Services, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5689",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Shutdown Guidance for Financial Institutions Act",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-10-24T12:41:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-09",
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
          "measure-id": "id119s2995",
          "measure-number": "2995",
          "measure-type": "s",
          "orig-publish-date": "2025-10-09",
          "originChamber": "SENATE",
          "update-date": "2025-10-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2995v00",
            "update-date": "2025-10-24"
          },
          "action-date": "2025-10-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Shutdown Guidance for Financial Institutions Act </strong></p><p>This bill directs financial regulators\u2014including the Federal Reserve Board, the Consumer Financial Protection Bureau, the Office of the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration\u2014to jointly issue guidance relating to a government shutdown.</p><p>Specifically, financial regulators must issue guidance encouraging financial institutions to</p><ul><li>work with consumers and businesses affected by a shutdown,</li><li>recognize that consumers and businesses affected by a shutdown may lose access to credit and face temporary hardship in making payments on debts,</li><li>consider efforts to modify terms on existing loans or extend new credit to assist consumers and businesses affected by a shutdown, and</li><li>take steps to prevent adverse credit information from being reported in a manner that harms consumers affected by a shutdown.</li></ul><p>In addition, financial regulators must jointly issue a press release to notify financial institutions, consumers, and businesses\u00a0of this guidance in the event of a government shutdown.</p><p>Financial regulators must also complete a report after a government shutdown regarding the guidance's effectiveness and update the guidance if any shortcoming are identified in the report.\u00a0</p>"
        },
        "title": "Shutdown Guidance for Financial Institutions Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2995.xml",
    "summary": {
      "actionDate": "2025-10-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Shutdown Guidance for Financial Institutions Act </strong></p><p>This bill directs financial regulators\u2014including the Federal Reserve Board, the Consumer Financial Protection Bureau, the Office of the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration\u2014to jointly issue guidance relating to a government shutdown.</p><p>Specifically, financial regulators must issue guidance encouraging financial institutions to</p><ul><li>work with consumers and businesses affected by a shutdown,</li><li>recognize that consumers and businesses affected by a shutdown may lose access to credit and face temporary hardship in making payments on debts,</li><li>consider efforts to modify terms on existing loans or extend new credit to assist consumers and businesses affected by a shutdown, and</li><li>take steps to prevent adverse credit information from being reported in a manner that harms consumers affected by a shutdown.</li></ul><p>In addition, financial regulators must jointly issue a press release to notify financial institutions, consumers, and businesses\u00a0of this guidance in the event of a government shutdown.</p><p>Financial regulators must also complete a report after a government shutdown regarding the guidance's effectiveness and update the guidance if any shortcoming are identified in the report.\u00a0</p>",
      "updateDate": "2025-10-24",
      "versionCode": "id119s2995"
    },
    "title": "Shutdown Guidance for Financial Institutions Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Shutdown Guidance for Financial Institutions Act </strong></p><p>This bill directs financial regulators\u2014including the Federal Reserve Board, the Consumer Financial Protection Bureau, the Office of the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration\u2014to jointly issue guidance relating to a government shutdown.</p><p>Specifically, financial regulators must issue guidance encouraging financial institutions to</p><ul><li>work with consumers and businesses affected by a shutdown,</li><li>recognize that consumers and businesses affected by a shutdown may lose access to credit and face temporary hardship in making payments on debts,</li><li>consider efforts to modify terms on existing loans or extend new credit to assist consumers and businesses affected by a shutdown, and</li><li>take steps to prevent adverse credit information from being reported in a manner that harms consumers affected by a shutdown.</li></ul><p>In addition, financial regulators must jointly issue a press release to notify financial institutions, consumers, and businesses\u00a0of this guidance in the event of a government shutdown.</p><p>Financial regulators must also complete a report after a government shutdown regarding the guidance's effectiveness and update the guidance if any shortcoming are identified in the report.\u00a0</p>",
      "updateDate": "2025-10-24",
      "versionCode": "id119s2995"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2995is.xml"
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
      "title": "Shutdown Guidance for Financial Institutions Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Shutdown Guidance for Financial Institutions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Federal financial regulators to issue guidance encouraging financial institutions to work with consumers and businesses affected by a Federal Government shutdown, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T02:48:26Z"
    }
  ]
}
```
