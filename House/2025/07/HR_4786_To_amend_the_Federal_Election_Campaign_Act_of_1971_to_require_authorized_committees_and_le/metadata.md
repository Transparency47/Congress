# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4786?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4786
- Title: Honest Elections and Campaign, No Gain Act
- Congress: 119
- Bill type: HR
- Bill number: 4786
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2026-03-31T15:31:51Z
- Update date including text: 2026-03-31T15:31:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-29 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-29 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4786",
    "number": "4786",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001066",
        "district": "14",
        "firstName": "Kathy",
        "fullName": "Rep. Castor, Kathy [D-FL-14]",
        "lastName": "Castor",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Honest Elections and Campaign, No Gain Act",
    "type": "HR",
    "updateDate": "2026-03-31T15:31:51Z",
    "updateDateIncludingText": "2026-03-31T15:31:51Z"
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-07-29T21:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-29T21:03:20Z",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "FL"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MD"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "GA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4786ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4786\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Ms. Castor of Florida (for herself, Mr. Bilirakis , and Mr. Raskin ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to require authorized committees and leadership PACs of candidates for election for Federal office to disburse funds remaining unexpended after the date of the election involved, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Honest Elections and Campaign, No Gain Act .\n#### 2. Requiring authorized committees of candidates to disburse funds remaining unexpended after date of election\n##### (a) Requiring disbursement\nTitle III of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101 et seq. ) is amended by inserting after section 303 the following new section:\n303A. Disbursement of funds remaining unexpended after date of election (a) Requiring disbursement (1) In general Each authorized committee or leadership PAC of a candidate shall, in accordance with subsection (b) and prior to the expiration of the applicable disbursement period, disburse any funds of the committee or PAC before the earliest of\u2014 (A) the last day of the applicable disbursement period; (B) the date on which the candidate first makes a lobbying contact or is employed or retained to make a lobbying contact that would require registration under section 4 of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1603 ); or (C) the date on which the candidate becomes an agent of a foreign principal that would require registration under section 2 of the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 612 ). (2) Exception for candidates in next election Paragraph (1) does not apply to the committee or PAC of a candidate who, prior to the first day of the applicable disbursement period, provides the appropriate State election official with the information and fees (if any) required under State law for the individual to qualify as a candidate for the next election for the office sought by the candidate or the next election for another Federal office. (3) Applicable disbursement period In this subsection, the applicable disbursement period is, with respect to a candidate seeking election for an office, the 2-year period which begins on the day after the latest date on which an individual may provide the appropriate State election official with the information and fees (if any) required under State law for the individual to qualify as a candidate for the next election for such office. (b) Rules for disbursement of funds (1) Payment of obligations In carrying out subsection (a), an authorized committee or leadership PAC shall first disburse funds to pay obligations incurred in connection with the operation of the committee. (2) Other permitted disbursements If, after disbursing all of the funds necessary to pay obligations under paragraph (1), funds of a committee or PAC remain unexpended, the committee or PAC may only disburse the funds for any of the following purposes, in such manner and combination as the committee or PAC considers appropriate: (A) To return to any person a contribution the person made to the committee or PAC. (B) To make a contribution to an organization described in section 170(c) of the Internal Revenue Code of 1986. (C) To make a transfer without limitation to a national, State, or local committee of a political party. (c) Restrictions on disbursement to relatives (1) Restriction In disbursing funds pursuant to the requirements of this section, an authorized committee or leadership PAC may not disburse funds to a relative of the candidate unless the funds are disbursed to pay an obligation of the committee as described in paragraph (1) of subsection (b) which is reported by the committee or PAC as a disbursement under section 304(b)(5) or which would be so reported if the amount of the disbursement were in excess of $200. (2) Relative defined In this subsection, the term relative means, with respect to a candidate, an individual who is related to the candidate as father, mother, son, daughter, brother, sister, uncle, aunt, first cousin, nephew, niece, husband, wife, father-in-law, mother-in-law, son-in-law, daughter-in-law, brother-in-law, sister-in-law, stepfather, stepmother, stepson, stepdaughter, stepbrother, stepsister, half brother, or half sister. (d) Definition In this section, the term leadership PAC has the meaning given such term in section 304(i)(8)(B). .\n##### (b) Conforming amendment relating to permitted uses of contributions\nSection 313(a) of such Act ( 52 U.S.C. 30114(a) ) is amended by striking A contribution and inserting Subject to section 303A, a contribution .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to the regularly scheduled general election for Federal office held in November 2026 and each succeeding election for Federal office.\n#### 3. Requiring former candidates serving as registered lobbyists to certify compliance with disbursement requirements\n##### (a) Certification of compliance\nSection 4(b) of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1603(b) ) is amended\u2014\n**(1)**\nby striking and at the end of paragraph (6);\n**(2)**\nby striking the period at the end of paragraph (7) and inserting ; and ; and\n**(3)**\nby inserting after paragraph (7) the following new paragraph:\n(8) in the case of an individual who was a candidate for election for Federal office, a certification (under penalty of perjury) that each authorized committee and leadership PAC (as defined in section 304(i)(8)(B) of the Federal Election Campaign Act of 1971) of the individual is in compliance with section 303A of the Federal Election Campaign Act of 1971 (relating to the disbursement of funds of the committee or leadership PAC which remain unexpended after the date of the election). .\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply with respect to registration statements filed under section 4(a) of the Lobbying Disclosure Act on or after the date of the regularly scheduled general election for Federal office held in November 2026.\n#### 4. Requiring former candidates serving as foreign agents to certify compliance with disbursement requirements\n##### (a) Certification of compliance\nSection 2(a) of the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 612(a) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (10) and (11) as paragraphs (11) and (12); and\n**(2)**\nby inserting after paragraph (9) the following new paragraph:\n(10) In the case of an individual who was a candidate for election for Federal office, a certification (under penalty of perjury) that each authorized committee and leadership PAC (as defined in section 304(i)(8)(B) of the Federal Election Campaign Act of 1971) of the individual is in compliance with section 303A of the Federal Election Campaign Act of 1971 (relating to the disbursement of funds of the committee or leadership PAC which remain unexpended after the date of the election). .\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply with respect to registration statements filed under section 2 of the Foreign Agents Registration Act of 1938, as amended on or after the date of the regularly scheduled general election for Federal office held in November 2026.",
      "versionDate": "2025-07-29",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-08-07T16:32:20Z"
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
          "measure-id": "id119hr4786",
          "measure-number": "4786",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-29",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4786v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-07-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Honest Elections and Campaign, No Gain Act</strong><strong></strong></p> <p>This bill establishes certain requirements for disbursing unused funds after a federal election. The bill also requires former candidates serving as registered lobbyists or foreign agents to comply with disbursement requirements.</p> <p>Specifically, the bill requires each authorized committee or leadership political action committee (PAC) of a candidate to disburse all unused funds within a specified time period beginning after an election or before the candidate registers as a lobbyist or foreign agent, unless the candidate files to run for office again before the disbursement period begins. </p> <p>A committee or PAC disbursing unspent funds shall first pay any obligations incurred. If funds are left over, the committee or PAC may only disburse the funds in one or more of the following ways: (1) returning funds to donors; (2) making contributions to nonprofit organizations; and (3) transferring funds without limitation to a national, state, or local committee of a political party. The bill generally prohibits disbursements to relatives of the candidate.</p> <p>A former candidate must, in order to register as a lobbyist or foreign agent, comply with the disbursement requirements outlined by this bill.</p>"
        },
        "title": "Honest Elections and Campaign, No Gain Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4786.xml",
    "summary": {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Honest Elections and Campaign, No Gain Act</strong><strong></strong></p> <p>This bill establishes certain requirements for disbursing unused funds after a federal election. The bill also requires former candidates serving as registered lobbyists or foreign agents to comply with disbursement requirements.</p> <p>Specifically, the bill requires each authorized committee or leadership political action committee (PAC) of a candidate to disburse all unused funds within a specified time period beginning after an election or before the candidate registers as a lobbyist or foreign agent, unless the candidate files to run for office again before the disbursement period begins. </p> <p>A committee or PAC disbursing unspent funds shall first pay any obligations incurred. If funds are left over, the committee or PAC may only disburse the funds in one or more of the following ways: (1) returning funds to donors; (2) making contributions to nonprofit organizations; and (3) transferring funds without limitation to a national, state, or local committee of a political party. The bill generally prohibits disbursements to relatives of the candidate.</p> <p>A former candidate must, in order to register as a lobbyist or foreign agent, comply with the disbursement requirements outlined by this bill.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4786"
    },
    "title": "Honest Elections and Campaign, No Gain Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Honest Elections and Campaign, No Gain Act</strong><strong></strong></p> <p>This bill establishes certain requirements for disbursing unused funds after a federal election. The bill also requires former candidates serving as registered lobbyists or foreign agents to comply with disbursement requirements.</p> <p>Specifically, the bill requires each authorized committee or leadership political action committee (PAC) of a candidate to disburse all unused funds within a specified time period beginning after an election or before the candidate registers as a lobbyist or foreign agent, unless the candidate files to run for office again before the disbursement period begins. </p> <p>A committee or PAC disbursing unspent funds shall first pay any obligations incurred. If funds are left over, the committee or PAC may only disburse the funds in one or more of the following ways: (1) returning funds to donors; (2) making contributions to nonprofit organizations; and (3) transferring funds without limitation to a national, state, or local committee of a political party. The bill generally prohibits disbursements to relatives of the candidate.</p> <p>A former candidate must, in order to register as a lobbyist or foreign agent, comply with the disbursement requirements outlined by this bill.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4786"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4786ih.xml"
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
      "title": "Honest Elections and Campaign, No Gain Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Honest Elections and Campaign, No Gain Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Election Campaign Act of 1971 to require authorized committees and leadership PACs of candidates for election for Federal office to disburse funds remaining unexpended after the date of the election involved, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T05:18:48Z"
    }
  ]
}
```
