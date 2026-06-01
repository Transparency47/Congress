# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/534?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/534
- Title: Presidential Allowance Modernization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 534
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2026-01-17T01:29:24Z
- Update date including text: 2026-01-17T01:29:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/534",
    "number": "534",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Presidential Allowance Modernization Act of 2025",
    "type": "S",
    "updateDate": "2026-01-17T01:29:24Z",
    "updateDateIncludingText": "2026-01-17T01:29:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T17:32:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s534is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 534\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Ms. Ernst introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend the Act of August 25, 1958, commonly known as the Former Presidents Act of 1958 , with respect to the monetary allowance payable to a former President, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Presidential Allowance Modernization Act of 2025 .\n#### 2. Amendments\n##### (a) Former Presidents\nThe first section of the Act entitled An Act to provide retirement, clerical assistants, and free mailing privileges to former Presidents of the United States, and for other purposes , approved August 25, 1958 (commonly known, and referred to in this Act, as the Former Presidents Act of 1958 ) ( 3 U.S.C. 102 note), is amended by striking the matter preceding subsection (e) and inserting the following:\n(a) Annuities and allowances (1) Annuity Each former President shall be entitled for the remainder of his or her life to receive from the United States an annuity at the rate of $200,000 per year, subject to subsections (b)(2) and (c), to be paid by the Secretary of the Treasury. (2) Allowance The Administrator of General Services is authorized to provide each former President a monetary allowance at the rate of $200,000 per year, subject to the availability of appropriations and subsections (b)(2), (c), and (d). (b) Duration; frequency (1) In general The annuity and allowance under subsection (a) shall each\u2014 (A) commence on the day after the date on which an individual becomes a former President; (B) terminate on the date on which the former President dies; and (C) be payable on a monthly basis. (2) Appointive or elective positions The annuity and allowance under subsection (a) shall not be payable for any period during which a former President holds an appointive or elective position in or under the Federal Government to which is attached a rate of pay other than a nominal rate. (c) Cost-of-Living increases Effective December 1 of each year, each annuity and allowance under subsection (a) that commenced before that date shall be increased by the same percentage by which benefit amounts under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ) are increased, effective as of that date, as a result of a determination under section 215(i) of that Act ( 42 U.S.C. 415(i) ). (d) Limitation on monetary allowance (1) In general Notwithstanding any other provision of this section, the monetary allowance payable under subsection (a)(2) to a former President for any 12-month period\u2014 (A) except as provided in subparagraph (B), may not exceed the amount by which\u2014 (i) the monetary allowance that (but for this subsection) would otherwise be so payable for such 12-month period, exceeds (if at all) (ii) the applicable reduction amount for such 12-month period; and (B) shall not be less than the amount determined under paragraph (4). (2) Definition (A) In general For purposes of paragraph (1), the term applicable reduction amount means, with respect to any former President and in connection with any 12-month period, the amount by which\u2014 (i) the sum of\u2014 (I) the adjusted gross income (as defined in section 62 of the Internal Revenue Code of 1986) of the former President for the most recent taxable year for which a tax return is available; and (II) any interest excluded from the gross income of the former President under section 103 of such Code for such taxable year, exceeds (if at all) (ii) $400,000, subject to subparagraph (C). (B) Joint returns In the case of a joint return, subclauses (I) and (II) of subparagraph (A)(i) shall be applied by taking into account both the amounts properly allocable to the former President and the amounts properly allocable to the spouse of the former President. (C) Cost-of-living increases The dollar amount specified in subparagraph (A)(ii) shall be adjusted at the same time that, and by the same percentage by which, the monetary allowance of the former President is increased under subsection (c) (disregarding this subsection). (3) Disclosure requirement (A) Definitions In this paragraph\u2014 (i) the terms return and return information have the meanings given those terms in section 6103(b) of the Internal Revenue Code of 1986; and (ii) the term Secretary means the Secretary of the Treasury or the Secretary of the Treasury\u2019s delegate. (B) Requirement A former President may not receive a monetary allowance under subsection (a)(2) unless the former President discloses to the Secretary, upon the request of the Secretary, any return or return information of the former President or spouse of the former President that the Secretary determines is necessary for purposes of calculating the applicable reduction amount under paragraph (2) of this subsection. (C) Confidentiality Except as provided in section 6103 of the Internal Revenue Code of 1986 and notwithstanding any other provision of law, the Secretary may not, with respect to a return or return information disclosed to the Secretary under subparagraph (B)\u2014 (i) disclose the return or return information to any entity or person; or (ii) use the return or return information for any purpose other than to calculate the applicable reduction amount under paragraph (2). (4) Increased costs due to security needs With respect to the monetary allowance that would be payable to a former President under subsection (a)(2) for any 12-month period but for the limitation under paragraph (1) of this subsection, the Administrator of General Services, in coordination with the Director of the United States Secret Service, shall determine the amount of the allowance that is needed to pay the increased cost of doing business that is attributable to the security needs of the former President. .\n##### (b) Surviving spouses of former Presidents\n**(1) Increase in amount of monetary allowance**\nSubsection (e) of the first section of the Former Presidents Act of 1958 is amended\u2014\n**(A)**\nin the first sentence, by striking $20,000 per annum, and inserting $100,000 per year (subject to paragraph (4)), ; and\n**(B)**\nin the second sentence\u2014\n**(i)**\nin paragraph (2)(B), by striking and at the end;\n**(ii)**\nin paragraph (3)\u2014\n**(I)**\nby striking or the government of the District of Columbia ; and\n**(II)**\nby striking the period and inserting ; and ; and\n**(iii)**\nby inserting after paragraph (3) the following:\n(4) shall, after its commencement date, be increased at the same time that, and by the same percentage by which, annuities of former Presidents are increased under subsection (c). .\n**(2) Coverage of widower of a former President**\nSubsection (e) of the first section of the Former Presidents Act of 1958, as amended by paragraph (1), is amended\u2014\n**(A)**\nby striking widow each place that term appears and inserting widow or widower ; and\n**(B)**\nby striking she and inserting she or he .\n##### (c) Subsection headings\nThe first section of the Former Presidents Act of 1958 is amended\u2014\n**(1)**\nin subsection (e), by inserting after the subsection enumerator the following: Widows and widowers .\u2014 ;\n**(2)**\nin subsection (f), by inserting after the subsection enumerator the following: Definition .\u2014 ; and\n**(3)**\nin subsection (g), by inserting after the subsection enumerator the following: Authorization of appropriations .\u2014 .\n#### 3. Rule of construction\nNothing in this Act or an amendment made by this Act shall be construed to affect\u2014\n**(1)**\nany provision of law relating to the security or protection of a former President or a member of the family of a former President; or\n**(2)**\nfunding, under the Former Presidents Act of 1958 or any other law, to carry out any provision of law described in paragraph (1).\n#### 4. Applicability\nThis Act and the amendments made by this Act shall not apply to\u2014\n**(1)**\nany individual who is a former President on the date of enactment of this Act; or\n**(2)**\nthe widow or widower of an individual described in paragraph (1).",
      "versionDate": "2025-02-12",
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
            "name": "Family relationships",
            "updateDate": "2025-07-03T14:00:50Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-07-03T14:00:40Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-07-03T14:00:44Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-07-03T14:00:31Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2025-07-03T14:00:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-12T14:31:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119s534",
          "measure-number": "534",
          "measure-type": "s",
          "orig-publish-date": "2025-02-12",
          "originChamber": "SENATE",
          "update-date": "2026-01-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s534v00",
            "update-date": "2026-01-17"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Presidential Allowance Modernization Act of 2025</strong></p><p>This bill changes the compensation provided to future former Presidents and increases the compensation for the widow or widower of a future former President.</p><p>Currently, former Presidents receive an allowance equivalent to the annual rate of basic pay of the head of an executive department ($250,600 in 2025), as well as government-provided\u00a0office space and office staff.</p><p>Under the bill, individuals who become former Presidents after enactment\u00a0shall annually receive from the United States an annuity of $200,000 and a monetary allowance of $200,000.\u00a0The allowance shall be reduced by the amount the former President's adjusted gross\u00a0income and interest on certain tax-exempt bonds exceeds $400,000\u00a0(although the reduction may be decreased to account for certain security-related expenditures). Both the annuity and allowance shall receive annual cost-of-living increases. The annuity and allowance shall not be payable for any period during which the former President holds a federal government position with a rate of pay other than a nominal rate.\u00a0</p><p>Other changes made by the\u00a0bill include (1) removing a statutory provision specifying that former Presidents receive government-provided office space and office staff,\u00a0and (2) increasing from $20,000 to $100,000 the annual allowance for surviving spouses of individuals who become former Presidents after enactment and providing annual cost-of-living increases for such allowance.</p>"
        },
        "title": "Presidential Allowance Modernization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s534.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Presidential Allowance Modernization Act of 2025</strong></p><p>This bill changes the compensation provided to future former Presidents and increases the compensation for the widow or widower of a future former President.</p><p>Currently, former Presidents receive an allowance equivalent to the annual rate of basic pay of the head of an executive department ($250,600 in 2025), as well as government-provided\u00a0office space and office staff.</p><p>Under the bill, individuals who become former Presidents after enactment\u00a0shall annually receive from the United States an annuity of $200,000 and a monetary allowance of $200,000.\u00a0The allowance shall be reduced by the amount the former President's adjusted gross\u00a0income and interest on certain tax-exempt bonds exceeds $400,000\u00a0(although the reduction may be decreased to account for certain security-related expenditures). Both the annuity and allowance shall receive annual cost-of-living increases. The annuity and allowance shall not be payable for any period during which the former President holds a federal government position with a rate of pay other than a nominal rate.\u00a0</p><p>Other changes made by the\u00a0bill include (1) removing a statutory provision specifying that former Presidents receive government-provided office space and office staff,\u00a0and (2) increasing from $20,000 to $100,000 the annual allowance for surviving spouses of individuals who become former Presidents after enactment and providing annual cost-of-living increases for such allowance.</p>",
      "updateDate": "2026-01-17",
      "versionCode": "id119s534"
    },
    "title": "Presidential Allowance Modernization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Presidential Allowance Modernization Act of 2025</strong></p><p>This bill changes the compensation provided to future former Presidents and increases the compensation for the widow or widower of a future former President.</p><p>Currently, former Presidents receive an allowance equivalent to the annual rate of basic pay of the head of an executive department ($250,600 in 2025), as well as government-provided\u00a0office space and office staff.</p><p>Under the bill, individuals who become former Presidents after enactment\u00a0shall annually receive from the United States an annuity of $200,000 and a monetary allowance of $200,000.\u00a0The allowance shall be reduced by the amount the former President's adjusted gross\u00a0income and interest on certain tax-exempt bonds exceeds $400,000\u00a0(although the reduction may be decreased to account for certain security-related expenditures). Both the annuity and allowance shall receive annual cost-of-living increases. The annuity and allowance shall not be payable for any period during which the former President holds a federal government position with a rate of pay other than a nominal rate.\u00a0</p><p>Other changes made by the\u00a0bill include (1) removing a statutory provision specifying that former Presidents receive government-provided office space and office staff,\u00a0and (2) increasing from $20,000 to $100,000 the annual allowance for surviving spouses of individuals who become former Presidents after enactment and providing annual cost-of-living increases for such allowance.</p>",
      "updateDate": "2026-01-17",
      "versionCode": "id119s534"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s534is.xml"
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
      "title": "Presidential Allowance Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-07T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Presidential Allowance Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Act of August 25, 1958, commonly known as the \"Former Presidents Act of 1958\", with respect to the monetary allowance payable to a former President, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T04:18:22Z"
    }
  ]
}
```
