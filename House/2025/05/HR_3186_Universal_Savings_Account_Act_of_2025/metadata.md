# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3186?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3186
- Title: Universal Savings Account Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3186
- Origin chamber: House
- Introduced date: 2025-05-05
- Update date: 2026-05-27T08:05:28Z
- Update date including text: 2026-05-27T08:05:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-05: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-05-05: Introduced in House

## Actions

- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3186",
    "number": "3186",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001086",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
        "lastName": "Harshbarger",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Universal Savings Account Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:28Z",
    "updateDateIncludingText": "2026-05-27T08:05:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-05",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-05",
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
          "date": "2025-05-05T16:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3186ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3186\nIN THE HOUSE OF REPRESENTATIVES\nMay 5, 2025 Mrs. Harshbarger introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to create Universal Savings Accounts.\n#### 1. Short title\nThis Act may be cited as the Universal Savings Account Act of 2025 .\n#### 2. Universal Savings Accounts\n##### (a) In general\nSubchapter F of Chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new part:\nIX Universal Savings Accounts 530A. Universal savings accounts (a) General rule A Universal Savings Account shall be exempt from taxation under this subtitle. Notwithstanding the preceding sentence, such account shall be subject to the taxes imposed by section 511 (relating to imposition of tax on unrelated business income of charitable organizations). (b) Universal Savings Account For purposes of this section, the term Universal Savings Account means a trust created or organized in the United States for the exclusive benefit of an individual and which is designated (in such manner as the Secretary shall prescribe) at the time of the establishment of the trust as a Universal Savings Account, but only if the written governing instrument creating the trust meets the following requirements: (1) Except in the case of a qualified rollover contribution described in subsection (d)\u2014 (A) no contribution will be accepted unless it is in cash, and (B) contributions will not be accepted for the calendar year in excess of the contribution limit specified in subsection (c)(1). (2) The trustee is a bank (as defined in section 408(n)) or another person who demonstrates to the satisfaction of the Secretary that the manner in which that person will administer the trust will be consistent with the requirements of this section or who has so demonstrated with respect to any individual retirement plan. (3) The interest of an individual in the balance of his account is nonforfeitable. (4) The assets of the trust shall not be commingled with other property except in a common trust fund or common investment fund. (5) No part of the trust funds will be invested in life insurance contracts. (c) Treatment of contributions and distributions (1) Contribution limit (A) In general The aggregate amount of contributions (other than qualified rollover contributions described in subsection (d)) for any calendar year to all Universal Savings Accounts maintained for the benefit of an individual shall not exceed the sum of\u2014 (i) $10,000, plus (ii) the product of\u2014 (I) $500, and (II) the number of calendar years after 2024 and before such calendar year, plus (iii) in the case of any calendar year after 2025, the product of\u2014 (I) the sum of the amount in clauses (i) and (ii) for such calendar year, multiplied by (II) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. If any increase under clause (iii) is not a multiple of $100, such amount shall be rounded to the next lower multiple of $100. (B) Limitation (i) In general The amount determined under subparagraph (A) for any calendar year shall not exceed $25,000. (ii) Inflation adjustment In the case of any calendar year after 2025, the $25,000 amount under clause (i) shall be increased by an amount equal to\u2014 (I) such dollar amount, multiplied by (II) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. If any increase under this clause is not a multiple of $100, such amount shall be rounded to the next lower multiple of $100. (2) Distributions (A) In general Except as provided in subparagraph (B), any distribution from a Universal Savings Account shall not be includible in gross income. (B) Net income attributable to excess contributions Any distribution of net income described in section 4973(i)(2) shall be includible in the gross income of the account holder in the taxable year in which the contribution to which such net income relates was made. (d) Qualified rollover contribution For purposes of this section, the term qualified rollover contribution means a contribution to a Universal Savings Account from another such account of the same beneficiary, but only if such amount is contributed not later than the 60th day after the distribution from such other account. (e) Treatment of account upon death Upon death of any account holder of a Universal Savings Account\u2014 (1) Spouse In the case of the account holder\u2019s surviving spouse acquiring such account holder\u2019s interest in such account by reason of the death of the account holder, such account shall be treated as if the spouse were the account holder. (2) Other cases In any other case\u2014 (A) all amounts in such account shall be treated as distributed on the date of such individual\u2019s death, and (B) such account shall cease to be treated as a Universal Savings Account. (f) Custodial accounts For purposes of this section, a custodial account shall be treated as a trust under this section if the assets of such account are held by a bank (as defined in section 408(n)) or another person who demonstrates, to the satisfaction of the Secretary, that the manner in which he will administer the account will be consistent with the requirements of this section, and if the custodial account would, except for the fact that it is not a trust, constitute a trust which meets the requirements of subsection (b). For purposes of this title, in the case of a custodial account treated as a trust by reason of the preceding sentence, the custodian of such account shall be treated as the trustee thereof. (g) Reports The trustee of a Universal Savings Account shall make such reports regarding such account to the Secretary and to the beneficiary of the account with respect to contributions, distributions, and such other matters as the Secretary may require. The reports required by this subsection shall be filed at such time and in such manner and furnished to such individuals at such time and in such manner as may be required. .\n##### (b) Tax on excess contributions\n**(1) In general**\nSection 4973(a) is amended by striking or at the end of paragraph (5), by inserting or at the end of paragraph (6), and by inserting after paragraph (6) the following new paragraph:\n(7) a Universal Savings Account (as defined in section 530U), .\n**(2) Excess contribution**\nSection 4973 is amended by adding at the end the following new subsection:\n(i) Excess contributions to universal savings accounts For purposes of this section\u2014 (1) In general In the case of Universal Savings Accounts (within the meaning of section 530U), the term excess contributions means the sum of\u2014 (A) the amount (if any) by which the amount contributed for the taxable year to such accounts (other than qualified rollover contributions (as defined in section 530U(d))) exceeds the contribution limit under section 530U(c)(2) for such taxable year, and (B) the amount determined under this subsection for the preceding taxable year, reduced by the sum of\u2014 (i) the distributions out of the account for the taxable year, and (ii) the amount (if any) by which the maximum amount allowable as a contribution under section 530U(c)(2) for the taxable year exceeds the amount contributed to the accounts for the taxable year. (2) Special rule A contribution shall not be taken into account under paragraph (1) if such contribution (together with the amount of net income attributable to such contribution) is distributed to the account holder on or before the due date of the account holder\u2019s return of tax for such taxable year. .\n##### (c) Tax on excess contributions\n**(1) In general**\nSubsection (a) of section 4973 of the Internal Revenue Code of 1986 is amended by striking or at the end of paragraph (5), by inserting or at the end of paragraph (6), and by inserting after paragraph (6) the following new paragraph:\n(7) a Universal Savings Account (as defined in section 530A), .\n**(2) Excess contribution**\nSection 4973 of such Code is amended by adding at the end the following new subsection:\n(i) Excess contributions to Universal Savings Accounts For purposes of this section\u2014 (1) In general In the case of Universal Savings Accounts (within the meaning of section 530A), the term excess contributions means the sum of\u2014 (A) the amount (if any) by which the amount contributed for the taxable year to such accounts (other than qualified rollover contributions (as defined in section 530A(d))) exceeds the contribution limit under section 530A(c)(1) for such taxable year, and (B) the amount determined under this subsection for the preceding taxable year, reduced by the sum of\u2014 (i) the distributions out of the account for the taxable year, and (ii) the amount (if any) by which the maximum amount allowable as a contribution under section 530A(c)(1) for the taxable year exceeds the amount contributed to the accounts for the taxable year. (2) Special rule A contribution shall not be taken into account under paragraph (1) if such contribution (together with the amount of net income attributable to such contribution) is distributed to the account holder on or before the due date of the account holder\u2019s return of tax for such taxable year. .\n##### (d) Tax on prohibited transactions\nSection 4975(e)(1) of the Internal Revenue Code of 1986 is amended by striking or at the end of subparagraph (F), by striking the period at the end of subparagraph (G) and inserting , or , and by adding at the end the following new subparagraph:\n(H) a Universal Savings Account (as defined in section 530A). .\n##### (e) Failure To provide reports on Universal Savings Accounts\nParagraph (2) of section 6693(a) of the Internal Revenue Code of 1986 is amended by striking and at the end of subparagraph (E), by striking the period at the end of subparagraph (F) and inserting , and , and by adding at the end the following new subparagraph:\n(G) section 530A(g) (relating to Universal Savings Accounts). .\n##### (f) Conforming amendment\nThe table of parts for subchapter F of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nPart IX. Universal Savings Accounts .\n##### (g) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-05-05",
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
        "actionDate": "2025-05-01",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1581",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Universal Savings Account Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-06-04T15:27:39Z"
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
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3186ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to create Universal Savings Accounts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T06:12:51Z"
    },
    {
      "title": "Universal Savings Account Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T06:09:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Universal Savings Account Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T06:08:15Z"
    }
  ]
}
```
