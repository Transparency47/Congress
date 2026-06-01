# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/253?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/253
- Title: Bipartisan Restoring Faith in Government Act
- Congress: 119
- Bill type: HR
- Bill number: 253
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-12-17T09:06:32Z
- Update date including text: 2025-12-17T09:06:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/253",
    "number": "253",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Bipartisan Restoring Faith in Government Act",
    "type": "HR",
    "updateDate": "2025-12-17T09:06:32Z",
    "updateDateIncludingText": "2025-12-17T09:06:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:35:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-09T14:35:40Z",
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
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "FL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "IL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "PA"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "KY"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "CA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NY"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "NM"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MD"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "PA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "NJ"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr253ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 253\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Fitzpatrick (for himself, Ms. Ocasio-Cortez , Mr. Mills , and Mr. Krishnamoorthi ) introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 5, United States Code, to restrict trading and ownership of certain financial instruments by Members of Congress and their spouses and dependents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bipartisan Restoring Faith in Government Act .\n#### 2. Prohibition of congressional ownership of financial investments\n##### (a) In general\nChapter 131 of title 5, United States Code, is amended by adding at the end the following:\nIV Prohibition on Congressional Ownership of Financial Investments 13151. Definitions In this subchapter: (1) Covered financial instrument The term covered financial instrument means\u2014 (A) any investment in\u2014 (i) a security (as defined in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) )); (ii) a security future (as defined in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) )); or (iii) a commodity (as defined in section 1a of the Commodity Exchange Act ( 7 U.S.C. 1a )); and (B) any economic interest comparable to an interest described in subclause (I) that is acquired through synthetic means, such as the use of a derivative, including an option, warrant, or other similar means. (2) Covered individual The term covered individual means any of the following: (A) A Member of Congress. (B) The spouse of a Member of Congress. (C) The dependent of a Member of Congress. (3) Dependent The term dependent has the meaning given that term in section 13101. (4) Member of Congress The term Member of Congress has the meaning given that term in section 13101. (5) Qualified blind trust The term qualified blind trust has the meaning given that term in section 13104(f)(3). (6) Supervising ethics office The term supervising ethics office has the meaning given that term in section 13101. 13152. Limitation on owning or trading certain assets (a) Requirement (1) In general Except as provided in this section, no covered individual may own or trade a covered financial instrument. (2) Exceptions Nothing in this subchapter shall be construed to prevent a covered individual from owning or trading\u2014 (A) a widely held investment fund (as that term is described in section 13104(f)(8)) that is registered as a management company under the Investment Company Act, as amended ( 15 U.S.C. 80a\u20131 et seq. ); (B) a United States Treasury bill, note, or bond; (C) any bond issued by a State or local government; or (D) any investment under the Thrift Savings Plan. (b) Compliance (1) In general To comply with the requirement under subsection (a), a covered individual shall divest of a covered financial instrument through sale or placement in a qualified blind trust in accordance with subsection (c). (2) Assets acquired through special circumstances In the event that a covered individual acquires a covered financial instrument after the date of enactment of the Bipartisan Restoring Faith in Government Act other than by purchase, the covered individual shall have 90 days from the date on which such individual received such instrument to divest of such instrument through any means provided under paragraph (1). (c) Time period for compliance (1) Covered individuals as of date of enactment (A) In general An individual who is a covered individual as of the date of enactment of Bipartisan Restoring Faith in Government Act shall have 90 days following the date of enactment of such Act to divest of such instrument through any means provided under subsection (b)(1). (B) Special rule for spouses A covered individual who is a spouse of a Member of Congress and who receives any financial instrument as compensation for their primary employment shall divest of such financial instrument not later than 90 days after the date that the spouse is contractually permitted to sell the covered investment. (2) Covered individuals after date of enactment An individual who becomes a covered individual after the date of enactment of the Bipartisan Restoring Faith in Government Act shall have 90 days from the date on which such individual becomes a covered individual to divest of such instrument through any means provided under subsection (b)(1). (3) Qualified blind trust requirements Notwithstanding paragraphs (1) and (2), a qualified blind trust may not be established for purposes of complying with this subchapter without the prior approval of the supervising ethics office. With respect to any such trust so approved, the applicable trustee\u2014 (A) shall divest of any such instrument placed in the trust not later than 6 months after the trust is established; (B) shall certify to the applicable supervising ethics office on an annual basis that the trustee has not provided any information on the trust\u2019s assets or transactions to the applicable covered individual; and (C) may not have a close personal or business relationship with the applicable covered individual. (d) Income tax A loss from a transaction or holding involving a covered financial instrument that is conducted in violation of this section may not be deducted from the amount of income tax owed by the covered individual. (e) Assets upon separation In the case of a spouse or dependent who ceases to be a covered individual, such spouse or dependent may regain control over any covered financial instrument that was placed into a qualified blind trust pursuant to subsection (a). (f) Proof of compliance (1) Submission A Member of Congress shall submit to the supervising ethics office a pledge of compliance with the requirements of this subchapter, and shall produce, upon request of the supervising ethics office, material or information determined by the supervising ethics committee to be necessary to indicate compliance with the provisions of this subchapter. (2) Certificate The supervising ethics office shall provide each Member of Congress in compliance with the provisions of this Act with a certificate of compliance. (3) Publication The supervising ethics office shall make available, on a publicly accessible website, all certificates issued under this subsection. 13153. Enforcement (a) Referral The supervising ethics office shall refer to the Attorney General the name of any covered individual who such office has reasonable cause to believe has willfully failed to comply with the requirements of section 13152. (b) Penalty (1) In general The Attorney General may bring a civil action in any appropriate United States district court against any covered individual who knowingly and willfully fails to comply with section 13152. The court in which such action is brought may assess against such individual a civil penalty in any amount, not to exceed $50,000. (2) Limitation A covered individual may not pay any penalty resulting from a civil action under paragraph (1) using\u2014 (A) funds from a Members\u2019 Representational Allowance or Senators\u2019 Official Personnel and Office Expense Account (as the case may be); or (B) funds of any political committee under the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101 et seq. ). .\n##### (b) Application of tax rules for sales of property To comply with conflict-of-Interest requirements\nSection 1043 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(d) Application to prohibition on Congressional ownership of certain assets (1) Treatment as conflict of interest statute For purposes of subsection (b)(2)(A), subchapter IV of chapter 131 of title 5, United States Code, shall be treated as a Federal conflict of interest statute. (2) Covered individuals treated as eligible persons For purposes of this section\u2014 (A) the term eligible person shall include covered individuals (as defined in section 13151 of title 5, United States Code), and (B) such covered individuals shall be treated as referred to in subsection (b)(1)(A) for purposes of applying subsection (b)(5)(A). (3) Certificates of divestiture issued by ethics committee In the case of any covered individual referred to in paragraph (2)(A), a certificate of divestiture meets the requirement of subsection (b)(2)(B) if such certificate is issued by the applicable Congressional ethics committee. .\n##### (c) Clerical amendment\nThe table of sections for such chapter is amended by inserting after the item relating to section 13146 the following:\nSUBCHAPTER IV\u2014PROHIBITION ON CONGRESSIONAL OWNERSHIP OF FINANCIAL INVESTMENTS 13151. Definitions. 13152. Limitation on owning or trading certain assets. 13153. Enforcement. .",
      "versionDate": "2025-01-09",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Family relationships",
            "updateDate": "2025-02-28T15:28:25Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-02-28T15:28:32Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-02-28T15:28:42Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-28T15:28:51Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-02-28T15:28:19Z"
          },
          {
            "name": "Securities",
            "updateDate": "2025-02-28T15:28:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-15T14:30:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr253",
          "measure-number": "253",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-05-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr253v00",
            "update-date": "2025-05-15"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Bipartisan Restoring Faith in Government Act</b></p> <p>This bill prohibits Members of Congress (and their spouses and dependents) from purchasing or selling certain investments, such as individual stocks and related financial instruments that are not diversified investment funds, U.S. Treasury securities, or other specified holdings.</p> <p>Members must divest prohibited investments within 90 days by selling them or placing them in a qualified blind trust. The bill also restricts communications between trustees and beneficiaries related to investments held in qualified blind trusts.</p> <p>Members must certify their compliance with the supervising ethics office, which must make the certificates publicly available online.</p> <p>Violations are subject to specified civil penalties. Additionally, losses stemming from a transaction involving a prohibited investment that violates the provisions of the bill may not be deducted from income taxes.</p>"
        },
        "title": "Bipartisan Restoring Faith in Government Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr253.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Bipartisan Restoring Faith in Government Act</b></p> <p>This bill prohibits Members of Congress (and their spouses and dependents) from purchasing or selling certain investments, such as individual stocks and related financial instruments that are not diversified investment funds, U.S. Treasury securities, or other specified holdings.</p> <p>Members must divest prohibited investments within 90 days by selling them or placing them in a qualified blind trust. The bill also restricts communications between trustees and beneficiaries related to investments held in qualified blind trusts.</p> <p>Members must certify their compliance with the supervising ethics office, which must make the certificates publicly available online.</p> <p>Violations are subject to specified civil penalties. Additionally, losses stemming from a transaction involving a prohibited investment that violates the provisions of the bill may not be deducted from income taxes.</p>",
      "updateDate": "2025-05-15",
      "versionCode": "id119hr253"
    },
    "title": "Bipartisan Restoring Faith in Government Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Bipartisan Restoring Faith in Government Act</b></p> <p>This bill prohibits Members of Congress (and their spouses and dependents) from purchasing or selling certain investments, such as individual stocks and related financial instruments that are not diversified investment funds, U.S. Treasury securities, or other specified holdings.</p> <p>Members must divest prohibited investments within 90 days by selling them or placing them in a qualified blind trust. The bill also restricts communications between trustees and beneficiaries related to investments held in qualified blind trusts.</p> <p>Members must certify their compliance with the supervising ethics office, which must make the certificates publicly available online.</p> <p>Violations are subject to specified civil penalties. Additionally, losses stemming from a transaction involving a prohibited investment that violates the provisions of the bill may not be deducted from income taxes.</p>",
      "updateDate": "2025-05-15",
      "versionCode": "id119hr253"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr253ih.xml"
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
      "title": "Bipartisan Restoring Faith in Government Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T01:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bipartisan Restoring Faith in Government Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T01:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to restrict trading and ownership of certain financial instruments by Members of Congress and their spouses and dependents, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:03:15Z"
    }
  ]
}
```
