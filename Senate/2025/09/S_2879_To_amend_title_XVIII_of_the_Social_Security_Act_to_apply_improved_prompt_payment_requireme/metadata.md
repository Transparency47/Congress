# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2879?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2879
- Title: Medicare Advantage Prompt Pay Act
- Congress: 119
- Bill type: S
- Bill number: 2879
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-03-19T11:03:27Z
- Update date including text: 2026-03-19T11:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2879",
    "number": "2879",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Medicare Advantage Prompt Pay Act",
    "type": "S",
    "updateDate": "2026-03-19T11:03:27Z",
    "updateDateIncludingText": "2026-03-19T11:03:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
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
            "date": "2025-09-18T19:01:49Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-18T19:01:49Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TN"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2879is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2879\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Ms. Cortez Masto (for herself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to apply improved prompt payment requirements to Medicare Advantage organizations.\n#### 1. Short title\nThis Act may be cited as the Medicare Advantage Prompt Pay Act .\n#### 2. Application of improved prompt payment requirements to Medicare Advantage organizations\n##### (a) Requirements\n**(1) In general**\nSection 1857 of the Social Security Act ( 42 U.S.C. 1395w\u201327 ) is amended\u2014\n**(A)**\nin subsection (f), by striking paragraph (1) and inserting the following:\n(1) Requirements (A) Items and services furnished by in-network and out-of-network providers of services and suppliers (i) In general A contract under this part between the Secretary and a Medicare Advantage organization offering a Medicare Advantage plan shall require the organization to provide prompt payment for not less than 95 percent of clean claims submitted to the organization, with respect to covered items or services furnished to enrollees by a provider of services or supplier, within the applicable number of calendar days after the date of initial receipt of such clean claim, regardless of whether such items or services are furnished under a contract between the organization and the provider of services or supplier. (ii) Applicable number of calendar days In clause (i), the term applicable number of calendar days means\u2014 (I) in the case of a claim submitted electronically, by a provider of services or supplier for items or services furnished under a contract between the organization and the provider of services or supplier, 14 days; and (II) in the case of a claim not described in subclause (I), 30 days. (B) Clean claim defined In this paragraph, the term clean claim means a claim that\u2014 (i) has a complete data set, with respect to the UB\u201304 or CMS 1500 form, as applicable (or successor to such applicable form) for all entries identified as mandatory entries by the National Uniform Billing Committee; and (ii) in the case of a claim submitted electronically, is completed in accordance with the applicable standards and data elements adopted under section 1173(a). (C) Rebuttable presumption for receipt of claim (i) In general For purposes of this paragraph, there shall be a rebuttable presumption that a claim has been received by an MA organization\u2014 (I) in the case of a claim submitted electronically, on the date verified in the health care claim status request and response transaction that is for such claim and meets applicable standards and data elements adopted under section 1173(a) for such electronic requests and responses; and (II) in the case of a claim submitted otherwise, on the fifth business day after the postmark date of the claim or the date specified in the time stamp of the transmission. (ii) Business day defined In clause (i)(II), the term business day means any day other than Saturday, Sunday, or a legal public holiday described in section 6103 of title 5, United States Code. (D) Interest applied for clean claims not promptly paid If payment for such covered items or services is not issued, mailed, or otherwise transmitted to the provider of services or supplier for such claims that are clean claims, in accordance with subparagraph (A), by not later than the deadline for such payment under such subparagraph, the MA organization shall pay the provider of services or supplier interest at the rate used for purposes of section 3902(a) of title 31, United States Code (relating to interest penalties for failure to make prompt payments) for the period beginning on the day after such required payment date and ending on the date on which payment is made. ; and\n**(B)**\nin subsection (g)\u2014\n**(i)**\nby redesignating paragraph (4) as paragraph (5);\n**(ii)**\nby inserting after paragraph (3) the following new paragraph:\n(4) Application of civil money penalties to prompt pay violations If the Secretary determines that an MA organization with a contract under this section is not in compliance with subsection (f)(1), the Secretary shall provide, in addition to any other remedies authorized by law, for civil money penalties of not more than $25,000 for each such determination. In making a determination under the previous sentence, the Secretary may take into account information collected pursuant to section 1851(d)(4)(D)(v). ; and\n**(iii)**\nin paragraph (5), as redesignated by clause (i), by striking or (3) and inserting , (3), or (4) .\n**(2) Effective date**\nThe amendments made by this subsection shall apply with respect to items and services furnished on or after January 1, 2027, and contract years beginning on or after such date.\n##### (b) Provision of information regarding compliance with prompt payment requirements\nSection 1851(d)(4)(D) of the Social Security Act ( 42 U.S.C. 1395w\u201321(d)(4)(D) ) is amended\u2014\n**(1)**\nin clause (iii), by striking and at the end;\n**(2)**\nin clause (iv), by striking the period and inserting , and ; and\n**(3)**\nby adding at the end the following new clause:\n(v) information regarding compliance of the plan with the prompt payment requirements under section 1857(f)(1), including, with respect to the most recent 12-month period for which data are available\u2014 (I) the number and percent of submitted claims for which payment was made by the plan; (II) the number and percent of submitted claims\u2014 (aa) that were for items or services furnished by a provider of services or supplier under a contract between the organization offering the plan and the provider of services or supplier; and (bb) that were for items or services not furnished under such a contract; (III) the number and percent of submitted claims described in each of items (aa) and (bb) of subclause (II) for which payment was made by the plan by the deadline required pursuant to section 1857(f)(1)(A); (IV) the number and percent of submitted claims described in each of items (aa) and (bb) of subclause (II) for which interest was paid by the plan pursuant to section 1857(f)(1)(D); and (V) the total amount of interest paid by the plan pursuant to such section. .",
      "versionDate": "2025-09-18",
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
        "actionDate": "2025-09-18",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5454",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Medicare Advantage Prompt Pay Act",
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
        "name": "Health",
        "updateDate": "2025-11-18T16:01:24Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2879is.xml"
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
      "title": "Medicare Advantage Prompt Pay Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Medicare Advantage Prompt Pay Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to apply improved prompt payment requirements to Medicare Advantage organizations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:30Z"
    }
  ]
}
```
