# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2989?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2989
- Title: Stop MPT Act
- Congress: 119
- Bill type: S
- Bill number: 2989
- Origin chamber: Senate
- Introduced date: 2025-10-08
- Update date: 2025-12-08T21:51:12Z
- Update date including text: 2025-12-08T21:51:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-08: Introduced in Senate
- 2025-10-08 - IntroReferral: Introduced in Senate
- 2025-10-08 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-10-08: Introduced in Senate

## Actions

- 2025-10-08 - IntroReferral: Introduced in Senate
- 2025-10-08 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-08",
    "latestAction": {
      "actionDate": "2025-10-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2989",
    "number": "2989",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Stop MPT Act",
    "type": "S",
    "updateDate": "2025-12-08T21:51:12Z",
    "updateDateIncludingText": "2025-12-08T21:51:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-08",
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
      "actionDate": "2025-10-08",
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
          "date": "2025-10-08T18:01:34Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CT"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-10-08",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2989is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2989\nIN THE SENATE OF THE UNITED STATES\nOctober 8, 2025 Mr. Markey (for himself, Mr. Blumenthal , and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo prohibit certain sales or leases of real property for a health care entity if the terms of such a sale or lease would lead to long-term weakened financial status of the health care entity or place the public health at risk, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Medical Profiteering and Theft Act or the Stop MPT Act .\n#### 2. Limitation on the use of real estate investment trusts in health care\n##### (a) In general\n**(1) Prohibition**\nNo health care entity or covered firm may enter into agreement to sell to, or lease from, a real estate investment trust (as defined in section 856 of the Internal Revenue Code of 1986) an interest in real property if the terms of such sale or lease would lead to long-term weakened financial status of the health care entity or place the public health at risk.\n**(2) Review of sale or lease terms**\n**(A) In general**\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ) shall require each health care entity, or the covered firm that owns such health care entity, seeking to enter into an agreement described in paragraph (1) to submit to the Secretary for review the terms of the sale or lease, as applicable.\n**(B) Standard**\nIn conducting a review of a sale or lease under subparagraph (A), the Secretary shall determine whether the terms of such sale or lease would lead to long-term weakened financial status of the health care entity or place the public health at risk.\n**(C) Consultation**\nThe Secretary may consult with the relevant State attorney general in conducting a review under subparagraph (A).\n**(3) Litigation authority**\nExcept as provided in section 518 of title 28, United States Code (relating to litigation before the Supreme Court), attorneys designated by the Secretary may appear for the Department of Health and Human Services and represent the Department in any civil action brought in connection with a violation of paragraph (1).\n##### (b) Enforcement\n**(1) State enforcement**\n**(A) State authority**\nEach State may require a person subject to the requirements of this section to satisfy such requirements applicable to the person.\n**(B) Failure to implement requirements**\nIn the case of a State that fails to substantially enforce the requirements of this section with respect to applicable persons in the State, the Secretary shall enforce the requirements of this section under paragraph (2) to the extent that such requirements relate to actions prohibited under this section occurring in such State.\n**(2) Secretarial enforcement authority**\nIf a person is found by the Secretary to be in violation of this section, the Secretary may apply a civil monetary penalty with respect to such person in an amount not to exceed $10,000 per violation.\n**(3) Continued applicability of State law**\nThis section shall not be construed to supersede any provision of State law that establishes, implements, or continues in effect any requirement or prohibition except to the extent that such requirement or prohibition prevents the application of a requirement or prohibition of this section.\n##### (c) Definitions\nIn this section:\n**(1) Affiliate**\nThe term affiliate means\u2014\n**(A)**\na person that directly or indirectly owns, controls, or holds with power to vote, 20 percent or more of the outstanding voting securities of another entity, other than a person that holds such securities\u2014\n**(i)**\nin a fiduciary or agency capacity without sole discretionary power to vote such securities; or\n**(ii)**\nsolely to secure a debt, if such entity has not in fact exercised such power to vote;\n**(B)**\na corporation 20 percent or more of whose outstanding voting securities are directly or indirectly owned, controlled, or held with power to vote, by another entity (referred to in this subparagraph as a covered entity ), or by an entity that directly or indirectly owns, controls, or holds with power to vote, 20 percent or more of the outstanding voting securities of the covered entity, other than an entity that holds such securities\u2014\n**(i)**\nin a fiduciary or agency capacity without sole discretionary power to vote such securities; or\n**(ii)**\nsolely to secure a debt, if such entity has not in fact exercised such power to vote;\n**(C)**\na person whose business is operated under a lease or operating agreement by another entity, or person substantially all of whose property is operated under an operating agreement with that other entity; or\n**(D)**\nan entity that operates the business or substantially all of the property of another entity under a lease or operating agreement.\n**(2) Corporation**\nThe term corporation means\u2014\n**(A)**\na joint-stock company;\n**(B)**\na company or partnership association organized under a law that makes only the capital subscribed or callable up to a specified amount responsible for the debts of the association, including a limited partnership and a limited liability company;\n**(C)**\na trust; or\n**(D)**\nan association having a power or privilege that a private corporation, but not an individual or a partnership, possesses.\n**(3) Covered firm**\nThe term covered firm means a for-profit corporation that owns or is an affiliate of a health care entity.\n**(4) Health care entity**\nThe term health care entity means an entity that consists of 1 or more of the following health care providers:\n**(A)**\nA hospital.\n**(B)**\nA physician practice.\n**(C)**\nA skilled nursing facility.\n**(D)**\nA hospice facility.\n**(E)**\nA mental or behavioral health care provider.\n**(F)**\nAn opioid treatment program.\n**(G)**\nA provider of services (as defined in section 1861(u) of the Social Security Act ( 42 U.S.C. 1395x(u) ) or a supplier (as defined in section 1861(d) of such Act ( 42 U.S.C. 1395(d) ))) enrolled in the Medicare program.\n**(H)**\nAny other entity the Secretary determines appropriate.\n#### 3. Treatment of rents from qualified health care property\n##### (a) In general\nSection 856(d)(2) of the Internal Revenue Code of 1986 is amended by striking and at the end of subparagraph (B), by striking the period and inserting , and at the end of subparagraph (C), and by adding at the end the following new subparagraph:\n(D) notwithstanding paragraphs (4), (6), and (8), any amount received or accrued directly or indirectly from qualified health care property (as defined in subsection (e)(6)(D)(i)). .\n##### (b) Conforming amendments\n**(1)**\nSection 856(d)(8)(B) of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nby striking or a qualified health care property (as defined in subsection (e)(6)(D)(i)) , and\n**(B)**\nby striking qualified health care property or .\n**(2)**\nSection 856(d)(9) of such Code is amended\u2014\n**(A)**\nby striking or a qualified health care property (as defined in subsection (e)(6)(D)(i)) in subparagraph (A),\n**(B)**\nby striking or qualified health care property each place it appears in subparagraph (A) and (B), and\n**(C)**\nby striking or qualified health care properties in subparagraph (A).\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-10-08",
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
        "name": "Taxation",
        "updateDate": "2025-12-08T21:51:12Z"
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
      "date": "2025-10-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2989is.xml"
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
      "title": "Stop MPT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop MPT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Medical Profiteering and Theft Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit certain sales or leases of real property for a health care entity if the terms of such a sale or lease would lead to long-term weakened financial status of the health care entity or place the public health at risk, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T02:48:15Z"
    }
  ]
}
```
