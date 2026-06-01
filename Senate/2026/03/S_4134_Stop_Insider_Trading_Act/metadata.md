# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4134?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4134
- Title: Stop Insider Trading Act
- Congress: 119
- Bill type: S
- Bill number: 4134
- Origin chamber: Senate
- Introduced date: 2026-03-18
- Update date: 2026-04-23T12:55:36Z
- Update date including text: 2026-04-23T12:55:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-18: Introduced in Senate
- 2026-03-18 - IntroReferral: Introduced in Senate
- 2026-03-18 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-03-18: Introduced in Senate

## Actions

- 2026-03-18 - IntroReferral: Introduced in Senate
- 2026-03-18 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-18",
    "latestAction": {
      "actionDate": "2026-03-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4134",
    "number": "4134",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Stop Insider Trading Act",
    "type": "S",
    "updateDate": "2026-04-23T12:55:36Z",
    "updateDateIncludingText": "2026-04-23T12:55:36Z"
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
      "actionDate": "2026-03-18",
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
          "date": "2026-03-18T17:45:34Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "OH"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "NE"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "KS"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "LA"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "IN"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "AK"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "IA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "ND"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "TX"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "WY"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "MT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "ID"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4134is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4134\nIN THE SENATE OF THE UNITED STATES\nMarch 18, 2026 Mr. Ricketts (for himself, Mr. McCormick , Mr. Husted , Mrs. Fischer , Mr. Marshall , Mr. Cassidy , and Mr. Young ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend chapter 131 of title 5, United States Code, to require certain restrictions on stocks for Members of Congress and their spouses and dependents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Insider Trading Act .\n#### 2. Restrictions on covered investments\n##### (a) Table of contents\nThe table of contents for chapter 131 of title 5, United States Code, is amended by adding at the end the following:\nSubchapter IV\u2014Restrictions on covered investments 13151. Definitions. 13152. Restrictions on covered investments. 13153. Penalties. .\n##### (b) Restrictions\nChapter 131 of title 5, United States Code, is amended by adding at the end the following:\nIV Restrictions on covered investments 13151. Definitions In this subchapter: (1) Covered individual The term covered individual means any of the following: (A) A Member of Congress, as defined in section 13101. (B) A dependent child (as defined in section 13101) or a spouse of a Member of Congress. (2) Covered investment (A) In general The term covered investment means\u2014 (i) a security issued by a publicly traded company; or (ii) any derivative, option, warrant, swap, or other instrument that provides economic exposure to, or the value of which is determined by reference to, a security described in clause (i). (B) Exclusion The term covered investment does not include\u2014 (i) an excepted investment fund (as described in section 13104(f)(8)); (ii) any other fund that would be an excepted investment fund but for the fact that the fund does not meet the diversification requirement solely because the fund is concentrated in\u2014 (I) the United States; or (II) the State, territory, or District of residence of the covered individual who owns the fund; (iii) an interest in a small business concern, as defined in section 3 of the Small Business Act ( 15 U.S.C. 632 ); or (iv) any investment held in a trust if\u2014 (I) no covered individual has any authority, directly or indirectly, to direct, veto, or materially influence any specific investment decisions of the trust, including any right to approve, disapprove, or require particular purchases, sales, or investment strategies; and (II) the trustee of the trust is not the spouse, child, parent, or sibling of a Member of Congress. (3) Publicly traded company The term publicly traded company means an issuer that has a class of securities registered under section 12 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78l ). (4) Security The term security has the meaning given the term in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) ). (5) Supervising ethics office The term supervising ethics office has the meaning given the term in section 13101. 13152. Restrictions on covered investments (a) Conduct during Federal service Except as described in subsection (c), no covered individual may purchase a covered investment. (b) Advanced notice requirement (1) In general No covered individual may sell a covered investment, unless a notice of intent to sell the covered investment is made by the relevant Member of Congress, on behalf of the Member of Congress or the spouse or dependent child of the Member of Congress, as applicable, and publicly disclosed at least 7 calendar days, and not more than 14 calendar days, prior to the sale in accordance with the requirements of this subsection. (2) Contents of notice The notice under paragraph (1) shall include the following: (A) The projected date of sale of a covered investment. (B) A description of such sale. (C) The number of shares in such sale. (3) Withdrawal The notice under paragraph (1) shall be withdrawn by the Member of Congress who filed it, prior to the close of the expiration of the notice, if the covered individual to whom the notice applies determines not to sell the covered investment. (4) Filing A Member of Congress shall file the notice under paragraph (1) for each intended sale by the Member of Congress, or the spouse or dependent child of the Member of Congress, with\u2014 (A) the Clerk of the House of Representatives, in the case of a Representative in Congress, a Delegate to Congress, or the Resident Commissioner from Puerto Rico; or (B) the Secretary of the Senate, in the case of a Senator. (5) Publication The notice under paragraph (1) and the withdrawal under paragraph (3) shall, upon receipt, be made publicly available on a website controlled by the Clerk of the House of Representatives or the Secretary of the Senate, as applicable. (c) Exceptions (1) Occupation The requirements of subsections (a) and (b) shall not apply to a spouse or dependent child of a Member of Congress with respect to a transaction in a covered investment which is\u2014 (A) on behalf, or for the benefit, of any person other than a covered individual; or (B) made as a part of compensation from an employer of such individual or in furtherance of any fiduciary or occupational obligations of such individual. (2) Other The requirements of subsection (a) shall not apply to a covered individual with respect to a transaction in a covered investment made for the purpose of reinvesting dividends received from such covered investment. 13153. Enforcement (a) In general Any covered individual who violates the restrictions under section 13152 with respect to a covered investment, shall, at the direction of the supervising ethics office\u2014 (1) incur a fee, as calculated under subsection (b), to be paid by the Member of Congress who\u2014 (A) caused the violation; or (B) is the spouse or parent of the covered individual who caused the violation; and (2) in the case of a purchase of a covered investment, be required to sell the covered investment purchased in violation of section 13152(a). (b) Calculation of fees The fee required under subsection (a)(1) shall be equal to the sum of\u2014 (1) $2,000 or 10 percent of the value of the transaction in the covered investment that violates section 13152, whichever is greater; and (2) the net gain realized, if any, from the covered investment during the period beginning on the most recent date on which the individual became a covered individual and ending on the date of disposition of the covered investment, as determined by the supervising ethics office. (c) Payment restrictions A Member of Congress may not pay any of the fees under this section by using amounts from the following sources: (1) If the covered individual is a Senator, the Senators' Official Personnel and Office Expense Account. (2) If the covered individual is a Member of the House of Representatives, the Members\u2019 Representational Allowance. (3) Any contribution (as defined in section 301 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101 )) accepted as a candidate (as defined in that section), and any other donation received as support for activities of the covered individual as a holder of Federal office (as defined in that section). (d) Miscellaneous receipts Any amounts collected in fees authorized by this section shall be deposited in the general fund of the Treasury as miscellaneous receipts in accordance with section 3302(b) of title 31. (e) Referral Upon the assessment of a fee under this section, the supervising ethics office may refer a Member of Congress to the Attorney General in the same manner and to the same extent as a violation under section 13106 if such Member of Congress resigns or retires before paying such assessed fee. (f) Interpretative guidance Each supervising ethics office may issue interpretative guidance relating to this subchapter and, in issuing such guidance, may consider mitigating or aggravating circumstances. .\n##### (c) Effective date\nThe amendments made by this Act shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2026-03-18",
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
        "actionDate": "2026-02-03",
        "text": "Placed on the Union Calendar, Calendar No. 409."
      },
      "number": "7008",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Insider Trading Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-03-30T22:29:34Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4134is.xml"
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
      "title": "Stop Insider Trading Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T11:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Insider Trading Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T04:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend chapter 131 of title 5, United States Code, to require certain restrictions on stocks for Members of Congress and their spouses and dependents, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T04:18:38Z"
    }
  ]
}
```
