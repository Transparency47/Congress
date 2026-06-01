# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2567?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2567
- Title: To amend the Internal Revenue Code of 1986 to provide special rules for purposes of determining if financial guaranty insurance companies are qualifying insurance corporations under the passive foreign investment company rules.
- Congress: 119
- Bill type: HR
- Bill number: 2567
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-01-07T09:05:46Z
- Update date including text: 2026-01-07T09:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2567",
    "number": "2567",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001160",
        "district": "4",
        "firstName": "Gwen",
        "fullName": "Rep. Moore, Gwen [D-WI-4]",
        "lastName": "Moore",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to provide special rules for purposes of determining if financial guaranty insurance companies are qualifying insurance corporations under the passive foreign investment company rules.",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:46Z",
    "updateDateIncludingText": "2026-01-07T09:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:01:40Z",
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
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "NE"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "AL"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2567ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2567\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Ms. Moore of Wisconsin (for herself and Mr. Smith of Nebraska ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide special rules for purposes of determining if financial guaranty insurance companies are qualifying insurance corporations under the passive foreign investment company rules.\n#### 1. Treatment of financial guaranty insurance companies as qualifying insurance corporations under passive foreign investment company rules\n##### (a) In general\nSection 1297(f)(3) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(C) Special rules for financial guaranty insurance companies (i) In general Notwithstanding subparagraphs (A)(ii) and (B), the applicable insurance liabilities of a financial guaranty insurance company shall include its unearned premium reserves if\u2014 (I) such company is prohibited under generally accepted accounting principles from reporting on its applicable financial statements reserves for losses and loss adjustment expenses with respect to a financial guaranty insurance or reinsurance contract except to the extent that losses and loss adjustment expenses are expected to exceed the unearned premium reserves on the contract, (II) the applicable financial statement of such company reports financial guaranty exposure of at least 15-to-1 or State or local bond exposure of at least 9-to-1, and (III) such company includes in its insurance liabilities only its unearned premium reserves relating to insurance written or assumed that is within the single risk limits set forth in subsection (D) of section 4 of the Financial Guaranty Insurance Guideline (modified by using total shareholder\u2019s equity as reported on the applicable financial statement of the company rather than aggregate of the surplus to policyholders and contingency reserves). (ii) Application of alternative facts and circumstances test A financial guaranty insurance company shall be treated as satisfying the requirements of paragraph (2)(B). (iii) Financial guaranty insurance company For purposes of this subparagraph, the term financial guaranty insurance company means any insurance company the sole business of which is writing or reinsuring financial guaranty insurance (as defined in subsection (A) of section 1 of the Financial Guaranty Insurance Guideline) which is permitted under subsection (B) of section 4 of such Guideline. (iv) Financial guaranty exposure For purposes of this subparagraph, the term financial guaranty exposure means the ratio of\u2014 (I) the net debt service outstanding insured or reinsured by the company that is within the single risk limits set forth in the Financial Guaranty Insurance Guideline (as reported on such company\u2019s applicable financial statement), to (II) the company\u2019s total assets (as so reported). (v) State or local bond exposure For purposes of this subparagraph, the term State or local bond exposure means the ratio of\u2014 (I) the net unpaid principal of State or local bonds (as defined in section 103(c)(1)) insured or reinsured by the company that is within the single risk limits set forth in the Financial Guaranty Insurance Guideline (as reported on such company\u2019s applicable financial statement), to (II) the company\u2019s total assets (as so reported). (vi) Financial Guaranty Insurance Guideline For purposes of this subparagraph\u2014 (I) In general The term Financial Guaranty Insurance Guideline means the October 2008 model regulation that was adopted by the National Association of Insurance Commissioners on December 4, 2007. (II) Determinations made by Secretary The determination of whether any provision of the Financial Guaranty Insurance Guideline has been satisfied shall be made by the Secretary. .\n##### (b) Reporting of certain items\nSection 1297(f)(4) of such Code is amended by adding at the end the following new subparagraph:\n(C) Clarification that certain items on applicable financial statement be separately reported with respect to corporation An amount described in paragraph (1)(B) or clause (i)(II), (i)(III), (iv)(I), (iv)(II), (v)(I), or (v)(II) of paragraph (3)(C) shall be treated as reported on an applicable financial statement for purposes of this section if\u2014 (i) such amount is separately reported on such statement with respect to the corporation referred to in paragraph (1), or (ii) such amount is separately determined for purposes of calculating an amount which is reported on such statement. (D) Authority of Secretary to require reporting (i) In general Each United States person who owns an interest in a specified non-publicly traded foreign corporation and who takes the position that such corporation is not a passive foreign investment company shall report to the Secretary such information with respect to such corporation as the Secretary may require. (ii) Specified non-publicly traded foreign corporation For purposes of this subparagraph, the term specified non-publicly traded foreign corporation means any foreign corporation\u2014 (I) which would be a passive foreign investment company if subsection (b)(2)(B) did not apply, and (II) no interest in which is traded on an established securities market. .\n##### (c) Effective date\n**(1) In general**\nExcept as otherwise provided in this subsection, the amendments made by this section shall apply to taxable years beginning after December 31, 2024.\n**(2) Reporting**\nThe amendment made by subsection (b) shall apply to reports made after December 31, 2024.\n**(3) Certain financial guarantee insurance companies not treated as passive foreign investment companies merely by reason of status in certain prior taxable years**\n**(A) In general**\nIn the case of any taxable year of a qualified financial guarantee insurance company beginning after December 31, 2024, section 1298(b)(1) of the Internal Revenue Code of 1986 shall be applied to stock held by any taxpayer in such company by treating the specified grace period with respect to such company as not part of such taxpayer\u2019s holding period of such stock.\n**(B) Qualified financial guarantee insurance company**\nFor purposes of this paragraph, the term qualified financial guarantee insurance company means any financial guarantee insurance company (as defined in subparagraph (C) of section 1297(f)(3) of the Internal Revenue Code of 1986, as added by this section) which would not be a passive foreign investment company if\u2014\n**(i)**\nsuch subparagraph applied to the specified grace period, and\n**(ii)**\nin the case of any taxable year ending before January 1, 2019, clause (i)(II) of such subparagraph were applied by substituting 8-to-1 for 9-to-1 .\n**(C) Specified grace period**\nFor purposes of this paragraph, the term specified grace period means, with respect to any financial guarantee insurance company, the period beginning with such company\u2019s first taxable year beginning after December 31, 2017, and ending with such company\u2019s last taxable year beginning before January 1, 2025.\n**(D) Regulations and other guidance**\nThe Secretary of the Treasury (or the Secretary\u2019s delegate) shall issue such regulations or other guidance as may be necessary or appropriate to provide for the proper treatment of any financial guarantee insurance company which ceases to be treated as a passive foreign investment company by reason of subparagraph (A), including regulations or other guidance which provide for\u2014\n**(i)**\nan opportunity for the revocation of any election made under section 1295(b) or 1296(k) of the Internal Revenue Code of 1986, and\n**(ii)**\nthe application of section 1293(c) of such Code to periods after such company ceases to be treated as a passive foreign investment company.",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-06-09",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1987",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide special rules for purposes of determining if financial guaranty insurance companies are qualifying insurance corporations under the passive foreign investment company rules.",
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
        "updateDate": "2025-05-09T13:57:52Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2567ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to provide special rules for purposes of determining if financial guaranty insurance companies are qualifying insurance corporations under the passive foreign investment company rules.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:31Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to provide special rules for purposes of determining if financial guaranty insurance companies are qualifying insurance corporations under the passive foreign investment company rules.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:12Z"
    }
  ]
}
```
