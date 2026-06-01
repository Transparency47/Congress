# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2045?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2045
- Title: Protecting Endowments from Our Adversaries Act
- Congress: 119
- Bill type: S
- Bill number: 2045
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2025-12-05T22:03:27Z
- Update date including text: 2025-12-05T22:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2045",
    "number": "2045",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
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
    "title": "Protecting Endowments from Our Adversaries Act",
    "type": "S",
    "updateDate": "2025-12-05T22:03:27Z",
    "updateDateIncludingText": "2025-12-05T22:03:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T15:42:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "AR"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2045is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2045\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mr. Ricketts (for himself, Mr. Cotton , and Mrs. Fischer ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to impose an excise tax on certain investments of private colleges and universities.\n#### 1. Short title\nThis Act may be cited as the Protecting Endowments from Our Adversaries Act .\n#### 2. Excise tax on certain investments of private colleges and universities\n##### (a) In general\nSubchapter H of chapter 42 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n4969. Excise tax on certain investments of private colleges and universities (a) Tax on acquisition of listed investments In the case of any specified educational institution which acquires (directly or indirectly through any chain of ownership) one or more listed investments during any taxable year, there is hereby imposed for such taxable year a tax equal to 50 percent of the fair market values of such investments determined as of the dates of such acquisitions. (b) Tax on net income from 1-Year listed investments (1) In general There is hereby imposed on each specified educational institution for the taxable year a tax equal to 100 percent of the excess (if any) of\u2014 (A) the sum of\u2014 (i) all income received with respect to any 1-year listed investment during such taxable year, plus (ii) all gains recognized with respect to the sale or other disposition of any 1-year listed investments during such taxable year, over (B) the sum of\u2014 (i) all deductions properly allocable to income described in subparagraph (A)(i), plus (ii) all losses recognized with respect to the sale or other disposition of any 1-year listed investments during such taxable year. (2) 1-year listed investment For purposes of this section, with respect to any income received or gain or loss recognized, the term 1-year listed investment means any listed investment which was such a listed investment at all times during the 1-year period ending on the date such income was received or such gain or loss was recognized. (c) Listed investment For purposes of this section\u2014 (1) In general The term listed investment means any specified interest with respect to any person listed on one or more of\u2014 (A) the Entity List maintained by the Secretary of Commerce, (B) the Military End User (MEU) List maintained by the Secretary of Commerce, (C) the Unverified List maintained by the Secretary of Commerce, or (D) the list maintained by the Federal Communications Commission of equipment and services covered by section 2 of the Secure and Trusted Communications Networks Act of 2019 (commonly referred to as the FCC Covered List). (2) Listed persons list The Secretary shall establish (not later than 60 days after the date of the enactment of this section), update, and maintain a list of the persons which are listed on one or more of the lists described in paragraph (1). (3) Specified interest The term specified interest means, with respect to any person\u2014 (A) stock or any other equity or profits interest of such person, (B) debt issued by such person, or (C) any contract or derivative with respect to any interest described in subparagraph (A) or (B). (4) Inclusion of certain pooled funds (A) In general Any specified interest acquired through a regulated investment company, exchange traded fund, or any other pooled investment shall not fail to be treated as acquired through a chain of ownership described in subsection (a). (B) Certifications of pooled funds The Secretary shall establish procedures under which regulated investment companies, exchange traded funds, and other pooled investments may be certified by the Secretary as not holding any listed investments. (d) Specified educational institution For purposes of this section\u2014 (1) In general The term specified educational institution means, with respect to any taxable year, any eligible educational institution (as defined in section 25A(f)(2))\u2014 (A) which is not described in the first sentence of section 511(a)(2)(B) (relating to State colleges and universities), and (B) the aggregate fair market value of the assets of which at the end of the preceding taxable year (other than those assets which are used directly in carrying out the institution\u2019s exempt purpose) is in excess of $1,000,000,000. (2) Treatment of related organizations For purposes of subsections (a) and (b), assets held by any related organization (as defined in section 4968(d)(2)) with respect to an educational institution shall be treated as held by such educational institution, except that\u2014 (A) such assets shall not be taken into account with respect to more than 1 educational institution, and (B) unless such organization is controlled by such institution or is described in section 509(a)(3) with respect to such institution, assets which are not intended or available for the use or benefit of such educational institution shall not be taken into account. (e) Valuation of debt For purposes of subsection (a), the fair market value of any debt shall be treated as being the principal amount of such debt. (f) Regulations The Secretary may issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section, including regulations or other guidance providing for the proper application of this section with respect to institutionally related foundations and pooled investments. .\n##### (b) Clerical amendments\n**(1)**\nThe table of sections for subchapter H of chapter 42 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 4969. Excise tax on certain investments of private colleges and universities. .\n**(2)**\nThe heading of subchapter H of chapter 42 of such Code (and the item relating to such subchapter in the table of subchapters for such chapter) are each amended by striking Tax Based on Investment Income and inserting Taxes Based on Investments .\n##### (c) Effective dates\n**(1) In general**\nExcept as otherwise provided in this subsection, the amendments made by this section shall apply to taxable years ending after the earlier of\u2014\n**(A)**\nthe end of the first calendar year beginning after the date of the enactment of this Act, or\n**(B)**\nthe end of the 1-year period beginning on the date on which the Secretary of the Treasury (or the Secretary\u2019s delegate) establishes the listed persons list under section 4969(c)(2) of the Internal Revenue Code of 1986 (as added by this section).\n**(2) Certain prior acquisitions**\nSection 4969(a) of the Internal Revenue Code of 1986 (as added by this section) shall not apply to investments acquired before the end of the calendar year referred to in paragraph (1)(A).\n**(3) Certain prior income and gains**\nSection 4969(b) of the Internal Revenue Code of 1986 (as added by this section) shall not apply to income received, or gains or losses recognized, before the end of the 1-year period referred to in paragraph (1)(B).",
      "versionDate": "2025-06-12",
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
        "actionDate": "2025-07-16",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "4462",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting Endowments from Our Adversaries Act",
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
        "name": "Taxation",
        "updateDate": "2025-06-30T18:06:22Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2045is.xml"
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
      "title": "Protecting Endowments from Our Adversaries Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-24T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Endowments from Our Adversaries Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-24T04:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to impose an excise tax on certain investments of private colleges and universities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-24T04:18:18Z"
    }
  ]
}
```
