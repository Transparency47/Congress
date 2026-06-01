# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/996?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/996
- Title: Paid Family and Medical Leave Tax Credit Extension and Enhancement Act
- Congress: 119
- Bill type: HR
- Bill number: 996
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-12-05T21:49:59Z
- Update date including text: 2025-12-05T21:49:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/996",
    "number": "996",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Paid Family and Medical Leave Tax Credit Extension and Enhancement Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:49:59Z",
    "updateDateIncludingText": "2025-12-05T21:49:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
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
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T15:02:05Z",
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
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "OK"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr996ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 996\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Feenstra (for himself, Mrs. Bice , and Ms. Perez ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to enhance the paid family and medical leave credit, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Paid Family and Medical Leave Tax Credit Extension and Enhancement Act .\n#### 2. Enhancement of paid family and medical leave credit\n##### (a) In general\nSection 45S of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking paragraph (1) and inserting the following:\n(1) In general For purposes of section 38, in the case of an eligible employer, the paid family and medical leave credit is an amount equal to either of the following (as elected by such employer): (A) The applicable percentage of the amount of wages paid to qualifying employees with respect to any period in which such employees are on family and medical leave. (B) If such employer has an insurance policy with regards to the provision of paid family and medical leave which is in force during the taxable year, the applicable percentage of the total amount of premiums paid or incurred by such employer during such taxable year with respect to such insurance policy. , and\n**(B)**\nby adding at the end the following:\n(3) Rate of payment determined without regard to whether leave is taken For purposes of determining the applicable percentage with respect to paragraph (1)(B), the rate of payment under the insurance policy shall be determined without regard to whether any qualifying employees were on family and medical leave during the taxable year. ,\n**(2)**\nin subsection (b)(1), by striking credit allowed and inserting wages taken into account ,\n**(3)**\nin subsection (c), by striking paragraphs (3) and (4) and inserting the following:\n(3) Aggregation rule (A) In general Except as provided in subparagraph (B), all persons which are treated as a single employer under subsections (b) and (c) of section 414 shall be treated as a single employer. (B) Exception (i) In general Subparagraph (A) shall not apply to any person who establishes to the satisfaction of the Secretary that such person has a substantial and legitimate business reason for failing to provide a written policy described in paragraph (1) or (2). (ii) Substantial and legitimate business reason For purposes of clause (i), the term substantial and legitimate business reason shall not include the operation of a separate line of business, the rate of wages or category of jobs for employees (or any similar basis), or the application of State or local laws relating to family and medical leave, but may include the grouping of employees of a common law employer. (4) Treatment of benefits mandated or paid for by State or local governments For purposes of this section, any leave which is paid by a State or local government or required by State or local law\u2014 (A) except as provided in subparagraph (B), shall be taken into account in determining the amount of paid family and medical leave provided by the employer, and (B) shall not be taken into account in determining the amount of the paid family and medical leave credit under subsection (a). ,\n**(4)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1), by inserting (or, at the election of the employer, for not less than 6 months) after 1 year or more , and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby inserting , as determined on an annualized basis (pro-rata for part-time employees), after compensation , and\n**(ii)**\nby striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following:\n(3) is customarily employed for not less than 20 hours per week. , and\n**(5)**\nby striking subsection (i).\n##### (b) No double benefit\nSection 280C(a) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking 45S(a) and inserting 45S(a)(1)(A) , and\n**(2)**\nby inserting after the first sentence the following: No deduction shall be allowed for that portion of the premiums paid or incurred for the taxable year which is equal to that portion of the paid family and medical leave credit which is determined for the taxable year under section 45S(a)(1)(B). .\n##### (c) Outreach\n**(1) SBA and resource partners**\nEach district office of the Small Business Administration and each resource partner of the Small Business Administration, including small business development centers described in section 21 of the Small Business Act ( 15 U.S.C. 648 ), women's business centers described in section 29 of such Act ( 15 U.S.C. 656 ), each chapter of the Service Corps of Retired Executives described in section 8(b)(1)(B) of such Act ( 15 U.S.C. 637(b)(1)(B) ), and Veteran Business Outreach Centers described in section 32 of such Act ( 15 U.S.C. 657b ), shall conduct outreach to relevant parties regarding the paid family and medical leave credit under section 45S of the Internal Revenue Code of 1986, including through\u2014\n**(A)**\ntargeted communications, education, training, and technical assistance; and\n**(B)**\nthe development of a written paid family leave policy, as described in paragraphs (1) and (2) of section 45S(c) of the Internal Revenue Code of 1986.\n**(2) Internal Revenue Service**\nThe Secretary of the Treasury (or the Secretary's delegate) shall perform targeted outreach to employers and other relevant entities regarding the availability and requirements of the paid family and medical leave credit under section 45S of the Internal Revenue Code of 1986, including providing relevant information as part of Internal Revenue Service communications that are regularly issued to entities that provide payroll services, tax professionals, and small businesses.\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of enactment of this Act.",
      "versionDate": "2025-02-05",
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
        "actionDate": "2025-02-04",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "400",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Paid Family and Medical Leave Tax Credit Extension and Enhancement Act",
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
        "updateDate": "2025-05-05T14:53:04Z"
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
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr996ih.xml"
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
      "title": "Paid Family and Medical Leave Tax Credit Extension and Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Paid Family and Medical Leave Tax Credit Extension and Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to enhance the paid family and medical leave credit, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:55Z"
    }
  ]
}
```
