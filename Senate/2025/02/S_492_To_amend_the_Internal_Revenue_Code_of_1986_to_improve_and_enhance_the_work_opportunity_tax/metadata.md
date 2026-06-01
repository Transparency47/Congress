# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/492?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/492
- Title: Improve and Enhance the Work Opportunity Tax Credit Act
- Congress: 119
- Bill type: S
- Bill number: 492
- Origin chamber: Senate
- Introduced date: 2025-02-10
- Update date: 2026-03-18T11:03:17Z
- Update date including text: 2026-03-18T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in Senate
- 2025-02-10 - IntroReferral: Introduced in Senate
- 2025-02-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-10: Introduced in Senate

## Actions

- 2025-02-10 - IntroReferral: Introduced in Senate
- 2025-02-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/492",
    "number": "492",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Improve and Enhance the Work Opportunity Tax Credit Act",
    "type": "S",
    "updateDate": "2026-03-18T11:03:17Z",
    "updateDateIncludingText": "2026-03-18T11:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-10",
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
      "actionDate": "2025-02-10",
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
            "date": "2025-02-10T21:13:08Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-10T21:13:08Z",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "NH"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s492is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 492\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2025 Mr. Cassidy (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to improve and enhance the work opportunity tax credit, to encourage longer-service employment, and to modernize the credit to make it more effective as a hiring incentive for targeted workers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improve and Enhance the Work Opportunity Tax Credit Act .\n#### 2. Improving and enhancing work opportunity tax credit\n##### (a) In general\nSection 51(a) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking shall be equal to 40 percent and all that follows and inserting the following:\nshall be equal to the sum of\u2014 (1) 50 percent of so much of the qualified first-year wages with respect to each individual for such year as does not exceed $6,000, plus (2) in the case of individuals who have performed at least 400 hours of service for the employer, 50 percent of so much of the qualified first-year wages with respect to each such individual for such year as exceeds $6,000, and does not exceed $12,000. .\n##### (b) Conforming amendments relating to limitation on wages taken into account for certain veterans\nSection 51(b)(3) of such Code is amended to read as follows:\n(3) Increased limitation on wages taken into account for veterans The $6,000 and $12,000 amounts under paragraphs (1) and (2) of subsection (a) shall be increased to\u2014 (A) $12,000 and $24,000, respectively, in the case of any individual who is a qualified veteran by reason of subsection (d)(3)(A)(ii)(I), (B) $14,000 and $28,000, respectively, in the case of any individual who is a qualified veteran by reason of subsection (d)(3)(A)(iv), and (C) $24,000 and $48,000, respectively, in the case of any individual who is a qualified veteran by reason of subsection (d)(3)(A)(ii)(II). .\n##### (c) Conforming amendments relating to individuals not meeting minimum employment periods\n**(1)**\nSubparagraphs (A) and (B) of section 51(i)(3) of such Code are each amended by striking subsection (a) and inserting subsection (a)(1) .\n**(2)**\nSection 51(i)(3)(A) of such Code is amended by striking 40 percent and inserting 50 percent .\n##### (d) Conforming amendments relating to treatment of summer youth employees\nSection 51(d)(7)(B) of such Code is amended\u2014\n**(1)**\nby striking clause (ii),\n**(2)**\nby striking , and at the end of clause (i) and inserting a period,\n**(3)**\nby redesignating clause (i) (as so amended) as clause (v), and\n**(4)**\nby inserting before such clause (v) (as so redesignated) the following new clauses:\n(i) in lieu of the amount determined under subsection (a), the amount of the work opportunity credit determined under this section for the taxable year shall be equal to 40 percent of the qualified first-year wages for such year, (ii) in the case of an individual described in subsection (i)(3)(A), clause (i) shall be applied by substituting 25 percent for 40 percent , (iii) in the case of an individual described in subsection (i)(3)(B), no wages shall be taken into account under clause (i), (iv) the amount of qualified first-year wages which may be taken into account with respect to such individual shall not exceed $3,000 per year, and .\n##### (e) Conforming amendments relating to long-Term family assistance recipients\n**(1) In general**\nSection 51(e)(1) of such Code is amended by striking family assistance recipient\u2014 and all that follows and inserting the following:\nfamily assistance recipient, in lieu of subsection (a), the amount of the work opportunity credit determined under this section for the taxable year shall be equal to\u2014 (1) 40 percent of so much of the qualified first-year wages with respect to such individual for such year as does not exceed $10,000, and (2) 50 percent of so much of the qualified second-year wages with respect to such individual for such year as does not exceed $10,000. .\n**(2) Clerical amendment**\nThe heading for section 51(e) of such Code is amended by striking Credit for second-year wages and inserting Special rules for determining credit .\n##### (f) Effective date\nThe amendments made by this section shall apply to individuals who begin work for the employer after December 31, 2024.\n#### 3. Removal of age limit for qualified supplemental nutrition assistance program benefits recipient\n##### (a) In general\nSection 51(d)(8)(A)(i) of the Internal Revenue Code of 1986 is amended by striking but not age 40 .\n##### (b) Effective date\nThe amendment made by this section shall apply to individuals who begin work for the employer after December 31, 2024.",
      "versionDate": "2025-02-10",
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
        "actionDate": "2025-02-10",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1177",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Improve and Enhance the Work Opportunity Tax Credit Act",
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
        "updateDate": "2025-05-06T12:42:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
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
          "measure-id": "id119s492",
          "measure-number": "492",
          "measure-type": "s",
          "orig-publish-date": "2025-02-10",
          "originChamber": "SENATE",
          "update-date": "2025-09-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s492v00",
            "update-date": "2025-09-23"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Improve and Enhance the Work Opportunity Tax Credit Act </strong></p><p>This bill increases the work opportunity tax credit (WOTC) for wages paid during the first year of employment to certain employees. The bill also eliminates the maximum age limit applicable to Supplemental Nutrition Assistance Program (SNAP) benefit recipients for purposes of the WOTC.</p><p>Under current law, an employer generally may claim a WOTC in the amount of 40% of up to $6,000 (or of up to $24,000 for certain veterans, $3,000 for summer youth employees, and $10,000 for long-term family aid recipients) of qualified wages paid during the first year of employment to an employee who is a member of a targeted group. (Exceptions and limitations apply.)</p><p>The bill increases the WOTC to (1) 50% of up to $6,000 (or of up to $24,000 for certain veterans) of qualified first-year wages paid to an employee who is a member of a targeted group (other than a summer youth employee or recipient of long-term family aid), and (2) 50% of up to $12,000 (or of up to $48,000 for certain veterans) of qualified wages paid during the first year of employment to such employee if the employee works at least 400 hours during the year.</p><p>Finally, the bill eliminates the maximum age limit applicable to SNAP benefit recipients and, thus, allows an employer to claim the\u00a0WOTC for qualified first-year wages paid to an employee who is at least 18 years old and\u00a0receiving SNAP benefits for a certain period of time.</p>"
        },
        "title": "Improve and Enhance the Work Opportunity Tax Credit Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s492.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Improve and Enhance the Work Opportunity Tax Credit Act </strong></p><p>This bill increases the work opportunity tax credit (WOTC) for wages paid during the first year of employment to certain employees. The bill also eliminates the maximum age limit applicable to Supplemental Nutrition Assistance Program (SNAP) benefit recipients for purposes of the WOTC.</p><p>Under current law, an employer generally may claim a WOTC in the amount of 40% of up to $6,000 (or of up to $24,000 for certain veterans, $3,000 for summer youth employees, and $10,000 for long-term family aid recipients) of qualified wages paid during the first year of employment to an employee who is a member of a targeted group. (Exceptions and limitations apply.)</p><p>The bill increases the WOTC to (1) 50% of up to $6,000 (or of up to $24,000 for certain veterans) of qualified first-year wages paid to an employee who is a member of a targeted group (other than a summer youth employee or recipient of long-term family aid), and (2) 50% of up to $12,000 (or of up to $48,000 for certain veterans) of qualified wages paid during the first year of employment to such employee if the employee works at least 400 hours during the year.</p><p>Finally, the bill eliminates the maximum age limit applicable to SNAP benefit recipients and, thus, allows an employer to claim the\u00a0WOTC for qualified first-year wages paid to an employee who is at least 18 years old and\u00a0receiving SNAP benefits for a certain period of time.</p>",
      "updateDate": "2025-09-23",
      "versionCode": "id119s492"
    },
    "title": "Improve and Enhance the Work Opportunity Tax Credit Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Improve and Enhance the Work Opportunity Tax Credit Act </strong></p><p>This bill increases the work opportunity tax credit (WOTC) for wages paid during the first year of employment to certain employees. The bill also eliminates the maximum age limit applicable to Supplemental Nutrition Assistance Program (SNAP) benefit recipients for purposes of the WOTC.</p><p>Under current law, an employer generally may claim a WOTC in the amount of 40% of up to $6,000 (or of up to $24,000 for certain veterans, $3,000 for summer youth employees, and $10,000 for long-term family aid recipients) of qualified wages paid during the first year of employment to an employee who is a member of a targeted group. (Exceptions and limitations apply.)</p><p>The bill increases the WOTC to (1) 50% of up to $6,000 (or of up to $24,000 for certain veterans) of qualified first-year wages paid to an employee who is a member of a targeted group (other than a summer youth employee or recipient of long-term family aid), and (2) 50% of up to $12,000 (or of up to $48,000 for certain veterans) of qualified wages paid during the first year of employment to such employee if the employee works at least 400 hours during the year.</p><p>Finally, the bill eliminates the maximum age limit applicable to SNAP benefit recipients and, thus, allows an employer to claim the\u00a0WOTC for qualified first-year wages paid to an employee who is at least 18 years old and\u00a0receiving SNAP benefits for a certain period of time.</p>",
      "updateDate": "2025-09-23",
      "versionCode": "id119s492"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s492is.xml"
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
      "title": "Improve and Enhance the Work Opportunity Tax Credit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improve and Enhance the Work Opportunity Tax Credit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to improve and enhance the work opportunity tax credit, to encourage longer-service employment, and to modernize the credit to make it more effective as a hiring incentive for targeted workers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:33Z"
    }
  ]
}
```
