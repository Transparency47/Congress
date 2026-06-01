# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/535?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/535
- Title: Inaugural Fund Integrity Act
- Congress: 119
- Bill type: HR
- Bill number: 535
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-04-14T16:47:39Z
- Update date including text: 2026-04-14T16:47:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/535",
    "number": "535",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001205",
        "district": "5",
        "firstName": "Mary",
        "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
        "lastName": "Scanlon",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Inaugural Fund Integrity Act",
    "type": "HR",
    "updateDate": "2026-04-14T16:47:39Z",
    "updateDateIncludingText": "2026-04-14T16:47:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-16T14:03:05Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "GA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "VT"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MD"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IN"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "VA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr535ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 535\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Ms. Scanlon (for herself, Ms. Norton , Ms. Tlaib , Mr. Tonko , Mr. Mullin , Mr. Johnson of Georgia , Ms. Balint , Mr. Raskin , Mr. Carson , Ms. Crockett , Ms. Ocasio-Cortez , and Mr. Morelle ) introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to prohibit certain donations to Inaugural Committees, to establish limitations on donations to Inaugural Committees, to require certain reporting by Inaugural Committees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Inaugural Fund Integrity Act .\n#### 2. Limitations and disclosure of certain donations to, and disbursements by, Inaugural Committees\n##### (a) Requirements for Inaugural Committees\nTitle III of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101 et seq. ) is amended by adding at the end the following new section:\n325. Inaugural committees (a) Prohibited donations (1) In general It shall be unlawful\u2014 (A) for an Inaugural Committee\u2014 (i) to solicit, accept, or receive a donation from a person that is not an individual; or (ii) to solicit, accept, or receive a donation from a foreign national; (B) for a person\u2014 (i) to make a donation to an Inaugural Committee in the name of another person, or to knowingly authorize his or her name to be used to effect such a donation; (ii) to knowingly accept a donation to an Inaugural Committee made by a person in the name of another person; or (iii) to convert a donation to an Inaugural Committee to personal use as described in paragraph (2); and (C) for a foreign national to, directly or indirectly, make a donation, or make an express or implied promise to make a donation, to an Inaugural Committee. (2) Conversion of donation to personal use For purposes of paragraph (1)(B)(iii), a donation shall be considered to be converted to personal use if any part of the donated amount is used to fulfill a commitment, obligation, or expense of a person that would exist irrespective of the responsibilities of the Inaugural Committee under chapter 5 of title 36, United States Code. (3) No effect on disbursement of unused funds to nonprofit organizations Nothing in this subsection may be construed to prohibit an Inaugural Committee from disbursing unused funds to an organization which is described in section 501(c)(3) of the Internal Revenue Code of 1986 and is exempt from taxation under section 501(a) of such Code. (b) Limitation on donations (1) In general It shall be unlawful for an individual to make donations to an Inaugural Committee which, in the aggregate, exceed $50,000. (2) Indexing At the beginning of each Presidential election year (beginning with 2032), the amount described in paragraph (1) shall be increased by the cumulative percent difference determined in section 315(c)(1)(A) since the previous Presidential election year. If any amount after such increase is not a multiple of $1,000, such amount shall be rounded to the nearest multiple of $1,000. (c) Disclosure of certain donations and disbursements (1) Donations over $1,000 (A) In general An Inaugural Committee shall file with the Commission a report disclosing any donation by an individual to the committee in an amount of $1,000 or more not later than 24 hours after the receipt of such donation. (B) Contents of report A report filed under subparagraph (A) shall contain\u2014 (i) the amount of the donation; (ii) the date the donation is received; and (iii) the name and address of the individual making the donation. (2) Final report Not later than the date that is 90 days after the date of the Presidential inaugural ceremony, the Inaugural Committee shall file with the Commission a report containing the following information: (A) For each donation of money or anything of value made to the committee in an aggregate amount equal to or greater than $200\u2014 (i) the amount of the donation; (ii) the date the donation is received; and (iii) the name and address of the individual making the donation. (B) The total amount of all disbursements, and all disbursements in the following categories: (i) Disbursements made to meet committee operating expenses. (ii) Repayment of all loans. (iii) Donation refunds and other offsets to donations. (iv) Any other disbursements. (C) The name and address of each person\u2014 (i) to whom a disbursement in an aggregate amount or value in excess of $200 is made by the committee to meet a committee operating expense, together with date, amount, and purpose of such operating expense; (ii) who receives a loan repayment from the committee, together with the date and amount of such loan repayment; (iii) who receives a donation refund or other offset to donations from the committee, together with the date and amount of such disbursement; and (iv) to whom any other disbursement in an aggregate amount or value in excess of $200 is made by the committee, together with the date and amount of such disbursement. (d) Definitions For purposes of this section: (1) (A) The term donation includes\u2014 (i) any gift, subscription, loan, advance, or deposit of money or anything of value made by any person to the committee; or (ii) the payment by any person of compensation for the personal services of another person which are rendered to the committee without charge for any purpose. (B) The term donation does not include the value of services provided without compensation by any individual who volunteers on behalf of the committee. (2) The term foreign national has the meaning given that term by section 319(b). (3) The term Inaugural Committee has the meaning given that term by section 501 of title 36, United States Code. .\n##### (b) Confirming amendment related to reporting requirements\nSection 304 of the Federal Election Campaign Act ( 52 U.S.C. 30104 ) is amended\u2014\n**(1)**\nby striking subsection (h); and\n**(2)**\nby redesignating subsection (i) as subsection (h).\n##### (c) Conforming amendment related to status of committee\nSection 510 of title 36, United States Code, is amended to read as follows:\n510. Disclosure of and prohibition on certain donations A committee shall not be considered to be the Inaugural Committee for purposes of this chapter unless the committee agrees to, and meets, the requirements of section 325 of the Federal Election Campaign Act of 1971. .\n##### (d) Effective date\nThe amendments made by this Act shall apply with respect to Inaugural Committees established under chapter 5 of title 36, United States Code, for inaugurations held in 2029 and any succeeding year.",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-09-17",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "2838",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Our Democracy Act",
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
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-02-19T21:27:51Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-02-19T21:27:51Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-19T21:27:51Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-02-19T21:27:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-15T14:35:01Z"
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
          "measure-id": "id119hr535",
          "measure-number": "535",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr535v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Inaugural Fund Integrity Act</strong></p><p>This bill limits donations to inaugural committees and requires these committees to disclose donations and disbursements.</p><p>Specifically, inaugural committees may not solicit, accept, or receive donations from corporations or foreign nationals. An individual may not make a donation in the name of another individual or authorize his or her name to be used to make such a donation. In addition, foreign nationals may not make donations or make promises to make donations to inaugural committees.</p><p>Further, the bill caps the amount an individual may donate to an inaugural committee.</p><p>Donations to inaugural committees may not be converted to personal use.</p><p>Finally, inaugural committees must report certain information on donations and disbursements to the Federal Election Commission.</p>"
        },
        "title": "Inaugural Fund Integrity Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr535.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Inaugural Fund Integrity Act</strong></p><p>This bill limits donations to inaugural committees and requires these committees to disclose donations and disbursements.</p><p>Specifically, inaugural committees may not solicit, accept, or receive donations from corporations or foreign nationals. An individual may not make a donation in the name of another individual or authorize his or her name to be used to make such a donation. In addition, foreign nationals may not make donations or make promises to make donations to inaugural committees.</p><p>Further, the bill caps the amount an individual may donate to an inaugural committee.</p><p>Donations to inaugural committees may not be converted to personal use.</p><p>Finally, inaugural committees must report certain information on donations and disbursements to the Federal Election Commission.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr535"
    },
    "title": "Inaugural Fund Integrity Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Inaugural Fund Integrity Act</strong></p><p>This bill limits donations to inaugural committees and requires these committees to disclose donations and disbursements.</p><p>Specifically, inaugural committees may not solicit, accept, or receive donations from corporations or foreign nationals. An individual may not make a donation in the name of another individual or authorize his or her name to be used to make such a donation. In addition, foreign nationals may not make donations or make promises to make donations to inaugural committees.</p><p>Further, the bill caps the amount an individual may donate to an inaugural committee.</p><p>Donations to inaugural committees may not be converted to personal use.</p><p>Finally, inaugural committees must report certain information on donations and disbursements to the Federal Election Commission.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr535"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr535ih.xml"
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
      "title": "Inaugural Fund Integrity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Inaugural Fund Integrity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Election Campaign Act of 1971 to prohibit certain donations to Inaugural Committees, to establish limitations on donations to Inaugural Committees, to require certain reporting by Inaugural Committees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T09:18:29Z"
    }
  ]
}
```
