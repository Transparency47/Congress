# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7473?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7473
- Title: CMMSA 2.0
- Congress: 119
- Bill type: HR
- Bill number: 7473
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-02-27T21:40:46Z
- Update date including text: 2026-02-27T21:40:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-10: Introduced in House

## Actions

- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7473",
    "number": "7473",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "R000599",
        "district": "25",
        "firstName": "Raul",
        "fullName": "Rep. Ruiz, Raul [D-CA-25]",
        "lastName": "Ruiz",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "CMMSA 2.0",
    "type": "HR",
    "updateDate": "2026-02-27T21:40:46Z",
    "updateDateIncludingText": "2026-02-27T21:40:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T15:00:20Z",
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
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7473ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7473\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2026 Mr. Ruiz (for himself and Mr. Evans of Colorado ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify the advanced manufacturing credit with respect to the production of battery components.\n#### 1. Short title\nThis Act may be cited as the Critical Minerals and Manufacturing Support Act 2.0 or the CMMSA 2.0 .\n#### 2. Modification of advanced manufacturing production credit relating to battery production\n##### (a) Increase in credit amount for electrode active materials\nSection 45X(b)(1)(J) of the Internal Revenue Code of 1986 is amended by striking 10 percent and inserting 25 percent .\n##### (b) Content requirements for qualifying battery component\nSection 45X(c)(5)(A) of such Code is amended by adding at the end the following:\nSuch term shall not include any materials, cells, or modules that contain any applicable critical minerals extracted, processed, or recycled after December 31, 2026, by a prohibited foreign entity (as defined in section 7701(a)(51)). .\n##### (c) Electrode active material definition To include precursor materials and solid state electrolytes\nSection 45X(c)(5)(B)(i) of such Code is amended\u2014\n**(1)**\nby striking material.\u2014 The term and inserting the following:\nmaterial.\u2014 (I) In general The term ,\n**(2)**\nby inserting , electrode active precursor materials used in the production of cathode and anode materials after anode materials ,\n**(3)**\nby inserting solid state electrolytes, after including , and\n**(4)**\nby adding at the end the following new subclause:\n(II) Electrode active precursor material The term electrode active precursor material means any of the following materials which are of a sufficient grade to meet the purity specifications of, and are intended to supply, the electrode active materials market: Cobalt sulfate, manganese sulfate, iron sulfate, lithium hydroxide, silicon, phosphoric acid, iron phosphate, nickel manganese cobalt oxide, silane, synthetic or natural graphite pitch, or lithium carbonate. .\n##### (d) Certain silicon treated as applicable critical material\nSection 45X(c)(6) of such Code is amended by redesignating subparagraphs (V) through (AA) as subparagraphs (W) through (BB), respectively, and by inserting after subparagraph (V) the following new subparagraph:\n(V) Silicon Silicon which is silicon or silicon composite used as an electrode active material in battery anodes. .\n##### (e) Extension of phase out for applicable critical minerals other than metallurgical coal\n**(1) In general**\nSection 45X(b)(3)(C)(i) of such Code is amended by striking 2030 and inserting 2041 .\n**(2) Phaseout percentages**\nSection 45X(b)(3)(C)(ii) of such Code is amended\u2014\n**(A)**\nby striking 2031 in subclause (I) and inserting 2042 ,\n**(B)**\nby striking 2032 in subclause (II) and inserting 2043 ,\n**(C)**\nby striking 2033 in subclause (III) and inserting 2044 , and\n**(D)**\nby striking 2033 in subclause (IV) and inserting 2044 .\n##### (f) Effective date\nThe amendments made by this section shall apply to components produced and sold after December 31, 2026.",
      "versionDate": "2026-02-10",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-02-27T21:40:46Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7473ih.xml"
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
      "title": "CMMSA 2.0",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-23T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CMMSA 2.0",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Critical Minerals and Manufacturing Support Act 2.0",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to modify the advanced manufacturing credit with respect to the production of battery components.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-23T13:18:27Z"
    }
  ]
}
```
