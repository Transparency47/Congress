# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1058?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1058
- Title: Preserving Patient Access to Home Infusion Act
- Congress: 119
- Bill type: S
- Bill number: 1058
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-03-09T20:28:21Z
- Update date including text: 2026-03-09T20:28:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1058",
    "number": "1058",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000805",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Warner, Mark R. [D-VA]",
        "lastName": "Warner",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Preserving Patient Access to Home Infusion Act",
    "type": "S",
    "updateDate": "2026-03-09T20:28:21Z",
    "updateDateIncludingText": "2026-03-09T20:28:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
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
      "actionDate": "2025-03-13",
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
          "date": "2025-03-13T21:26:30Z",
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
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1058is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1058\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Warner (for himself and Mr. Scott of South Carolina ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to clarify congressional intent and preserve patient access to home infusion therapy under the Medicare program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preserving Patient Access to Home Infusion Act .\n#### 2. Preservation of patient access to home infusion therapy under Medicare program\n##### (a) Inclusion of pharmacy services\nSection 1861(iii)(2) of the Social Security Act ( 42 U.S.C. 1395x(iii)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A), by inserting and pharmacy services after nursing services ; and\n**(2)**\nin subparagraph (B), by inserting , assessments, drug preparation and compounding, coordination and documentation of infusion therapy services in the plan of care after subsection (n)) .\n##### (b) Payment\nSection 1834(u)(1)(A) of the Social Security Act ( 42 U.S.C. 1395m(u)(1)(A) ) is amended\u2014\n**(1)**\nin clause (i), by striking clause (iii) and inserting clauses (iii) and (iv) ;\n**(2)**\nin clause (ii) by inserting after the first sentence the following new sentence: For purposes of the previous sentence, a reference to payment to a qualified home infusion therapy supplier for an infusion drug administration calendar day in the home of such individual shall refer to payment for each day on which such a drug was administered to the individual (regardless of whether a qualified home infusion therapy supplier was physically present in the home of such individual on such date). ; and\n**(3)**\nin clause (iii)\u2014\n**(A)**\nby striking The single payment amount and inserting the following:\n(I) In general Subject to subclause (II), the single payment amount ; and\n**(B)**\nby adding at the end the following new subclause:\n(II) Transitional rule For home infusion therapy furnished on or after January 1, 2026, and before January 1, 2030, the Secretary shall ensure that the single payment amount determined under this subparagraph reflects 5 hours of infusion for a particular therapy in a calendar day. ; and\n**(4)**\nby adding at the end the following new clause:\n(iv) Special rule when a qualified home infusion therapy supplier not physically present in the individual's home In the case where a qualified home infusion therapy supplier is not physically present in the individual's home on the day the home infusion drug is administered to the individual, the single payment amount under this subsection for items and services described in clause (i) furnished on such day to such individual shall be an amount equal to 50 percent of the amount that would have applied under this subsection for such items and services if such a supplier had been physically present. .\n##### (c) Permitting nurse practitioners and physician assistants To establish and review a home infusion plan of care\nSection 1861(iii)(1)(B) of the Social Security Act ( 42 U.S.C. 1395x(iii)(1)(B) ) is amended by striking physician (as defined in subsection (r)(1)) and is periodically reviewed by a physician and inserting physician (as defined in subsection (r)(1)) or a nurse practitioner or physician assistant (as those terms are defined in subsection (aa)(5)) and is periodically reviewed by a physician, nurse practitioner, or physician assistant .\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to items and services furnished on or after January 1, 2026.\n#### 3. Access to home infusion for non-pump drugs and biologicals\n##### (a) Modification of definition of home infusion drug\nSection 1861(iii)(3) of the Social Security Act ( 42 U.S.C. 1395x(iii)(3) ) is amended\u2014\n**(1)**\nin subparagraph (C), by inserting and, in the case of a drug or biological other than a specified non-pump drug or biological (as defined in subparagraph (E)), before through ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(E) The term specified non-pump drug or biological means a drug or biological that\u2014 (i) is administered intravenously but not through a pump that is an item of durable medical equipment (as defined in subsection (n)); and (ii) is an antibacterial, antifungal, or antiviral (as categorized by the United States Pharmacopeia). .\n##### (b) Clarification on billing\nSection 1834(u) of the Social Security Act ( 42 U.S.C. 1395m(u) ) is amended by adding at the end the following new paragraph:\n(8) Clarification on billing for a specified non-pump drug or biological In the case of a qualified home infusion supplier (as defined in section 1861(iii)(3)(D)) that furnishes items and services described in subparagraphs (A) and (B) of section 1861(iii)(2) in coordination with the furnishing of a home infusion drug (as defined in section 1861(iii)(3)(C)) that is a specified non-pump drug or biological (as defined in section 1861(iii)(3)(E)) where the method of infusion utilized in furnishing such drug or biological does not involve a pump that is an item of durable medical equipment, payment under this subsection for the items and services described in subparagraphs (A) and (B) of section 1861(iii)(2) shall be made with respect to such drug or biological regardless of whether such drug or biological so furnished is payable under this part. .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to items and services furnished on or after January 1, 2026.\n#### 4. Modification of payment for home infusion supplies\nSection 1834(a) of the Social Security Act ( 42 U.S.C. 1395m(a) ) is amended by adding at the end the following new paragraph:\n(23) Special payment rule for items and supplies furnished in conjunction with home infusion therapy (A) In general Notwithstanding the preceding provisions of this subsection, no payment may be made under this subsection with respect to applicable items and services (as defined in subparagraph (B)) that are furnished on or after January 1, 2026, in conjunction home infusion therapy (as defined in section 1861(iii)(1)) for which payment is made under subsection (u) and which are so furnished on the same day as such home infusion therapy and with respect to the same home infusion drug (as defined in section 1861(iii)(3)(C)) for which such payment was so made. (B) Applicable items and services defined For purposes of subparagraph (A), the term applicable items and services means tubing, catheters, dressings, needles, syringes, and other supplies identified by HCPCS code A4221, A4222, or K0552 (or any successor code). .",
      "versionDate": "2025-03-13",
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
        "actionDate": "2025-03-18",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2172",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Preserving Patient Access to Home Infusion Act",
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
        "updateDate": "2025-04-04T12:49:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-13",
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
          "measure-id": "id119s1058",
          "measure-number": "1058",
          "measure-type": "s",
          "orig-publish-date": "2025-03-13",
          "originChamber": "SENATE",
          "update-date": "2026-03-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1058v00",
            "update-date": "2026-03-09"
          },
          "action-date": "2025-03-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Preserving Patient Access to Home Infusion Act\u00a0</strong></p><p>This bill specifically includes pharmacy services and home infusion drugs that are administered\u00a0without a pump as part of covered home infusion therapy under Medicare. The bill also allows nurses and physician assistants to establish and review the plan of care for home infusion therapy, and it specifies that payment may be made regardless of whether a practitioner is physically present in the home at the time the drug is administered.\u00a0</p>"
        },
        "title": "Preserving Patient Access to Home Infusion Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1058.xml",
    "summary": {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Preserving Patient Access to Home Infusion Act\u00a0</strong></p><p>This bill specifically includes pharmacy services and home infusion drugs that are administered\u00a0without a pump as part of covered home infusion therapy under Medicare. The bill also allows nurses and physician assistants to establish and review the plan of care for home infusion therapy, and it specifies that payment may be made regardless of whether a practitioner is physically present in the home at the time the drug is administered.\u00a0</p>",
      "updateDate": "2026-03-09",
      "versionCode": "id119s1058"
    },
    "title": "Preserving Patient Access to Home Infusion Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Preserving Patient Access to Home Infusion Act\u00a0</strong></p><p>This bill specifically includes pharmacy services and home infusion drugs that are administered\u00a0without a pump as part of covered home infusion therapy under Medicare. The bill also allows nurses and physician assistants to establish and review the plan of care for home infusion therapy, and it specifies that payment may be made regardless of whether a practitioner is physically present in the home at the time the drug is administered.\u00a0</p>",
      "updateDate": "2026-03-09",
      "versionCode": "id119s1058"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1058is.xml"
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
      "title": "Preserving Patient Access to Home Infusion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preserving Patient Access to Home Infusion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to clarify congressional intent and preserve patient access to home infusion therapy under the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:40Z"
    }
  ]
}
```
