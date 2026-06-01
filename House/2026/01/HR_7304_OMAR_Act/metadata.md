# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7304?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7304
- Title: OMAR Act
- Congress: 119
- Bill type: HR
- Bill number: 7304
- Origin chamber: House
- Introduced date: 2026-01-30
- Update date: 2026-04-10T13:23:29Z
- Update date including text: 2026-04-10T13:23:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-01-30: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2026-01-30: Introduced in House

## Actions

- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-30",
    "latestAction": {
      "actionDate": "2026-01-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7304",
    "number": "7304",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "T000165",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
        "lastName": "Tiffany",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "OMAR Act",
    "type": "HR",
    "updateDate": "2026-04-10T13:23:29Z",
    "updateDateIncludingText": "2026-04-10T13:23:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
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
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-30",
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
          "date": "2026-01-30T15:33:10Z",
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
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7304ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7304\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 30, 2026 Mr. Tiffany (for himself and Mr. Wied ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to prohibit certain political committees from compensating the spouse of the candidate for services provided to or on behalf of the committee, to require such committees to report on payments made to the spouse and the immediate family members of the candidate, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Oversight for Members And Relatives Act or the OMAR Act .\n#### 2. Prohibiting use of campaign funds to compensate spouses of candidates; disclosure of payments made to spouses and family members\n##### (a) Prohibition; Disclosure\nSection 313 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30114 ) is amended by adding at the end the following new subsection:\n(c) Prohibiting Compensation of Spouses; Disclosure of Payments to Spouses and Family Members (1) Prohibiting compensation of spouses Notwithstanding any other provision of this Act, no authorized committee of a candidate or any other political committee established, maintained, or controlled by a candidate or an individual holding Federal office (other than a political committee of a political party) shall directly or indirectly compensate the spouse of the candidate or individual (as the case may be) for services provided to or on behalf of the committee. (2) Disclosure of payments to spouses and immediate family members In addition to any other information included in a report submitted under section 304 by a committee described in paragraph (1), the committee shall include in the report a separate statement of any payments, including direct or indirect compensation, made to the spouse or any immediate family member of the candidate or individual involved during the period covered by the report. (3) Immediate family member defined In this subsection, the term immediate family member means the son, daughter, son-in-law, daughter-in-law, mother, father, brother, sister, brother-in-law, sister-in-law, or grandchild of the candidate or individual involved. .\n##### (b) Conforming Amendment\nSection 313(a)(1) of such Act ( 52 U.S.C. 30114(a)(1) ) is amended by striking for otherwise and inserting subject to subsection (c), for otherwise .\n#### 3. Imposition of penalty against candidate or officeholder\n##### (a) In General\nSection 309 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30109 ) is amended by adding at the end the following new subsection:\n(e) In the case of a violation of section 313(c) committed by a committee described in such section, if the candidate or individual involved knew of the violation, any penalty imposed under this section shall be imposed on the candidate or individual and not on the committee. .\n##### (b) Prohibiting Reimbursement by Committee\nSection 313(c) of such Act ( 52 U.S.C. 30114(c) ), as added by section 2(a), is amended\u2014\n**(1)**\nby redesignating paragraph (3) as paragraph (4); and\n**(2)**\nby inserting after paragraph (2) the following new paragraph:\n(3) Prohibiting reimbursement by committee of penalty paid by candidate for violations A committee described in paragraph (1) may not make any payment to reimburse the candidate or individual involved for any penalty imposed for a violation of this subsection which is required to be paid by the candidate or individual under section 309(e). .\n#### 4. Effective date\nThe amendments made by this Act shall apply with respect to compensation and payments made on or after the date of enactment of this Act.",
      "versionDate": "2026-01-30",
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
        "updateDate": "2026-02-03T21:33:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-30",
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
          "measure-id": "id119hr7304",
          "measure-number": "7304",
          "measure-type": "hr",
          "orig-publish-date": "2026-01-30",
          "originChamber": "HOUSE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7304v00",
            "update-date": "2026-04-10"
          },
          "action-date": "2026-01-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Oversight for Members And Relatives Act or the OMAR Act</b></p> <p>This bill prohibits the use of campaign funds to compensate the spouse of a candidate or an individual holding federal office. It also requires disclosure of payments made to spouses or immediate family members.</p> <p>Specifically, the bill prohibits an authorized committee of a candidate or any other political committee that is established, maintained, or controlled by a candidate or an individual holding federal office from directly or indirectly compensating the spouse of the candidate or individual for services provided to or on behalf of the committee. The prohibition does not apply to a political committee of a political party.</p> <p>Next, the bill requires a political committee to report on disbursements to the spouse or an immediate family member of the candidate or the individual holding federal office.</p> <p>Finally, the bill requires any penalty for a violation of the bill to be imposed on the candidate or the individual holding federal office if the candidate or individual involved knew of the violation. Further, it prohibits the committee involved from reimbursing the candidate or individual for the penalty.</p>"
        },
        "title": "OMAR Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7304.xml",
    "summary": {
      "actionDate": "2026-01-30",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Oversight for Members And Relatives Act or the OMAR Act</b></p> <p>This bill prohibits the use of campaign funds to compensate the spouse of a candidate or an individual holding federal office. It also requires disclosure of payments made to spouses or immediate family members.</p> <p>Specifically, the bill prohibits an authorized committee of a candidate or any other political committee that is established, maintained, or controlled by a candidate or an individual holding federal office from directly or indirectly compensating the spouse of the candidate or individual for services provided to or on behalf of the committee. The prohibition does not apply to a political committee of a political party.</p> <p>Next, the bill requires a political committee to report on disbursements to the spouse or an immediate family member of the candidate or the individual holding federal office.</p> <p>Finally, the bill requires any penalty for a violation of the bill to be imposed on the candidate or the individual holding federal office if the candidate or individual involved knew of the violation. Further, it prohibits the committee involved from reimbursing the candidate or individual for the penalty.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr7304"
    },
    "title": "OMAR Act"
  },
  "summaries": [
    {
      "actionDate": "2026-01-30",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Oversight for Members And Relatives Act or the OMAR Act</b></p> <p>This bill prohibits the use of campaign funds to compensate the spouse of a candidate or an individual holding federal office. It also requires disclosure of payments made to spouses or immediate family members.</p> <p>Specifically, the bill prohibits an authorized committee of a candidate or any other political committee that is established, maintained, or controlled by a candidate or an individual holding federal office from directly or indirectly compensating the spouse of the candidate or individual for services provided to or on behalf of the committee. The prohibition does not apply to a political committee of a political party.</p> <p>Next, the bill requires a political committee to report on disbursements to the spouse or an immediate family member of the candidate or the individual holding federal office.</p> <p>Finally, the bill requires any penalty for a violation of the bill to be imposed on the candidate or the individual holding federal office if the candidate or individual involved knew of the violation. Further, it prohibits the committee involved from reimbursing the candidate or individual for the penalty.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr7304"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7304ih.xml"
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
      "title": "OMAR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-31T09:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "OMAR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-31T09:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Oversight for Members And Relatives Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-31T09:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Election Campaign Act of 1971 to prohibit certain political committees from compensating the spouse of the candidate for services provided to or on behalf of the committee, to require such committees to report on payments made to the spouse and the immediate family members of the candidate, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-31T09:18:21Z"
    }
  ]
}
```
