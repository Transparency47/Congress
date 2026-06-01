# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4191?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4191
- Title: Extending WIC for New Moms Act
- Congress: 119
- Bill type: S
- Bill number: 4191
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-04-09T14:23:21Z
- Update date including text: 2026-04-09T14:23:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4191",
    "number": "4191",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "A000382",
        "district": "",
        "firstName": "Angela",
        "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
        "lastName": "Alsobrooks",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Extending WIC for New Moms Act",
    "type": "S",
    "updateDate": "2026-04-09T14:23:21Z",
    "updateDateIncludingText": "2026-04-09T14:23:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T17:24:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "sponsorshipDate": "2026-03-25",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4191is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4191\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Ms. Alsobrooks (for herself, Mr. Blumenthal , Mr. Booker , Ms. Duckworth , and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Child Nutrition Act of 1966 to extend eligibility of new moms for the special supplemental nutrition program for women, infants, and children.\n#### 1. Short title\nThis Act may be cited as the Extending WIC for New Moms Act .\n#### 2. Extending WIC eligibility for new moms\n##### (a) Extension of postpartum period\nSection 17(b)(10) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(b)(10) ) is amended by striking six months and inserting 24 months .\n##### (b) Extension of breastfeeding period\nSection 17(d)(3)(A)(ii) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(d)(3)(A)(ii) ) is amended by striking 1 year and inserting 24 months .\n##### (c) Report\nNot later than 2 years after the date of the enactment of this Act, the Secretary of Agriculture shall submit to Congress a report that includes an evaluation of the effect of each of the amendments made by this section on\u2014\n**(1)**\nmaternal and infant health outcomes, including racial and ethnic disparities with respect to such outcomes;\n**(2)**\nbreastfeeding rates among postpartum individuals;\n**(3)**\nqualitative evaluations of family experiences under the special supplemental nutrition program for women, infants, and children established by section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ); and\n**(4)**\nother relevant information, as determined by the Secretary.",
      "versionDate": "2026-03-25",
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
        "actionDate": "2026-03-24",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "8055",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Extending WIC for New Moms Act",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-04-09T14:23:21Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4191is.xml"
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
      "title": "Extending WIC for New Moms Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T05:38:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Extending WIC for New Moms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Child Nutrition Act of 1966 to extend eligibility of new moms for the special supplemental nutrition program for women, infants, and children.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T05:33:29Z"
    }
  ]
}
```
