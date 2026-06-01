# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2069?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2069
- Title: Stop Secret Spending Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2069
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2026-05-26T18:20:23Z
- Update date including text: 2026-05-26T18:20:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-03-18 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-03-18 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2069",
    "number": "2069",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001212",
        "district": "1",
        "firstName": "Barry",
        "fullName": "Rep. Moore, Barry [R-AL-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Stop Secret Spending Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-26T18:20:23Z",
    "updateDateIncludingText": "2026-05-26T18:20:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
        "item": [
          {
            "date": "2026-03-18T13:00:39Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-11T14:00:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NH"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2069ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2069\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Moore of Alabama (for himself, Mr. Panetta , and Ms. Goodlander ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend the Federal Funding Accountability and Transparency Act of 2006 to ensure that other transaction agreements are reported to USAspending.gov, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Secret Spending Act of 2025 .\n#### 2. Other transaction agreement reporting\n##### (a) Other transaction agreements\nSection 2(a) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended\u2014\n**(1)**\nin paragraph (4)(A)\u2014\n**(A)**\nin clause (ii), by adding and and the end; and\n**(B)**\nby adding at the end the following:\n(iii) includes other transaction agreements; ; and\n**(2)**\nin paragraph (7)\u2014\n**(A)**\nin subparagraph (B), by striking (2)(A)(i) and inserting (4)(A)(i) ; and\n**(B)**\nin subparagraph (C), by striking (2)(A)(ii) and inserting (4)(A)(ii) .\n##### (b) Data standards\nSection 4 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended by adding at the end the following:\n(e) Other transaction agreement data Not later than 3 years after the date of enactment of the Stop Secret Spending Act of 2025 , the Secretary shall ensure that, with respect to the website established under section 2, or any successor website\u2014 (1) data relating to other transaction agreements is automatically transmitted to the website, and (2) a centralized view of the data described in paragraph (1) is available on the website. .\n##### (c) Annual report on unreported funding\nSection 2 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended by adding at the end the following:\n(h) Annual report Not later than 1 year after the date of enactment of the Stop Secret Spending Act of 2025 , and annually thereafter, the Secretary, in consultation with the Director, shall post to the website established under this section a report that includes\u2014 (1) the total amount of Federal spending on Federal awards for which data has not been posted to the website; and (2) the reason data on the Federal spending described in paragraph (1) has not been posted to the website, including whether the Federal spending was\u2014 (A) national security-related or classified; (B) a grant or contract awarded or entered into by a legislative or judicial branch agency; or (C) a subaward below a primary subaward. .\n##### (d) Implementation plan\n**(1) Definitions**\nIn this subsection:\n**(A) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(B) Relevant agency**\nThe term relevant agency means a Federal agency (as defined in section 2(a) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note)) that has the authority to enter into an other transaction agreement, as determined by the Director.\n**(C) Secretary**\nThe term Secretary means the Secretary of the Treasury.\n**(D) USAspending.gov**\nThe term USAspending.gov means the website established under section 2 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note).\n**(2) Initial compilation**\nIf the Secretary has not yet complied with subsection (e) of section 4 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note), as added by this section, by the date that is 1 year after the date of enactment of this Act, not later than 1 year after the date of enactment of this Act, the Secretary, in coordination with the Director and the heads of relevant agencies, shall publish on USAspending.gov a report that lists and includes a detailed description of all other transaction agreements entered into by the relevant agencies for the fiscal year preceding the fiscal year during which the report is published.\n**(3) Plan**\nIf the Secretary has not yet complied with subsection (e) of section 4 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note), as added by this section, by the date that is 2 years after the date of enactment of this Act, not later than 2 years after the date of enactment of this Act, the Secretary, in consultation with the Director and the heads of relevant agencies, shall submit to Congress a plan that includes\u2014\n**(A)**\nthe status of including data relating to other transaction agreements on USAspending.gov; and\n**(B)**\nactions underway and planned to ensure that the data described in subparagraph (A) is fully incorporated into USAspending.gov by the date that is 3 years after the date of enactment of this Act.\n#### 3. Other amendments\n##### (a) Inspector General reports\nSection 6(a) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking each Federal agency and inserting each agency described in paragraphs (1) and (2) of section 901(b) of title 31, United States Code ;\n**(B)**\nin subparagraph (A), by striking Federal agency and inserting agency ; and\n**(C)**\nin subparagraph (B), by striking Federal agency and inserting agency ; and\n**(2)**\nby striking paragraph (2) and inserting the following:\n(2) Deadlines The inspector general of each agency described in paragraphs (1) and (2) of section 901(b) of title 31, United States Code, shall submit to Congress and make publicly available a report described in paragraph (1)(B)\u2014 (A) not later than 1 year after the date of enactment of the Stop Secret Spending Act of 2025 ; and (B) not less than frequently than once every 2 years after the date described in subparagraph (A) until the date that is 10 years after the date of enactment of the Stop Secret Spending Act of 2025 on the date of submission of the report required under section 3521(f) or 9105(a)(3) of title 31, United States Code, for the applicable fiscal year. .\n##### (b) Full disclosure of Federal funds\n**(1) In general**\nSection 3 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nparagraph (1), in the matter preceding subparagraph (A), by striking a Federal agency or component of a Federal agency and inserting a Federal agency or a component of a Federal agency included on the list posted under subsection (e)(2) ; and\n**(ii)**\nin paragraph (2)(B), in the matter preceding clause (i), by striking to be posted and inserting to be posted by a Federal agency or a component of a Federal agency included on the list posted under subsection (e)(2) ; and\n**(B)**\nby adding at the end the following:\n(c) Quality of information (1) In general The Secretary and the Director, in consultation with the heads of Federal agencies, shall establish requirements to ensure that the information to be posted under subsection (b) that is posted by a Federal agency or component of a Federal agency is complete and accurate. (2) Federal agency responsibility The head of each Federal agency or component of a Federal agency posting data under subsection (b) shall ensure that the data is complete and accurate. (3) Authority to verify accuracy The Secretary and the Director may verify that the data posted under subsection (b) by a Federal agency or component of a Federal agency are complete, accurate, and consistent. (d) Display standards The Secretary, in consultation with the Director, shall ensure that the heads of Federal agencies that post information under subsection (b) comply with display standards established by the Secretary. (e) Agency reporting determination Not later than 1 year after the date of enactment of the Stop Secret Spending Act of 2025 , and not less frequently than once every 2 years thereafter, the Secretary, in coordination with the Director, shall\u2014 (1) assess and make a determination with respect to which Federal agencies and components of Federal agencies are required to post information under subsection (b); (2) publish a list of the Federal agencies and components of Federal agencies determined under paragraph (1) on the website established under section 2(b)(1); and (3) provide to the head and inspector general of each Federal agency or component of a Federal agency included on the list published under paragraph (2) written notice of the inclusion of the Federal agency or component of a Federal agency on the list. .\n**(2) Effective date**\nThe amendments made by paragraph (1)(A) shall take effect on the date on which the Secretary publishes the first list under section 3(e)(2) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note), as added by paragraph (1).\n#### 4. GAO report\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall make recommendations for any updates the Comptroller General of the United States determines advisable to clause 52.204.10 of the Federal Acquisition Regulation with respect to incorporating requirements under the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note).",
      "versionDate": "2025-03-11",
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
        "actionDate": "2026-03-18",
        "text": "Committee on Small Business and Entrepreneurship. Hearings held."
      },
      "number": "872",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Stop Secret Spending Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Budget deficits and national debt",
            "updateDate": "2025-08-07T17:51:57Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-07T17:51:57Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-08-07T17:51:57Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-08-07T17:51:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-20T15:14:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119hr2069",
          "measure-number": "2069",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-11",
          "originChamber": "HOUSE",
          "update-date": "2026-03-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2069v00",
            "update-date": "2026-03-02"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stop Secret Spending Act of 2025</strong></p><p>This bill expands a requirement for federal agencies to report expenditures on the USAspending.gov website to include <em>other transaction agreement </em>expenditures. (Other transaction agreements, or OTAs, are contractual instruments other than standard procurement contracts, grants, or cooperative agreements; they are exempt from many federal procurement laws and regulations).</p><p>Under current law, federal agencies must report expenditures on federal awards to USAspending.gov with the term <em>federal award</em> defined as federal grants, loans, cooperative agreements, contracts, and certain other types of expenditures. This bill expands the definition of federal award to include expenditures under OTAs, and therefore such expenditures must be included on the USAspending.gov website.</p><p>The Department of the Treasury must ensure that data relating to OTAs are automatically transmitted to the website and a centralized view of this data is available on the website.\u00a0Treasury must also annually post on the\u00a0USAspending.gov website a report that includes (1) the total amount of federal spending on federal awards for which data has not been posted on the website, and (2) the reason why such spending data was not posted.</p><p>For 10 years after enactment, the Office of Inspector General of specified federal agencies must periodically submit to Congress and make publicly available a report assessing the agency's spending data and use of data standards.</p>"
        },
        "title": "Stop Secret Spending Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2069.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Secret Spending Act of 2025</strong></p><p>This bill expands a requirement for federal agencies to report expenditures on the USAspending.gov website to include <em>other transaction agreement </em>expenditures. (Other transaction agreements, or OTAs, are contractual instruments other than standard procurement contracts, grants, or cooperative agreements; they are exempt from many federal procurement laws and regulations).</p><p>Under current law, federal agencies must report expenditures on federal awards to USAspending.gov with the term <em>federal award</em> defined as federal grants, loans, cooperative agreements, contracts, and certain other types of expenditures. This bill expands the definition of federal award to include expenditures under OTAs, and therefore such expenditures must be included on the USAspending.gov website.</p><p>The Department of the Treasury must ensure that data relating to OTAs are automatically transmitted to the website and a centralized view of this data is available on the website.\u00a0Treasury must also annually post on the\u00a0USAspending.gov website a report that includes (1) the total amount of federal spending on federal awards for which data has not been posted on the website, and (2) the reason why such spending data was not posted.</p><p>For 10 years after enactment, the Office of Inspector General of specified federal agencies must periodically submit to Congress and make publicly available a report assessing the agency's spending data and use of data standards.</p>",
      "updateDate": "2026-03-02",
      "versionCode": "id119hr2069"
    },
    "title": "Stop Secret Spending Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Secret Spending Act of 2025</strong></p><p>This bill expands a requirement for federal agencies to report expenditures on the USAspending.gov website to include <em>other transaction agreement </em>expenditures. (Other transaction agreements, or OTAs, are contractual instruments other than standard procurement contracts, grants, or cooperative agreements; they are exempt from many federal procurement laws and regulations).</p><p>Under current law, federal agencies must report expenditures on federal awards to USAspending.gov with the term <em>federal award</em> defined as federal grants, loans, cooperative agreements, contracts, and certain other types of expenditures. This bill expands the definition of federal award to include expenditures under OTAs, and therefore such expenditures must be included on the USAspending.gov website.</p><p>The Department of the Treasury must ensure that data relating to OTAs are automatically transmitted to the website and a centralized view of this data is available on the website.\u00a0Treasury must also annually post on the\u00a0USAspending.gov website a report that includes (1) the total amount of federal spending on federal awards for which data has not been posted on the website, and (2) the reason why such spending data was not posted.</p><p>For 10 years after enactment, the Office of Inspector General of specified federal agencies must periodically submit to Congress and make publicly available a report assessing the agency's spending data and use of data standards.</p>",
      "updateDate": "2026-03-02",
      "versionCode": "id119hr2069"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2069ih.xml"
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
      "title": "Stop Secret Spending Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Secret Spending Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Funding Accountability and Transparency Act of 2006 to ensure that other transaction agreements are reported to USAspending.gov, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:48Z"
    }
  ]
}
```
