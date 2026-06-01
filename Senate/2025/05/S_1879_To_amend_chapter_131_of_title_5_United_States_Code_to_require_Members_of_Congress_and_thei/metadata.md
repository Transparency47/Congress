# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1879?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1879
- Title: Ban Congressional Stock Trading Act
- Congress: 119
- Bill type: S
- Bill number: 1879
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-05-01T11:03:33Z
- Update date including text: 2026-05-01T11:03:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1879",
    "number": "1879",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "O000174",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Ossoff, Jon [D-GA]",
        "lastName": "Ossoff",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Ban Congressional Stock Trading Act",
    "type": "S",
    "updateDate": "2026-05-01T11:03:33Z",
    "updateDateIncludingText": "2026-05-01T11:03:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
        "item": [
          {
            "date": "2025-05-22T17:49:06Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-22T17:49:06Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "AZ"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "WI"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "IL"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "HI"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "NH"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "GA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "CO"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "NY"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MI"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "AZ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "MD"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "MN"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CO"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NJ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "DE"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CT"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1879is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1879\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Ossoff (for himself, Mr. Kelly , Ms. Baldwin , Ms. Duckworth , Mr. Schatz , Mrs. Shaheen , Mr. Warnock , Mr. Bennet , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend chapter 131 of title 5, United States Code, to require Members of Congress and their spouses and dependent children to place certain assets into blind trusts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ban Congressional Stock Trading Act .\n#### 2. Placement of certain assets of Members of Congress, spouses, and dependent children in qualified blind trusts\n##### (a) In general\nChapter 131 of title 5, United States Code, is amended by adding at the end the following:\nIV Certain assets of Members of Congress, spouses, and dependent children 13161. Definitions In this title: (1) Commodity The term commodity has the meaning given the term in section 1a of the Commodity Exchange Act ( 7 U.S.C. 1a ). (2) Covered investment (A) In general The term covered investment means\u2014 (i) an investment in a security, a commodity, or a future; and (ii) any economic interest comparable to an interest described in clause (i) that is acquired through synthetic means, such as the use of a derivative, including an option, warrant, or other, similar means. (B) Inclusions The term covered investment includes an investment or economic interest described in subparagraph (A) that is held directly, or in which an individual has an indirect, beneficial, or economic interest, through\u2014 (i) an investment fund; (ii) a trust (other than a qualified blind trust); (iii) an employee benefit plan; or (iv) a deferred compensation plan, including a carried interest or other agreement tied to the performance of an investment, other than a fixed cash payment. (C) Exclusions The term covered investment does not include\u2014 (i) a diversified mutual fund (including any holdings of such a fund); (ii) a diversified exchange-traded fund (including any holdings of such a fund); (iii) a United States Treasury bill, note, or bond; (iv) compensation from the primary occupation of a spouse or dependent child of a Member of Congress; or (v) any investment fund held in a Federal, State, or local government employee retirement plan. (D) Clarification An investment that achieves compliance with applicable environmental, social, and governance criteria shall not be considered to be a covered investment solely by reason of that compliance. (3) Current The term current , with respect to a Member of Congress, means an individual who is serving as a Member of Congress on the date of enactment of the Ban Congressional Stock Trading Act . (4) Dependent child The term dependent child means, with respect to any Member of Congress, any individual\u2014 (A) who has not attained the age of 19; and (B) who is a dependent, within the meaning of section 152 of the Internal Revenue Code of 1986, of the Member of Congress. (5) Diversified The term diversified , with respect to a fund, trust, or plan, means that the fund, trust, or plan does not have a stated policy of concentrating its investments in any industry, business, single country other than the United States, or bonds of a single State. (6) Future The term future means\u2014 (A) a security future (as defined in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) )); and (B) any other contract for the sale of a commodity for future delivery. (7) Initial property The term initial property means an asset or financial interest transferred to a qualified blind trust by, or on behalf of, an interested party or a relative of an interested party, regardless of whether the asset or financial interest is transferred to the qualified blind trust on or after the date of establishment of the qualified blind trust. (8) Interested party The term interested party has the meaning given the term in section 13104(f)(3)(E). (9) Member of Congress The term Member of Congress has the meaning given the term in section 13101. (10) New The term new , with respect to a Member of Congress, means an individual who\u2014 (A) is not a current Member of Congress; but (B) commences service as a Member of Congress after the date of enactment of the Ban Congressional Stock Trading Act . (11) Qualified blind trust The term qualified blind trust means a qualified blind trust (as defined in section 13104(f)(3)) that has been approved in writing by the applicable supervising ethics office under section 13104(f)(3)(D). (12) Security The term security has the meaning given the term in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) ). (13) Supervising ethics office The term supervising ethics office has the meaning given the term in section 13101. 13162. Placement of certain assets in qualified blind trusts (a) Current Members of Congress (1) Certification Not later than 30 days after the date of enactment of the Ban Congressional Stock Trading Act , each current Member of Congress shall submit to the applicable supervising ethics office a certification that, as applicable\u2014 (A) for each covered investment owned by the Member of Congress or a spouse or dependent child of the Member of Congress, the Member of Congress, or the applicable spouse or dependent child of the Member of Congress, will\u2014 (i) divest the covered investment; or (ii) place the covered investment in a qualified blind trust, including by establishing a qualified blind trust for that purpose, if necessary; or (B) neither the Member of Congress nor any spouse or dependent child of the Member of Congress owns a covered investment. (2) Divestiture or placement in qualified blind trust (A) Requirement Subject to paragraph (3), not later than 120 days after the date of enactment of the Ban Congressional Stock Trading Act , each current Member of Congress shall divest, or place in a qualified blind trust (including by establishing a qualified blind trust for that purpose, if necessary), each covered investment owned by the Member of Congress or a spouse or dependent child of the Member of Congress. (B) Divestiture A current Member of Congress shall divest a covered investment held by the Member of Congress or a spouse or dependent child of the Member of Congress if\u2014 (i) the Member of Congress, or the applicable spouse or dependent child of the Member of Congress, is unable to place the covered investment in a qualified blind trust by the date described in subparagraph (A); and (ii) the Member of Congress fails to obtain an extension pursuant to paragraph (3). (3) Extensions If a current Member of Congress, or a spouse or dependent child of the Member of Congress, is unable to place a covered investment in a qualified blind trust by the date described in paragraph (2)(A), the Member of Congress may request, and the supervising ethics office may grant, 1 or more reasonable extensions, subject to the conditions that\u2014 (A) the total period of time covered by all extensions granted to the Member of Congress for the covered investment shall not exceed 180 days; and (B) the period covered by a single extension shall be not longer than 45 days. (b) New Members of Congress (1) Certification Not later than 30 days after the date on which an individual becomes a new Member of Congress, the new Member of Congress shall submit to the applicable supervising ethics office a certification that, as applicable\u2014 (A) for each covered investment owned by the Member of Congress or a spouse or dependent child of the Member of Congress, the Member of Congress, or the applicable spouse or dependent child of the Member of Congress, will\u2014 (i) divest the covered investment; or (ii) place the covered investment in a qualified blind trust, including by establishing a qualified blind trust for that purpose, if necessary; or (B) neither the Member of Congress nor a spouse or dependent child of the Member of Congress owns a covered investment. (2) Divestiture or placement in qualified blind trust (A) Requirement Subject to paragraph (3), not later than 120 days after the date on which an individual becomes a new Member of Congress, the individual shall divest, or place in a qualified blind trust (including by establishing a qualified blind trust for that purpose, if necessary), each covered investment owned by the Member of Congress or a spouse or dependent child of the Member of Congress. (B) Divestiture A new Member of Congress shall divest a covered investment held by the Member of Congress or a spouse or dependent child of the Member of Congress if\u2014 (i) the Member of Congress, or the applicable spouse or dependent child of the Member of Congress, is unable to place the covered investment in a qualified blind trust by the date described in subparagraph (A); and (ii) the Member of Congress fails to obtain an extension pursuant to paragraph (3). (3) Extensions If a new Member of Congress, or a spouse or dependent child of the Member of Congress, is unable to place a covered investment in a qualified blind trust by the date described in paragraph (2)(A), the Member of Congress may request, and the supervising ethics office may grant, 1 or more reasonable extensions, subject to the conditions that\u2014 (A) the total period of time covered by all extensions granted to the Member of Congress for the covered investment shall not exceed 180 days; and (B) the period covered by a single extension shall be not longer than 45 days. (c) Acquisitions during service (1) In general Subject to paragraph (2), and any applicable rules issued pursuant to subsection (h)(3), effective beginning on the date of enactment of the Ban Congressional Stock Trading Act , a Member of Congress, and a spouse or dependent child of the Member of Congress, may not acquire a covered investment. (2) Inheritances (A) In general Subject to subparagraph (B), a Member of Congress or a spouse or dependent child of a Member of Congress who inherits a covered investment shall divest or place the covered investment in a qualified blind trust by not later than 120 days after the date on which the covered investment is inherited. (B) Extensions If a Member of Congress, or a spouse or dependent child of the Member of Congress, is unable to place a covered investment in a qualified blind trust by the date described in subparagraph (A), the Member of Congress may request, and the supervising ethics office may grant, 1 or more reasonable extensions, subject to the conditions that\u2014 (i) the total period of time covered by all extensions granted to the Member of Congress for the covered investment shall not exceed 180 days; and (ii) the period covered by a single extension shall be not longer than 45 days. (d) Mingling of assets A spouse or dependent child of a Member of Congress may place a covered investment in a qualified blind trust established by the Member of Congress under subsection (a)(1)(A)(ii) or (b)(1)(A)(ii). (e) Separation from service and cooling-Off period required for control During the period beginning on the date on which an individual becomes a Member of Congress and ending on the date that is 180 days after the date on which the individual ceases to serve as a Member of Congress, the Member of Congress, and any spouse or dependent child of the Member of Congress, may not\u2014 (1) dissolve any qualified blind trust in which a covered investment has been placed pursuant to subsection (a), (b), (c)(2), or (d); or (2) except as provided in this section, otherwise control a covered investment. (f) Reporting requirements (1) Supervising ethics offices Each supervising ethics office shall make available on the public website of the supervising ethics office\u2014 (A) a copy of\u2014 (i) each certification submitted to the supervising ethics office under subsection (a)(1) or (b)(1); (ii) each qualified blind trust agreement of each Member of Congress; (iii) each notice and other documentation submitted to the supervising ethics office under paragraph (2) or (3); and (iv) each notice, rule, and other documentation issued or received by the supervising ethics office under subsection (g); (B) a schedule of all assets placed in a qualified blind trust by each Member of Congress and interested party; and (C) a description of each extension granted, and each civil penalty imposed, pursuant to this section. (2) Trustees Each trustee of a qualified blind trust established by a Member of Congress shall submit to the Member of Congress and the applicable supervising ethics office a written notice in any case in which the trustee\u2014 (A) learns that\u2014 (i) an interested party has obtained knowledge of any trust property other than the initial property of the qualified blind trust; or (ii) the value of the initial property of the qualified blind trust is less than $1,000; or (B) divests any initial property of the qualified blind trust. (3) Members of Congress Each Member of Congress who is a beneficiary of a qualified blind trust shall submit to the applicable supervising ethics office\u2014 (A) a copy of the executed qualified blind trust agreement by not later than 30 days after the date of execution; (B) a list of each asset and each financial interest transferred to the qualified blind trust by an interested party by not later than 30 days after the date of the transfer; (C) a copy of each notice submitted to the Member of Congress under paragraph (2) by not later than 30 days after the date of receipt; (D) a written notice that an interested party has obtained knowledge of any holding of the qualified blind trust by not later than the date that is 30 days after the date on which the Member of Congress discovered that the knowledge had been obtained; and (E) a written notice of dissolution of the qualified blind trust by not later than 30 days after the date of dissolution. (g) Enforcement (1) In general The applicable supervising ethics office shall provide a written notice (including notice of the potential for civil penalties under paragraph (2)) to any Member of Congress who fails\u2014 (A) to submit a certification under subsection (a)(1) or (b)(1) by the date on which the certification is required to be submitted; or (B) to place 1 or more covered investments owned by the Member of Congress or a spouse or dependent child of the Member of Congress in a qualified blind trust in accordance with subsection (a)(2), (b)(2), (c)(2)(C)(i)(II), or (c)(2)(A) by the applicable deadline, subject to any extension under subsection (a)(3), (b)(3), or (c)(2)(B). (2) Civil penalties (A) In general A supervising ethics office shall impose a civil penalty, in the amount described in subparagraph (B), on a Member of Congress to whom a notice is provided under subparagraph (A) or (B) of paragraph (1)\u2014 (i) on the date that is 30 days after the date of provision of the notice; and (ii) not less frequently than once every 30 days thereafter. (B) Amount The amount of each civil penalty imposed on a Member of Congress pursuant to subparagraph (A) shall be equal to the monthly equivalent of the annual rate of pay payable to the Member of Congress. (h) Authorization of supervising ethics offices Each supervising ethics office in the legislative branch may\u2014 (1) impose and collect civil penalties in accordance with subsection (g); (2) establish such procedures and standard forms as the supervising ethics office determines to be appropriate to implement this section; (3) issue rules in accordance with this section to establish new, and supplement existing, definitions applicable to this section; and (4) publish on a website all documents and communications described in this subsection. .\n##### (b) Clerical amendment\nThe table of sections for chapter 131 of title 5, United States Code, is amended by adding at the end the following:\nSUBCHAPTER IV\u2014Certain assets of Members of Congress, spouses, and dependent children 13161. Definitions. 13162. Placement of certain assets in qualified blind trusts. .",
      "versionDate": "2025-05-22",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-06-12T13:49:40Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1879is.xml"
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
      "title": "Ban Congressional Stock Trading Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T11:03:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ban Congressional Stock Trading Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend chapter 131 of title 5, United States Code, to require Members of Congress and their spouses and dependent children to place certain assets into blind trusts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:20Z"
    }
  ]
}
```
