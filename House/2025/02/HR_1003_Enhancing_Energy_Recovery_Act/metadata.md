# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1003?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1003
- Title: Enhancing Energy Recovery Act
- Congress: 119
- Bill type: HR
- Bill number: 1003
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-12-05T22:02:11Z
- Update date including text: 2025-12-05T22:02:11Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1003",
    "number": "1003",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001082",
        "district": "1",
        "firstName": "Kevin",
        "fullName": "Rep. Hern, Kevin [R-OK-1]",
        "lastName": "Hern",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Enhancing Energy Recovery Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:02:11Z",
    "updateDateIncludingText": "2025-12-05T22:02:11Z"
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
          "date": "2025-02-05T15:07:50Z",
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
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "WV"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1003ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1003\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Hern of Oklahoma introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify the carbon oxide sequestration credit to ensure parity for different uses and utilizations of qualified carbon oxide.\n#### 1. Short title\nThis Act may be cited as the Enhancing Energy Recovery Act .\n#### 2. Parity for different uses and utilizations of qualified carbon oxide\n##### (a) In general\nSection 45Q of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2)(B)(ii), by adding and at the end,\n**(B)**\nin paragraph (3), by striking subparagraph (B) and inserting the following:\n(B) (i) disposed of by the taxpayer in secure geological storage and not used by the taxpayer as described in clause (ii) or (iii), (ii) used by the taxpayer as a tertiary injectant in a qualified enhanced oil or natural gas recovery project and disposed of by the taxpayer in secure geological storage, or (iii) utilized by the taxpayer in a manner described in subsection (f)(5). , and\n**(C)**\nby striking paragraph (4),\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking subparagraph (A) and inserting the following:\n(A) Except as provided in subparagraph (B) or (C), the applicable dollar amount shall be an amount equal to\u2014 (i) for any taxable year beginning in a calendar year after 2024 and before 2027, $17, and (ii) for any taxable year beginning in a calendar year after 2026, an amount equal to the product of $17 and the inflation adjustment factor for such calendar year determined under section 43(b)(3)(B) for such calendar year, determined by substituting 2025 for 1990 . , and\n**(ii)**\nin subparagraph (B), by striking shall be applied and all that follows through the period and inserting shall be applied by substituting $36 for $17 each place it appears. ,\n**(B)**\nin paragraph (2)(B), by striking paragraphs (3)(A) and (4)(A) and inserting paragraph (3)(A) , and\n**(C)**\nin paragraph (3), by striking the dollar amounts applicable under paragraph (3) or (4) and inserting the dollar amount applicable under paragraph (3) ,\n**(3)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (5)(B)(i), by striking (4)(B)(ii) and inserting (3)(B)(iii) , and\n**(B)**\nin paragraph (9), by striking paragraphs (3) and (4) of subsection (a) and inserting subsection (a)(3) , and\n**(4)**\nin subsection (h)(3)(A)(ii), by striking paragraph (3)(A) or (4)(A) of subsection (a) and inserting subsection (a)(3)(A) .\n##### (b) Conforming amendment\nSection 6417(d)(3)(C)(i)(II)(bb) of the Internal Revenue Code of 1986 is amended by striking paragraph (3)(A) or (4)(A) of section 45Q(a) and inserting section 45Q(a)(3)(A) .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
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
        "actionDate": "2025-02-05",
        "text": "Read twice and referred to the Committee on Finance. (text: CR S668)"
      },
      "number": "425",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Enhancing Energy Recovery Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-04",
        "text": "Became Public Law No: 119-21."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "An act to provide for reconciliation pursuant to title II of H. Con. Res. 14.",
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
        "updateDate": "2025-05-05T15:01:30Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1003ih.xml"
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
      "title": "Enhancing Energy Recovery Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Enhancing Energy Recovery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to modify the carbon oxide sequestration credit to ensure parity for different uses and utilizations of qualified carbon oxide.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:21Z"
    }
  ]
}
```
