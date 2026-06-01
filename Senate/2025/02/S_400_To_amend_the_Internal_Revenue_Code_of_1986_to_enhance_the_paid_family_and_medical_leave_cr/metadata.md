# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/400?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/400
- Title: Paid Family and Medical Leave Tax Credit Extension and Enhancement Act
- Congress: 119
- Bill type: S
- Bill number: 400
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2026-05-05T14:50:53Z
- Update date including text: 2026-05-05T14:50:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/400",
    "number": "400",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Paid Family and Medical Leave Tax Credit Extension and Enhancement Act",
    "type": "S",
    "updateDate": "2026-05-05T14:50:53Z",
    "updateDateIncludingText": "2026-05-05T14:50:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T22:43:38Z",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-04",
      "state": "ME"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "KS"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s400is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 400\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mrs. Fischer (for herself and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to enhance the paid family and medical leave credit, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Paid Family and Medical Leave Tax Credit Extension and Enhancement Act .\n#### 2. Enhancement of paid family and medical leave credit\n##### (a) In general\nSection 45S of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking paragraph (1) and inserting the following:\n(1) In general For purposes of section 38, in the case of an eligible employer, the paid family and medical leave credit is an amount equal to either of the following (as elected by such employer): (A) The applicable percentage of the amount of wages paid to qualifying employees with respect to any period in which such employees are on family and medical leave. (B) If such employer has an insurance policy with regards to the provision of paid family and medical leave which is in force during the taxable year, the applicable percentage of the total amount of premiums paid or incurred by such employer during such taxable year with respect to such insurance policy. , and\n**(B)**\nby adding at the end the following:\n(3) Rate of payment determined without regard to whether leave is taken For purposes of determining the applicable percentage with respect to paragraph (1)(B), the rate of payment under the insurance policy shall be determined without regard to whether any qualifying employees were on family and medical leave during the taxable year. ,\n**(2)**\nin subsection (b)(1), by striking credit allowed and inserting wages taken into account ,\n**(3)**\nin subsection (c), by striking paragraphs (3) and (4) and inserting the following:\n(3) Aggregation rule (A) In general Except as provided in subparagraph (B), all persons which are treated as a single employer under subsections (b) and (c) of section 414 shall be treated as a single employer. (B) Exception (i) In general Subparagraph (A) shall not apply to any person who establishes to the satisfaction of the Secretary that such person has a substantial and legitimate business reason for failing to provide a written policy described in paragraph (1) or (2). (ii) Substantial and legitimate business reason For purposes of clause (i), the term substantial and legitimate business reason shall not include the operation of a separate line of business, the rate of wages or category of jobs for employees (or any similar basis), or the application of State or local laws relating to family and medical leave, but may include the grouping of employees of a common law employer. (4) Treatment of benefits mandated or paid for by State or local governments For purposes of this section, any leave which is paid by a State or local government or required by State or local law\u2014 (A) except as provided in subparagraph (B), shall be taken into account in determining the amount of paid family and medical leave provided by the employer, and (B) shall not be taken into account in determining the amount of the paid family and medical leave credit under subsection (a). ,\n**(4)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1), by inserting (or, at the election of the employer, for not less than 6 months) after 1 year or more , and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby inserting , as determined on an annualized basis (pro-rata for part-time employees), after compensation , and\n**(ii)**\nby striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following:\n(3) is customarily employed for not less than 20 hours per week. , and\n**(5)**\nby striking subsection (i).\n##### (b) No double benefit\nSection 280C(a) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking 45S(a) and inserting 45S(a)(1)(A) , and\n**(2)**\nby inserting after the first sentence the following: No deduction shall be allowed for that portion of the premiums paid or incurred for the taxable year which is equal to that portion of the paid family and medical leave credit which is determined for the taxable year under section 45S(a)(1)(B). .\n##### (c) Outreach\n**(1) SBA and resource partners**\nEach district office of the Small Business Administration and each resource partner of the Small Business Administration, including small business development centers described in section 21 of the Small Business Act ( 15 U.S.C. 648 ), women's business centers described in section 29 of such Act ( 15 U.S.C. 656 ), each chapter of the Service Corps of Retired Executives described in section 8(b)(1)(B) of such Act ( 15 U.S.C. 637(b)(1)(B) ), and Veteran Business Outreach Centers described in section 32 of such Act ( 15 U.S.C. 657b ), shall conduct outreach to relevant parties regarding the paid family and medical leave credit under section 45S of the Internal Revenue Code of 1986, including through\u2014\n**(A)**\ntargeted communications, education, training, and technical assistance; and\n**(B)**\nthe development of a written paid family leave policy, as described in paragraphs (1) and (2) of section 45S(c) of the Internal Revenue Code of 1986.\n**(2) Internal Revenue Service**\nThe Secretary of the Treasury (or the Secretary's delegate) shall perform targeted outreach to employers and other relevant entities regarding the availability and requirements of the paid family and medical leave credit under section 45S of the Internal Revenue Code of 1986, including providing relevant information as part of Internal Revenue Service communications that are regularly issued to entities that provide payroll services, tax professionals, and small businesses.\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of enactment of this Act.",
      "versionDate": "2025-02-04",
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
        "actionDate": "2025-02-05",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "996",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Paid Family and Medical Leave Tax Credit Extension and Enhancement Act",
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
        "updateDate": "2025-05-05T15:43:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119s400",
          "measure-number": "400",
          "measure-type": "s",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2026-05-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s400v00",
            "update-date": "2026-05-05"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Paid Family and Medical Leave Tax Credit Extension and Enhancement Act </strong></p><p>This bill makes the paid family and medical leave tax credit permanent, expands eligibility for the credit,\u00a0requires outreach to increase awareness of the tax credit, and makes other changes to the credit.</p><p>Currently, an eligible employer may claim a tax credit (through 2025) for up to 25% of wages paid to a qualifying employee (who has worked for the employer for one year or more) while the employee is on family and medical leave.</p><p>The bill makes the tax credit for paid family and medical leave permanent and allows an eligible employer to claim the tax credit for 25% of either (1) wages paid to a qualifying employee while the employee is on family and medical leave, or (2) premiums paid for paid family or medical leave insurance.</p><p>The bill also</p><ul><li>allows an employer to provide family and medical leave to an employee who has worked for the employer for six months or more,</li><li>provides that leave that is paid by a state or local government or required by state or local law must be taken into account in determining the amount of leave provided by the employer but may not be counted when determining the amount of the credit, and</li><li>provides a limited exception to the requirements related to written family and medical leave policies.</li></ul><p>Finally, the bill requires targeted outreach to employers and other relevant parties regarding the availability and requirements of the tax credit.</p>"
        },
        "title": "Paid Family and Medical Leave Tax Credit Extension and Enhancement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s400.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Paid Family and Medical Leave Tax Credit Extension and Enhancement Act </strong></p><p>This bill makes the paid family and medical leave tax credit permanent, expands eligibility for the credit,\u00a0requires outreach to increase awareness of the tax credit, and makes other changes to the credit.</p><p>Currently, an eligible employer may claim a tax credit (through 2025) for up to 25% of wages paid to a qualifying employee (who has worked for the employer for one year or more) while the employee is on family and medical leave.</p><p>The bill makes the tax credit for paid family and medical leave permanent and allows an eligible employer to claim the tax credit for 25% of either (1) wages paid to a qualifying employee while the employee is on family and medical leave, or (2) premiums paid for paid family or medical leave insurance.</p><p>The bill also</p><ul><li>allows an employer to provide family and medical leave to an employee who has worked for the employer for six months or more,</li><li>provides that leave that is paid by a state or local government or required by state or local law must be taken into account in determining the amount of leave provided by the employer but may not be counted when determining the amount of the credit, and</li><li>provides a limited exception to the requirements related to written family and medical leave policies.</li></ul><p>Finally, the bill requires targeted outreach to employers and other relevant parties regarding the availability and requirements of the tax credit.</p>",
      "updateDate": "2026-05-05",
      "versionCode": "id119s400"
    },
    "title": "Paid Family and Medical Leave Tax Credit Extension and Enhancement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Paid Family and Medical Leave Tax Credit Extension and Enhancement Act </strong></p><p>This bill makes the paid family and medical leave tax credit permanent, expands eligibility for the credit,\u00a0requires outreach to increase awareness of the tax credit, and makes other changes to the credit.</p><p>Currently, an eligible employer may claim a tax credit (through 2025) for up to 25% of wages paid to a qualifying employee (who has worked for the employer for one year or more) while the employee is on family and medical leave.</p><p>The bill makes the tax credit for paid family and medical leave permanent and allows an eligible employer to claim the tax credit for 25% of either (1) wages paid to a qualifying employee while the employee is on family and medical leave, or (2) premiums paid for paid family or medical leave insurance.</p><p>The bill also</p><ul><li>allows an employer to provide family and medical leave to an employee who has worked for the employer for six months or more,</li><li>provides that leave that is paid by a state or local government or required by state or local law must be taken into account in determining the amount of leave provided by the employer but may not be counted when determining the amount of the credit, and</li><li>provides a limited exception to the requirements related to written family and medical leave policies.</li></ul><p>Finally, the bill requires targeted outreach to employers and other relevant parties regarding the availability and requirements of the tax credit.</p>",
      "updateDate": "2026-05-05",
      "versionCode": "id119s400"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s400is.xml"
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
      "title": "Paid Family and Medical Leave Tax Credit Extension and Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Paid Family and Medical Leave Tax Credit Extension and Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to enhance the paid family and medical leave credit, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T04:18:28Z"
    }
  ]
}
```
