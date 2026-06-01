# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5689?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5689
- Title: Shutdown Guidance for Financial Institutions Act
- Congress: 119
- Bill type: HR
- Bill number: 5689
- Origin chamber: House
- Introduced date: 2025-10-03
- Update date: 2026-04-07T08:05:42Z
- Update date including text: 2026-04-07T08:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-03: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-10-03: Introduced in House

## Actions

- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5689",
    "number": "5689",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Shutdown Guidance for Financial Institutions Act",
    "type": "HR",
    "updateDate": "2026-04-07T08:05:42Z",
    "updateDateIncludingText": "2026-04-07T08:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-03",
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
          "date": "2025-10-03T19:31:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-10-03T19:30:50Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NV"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MD"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "DC"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MD"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "IN"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "OH"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "MD"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "RI"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "PR"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "WA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NJ"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "TX"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "NV"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5689ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5689\nIN THE HOUSE OF REPRESENTATIVES\nOctober 3, 2025 Mr. Subramanyam (for himself, Mr. Beyer , Mr. Horsford , Mr. Lieu , Mrs. McClain Delaney , Ms. McClellan , Ms. Norton , Mr. Raskin , and Mr. Walkinshaw ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Federal financial regulators to issue guidance encouraging financial institutions to work with consumers and businesses affected by a Federal Government shutdown, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shutdown Guidance for Financial Institutions Act .\n#### 2. Shutdown guidance for financial institutions\n##### (a) Guidance\nNot later than the end of the 180-day period beginning on the date of enactment of this Act, the Federal financial regulators shall, jointly, in consultation with State banking regulators and other appropriate Federal and State agencies, issue shutdown guidance to the financial institutions they regulate encouraging the financial institutions to\u2014\n**(1)**\nwork with consumers and businesses affected by a shutdown;\n**(2)**\nrecognize that consumers and businesses affected by a shutdown may lose access to credit and face temporary hardship in making payments on debts such as mortgages, student loans, car loans, business loans, or credit cards;\n**(3)**\nconsider prudent efforts to modify terms on existing loans or extend new credit to help consumers and businesses affected by a shutdown, consistent with safe-and-sound lending practices; and\n**(4)**\ntake steps to prevent adverse information being reported in a manner that harms consumers affected by a shutdown, including by preventing modified credit arrangements intended to help consumers fulfill their financial obligations from being reported to, and coded by, consumer reporting agencies on a consumer's credit report in a manner that hurts the creditworthiness of the consumer.\n##### (b) Notice of guidance during a shutdown\nNot later than the end of the 24-hour period beginning at the start of a shutdown, the Federal financial regulators shall, jointly, issue a press release to alert financial institutions, consumers, and businesses to the existence, and content, of the guidance issued pursuant to subsection (a).\n##### (c) Post-Shutdown report to Congress and updated guidance\n**(1) In general**\nNot later than the end of the 90-day period beginning on the date a shutdown ends, the Federal financial regulators shall, jointly, issue a report to Congress containing an analysis of the effectiveness of the guidance issued pursuant to subsection (a).\n**(2) Updated guidance**\nNot later than the end of the 180-day period beginning on the date a report is issued under paragraph (1), the Federal financial regulators shall update the guidance required under subsection (a) if any shortcomings are identified in such report.\n##### (d) Definitions\nIn this section:\n**(1) Consumers affected by a shutdown**\nThe term consumers affected by a shutdown means an individual who is an employee of\u2014\n**(A)**\nthe Federal Government, and who is furloughed or excepted from a furlough during the shutdown;\n**(B)**\nthe District of Columbia, and who is not receiving pay because of the shutdown; or\n**(C)**\na Federal contractor (as defined under section 7101 of title 41, United States Code) or other business, and who has experienced a substantial reduction in pay due to the shutdown.\n**(2) Consumers and businesses affected by a shutdown**\nThe term consumers and businesses affected by a shutdown means\u2014\n**(A)**\na consumer affected by a shutdown; and\n**(B)**\na Federal contractor (as defined under section 7101 of title 41, United States Code) or other business that has experienced a substantial reduction in income due to the shutdown.\n**(3) Federal financial regulators**\nThe term Federal financial regulators means the Board of Governors of the Federal Reserve System, the Bureau of Consumer Financial Protection, the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration.\n**(4) Shutdown**\nThe term shutdown means any period in which there is more than a 24-hour lapse in appropriations as a result of a failure to enact a regular appropriations bill or continuing resolution.\n#### 3. Determination of budgetary effects\nThe budgetary effects of this Act, for the purpose of complying with the Statutory Pay-As-You-Go Act of 2010, shall be determined by reference to the latest statement titled Budgetary Effects of PAYGO Legislation for this Act, submitted for printing in the Congressional Record by the Chairman of the House Budget Committee, provided that such statement has been submitted prior to the vote on passage.",
      "versionDate": "2025-10-03",
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
        "actionDate": "2025-10-09",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2995",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Shutdown Guidance for Financial Institutions Act",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-10-17T17:50:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-03",
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
          "measure-id": "id119hr5689",
          "measure-number": "5689",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-03",
          "originChamber": "HOUSE",
          "update-date": "2025-10-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5689v00",
            "update-date": "2025-10-17"
          },
          "action-date": "2025-10-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Shutdown Guidance for Financial Institutions Act </strong></p><p>This bill directs financial regulators\u2014including the Federal Reserve Board, the Consumer Financial Protection Bureau, the Office of the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration\u2014to jointly issue guidance relating to a government shutdown.</p><p>Specifically, financial regulators must issue guidance encouraging financial institutions to</p><ul><li>work with consumers and businesses affected by a shutdown,</li><li>recognize that consumers and businesses affected by a shutdown may lose access to credit and face temporary hardship in making payments on debts,</li><li>consider efforts to modify terms on existing loans or extend new credit to assist consumers and businesses affected by a shutdown, and</li><li>take steps to prevent adverse credit information from being reported in a manner that harms consumers affected by a shutdown.</li></ul><p>In addition, financial regulators must jointly issue a press release to notify financial institutions, consumers, and businesses\u00a0of this guidance in the event of a government shutdown.</p><p>Financial regulators must also complete a report after a government shutdown regarding the guidance's effectiveness and update the guidance if any shortcoming are identified in the report.\u00a0</p>"
        },
        "title": "Shutdown Guidance for Financial Institutions Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5689.xml",
    "summary": {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Shutdown Guidance for Financial Institutions Act </strong></p><p>This bill directs financial regulators\u2014including the Federal Reserve Board, the Consumer Financial Protection Bureau, the Office of the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration\u2014to jointly issue guidance relating to a government shutdown.</p><p>Specifically, financial regulators must issue guidance encouraging financial institutions to</p><ul><li>work with consumers and businesses affected by a shutdown,</li><li>recognize that consumers and businesses affected by a shutdown may lose access to credit and face temporary hardship in making payments on debts,</li><li>consider efforts to modify terms on existing loans or extend new credit to assist consumers and businesses affected by a shutdown, and</li><li>take steps to prevent adverse credit information from being reported in a manner that harms consumers affected by a shutdown.</li></ul><p>In addition, financial regulators must jointly issue a press release to notify financial institutions, consumers, and businesses\u00a0of this guidance in the event of a government shutdown.</p><p>Financial regulators must also complete a report after a government shutdown regarding the guidance's effectiveness and update the guidance if any shortcoming are identified in the report.\u00a0</p>",
      "updateDate": "2025-10-17",
      "versionCode": "id119hr5689"
    },
    "title": "Shutdown Guidance for Financial Institutions Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Shutdown Guidance for Financial Institutions Act </strong></p><p>This bill directs financial regulators\u2014including the Federal Reserve Board, the Consumer Financial Protection Bureau, the Office of the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration\u2014to jointly issue guidance relating to a government shutdown.</p><p>Specifically, financial regulators must issue guidance encouraging financial institutions to</p><ul><li>work with consumers and businesses affected by a shutdown,</li><li>recognize that consumers and businesses affected by a shutdown may lose access to credit and face temporary hardship in making payments on debts,</li><li>consider efforts to modify terms on existing loans or extend new credit to assist consumers and businesses affected by a shutdown, and</li><li>take steps to prevent adverse credit information from being reported in a manner that harms consumers affected by a shutdown.</li></ul><p>In addition, financial regulators must jointly issue a press release to notify financial institutions, consumers, and businesses\u00a0of this guidance in the event of a government shutdown.</p><p>Financial regulators must also complete a report after a government shutdown regarding the guidance's effectiveness and update the guidance if any shortcoming are identified in the report.\u00a0</p>",
      "updateDate": "2025-10-17",
      "versionCode": "id119hr5689"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5689ih.xml"
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
      "title": "Shutdown Guidance for Financial Institutions Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T09:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Shutdown Guidance for Financial Institutions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T09:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Federal financial regulators to issue guidance encouraging financial institutions to work with consumers and businesses affected by a Federal Government shutdown, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T09:33:16Z"
    }
  ]
}
```
