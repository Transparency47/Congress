# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2902?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2902
- Title: Hidden Foster Care Transparency Act
- Congress: 119
- Bill type: S
- Bill number: 2902
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2025-12-05T22:50:11Z
- Update date including text: 2025-12-05T22:50:11Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2902",
    "number": "2902",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Hidden Foster Care Transparency Act",
    "type": "S",
    "updateDate": "2025-12-05T22:50:11Z",
    "updateDateIncludingText": "2025-12-05T22:50:11Z"
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
        "item": {
          "date": "2025-09-18T20:49:03Z",
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
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2902is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2902\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Cornyn (for himself and Mr. Ossoff ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo require States to measure and publicly report on the separation of children from parents by hidden foster care arrangements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Hidden Foster Care Transparency Act .\n#### 2. Definitions\nIn this Act:\n**(1) CPS agency**\nThe term CPS agency means the State agency responsible for the administration of the State plans under parts B and E of title IV of the Social Security Act ( 42 U.S.C. 621 et seq. , 671 et seq.) and any State, county, local, or tribal child protective services agency.\n**(2) Hidden foster care arrangement**\n**(A) In general**\nThe term hidden foster care arrangement means any separation of a child from the child\u2019s parents or primary caregivers that occurs without the State taking responsibility for the care or placement of the child and without a court order or the involvement and oversight of a court of law, whether voluntary or involuntary. Such term includes a separation of a child that occurs\u2014\n**(i)**\nfollowing a child protection hotline call or during an investigation by a CPS agency; or\n**(ii)**\nwhile a CPS agency has any involvement with a child\u2019s parents or primary caregivers but without the State taking responsibility for the care or placement of the child and without a court order or the involvement and oversight of a court of law, whether voluntary or involuntary.\n**(B) Included arrangements**\nSuch term includes\u2014\n**(i)**\nany arrangement in which a CPS agency suggests, implies, or insists that a parent should or must permit the parent\u2019s child to live with someone else in response to an investigation of allegations that the parent, or a spouse, partner, or other individual who resides with the parent, has neglected or abused the child; and\n**(ii)**\nany arrangement commonly referred to as kinship diversion, foster care diversion, safety planning, informal family planning, or hidden foster care to the extent that such arrangement occurs without a court order or court oversight.\n**(3) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(4) State**\nThe term State has the meaning given that term in section 1101(a) of the Social Security Act ( 42 U.S.C. 1301(a) ) for purposes of parts B and E of title IV of the Social Security Act ( 42 U.S.C. 621 et seq. , 671 et seq.).\n#### 3. State reports on hidden foster care arrangements\nAs a condition for payment of funds under a State plan approved under part E of title IV of the Social Security Act ( 42 U.S.C. 671 et seq. ), a State shall submit to the Secretary as part of the Adoption and Foster Care Analysis and Reporting System ( 42 U.S.C. 679 ) data that specifies, for each such fiscal year\u2014\n**(1)**\nthe number of children separated from their parents by a hidden foster care arrangement;\n**(2)**\nthe number of hidden foster care arrangements that ended without the child entering the formal foster care system;\n**(3)**\nthe number of hidden foster care arrangements that ended through the placement of the child into the formal foster care system;\n**(4)**\nthe category or type of allegation raised in each case which resulted in a separation of a child from their parents by a hidden foster care arrangement;\n**(5)**\nto the extent data is available, the number of caregivers in a hidden foster care arrangement who received additional services including referrals to kinship navigator programs, prevention services programs funded under part B or E of title IV of the Social Security Act ( 42 U.S.C. 621 et seq. , 671 et seq.), services provided by an entity or organization other than a CPS agency, or to legal counsel;\n**(6)**\nthe result of any investigation leading to a hidden foster care arrangement (whether an allegation is substantiated or indicated or not substantiated or indicated;\n**(7)**\nhow many parents\u2014\n**(A)**\nwere\u2014\n**(i)**\nprovided legal counsel; or\n**(ii)**\nreferred to a legal services provider before a hidden foster care arrangement began or within 72 hours of such an arrangement; and\n**(B)**\nwere actually represented by legal counsel within 72 hours of such an arrangement;\n**(8)**\nthe length of time children were in a hidden foster care arrangement, including the number of children in a hidden foster care arrangement for more than 90 days without any court orders addressing custody;\n**(9)**\nthe number of children who left hidden foster care arrangements\u2014\n**(A)**\nby reunification with the parent or guardian from whom they were initially separated;\n**(B)**\nby returning to a different parent or guardian; or\n**(C)**\nthrough\u2014\n**(i)**\na kinship caregiver obtaining legal custody or guardianship outside of the foster care system;\n**(ii)**\nentry in the foster care system and placement with kin; and\n**(iii)**\nentry in the foster care system and placement with someone else;\n**(10)**\na list of specific services provided to parents, children, and kinship caregivers affected by a hidden foster care arrangement and, for each such group, the number and specific services provided; and\n**(11)**\na list of reports of substantiated abuse or neglect made to a CPS agency within 3, 6, 9, or 12 months after a child is identified as being in a hidden foster care arrangement, where the child was living at time of report.\n#### 4. Secretarial responsibilities\n##### (a) Annual report to Congress on hidden foster care arrangement practices\nThe Secretary shall submit an annual report to Congress based on the most recent State reports submitted under section 3. Each annual report shall include the following:\n**(1)**\nThe total number of children for whom a hidden foster care arrangement ended during the fiscal year reported on, and of that number\u2014\n**(A)**\nhow many of the hidden foster care arrangements ended without the child entering the formal foster care system; and\n**(B)**\nhow many of the hidden foster care arrangements ended through the placement of the child into the formal foster care system.\n**(2)**\nThe total number of each category or type of allegation raised in a case which resulted in a separation of a child from their parents by a hidden foster care arrangement.\n**(3)**\nTo the extent data is available, the number of caregivers in a hidden foster care arrangement who received additional services, including referrals to kinship navigator programs, prevention services programs funded under part B or E of title IV of the Social Security Act ( 42 U.S.C. 621 et seq. , 671 et seq.), services provided by an entity or organization other than a CPS agency, or legal counsel.\n**(4)**\nThe number of States that submit a report under section 3 for the fiscal year involved and a summary of such reports that includes a summary of the ways in which States address hidden foster care arrangements within the most recent State plan reports submitted part B or E of title IV of the Social Security Act ( 42 U.S.C. 621 et seq. , 671 et seq.).\n##### (b) Implementation\n**(1) Consistent data**\nThe Secretary shall ensure that, to the extent practicable, the data and information required to be reported under section 3\u2014\n**(A)**\nis collected and reported in a reliable and standardized manner by all States;\n**(B)**\nprovides a comprehensive, national picture of the practice of hidden foster care arrangements; and\n**(C)**\ndraws upon and does not duplicate other required child welfare data collection and reporting regarding children for, or on whose behalf, prevention services are offered, including under section 471(e)(5)(B)(x) of the Social Security Act ( 42 U.S.C. 671(e)(5)(B)(x) ), section 479 of such Act ( 42 U.S.C. 679 ), and subparagraphs (C) and (D) of section 103(c)(1) of the Child Abuse Prevention and Treatment Act and 106(d) of the Child Abuse Prevention and Treatment Act ( 42 U.S.C. 5103(c)(1) , 5106a(d)).\n**(2) Guidance; technical assistance**\nThe Secretary may use funds made available to carry out part E of title IV of the Social Security Act ( 42 U.S.C. 670 et seq. ) to issue guidance or provide technical assistance to States with respect to the data and information required to be reported under section 3.\n**(3) Publication and manner of submission**\nThe Secretary\u2014\n**(A)**\nmay include the report required by subsection (a) in the annual compilation of State reports required to be submitted to Congress under section 479A of the Social Security Act ( 42 U.S.C. 679b ); and\n**(B)**\nshall make each report submitted to Congress in accordance with subsection (a) publicly available.",
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
        "actionDate": "2025-09-19",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5507",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Hidden Foster Care Transparency Act",
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
        "name": "Families",
        "updateDate": "2025-11-18T18:24:17Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2902is.xml"
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
      "title": "Hidden Foster Care Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-10T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Hidden Foster Care Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require States to measure and publicly report on the separation of children from parents by hidden foster care arrangements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T05:48:19Z"
    }
  ]
}
```
